# 現状スナップショット（中断復旧用）

> 「いま中断するなら、再開時にここから始めよ」を**最小限**で表す。
> セッション開始時にまず読み、終了時に必ず更新する。詳しい運用は [README.md](README.md)。

---

## 最終更新：2026-06-14

**フェーズ**：**Phase 0（舞台装置の設計）＝ほぼ完了**。設定の主要レイヤー（世界・戦闘・装備・成長・人物・勢力・連作）を規格書化し、第1話の核（喪失・容姿・10巻受容）まで確定。第1話の試作3本＋ストーリーボード3枚を作成。動画ワークフロー（storyboard/seedance スキル）と**管理基盤（ops/series/レビュースキル）を本セッションで導入**。

## いま走っているもの

- ✅ 設定規格書：[battle_system](../settings/battle_system.md)／[digital_tattoo](../settings/digital_tattoo.md)／[anomaly_mark](../settings/anomaly_mark.md)／[dungeon_design](../settings/dungeon_design.md)／[fab_persona](../settings/fab_persona.md)／[factions](../settings/factions.md)／[protagonist_core](../settings/protagonist_core.md)
- ✅ 第1話試作3本：[prototypes/](../manuscript/prototypes/)（静止した雨／剣のひと／ひと晩寝かせる）
- ✅ ストーリーボード3枚（確定容姿v2）：[../../media/storyboard/](../../media/storyboard/)（剣・バトル）＋ストーリーボードリポジトリ（訓練）
- ✅ 制作スキル：`storyboard`／`seedance`（codex MCP・Higgsfield 確認済）
- ✅ 管理基盤：ops三層・series台帳（canon/timeline/disclosure/episode_id）・レビュースキル3（reader-personas/editor-kawahara/editor-tsukikage）
- ✅ Git運用：ブランチ運用＋フック（pre-commit/commit-msg/post-commit＋Claude SessionStart/Stop）＋`git-flow`スキル。現在 `feature/infra-and-management` に成果コミット済（**main へのマージは未／著者承認待ち**）

## 次のアクション（優先順）

1. **第1話プロット構成**（`B1-00`〜）を組む：確定した喪失の核を起点に、序章〜第1章の章立て・伏線の出し入れを [../series/disclosure_ledger.md](../series/disclosure_ledger.md) と照合しながら作る。→ `docs/manuscript/book1/` を作成し episode_id 規約で運用開始。
2. または **試作のレビュー**：移植したレビュースキルで現プロトタイプを多角検証（`reader-personas` 読者目線／`editor-kawahara` 川原礫＝アクセルワールド構造／`editor-tsukikage` テンポ）。
3. または **実動画化**：既存ストーリーボードを `seedance` で動画化（get_cost 確認の上）。

## 引っかかり・判断待ち

- 主人公の正式名（現「ナギ」仮）・どの国の欧米ハーフか（あざ意匠と連動）＝[protagonist_core 残課題](../settings/protagonist_core.md)。
- 4学派の人物・組織名は全て仮（[factions 残課題](../settings/factions.md)）。
- レビュースキルのペルソナ profile は naro 由来の理論をそのまま使用（CVE-0 例での微調整は使いながら最適化）。

## 改訂履歴（直近5世代）

| 日付 | 更新概要 |
|---|---|
| 2026-06-14 | 初版。Phase0 完了間際の状態＋管理基盤導入を記録 |
