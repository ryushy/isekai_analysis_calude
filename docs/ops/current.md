# 現状スナップショット（中断復旧用）

> 「いま中断するなら、再開時にここから始めよ」を**最小限**で表す。
> セッション開始時にまず読み、終了時に必ず更新する。詳しい運用は [README.md](README.md)。

---

## 最終更新：2026-06-14

**フェーズ**：**Phase 0（舞台装置の設計）＝ほぼ完了**。設定の主要レイヤー（世界・戦闘・装備・成長・人物・勢力・連作）を規格書化し、第1話の核（喪失・容姿・10巻受容）まで確定。第1話の試作3本＋ストーリーボード3枚を作成。動画ワークフロー（storyboard/seedance スキル）と**管理基盤（ops/series/レビュースキル）を本セッションで導入**。

## いま走っているもの

- ✅ 設定規格書：[battle_system](../settings/battle_system.md)／[digital_tattoo](../settings/digital_tattoo.md)／[anomaly_mark](../settings/anomaly_mark.md)／[dungeon_design](../settings/dungeon_design.md)／[fab_persona](../settings/fab_persona.md)／[factions](../settings/factions.md)／[protagonist_core](../settings/protagonist_core.md)
- ✅ 第1話試作3本：[prototypes/](../manuscript/prototypes/)（静止した雨／剣のひと／ひと晩寝かせる）
- ✅ **第1話 本文 v0.3**：[manuscript/book1/01-01_modori_jirushi.md](../manuscript/book1/01-01_modori_jirushi.md)「戻り標」（横浜＝学校:山手／ダンジョン:みなとみらい駅。レビュー反映＋密度up 約6,000字＝NG0/WARN0）。レビュー＝[review/01-01_*](../review/)。**1話の目安字数5,500〜6,500・密度の四要素**を [guides/writing_style_notes §4.5](../guides/writing_style_notes.md)・[roadmap §3](../project_roadmap.md) に制度化
- ✅ ストーリーボード3枚（確定容姿v2）：[../../media/storyboard/](../../media/storyboard/)（剣・バトル）＋ストーリーボードリポジトリ（訓練）
- ✅ 制作スキル：`storyboard`／`seedance`（codex MCP・Higgsfield 確認済）
- ✅ 管理基盤：ops三層・series台帳（canon/timeline/disclosure/episode_id）・レビュースキル3（reader-personas/editor-kawahara/editor-tsukikage）
- ✅ Git運用：ブランチ運用＋フック（pre-commit/commit-msg/post-commit＋Claude SessionStart/Stop）＋`git-flow`スキル。現在 `feature/infra-and-management` に成果コミット済（**main へのマージは未／著者承認待ち**）

## 次のアクション（優先順）

- ✅ **第1話 v0.3 完了**（横浜＝本牧自宅/山手駅学校/みなとみらいダンジョン・レビュー反映・約6,000字）。✅ **第2話プロット done**＝[../plot/ep2_plot.md](../plot/ep2_plot.md)「見られていた」。
1. **第2話 本文化**：[../plot/ep2_plot.md](../plot/ep2_plot.md) を新フロー（手触りをビートに仕込み済）で執筆→機械検査(--min/--max)＋セルフチェック→レビュー。
2. または **第1話 v0.3 再レビュー**（v0.2指摘の解消確認）。
3. または **ストーリーボード再試作**：v0.3＋横浜実在地（みなとみらい駅アトリウム・山手・本牧）で。
- 重力/量子/4学派/Mythos/喪失真相は完全隠蔽（大弧I前半）。

## 引っかかり・判断待ち

- 主人公の正式名（現「ナギ」仮）・どの国の欧米ハーフか（あざ意匠と連動）＝[protagonist_core 残課題](../settings/protagonist_core.md)。
- 4学派の人物・組織名は全て仮（[factions 残課題](../settings/factions.md)）。
- レビュースキルのペルソナ profile は naro 由来の理論をそのまま使用（CVE-0 例での微調整は使いながら最適化）。

## 改訂履歴（直近5世代）

| 日付 | 更新概要 |
|---|---|
| 2026-06-14 | 初版。Phase0 完了間際の状態＋管理基盤導入を記録 |
