"""Markdown 相対リンクの健全性チェッカー（再利用・git フックからも使用）。

使い方:
    python scripts/check_links.py            # docs/ media/ .claude/skills/ を検査
    python scripts/check_links.py --quiet    # 出力抑制（戻り値のみ。フック用）
    python scripts/check_links.py docs        # 対象ディレクトリ指定
戻り値: 破損リンクがあれば 1、無ければ 0。
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
DEFAULT_ROOTS = ["docs", "media", ".claude/skills"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true", help="出力を抑制し戻り値のみ返す")
    ap.add_argument("roots", nargs="*", help="検査対象ディレクトリ（既定: docs media .claude/skills）")
    args = ap.parse_args()
    roots = args.roots or DEFAULT_ROOTS

    checked = 0
    broken = 0
    for base in roots:
        base_path = ROOT / base
        if not base_path.exists():
            continue
        for md in base_path.rglob("*.md"):
            text = md.read_text(encoding="utf-8")
            for m in LINK_RE.finditer(text):
                target = m.group(1)
                if re.match(r"^(https?:|mailto:|#|/)", target):
                    continue
                path = target.split("#", 1)[0]
                if not path:
                    continue
                checked += 1
                if not (md.parent / path).resolve().exists():
                    broken += 1
                    if not args.quiet:
                        print(f"BROKEN: {md.relative_to(ROOT).as_posix()} -> {target}")

    if not args.quiet:
        print(f"チェック {checked} リンク / 破損 {broken}")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
