#!/usr/bin/env python3
"""原稿の機械検査（CVE-0）。「AI 執筆の癖」を人格レビューの前に機械検出する。

naro_novel の check_manuscript.py のエッセンスを抽出し、CVE-0 向けに移植。
**読み取り専用・自動修正なし**。

CVE-0 の核：
  - 最重要＝**git 用語の表層露出**（著者要件B）。本文・台詞・技名に commit/repo/deploy 等を出さない。
  - ライトな現代口語（難語・古風・硬い造語を避ける）。
  - 開示台帳（docs/series/disclosure_ledger.md）の早出し語を警告。

検査項目:
    [NG]   1. git 用語の表層露出        … commit/repo/push/merge/deploy/origin 等
    [NG]   2. メタ作者用語・強          … 主人公/ヒロイン/伏線/クライマックス/本作/地の文 等
    [WARN] 3. メタ作者用語・弱          … 読者/展開/回収/視点/場面（別義あり要目視）
    [NG]   4. 章番号参照               … 「第二章で」型を本文に書かない
    [NG]   5. 地の文太字               … 「」『』・引用(>)以外の **...**
    [WARN] 6. 難語・古風語             … 残滓/邂逅/慟哭 等（ライト口語に置換）
    [WARN] 7. 開示台帳の早出し語       … 偽origin/マスターオリジン/upstream/Mythos/心意 等（段階照合）
    [NG]   8. 異文字混入               … ハングル/キリル/タイ/アラビア 等
    [WARN] 9. 三点リーダ奇数連         … 「……」偶数連が標準
    [WARN] 10. ダーシ運用              … 単独行・会話直前・奇数連
    [WARN] 11. 半角感嘆・疑問符        … 本文は全角（！？）
    [WARN] 12. 読点過密                … 一文に読点6箇所以上
    [WARN] 13. 長文                    … 一文80字超（ライト口語は短文志向）
    [WARN] 14. 短行3連続              … 詩的一語改行の連続（演出過多）
    [WARN] 15. Markdownリンク残骸      … 本文中の [text](url)
    [WARN] 16. 字数範囲                … --min/--max 指定時のみ
    [WARN] 17. 呼称ゆれ                … 同一人物に複数の敬称（〇〇先輩／〇〇さん）が混在＝要目視

使い方:
    python scripts/check_manuscript.py docs/manuscript/prototypes/prototype_ep1_battle.md
    python scripts/check_manuscript.py docs/manuscript/prototypes/
    python scripts/check_manuscript.py <file> --min 1500 --max 4000

終了コード: NG が1件以上 → 1、NG なし → 0
"""

from __future__ import annotations

import argparse
import io
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

# 1. git 用語（表層露出は最大の禁忌。大文字小文字無視で英語＋カナ）
GIT_TERMS = [
    "commit", "repository", "repo", "push", "pull request", "pull", "merge",
    "branch", "fork", "clone", "deploy", "origin", "upstream", "rebase",
    "bisect", "blame", "append-only", "force-push", "force push", "rollback",
    "revert", "checkout", "staging", "pull-request",
    "コミット", "リポジトリ", "プッシュ", "マージ", "ブランチ", "フォーク",
    "デプロイ", "オリジン", "リベース", "アペンドオンリー",
]

# 2. メタ作者用語・強（地の文・台詞に出たらほぼ事故）
META_STRONG = [
    "群像", "主人公", "ヒロイン", "キャラクター", "モブ", "端役",
    "伏線", "クライマックス", "本作", "本章", "本話", "前章", "次章",
    "地の文", "一人称", "三人称", "読者諸君",
]

# 3. メタ作者用語・弱（別義あり＝要目視）
META_WEAK = ["読者", "展開", "回収", "役割", "視点", "場面"]

# 6. 難語・古風語（ライト現代口語に反する。要置換の目安。文脈で可の場合あり＝WARN）
HARD_WORDS = [
    "残滓", "邂逅", "慟哭", "黎明", "刹那", "泰然", "傍証", "技倆", "旅嚢",
    "鐘楼", "灌木", "鎧戸", "瀟洒", "矜持", "怜悧", "嗚咽", "逡巡", "畢竟",
    "刹那的", "森羅万象", "森閑", "慄然", "蕭条",
]

