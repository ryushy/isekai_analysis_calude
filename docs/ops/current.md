# 現状スナップショット（中断復旧用）

> 「いま中断するなら、再開時にここから始めよ」を**最小限**で表す。
> セッション開始時にまず読み、終了時に必ず更新する。詳しい運用は [README.md](README.md)。

---

## 最終更新：2026-06-14

**フェーズ**：**Phase 0（舞台装置の設計）＝ほぼ完了**。設定の主要レイヤー（世界・戦闘・装備・成長・人物・勢力・連作）を規格書化し、第1話の核（喪失・容姿・10巻受容）まで確定。第1話の試作3本＋ストーリーボード3枚を作成。動画ワークフロー（storyboard/seedance スキル）と**管理基盤（ops/series/レビュースキル）を本セッションで導入**。

## いま走っているもの

- ✅ 設定規格書：[battle_system](../settings/battle_system.md)／[digital_tattoo](../settings/digital_tattoo.md)／[anomaly_mark](../settings/anomaly_mark.md)／[dungeon_design](../settings/dungeon_design.md)／[fab_persona](../settings/fab_persona.md)／[factions](../settings/factions.md)／[protagonist_core](../settings/protagonist_core.md)
- ✅ 第1話試作3本：[prototypes/](../manuscript/prototypes/)（静止した雨／剣のひと／ひと晩寝かせる）
- ✅ **第1話 本文 v0.4**：[manuscript/book1/01-01_modori_jirushi.md](../manuscript/book1/01-01_modori_jirushi.md)「戻り標」（横浜＝学校:山手／ダンジョン:みなとみらい駅。**漢字LN是正＋シールド統一済**・空白除き約6,000字＝NG0/WARN0）。レビュー＝[review/01-01_*](../review/)。**1話の目安字数5,500〜6,500・密度の四要素**を [guides/writing_style_notes §4.5](../guides/writing_style_notes.md)・[roadmap §3](../project_roadmap.md) に制度化
- ✅ ストーリーボード3枚（確定容姿v2）：[../../media/storyboard/](../../media/storyboard/)（剣・バトル）＋ストーリーボードリポジトリ（訓練）
- ✅ 制作スキル：`storyboard`／`seedance`（codex MCP・Higgsfield 確認済）
- ✅ 管理基盤：ops三層・series台帳（canon/timeline/disclosure/episode_id）・レビュースキル3（reader-personas/editor-kawahara/editor-tsukikage）
- ✅ **第2話 本文 v0.2**：[manuscript/book1/02-01_mirareteita.md](../manuscript/book1/02-01_mirareteita.md)「見られていた」（篠宮澪 初登場・見逃しの三本足場・イレギュラー共闘＝点vs面・コスチューム変身・約5,700字＝NG0/WARN0）。
- ✅ Git運用：ブランチ運用＋フック（pre-commit/commit-msg/post-commit＋Claude SessionStart/Stop）＋`git-flow`スキル。**第2話プロット・ヒロイン設定・学校確定まで main へマージ済**。**本セッション分（ヒロイン確定v0.2・ep2_plot v0.3・第2話本文v0.2・コスチューム機構C-027・文体ルールv0.2）は未コミット**。

## 次のアクション（優先順）— ★ここから再開する

> 直近の流れ：第1話 v0.3 → 第2話プロット → ヒロイン置換 → 学校確定 → **本セッション：ヒロイン確定（篠宮澪／外付け弓／聖稜学院・山手聖二葉女学院）→ 著者FB「葛藤が唐突」→見逃しの三本足場（手順/弓道の規律/第3勢力＝ダンジョンのイレギュラー共闘）で再設計→第2話本文化→著者FB（漢字レベル是正・シールド化・コスチューム変身機構）反映**。

1. **【推奨・次の一手】本セッション成果を main へマージ**（`git-flow`）：ヒロインv0.2・ep2_plot v0.3・第2話本文v0.2・digital_tattoo §6.5＋C-027（コスチューム）・writing_style §1.1（漢字レベル）・canon/locations/protagonist 反映。
2. **第2話レビュー**：reader-personas（離脱/整合）／editor-kawahara（見逃しのロジック＝唐突さが解消されたか）／editor-tsukikage（テンポ・澪の口調の地の文判別）。
3. 任意：ストーリーボード再試作（澪の深層コスチューム＝image.png黒髪版／点vs面のイレギュラー絵）。

- **開示厳守**：重力/量子/4学派/Mythos/偽origin/喪失真相/"上"の正体は完全隠蔽（大弧I前半）。B2段階の上限＝[disclosure_ledger](../series/disclosure_ledger.md)。

## 引っかかり・判断待ち

- ✅ **第1話の漢字レベル是正＝完了**（v0.4＝LN相当・シールド統一・NG0/WARN0）。第1話・第2話の文体基準がそろった。
- **剣の少年＝温存**：後巻の近接ライバル候補（聖光モチーフ男子校）。当てる巻は series_arc 設計時。
- **イレギュラーの収束のさせ方[未決]**：第2話で誰が・何で鎮めたか（一過性の扱い）は本文で曖昧化したまま＝後で要設計（ep2_plot §5）。
- 主人公の正式名（現「ナギ」仮）・どの国の欧米ハーフか（あざ意匠と連動）＝[protagonist_core 残課題](../settings/protagonist_core.md)。
- 4学派の人物・組織名は全て仮（[factions 残課題](../settings/factions.md)）。

## 改訂履歴（直近5世代）

| 日付 | 更新概要 |
|---|---|
| 2026-06-14 | 初版。Phase0 完了間際の状態＋管理基盤導入を記録 |
| 2026-06-14 | 第2話プロット作成→**剣の少年を弓道狙撃ヒロイン（監視役・見逃す葛藤型）へ置換**（[heroine_core.md](../settings/heroine_core.md) 新設）。**学校確定**（聖光/雙葉モチーフ・モチーフ化・C-025/C-026）。すべて main マージ済。**次の一手＝ヒロインのキャラ設計→第2話本文化** |
| 2026-06-14 | **ヒロイン確定**（篠宮澪／弓＝外付け支給品／聖稜学院・山手聖二葉女学院・容姿/口調/出自）。著者FB「葛藤が唐突」→**見逃しの三本足場**（手順/弓道の規律/**第3勢力＝ダンジョンのイレギュラー共闘**＝弓と相性悪い"点の無い混沌"・点vs面）でヒロイン§1.5・ep2_plot v0.3 を再設計。**第2話本文 v0.2 執筆**（NG0/WARN0）。著者FB反映＝**漢字レベルLN相当に是正（writing_style §1.1）**・《アンブレラ》＝**半透明のシールド**統一・**コスチューム変身機構**（digital_tattoo §6.5・C-027＝深層で能力外在化・澪=和風射手装束 image.png黒髪版）。**未コミット**＝次は main マージ＋第2話レビュー |
