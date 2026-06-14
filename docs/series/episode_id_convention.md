# エピソードID命名規則（連作横断）

> 全10巻のエピソードを一意に識別するプロジェクトID規則。**物語全体→Book→章→話** の情報アドレス。
> 関連：[../plot/series_arc_draft.md](../plot/series_arc_draft.md)（全10巻構成）／[canon_log.md](canon_log.md)／[disclosure_ledger.md](disclosure_ledger.md)／[../ops/README.md](../ops/README.md)。

---

## 0. 一目で分かる版

| 項目 | 値 |
|---|---|
| **ID形式** | `B{巻}-{章2桁}-{話2桁}` |
| **例** | `B1-03-01`（第1巻 第3章 第1話） |
| **巻番号** | `B1`〜`B10`（全10巻・3大弧） |
| **特殊章番号** | `00`＝序章／`01`〜`NN`＝通常章／`EP`＝エピローグ／`IL`＝幕間 |
| **ファイル名** | `{章2桁}-{話2桁}_{slug}.md`（例：`03-01_frozen_rain.md`） |
| **章アウトライン** | `{章2桁}_outline.md`（例：`03_outline.md`） |
| **巻ディレクトリ** | `docs/manuscript/book{N}/`（執筆開始時に作成） |
| **試作（巻未確定）** | `docs/manuscript/prototypes/` に slug 名で置く（例：`prototype_ep1_battle.md`）。本採用時に B1-... へ昇格 |

---

## 1. 階層と責務（情報コントロールの単位）

| 階層 | アドレス | 正本ドキュメント | 何を管理するか |
|---|---|---|---|
| **物語全体（連作）** | 連作 | [../plot/series_arc_draft.md](../plot/series_arc_draft.md) | 3大弧・敵の階段・続編(upstream)・通しテーマ |
| **大弧（部）** | 大弧I/II/III | series_arc §大弧表 | 弧ごとの焦点・登る敵・開示の山 |
| **Book（巻）** | `B{N}` | `docs/manuscript/book{N}/book{N}_skeleton.md`（執筆時作成） | 巻の目的・章立て・到達点・隠蔽上限 |
| **章** | `B{N}-{章}` | `{章2桁}_outline.md` | 章の引き・カット割り・伏線の出し入れ |
| **話** | `B{N}-{章}-{話}` | `{章2桁}-{話2桁}_{slug}.md` | 本文。1話＝1公開単位の想定 |

- **開示の可否は必ず [disclosure_ledger.md](disclosure_ledger.md) で確認**：その章・話の「現在の開示段階」を超える描写は NG。
- **確定事実は [canon_log.md](canon_log.md)** に追記（IDで紐づけ）。

---

## 2. 表示書式

- 通常：`B1-03-01`。
- メディア案件との対応：ストーリーボード案件 slug（[../../media/](../../media/)）には対応する話IDを案件 README に明記（例：`isekai-cve0-battle-rain` ↔ B1-03 想定）。
- 連作通し話数（任意）：必要なら `ep.NNN`（3桁ゼロ埋め・全巻通し）を併記してよい。現時点は未公開のため必須としない。

---

## 3. 大弧と巻の対応（[../plot/series_arc_draft.md](../plot/series_arc_draft.md) 準拠）

| 大弧 | 巻 | 焦点（概略） |
|---|---|---|
| 大弧I | B1〜B3 | 覚醒・特訓・最初の仲間・4学派の登場 |
| 大弧II | B4〜B7 | 学派の政治・deploy の倫理・偽origin接近・**7巻 FAB 裏切り** |
| 大弧III | B8〜B10 | 起源への旅・黒幕・中心の誘惑・**10巻 受容**＋upstream 露見（続編へ） |

---

## 4. 改訂履歴

| 日付 | 内容 |
|---|---|
| 2026-06-14 初版 | naro_novel の命名規則を移植。全10巻 `B{N}-{章}-{話}`、階層別正本、試作→本採用の昇格ルール、大弧対応を規定 |
