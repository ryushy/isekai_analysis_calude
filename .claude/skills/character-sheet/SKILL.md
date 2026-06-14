---
name: character-sheet
description: Use this when the user wants to create or update a CVE-0 character production sheet (制作用・即参照シート) in docs/settings/character_sheet_<name>.md. Claude reads the canonical core doc (protagonist_core.md / heroine_core.md など正本) directly, then fills the fixed template — 0.基本 / 1.容姿・体型 / 2.服装 / 3.性格・ペルソナ / 4.口調・セリフ / 5.能力 / 6.関係 / 改訂履歴 — for visual / casting / acting / short-video reference. Respects canon_log・disclosure_ledger and project expression rules (FAB＝光のみ・git用語非表示). Use for キャラクターシート/キャラシート/character sheet requests. Do NOT use to design new settings from scratch — that is the 正本 (core doc) side.
---

# Character Sheet（キャラクターシート作成）

CVE-0 のキャラを **制作用・即参照シート** に起こす。
**役割分担：正本（core doc）が設計の根拠、本スキルはビジュアル/キャスティング/演技/短尺制作のための要約**。設定をゼロから創作せず、正本と台帳に準拠して要約・可視化する。

## 前提

- **正本が先**：キャラの設計根拠は `docs/settings/*_core.md`（[protagonist_core.md](../../../docs/settings/protagonist_core.md)／[heroine_core.md](../../../docs/settings/heroine_core.md) 等）にある。本シートはその要約。正本が無い新キャラは、先に正本を作るか著者に確認。
- **確定事実は台帳に従う**：[canon_log.md](../../../docs/series/canon_log.md)（確定）／[disclosure_ledger.md](../../../docs/series/disclosure_ledger.md)（開示可否）。未開示の核心は本文で出すと割れるので、シートでは扱いに注意（中盤開示等の注記を付す）。
- 出力先＝`docs/settings/character_sheet_<name>.md`（name は英数字。例：`character_sheet_mio.md`）。既存例＝[mio](../../../docs/settings/character_sheet_mio.md)／[nagi](../../../docs/settings/character_sheet_nagi.md)。
- テンプレート＝[references/template.md](references/template.md)（節構成・各表の列・書き方の定義）。

## ワークフロー

1. **対象キャラと正本を特定**：ユーザー指定のキャラ名から正本（`*_core.md`）と関連規格書（[digital_tattoo](../../../docs/settings/digital_tattoo.md)／[anomaly_mark](../../../docs/settings/anomaly_mark.md)／[fab_persona](../../../docs/settings/fab_persona.md) 等）を**直接読む**。既存シートがあれば更新、無ければ新規。
2. **リファレンス画像の確認**：容姿・体型・コスチュームの著者提示画像（`media/reference/` や `media/storyboard/参考画像/`）は**イラストイメージを伝えるための入力**。画像を Read で見て、髪・顔立ち・体型・雰囲気を**文章で記述**する。**シート本体に画像リンク・埋め込みは含めない**（画像は制作時の参照であってシートの一部ではない）。実在人物がモデルの場合も画像は載せず、必要なら「※雰囲気の参照（経歴等は断定しない）」の趣旨を文章に留める。
3. **GATE 準拠チェック**：(a) 全項目が正本・台帳・著者提示に遡れるか（憶測で能力や過去を盛らない）／(b) 未開示の核心（disclosure_ledger）を不用意に確定記述していないか／(c) 表現規則＝**FAB は淡い光のみ**（人型・顔・ロボット禁止）・**武器＝光の象徴**（金属でなく力の具現）・**git 用語は世界観上も非表示**。引っかかれば「創作補完」として分離し著者承認を仰ぐ。
4. **テンプレートで起票**：[references/template.md](references/template.md) の節構成（0〜6＋改訂履歴）で記述。ヘッダーに正本リンク・関連リンク・**ステータス（vX.Y＋日付）**を置く。一文目に正本との関係（「設計の根拠は ◯◯_core.md。本シートは要約」）を書く。
5. **対のシートと整合**：相手キャラのシート（例：主人公↔ヒロイン）と身長・関係・対比（点vs面 等）が食い違わないか相互参照。食い違えば指摘して片方を直す。
6. **§7 ビジュアルリファレンス仕様を書く**：動画制作で一貫した画を作れるよう、多角度（ターンアラウンド）・小物・**カラー指定**・プロンプト用キャラ正典ブロックを**言葉で**定義（[references/template.md §7](references/template.md)）。これが画像生成の台本になる。
7. **リファレンス画像を codex で生成（任意・著者が望んだ時）**：§7 の仕様を台本に、**画像生成は codex MCP（`mcp__codex__codex`）に依頼**＝`storyboard` と同じ役割分担（**Claude が台本＝プロンプト、codex は生成のみ**）。出力は `media/storyboard/<char-slug>/outputs/` 等に保存。プロンプトの作法・表現規則は [storyboard スキル](../storyboard/SKILL.md)／[character-canon](../storyboard/references/character-canon.md) に準拠（縦9:16・読める文字/数字/HUD なし・git 用語非表示・FAB＝光のみ）。多角度シートは「1枚に正面/斜め/横/背面＋表情差分、隅に番号のみ」の形で依頼。
8. **改訂履歴を記録**：末尾の表に日付・版・反映内容を追記。新規は v0.1。
9. **レビュー（任意）**：容姿・演技の妥当性は `actor-review`、テンポ・口調の判別は `editor-tsukikage`、構造は `editor-kawahara` へ回せる。

## 固定ルール

- **正本を上書きしない**：設定の追加・変更は正本側で行い、本シートは要約に徹する。矛盾を見つけたら正本を直す（勝手にシートだけ変えない）。
- **憶測禁止**：正本・台帳・著者提示に無い設定を埋めない。空欄は `[未決]` と明記。
- 表現規則：FAB＝淡い光のみ／武器＝光の象徴／**git 用語は非表示**。
- 実在人物リファレンスは雰囲気参照に限定（経歴等を断定しない）。
- 性的表現は健全・年齢相応（ラッキースケベ等は事故的接触・取り乱しの可笑しさで魅せ、過度な描写をしない）。
- 日本語で記述。氏名にはふりがなを添える。
- **画像生成は codex に依頼のみ**（プロンプト・設定の創作は codex にさせない）。生成手段が使えない場合 codex は課金せず正直に報告する旨を依頼文に明記。画像生成はユーザーが明示的に望んだ時のみ。
