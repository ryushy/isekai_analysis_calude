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
- ✅ Git運用：ブランチ運用＋フック（pre-commit/commit-msg/post-commit＋Claude SessionStart/Stop）＋`git-flow`スキル。**管理基盤・第2話プロット・ヒロイン設定・学校確定まで main へマージ済**（未コミット0）。

## 次のアクション（優先順）— ★ここから再開する

> 直近の流れ：第1話 v0.3 完了 → 第2話プロット作成 → **剣の少年を弓道狙撃ヒロインへ置換**（[heroine_core.md](../settings/heroine_core.md) 新設）→ **学校確定**（主人公校＝聖光学院モチーフ／ヒロイン校＝横浜雙葉モチーフ＝山手の同じ"洋の器"の丘・校名はモチーフ化＝作中仮名）。第2話は**初ヒロイン登場回**。

1. **【推奨・次の一手】ヒロインのキャラ設計を確定**：正式名（仮称「澪」）・容姿・口調・**作中校名の最終決定**（仮案＝山手聖二葉女学院／主人公校＝聖稜学院）・**弓型タトゥーの型**（外付け＝支給品／身体型＝個人）。→ 残課題＝[heroine_core.md §4](../settings/heroine_core.md)。初登場回なので名・容姿・口調が定まると本文密度が一発で出る。
2. **第2話 本文化**：[../plot/ep2_plot.md](../plot/ep2_plot.md)（v0.2.1＝手触り仕込み済・弓道狙撃ヒロイン版）を新フローで執筆→機械検査(`--min 5500 --max 6500`)＋セルフチェック §2.5→レビュー（reader-personas/editor-kawahara/editor-tsukikage）。
3. 任意：第1話 v0.3 再レビュー／ストーリーボード再試作（v0.3＋横浜実在地・ヒロイン弓道）。
- **開示厳守**：重力/量子/4学派/Mythos/偽origin/喪失真相/"上"の正体は完全隠蔽（大弧I前半）。B2段階の上限＝[disclosure_ledger](../series/disclosure_ledger.md)。

## 引っかかり・判断待ち

- **ヒロイン詳細[未決]**：正式名（澪仮）・容姿・口調・**作中校名**（横浜雙葉モチーフのモチーフ化）・弓型タトゥーの型・監視者になった経緯＝[heroine_core.md §4](../settings/heroine_core.md)。
- **作中校名のモチーフ化[未決]**：主人公校（聖光モチーフ・仮案 聖稜学院）／ヒロイン校（雙葉モチーフ・仮案 山手聖二葉女学院）。**実名は内部資料のモチーフ基準のみ・本文には出さない**（著者方針）。
- **剣の少年＝温存**：後巻の近接ライバル候補（聖光モチーフ男子校）。当てる巻は series_arc 設計時。
- 主人公の正式名（現「ナギ」仮）・どの国の欧米ハーフか（あざ意匠と連動）＝[protagonist_core 残課題](../settings/protagonist_core.md)。
- 4学派の人物・組織名は全て仮（[factions 残課題](../settings/factions.md)）。

## 改訂履歴（直近5世代）

| 日付 | 更新概要 |
|---|---|
| 2026-06-14 | 初版。Phase0 完了間際の状態＋管理基盤導入を記録 |
| 2026-06-14 | 第2話プロット作成→**剣の少年を弓道狙撃ヒロイン（監視役・見逃す葛藤型）へ置換**（[heroine_core.md](../settings/heroine_core.md) 新設）。**学校確定**（聖光/雙葉モチーフ・モチーフ化・C-025/C-026）。すべて main マージ済。**次の一手＝ヒロインのキャラ設計→第2話本文化** |