# 7. 開示台帳の早出し注意語（docs/series/disclosure_ledger.md と照合）
DISCLOSURE_SENSITIVE = [
    "偽origin", "偽オリジン", "マスターオリジン", "upstream", "Mythos", "ミトス",
    "心意", "グラスウィング", "Fable", "Fable 5", "世界はgit", "分散台帳",
]

# 8. 異文字（日本語原稿に混入してはいけない文字ブロック）
RE_FOREIGN = re.compile(
    "[" "ᄀ-ᇿ가-힯㄰-㆏" "Ѐ-ӿ" "฀-๿" "؀-ۿ" "ऀ-ॿ" "]"
)

# 17. 呼称（敬称）。会話・地の文で人物をどう呼ぶか。同一人物に複数の呼び方が
#     混在したら WARN（話者で変わるのは正常＝要目視。表記ゆれ・取り違えの検出）。
HONORIFICS = [
    "先輩", "後輩", "先生", "師匠", "隊長", "団長", "殿下", "陛下",
    "さん", "くん", "ちゃん", "さま", "様", "殿", "氏", "嬢", "姫",
]
RE_APPELLATION = re.compile(
    r"([一-鿿ァ-ヶぁ-んA-Za-z々]{1,6}?)("
    + "|".join(map(re.escape, sorted(HONORIFICS, key=len, reverse=True)))
    + r")"
)
# 敬称の前が一般名詞で固有名でない（誤検出しやすい）ベースは除外
STOP_BASE = {
    "皆", "みな", "みんな", "お姉", "お兄", "おじ", "おば", "母", "父",
    "兄", "姉", "神", "お嬢", "お客", "お婆", "お爺", "おまわり", "お巡り",
    "おっ", "あの", "その", "この", "どの", "うち", "ねえ", "おねえ", "おにい",
}

RE_CHAPTER_REF = re.compile(r"第[0-9０-９一二三四五六七八九十百]+章")
KATAKANA = r"゠-ヿ"


@dataclass
class Finding:
    check_id: str
    severity: str
    line_no: int
    message: str


@dataclass
class FileReport:
    path: Path
    char_count_with_lf: int = 0
    char_count_body: int = 0
    findings: list[Finding] = field(default_factory=list)

    def add(self, check_id: str, severity: str, line_no: int, message: str) -> None:
        self.findings.append(Finding(check_id, severity, line_no, message))


def strip_html_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.DOTALL)


def mask_quotes(line: str) -> str:
    def _mask(m: re.Match[str]) -> str:
        return m.group(1) + "■" * len(m.group(2)) + m.group(3)

    line = re.sub(r"(「)([^「」]*)(」)", _mask, line)
    line = re.sub(r"(『)([^『』]*)(』)", _mask, line)
    return line


def iter_sentences(text: str):
    for line_no, line in enumerate(text.splitlines(), start=1):
        body = line.strip()
        if not body or body.startswith(("#", ">", "***", "|", "-", "*")):
            continue
        for sent in re.split(r"(?<=[。！？!?])", body):
            sent = sent.strip()
            if sent:
                yield line_no, sent


# 本文の終端マーカー（これ以降は作者ノート＝検査対象外）
RE_NOTE_HEADING = re.compile(r"^#{1,6}\s.*(検証メモ|改訂履歴|残課題|レビュー|設計メモ|改定履歴)")


