#!/usr/bin/env python
"""Stop フック（事後）：本セッションで Claude が編集したファイルのうち、
未コミット変更が残っているものを差分サマリーとして出力し exit 2 で再起動を促す。

セッション開始前から既に変更されていた別作業の差分では再起動しない
（transcript から Claude が触ったファイルだけを対象にする）。naro_novel から移植。
"""

from __future__ import annotations

import io
import json
import subprocess
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

EDIT_TOOL_NAMES = {"Edit", "Write", "MultiEdit", "NotebookEdit"}


def collect_touched_paths(transcript_path: Path, repo_root: Path) -> set[Path]:
    touched: set[Path] = set()
    repo_root_resolved = repo_root.resolve()
    with transcript_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            content = (entry.get("message") or {}).get("content")
            if not isinstance(content, list):
                continue
            for block in content:
                if not isinstance(block, dict) or block.get("type") != "tool_use":
                    continue
                if block.get("name") not in EDIT_TOOL_NAMES:
                    continue
                file_path = (block.get("input") or {}).get("file_path")
                if not file_path:
                    continue
                try:
                    rel = Path(file_path).resolve().relative_to(repo_root_resolved)
                except (ValueError, OSError):
                    continue
                touched.add(rel)
    return touched


def has_uncommitted_changes(rel_path: str) -> bool:
    unstaged = subprocess.run(["git", "diff", "--quiet", "--", rel_path], capture_output=True).returncode
    staged = subprocess.run(["git", "diff", "--cached", "--quiet", "--", rel_path], capture_output=True).returncode
    return unstaged != 0 or staged != 0


def main() -> int:
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        return 0

    transcript_path_str = payload.get("transcript_path")
    if not transcript_path_str:
        return 0
    transcript_path = Path(transcript_path_str)
    if not transcript_path.is_file():
        return 0

    try:
        repo_root = Path(
            subprocess.run(
                ["git", "rev-parse", "--show-toplevel"],
                capture_output=True, text=True, check=True,
            ).stdout.strip()
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return 0

    touched = collect_touched_paths(transcript_path, repo_root)
    if not touched:
        return 0

    targets = [p.as_posix() for p in sorted(touched) if has_uncommitted_changes(p.as_posix())]
    if not targets:
        return 0

    branch = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True
    ).stdout.strip()
    print(f"=== 未コミットの変更（現在ブランチ: {branch}）===")
    subprocess.run(["git", "status", "--short", "--"] + targets, check=False)
    print()
    print("=== 差分統計（未ステージ） ===")
    subprocess.run(["git", "diff", "--stat", "--"] + targets, check=False)
    print()
    print("=== 差分統計（ステージ済み） ===")
    subprocess.run(["git", "diff", "--cached", "--stat", "--"] + targets, check=False)

    # exit 2 = blocking → asyncRewake で Claude を起こしコミットを促す
    return 2


if __name__ == "__main__":
    sys.exit(main())
