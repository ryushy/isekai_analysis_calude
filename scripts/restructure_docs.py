"""docs/ ディレクトリ再構成スクリプト。

増殖する試作・連作・メディアを目的別サブディレクトリへ移動し、
Markdown 内の相対リンクを移動後の位置に合わせて自動で張り替える。
密結合の docs/settings/ は一体のまま維持する。

使い方:
    python scripts/restructure_docs.py            # 実行（移動＋リンク修正）
    python scripts/restructure_docs.py --dry-run  # 変更内容の確認のみ
"""

from __future__ import annotations

import posixpath
import re
import shutil
import sys
from pathlib import Path

# リポジトリルート（このスクリプトの1つ上）
ROOT = Path(__file__).resolve().parent.parent

# 移動マップ（リポジトリルート相対・posix）。末尾 "/" はディレクトリ接頭辞移動。
MOVES: list[tuple[str, str]] = [
    ("docs/series_arc_draft.md", "docs/plot/series_arc_draft.md"),
    ("docs/prototype_ep1_battle.md", "docs/manuscript/prototypes/prototype_ep1_battle.md"),
    ("docs/prototype_ep1_sword.md", "docs/manuscript/prototypes/prototype_ep1_sword.md"),
    ("docs/prototype_ep1_training.md", "docs/manuscript/prototypes/prototype_ep1_training.md"),
    ("docs/writing_style_notes.md", "docs/guides/writing_style_notes.md"),
    ("docs/storyboard/", "media/storyboard/"),
]

# Markdown リンク／画像リンクの target を捕捉
LINK_RE = re.compile(r"(!?\[[^\]]*\]\()([^)]+)(\))")


def remap(path: str) -> str:
    """リポジトリルート相対 posix パスを移動後の位置へ変換する。"""
    for old, new in MOVES:
        if old.endswith("/"):
            if path == old.rstrip("/"):
                return new.rstrip("/")
            if path.startswith(old):
                return new + path[len(old):]
        elif path == old:
            return new
    return path


def rewrite_links(text: str, file_old: str, file_new: str) -> tuple[str, int]:
    """1ファイル分のリンクを張り替える。戻り値: (新テキスト, 変更数)。"""
    dir_old = posixpath.dirname(file_old)
    dir_new = posixpath.dirname(file_new)
    changed = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal changed
        prefix, target, suffix = m.group(1), m.group(2), m.group(3)
        # 外部・アンカーのみ・絶対は対象外
        if re.match(r"^(https?:|mailto:|#|/)", target):
            return m.group(0)
        # アンカー分離
        anchor = ""
        path = target
        if "#" in target:
            path, anchor = target.split("#", 1)
            anchor = "#" + anchor
        if path == "":  # 純アンカー
            return m.group(0)
        # リンク先の現在位置（リポジトリルート相対）
        target_old = posixpath.normpath(posixpath.join(dir_old, path))
        target_new = remap(target_old)
        # ファイルもリンク先も動かないなら原文維持（無用な差分を避ける）
        if target_old == target_new and dir_old == dir_new:
            return m.group(0)
        new_path = posixpath.relpath(target_new, dir_new)
        if new_path + anchor != target:
            changed += 1
        return f"{prefix}{new_path}{anchor}{suffix}"

    return LINK_RE.sub(repl, text), changed


def main() -> None:
    dry = "--dry-run" in sys.argv

    # 対象 .md（docs 配下すべて＝移動前の現在位置）
    md_files = sorted(ROOT.joinpath("docs").rglob("*.md"))

    total_changed = 0
    # 1) 先にリンクを（移動後の位置を見越して）現在位置のファイルへ書き戻す
    for md in md_files:
        rel = md.relative_to(ROOT).as_posix()
        rel_new = remap(rel)
        text = md.read_text(encoding="utf-8")
        new_text, changed = rewrite_links(text, rel, rel_new)
        if changed:
            total_changed += changed
            print(f"  link x{changed:<2} {rel}")
            if not dry:
                md.write_text(new_text, encoding="utf-8")

    print(f"\nリンク張替え: {total_changed} 箇所" + ("（dry-run）" if dry else ""))

    # 2) ファイル／ディレクトリを移動
    print("\n移動:")
    for old, new in MOVES:
        src = ROOT / old.rstrip("/")
        dst = ROOT / new.rstrip("/")
        if not src.exists():
            print(f"  skip (なし) {old}")
            continue
        print(f"  {old}  ->  {new}")
        if not dry:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))

    print("\n完了" + ("（dry-run：変更なし）" if dry else ""))


if __name__ == "__main__":
    main()