def check_file(path: Path, args: argparse.Namespace) -> FileReport:
    report = FileReport(path=path)
    raw = path.read_text(encoding="utf-8")
    text = strip_html_comments(raw)
    lines = text.splitlines()

    # 作者ノート節（検証メモ・改訂履歴 等）以降は検査しない＝本文のみを対象にする
    for i, ln in enumerate(lines):
        if RE_NOTE_HEADING.match(ln.strip()):
            lines = lines[:i]
            break
    text = "\n".join(lines)

    body_lines = [ln for ln in lines if not ln.strip().startswith("#")]
    body_text = "\n".join(body_lines)
    report.char_count_with_lf = len(body_text)
    report.char_count_body = len(re.sub(r"\s", "", body_text))
    if args.min and report.char_count_with_lf < args.min:
        report.add("16-字数", "WARN", 0, f"改行込み {report.char_count_with_lf}字 < 下限 {args.min}字")
    if args.max and report.char_count_with_lf > args.max:
        report.add("16-字数", "WARN", 0, f"改行込み {report.char_count_with_lf}字 > 上限 {args.max}字")

    # 17. 呼称収集用： base -> {honorific -> [行番号...]}
    appellations: dict[str, dict[str, list[int]]] = {}

    prev_short_run = 0
    for line_no, line in enumerate(lines, start=1):
        stripped = line.strip()
        # メタ的な見出し・表・引用行は本文検査の一部を除外
        is_quote_line = stripped.startswith(">")
        is_meta_line = stripped.startswith(("#", "|", ">", "***", "---"))
        masked = mask_quotes(line)
        low = line.lower()

        # 見出し・表・引用（>）行＝作者側スキャフォールドは本文検査の対象外
        if not is_meta_line:
            # 1. git 用語（英語は小文字化して語境界、カナはそのまま）
            for term in GIT_TERMS:
                if term.isascii():
                    if re.search(rf"(?<![a-z]){re.escape(term)}(?![a-z])", low):
                        report.add("01-git用語", "NG", line_no, f"「{term}」（表層に git 用語を出さない＝著者要件B）")
                elif term in line:
                    report.add("01-git用語", "NG", line_no, f"「{term}」（表層に git 用語を出さない＝著者要件B）")

            # 4. 章番号参照
            for m in RE_CHAPTER_REF.finditer(line):
                report.add("04-章番号参照", "NG", line_no, f"「{m.group(0)}」（場面・時間表現に置換）")

        if not is_meta_line:
            # 2./3. メタ作者用語
            for w in META_STRONG:
                if w in line:
                    report.add("02-メタ用語強", "NG", line_no, f"「{w}」（作者視点の漏れ）")
            for w in META_WEAK:
                if w in line:
                    report.add("03-メタ用語弱", "WARN", line_no, f"「{w}」（別義なら可・要目視）")

            # 5. 地の文太字
            if not is_quote_line:
                for m in re.finditer(r"\*\*([^*]+)\*\*", masked):
                    if "■" not in m.group(1):
                        report.add("05-地の文太字", "NG", line_no, f"「**{m.group(1)}**」（本文に強調記号を使わない）")

            # 6. 難語・古風語
            for w in HARD_WORDS:
                if w in line:
                    report.add("06-難語", "WARN", line_no, f"「{w}」（ライト口語に置換を検討）")

            # 7. 開示台帳の早出し語
            for w in DISCLOSURE_SENSITIVE:
                if (w.isascii() and w.lower() in low) or (not w.isascii() and w in line):
                    report.add("07-早出し語", "WARN", line_no, f"「{w}」（開示台帳の段階と照合）")

            # 11. 半角感嘆・疑問符
            if "http" not in low:
                for m in re.finditer(r"[!?]", masked):
                    report.add("11-半角記号", "WARN", line_no, f"半角「{m.group(0)}」（全角に統一）")

            # 15. Markdown リンク残骸
            if re.search(r"\[[^\]]+\]\([^)]+\)", line):
                report.add("15-リンク残骸", "WARN", line_no, "Markdown リンク（本文には残さない）")

            # 17. 呼称（敬称）の収集（同一人物の呼び方ゆれを後で検出）
            for m in RE_APPELLATION.finditer(line):
                base, hon = m.group(1), m.group(2)
                if not base or base in STOP_BASE:
                    continue
                appellations.setdefault(base, {}).setdefault(hon, []).append(line_no)

        # 8. 異文字
        for m in RE_FOREIGN.finditer(line):
            report.add("08-異文字", "NG", line_no, f"「{m.group(0)}」（{unicodedata.name(m.group(0), '不明文字')}）")

        # 9. 三点リーダ
        for m in re.finditer(r"…+", line):
            if len(m.group(0)) % 2 == 1:
                report.add("09-三点リーダ", "WARN", line_no, f"「…」×{len(m.group(0))}（偶数連が標準）")
        if re.search(r"・・・|。。。", line):
            report.add("09-三点リーダ", "WARN", line_no, "「・・・」型（「……」に統一）")

        # 10. ダーシ
        if re.fullmatch(r"[―—]+", stripped):
            report.add("10-ダーシ", "WARN", line_no, "ダーシ単独行")
        if re.match(r"^[―—]+「", stripped):
            report.add("10-ダーシ", "WARN", line_no, "会話文直前ダーシ")
        for m in re.finditer(r"―+", line):
            if len(m.group(0)) % 2 == 1:
                report.add("10-ダーシ", "WARN", line_no, f"「―」×{len(m.group(0))}（偶数連が標準）")

        # 14. 短行3連続（詩的一語改行）
        if stripped and not is_meta_line and len(stripped) < 10:
            prev_short_run += 1
            if prev_short_run == 3:
                report.add("14-短行連続", "WARN", line_no, "短行3連続（一語改行の連続を避ける）")
        elif stripped:
            prev_short_run = 0

    # 12./13. 文単位
    for line_no, sent in iter_sentences(text):
        commas = sent.count("、")
        if commas >= 6:
            report.add("12-読点過密", "WARN", line_no, f"読点{commas}箇所：「{sent[:28]}…」")
        if len(sent) > 80:
            report.add("13-長文", "WARN", line_no, f"{len(sent)}字の一文：「{sent[:28]}…」")

    # 17. 呼称ゆれ：同一ベース名に2種以上の敬称が混在＝表記ゆれ／取り違えの疑い
    for base, hons in sorted(appellations.items()):
        if len(hons) >= 2:
            variants = "／".join(f"{base}{h}" for h in hons)
            first_line = min(min(v) for v in hons.values())
            report.add(
                "17-呼称ゆれ", "WARN", first_line,
                f"「{variants}」が混在（話者で変わるのは正常＝要目視。呼称表 docs/series/appellations.md と照合）",
            )

    return report


