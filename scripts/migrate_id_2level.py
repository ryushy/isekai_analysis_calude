"""エピソードID 3階層→2階層 移行スクリプト（ワンショット）。

`B{巻}-{章2桁}-{話2桁}` → `B{巻}-{話2桁}` へ簡略化し、「章」を廃止する
（episode_id_convention.md 2026-06-15 改定）。

実施内容:
  1. ファイル名のリネーム: `{NN}-01_{slug}.md` → `{NN}_{slug}.md`
     （本文 docs/manuscript/ ＋ レビュー docs/review/）
  2. 全 docs/*.md の本文置換:
     - ID 表記   `B{巻}-{NN}-{NN}` → `B{巻}-{NN}`（末尾の話番号を落とす）
     - リンク内のファイル名語幹 `{NN}-01_` → `{NN}_`

使い方:
    python scripts/migrate_id_2level.py --dry-run  # 変更内容の確認のみ
    python scripts/migrate_id_2level.py            # 実行（git mv ＋ 本文置換）
"""

from __future__ import annotations

import io
import re
import subprocess
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

# リポジトリルート（このスクリプトの1つ上）
ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# ID 表記: B{巻}-{章2桁}-{話2桁} → B{巻}-{章2桁}（章番号を新・話番号として残す）
ID_PATTERN = re.compile(r"B(\d+)-(\d{2})-\d{2}")
# リンク/ファイル名語幹: {NN}-01_ → {NN}_
STEM_PATTERN = re.compile(r"(\d{2})-01_")
# リネーム対象ファイル名: {NN}-01_{slug}.md
RENAME_PATTERN = re.compile(r"^(\d{2})-01_(.+\.md)$")

# 本文置換から除外（旧IDを意図的に記述している規約・改訂台帳）
EXCLUDE_FROM_TEXT = {"episode_id_convention.md"}


def replace_text(text: str) -> str:
    """ID 表記とリンク語幹を2階層形式へ置換する。"""
    text = ID_PATTERN.sub(r"B\1-\2", text)
    text = STEM_PATTERN.sub(r"\1_", text)
    return text


def main() -> None:
    dry_run = "--dry-run" in sys.argv

    md_files = sorted(DOCS.rglob("*.md"))

    # --- 1. 本文置換 ---
    changed_texts: list[Path] = []
    for path in md_files:
        if path.name in EXCLUDE_FROM_TEXT:
            continue
        original = path.read_text(encoding="utf-8")
        updated = replace_text(original)
        if original != updated:
            changed_texts.append(path)
            if not dry_run:
                path.write_text(updated, encoding="utf-8")

    # --- 2. ファイル名リネーム（git mv）---
    renames: list[tuple[Path, Path]] = []
    for path in md_files:
        m = RENAME_PATTERN.match(path.name)
        if m:
            new_name = f"{m.group(1)}_{m.group(2)}"
            renames.append((path, path.with_name(new_name)))

    for old, new in renames:
        if not dry_run:
            subprocess.run(
                ["git", "mv", str(old.relative_to(ROOT)), str(new.relative_to(ROOT))],
                cwd=ROOT,
                check=True,
            )

    # --- サマリ出力 ---
    head = "【dry-run】" if dry_run else "【実行】"
    print(f"{head} 本文置換: {len(changed_texts)} ファイル")
    for path in changed_texts:
        print(f"  - {path.relative_to(ROOT).as_posix()}")
    print(f"{head} リネーム: {len(renames)} ファイル")
    for old, new in renames:
        print(f"  - {old.relative_to(ROOT).as_posix()} → {new.name}")


if __name__ == "__main__":
    main()