def collect_targets(paths: list[str]) -> list[Path]:
    targets: list[Path] = []
    for p in paths:
        path = Path(p)
        if path.is_dir():
            targets.extend(sorted(path.glob("*.md")))
        elif path.is_file():
            targets.append(path)
        else:
            print(f"  ⚠ 対象が見つかりません: {p}", file=sys.stderr)
    return targets


def main() -> int:
    parser = argparse.ArgumentParser(description="原稿の機械検査（CVE-0・読み取り専用）")
    parser.add_argument("paths", nargs="+", help="原稿ファイルまたはディレクトリ")
    parser.add_argument("--min", type=int, default=0, help="字数下限（改行込み。0で無効）")
    parser.add_argument("--max", type=int, default=0, help="字数上限（改行込み。0で無効）")
    args = parser.parse_args()

    targets = collect_targets(args.paths)
    if not targets:
        print("検査対象がありません。", file=sys.stderr)
        return 2

    total_ng = 0
    total_warn = 0
    for path in targets:
        report = check_file(path, args)
        ngs = [f for f in report.findings if f.severity == "NG"]
        warns = [f for f in report.findings if f.severity == "WARN"]
        total_ng += len(ngs)
        total_warn += len(warns)
        status = "❌" if ngs else ("⚠" if warns else "✅")
        print(f"\n{status} {path}  （改行込み {report.char_count_with_lf}字／空白除き {report.char_count_body}字）")
        for f in sorted(report.findings, key=lambda x: (x.severity != "NG", x.line_no)):
            mark = "NG  " if f.severity == "NG" else "WARN"
            loc = f"L{f.line_no}" if f.line_no else "-"
            print(f"   [{mark}] {f.check_id} {loc}: {f.message}")
        if not report.findings:
            print("   指摘なし")

    print(f"\n=== 合計: NG {total_ng}件 / WARN {total_warn}件 / 対象 {len(targets)}ファイル ===")
    return 1 if total_ng else 0


if __name__ == "__main__":
    sys.exit(main())
