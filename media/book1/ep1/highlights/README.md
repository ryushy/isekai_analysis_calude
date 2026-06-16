# 第1話「戻り標」ハイライト10枚（観賞用・16:9）

第1話の山場を**連続で見る**ための1枚絵×10（PC観賞用・16:9 横・背景重視）。
台本＝[01_highlights_script.md](01_highlights_script.md)／本文正典＝[01_modori_jirushi.md](../../../../docs/manuscript/book1/01_modori_jirushi.md)。

## 生成物（v1・codex `image_gen`・1920x1080）

| # | ファイル | 場面 |
|---|---|---|
| 01 | [outputs/hl_01_morning.png](outputs/hl_01_morning.png) | 朝の下宿・味噌汁と小鉢（日常の温度） |
| 02 | [outputs/hl_02_school.png](outputs/hl_02_school.png) | 煉瓦の校舎・悠の誘い |
| 03 | [outputs/hl_03_threshold.png](outputs/hl_03_threshold.png) | 裏手・非常口（**実在コスモワールド再現**＝コスモクロック21・21:00閉店後の活気ある夜景） |
| 04 | [outputs/hl_04_crossing.png](outputs/hl_04_crossing.png) | 越境・足元の青い光（実在コスモワールドの非常口から異界へ） |
| 05 | [outputs/hl_05_carnival.png](outputs/hl_05_carnival.png) | 深層の遊園地（炎と森のカーニバル＝世界観の一枚） |
| 06 | [outputs/hl_06_clown.png](outputs/hl_06_clown.png) | ずぶ濡れの道化（敵）登場 |
| 07 | [outputs/hl_07_umbrella.png](outputs/hl_07_umbrella.png) | 《アンブレラ》で受ける「重い」 |
| 08 | [outputs/hl_08_rainstop.png](outputs/hl_08_rainstop.png) | 雨が止まる（覚醒・ヘッドホンが青く灯る） |
| 09 | [outputs/hl_09_sunbreak.png](outputs/hl_09_sunbreak.png) | **抜け出して現実へ帰還**（実在コスモワールドの夕方の地上へ） |
| 10 | [outputs/hl_10_night.png](outputs/hl_10_night.png) | その夜・喪失（あざが淡く熱を持つ） |

## 背景プレート（人物なし・再利用基盤）

動画化や差し替えのため、**人物を描かない背景プレート**を別レイヤーで保持＝[outputs/plates/](outputs/plates/)（`hl_NN_*_plate.png` ×10）。キャラは [character-sheet](../../../../docs/settings/character_sheet_nagi.md) の正典を別参照で合成（[stage-background レイヤー方針](../../../../.claude/skills/stage-background/SKILL.md)）。`outputs/` のキャラ込み版＝観賞用。

## 複数生成と採用

今後は一発生成ではなく、生成回ごとの候補を [runs/](runs/) に残し、比較資料を [reviews/](reviews/) に置く。採用版だけを [outputs/](outputs/) に置く。

- 旧 `outputs_backup_20260615_132952/` は [runs/20260615_132952_previous_outputs/outputs/](runs/20260615_132952_previous_outputs/outputs/) に整理済み。
- 2026-06-15 の比較資料は [reviews/20260615_generation_compare/](reviews/20260615_generation_compare/) に整理済み。
- 人物の一貫性が必要な場合は、`media/common/characters/character-nagi/outputs/ref_sheet_v*.png` と、必要に応じて `references/model-photos/approved/` を参照する。

## 背景区分（現実世界／ダンジョン）

| 区分 | 方針 | 該当 |
|---|---|---|
| **現実世界** | 実写ベースで**構図を再現**（改変しない） | 01・02・03・04・09・10 |
| **ダンジョン** | **ご都合主義で改変可**（深層）。ただし**元構図はできるだけ維持** | 05・06・07・08 |

## 表現規則（厳守・全枚クリア）

読める文字／数字／ロゴ／HUD なし・FAB/能力＝淡い光のみ（人型/顔/ロボット非表示）・武器＝光の象徴・流血/グロなし。

## 改訂履歴

| バージョン | 内容 |
|---|---|
| v1（2026-06-15） | 10枚を 16:9・背景重視・人物小で初回生成（既存背景3枚＋ナギ正典をリファレンス・絵画調シネマティックで統一） |
| 03 改訂（2026-06-15） | 著者FB＝#03は現実世界側ゆえ荒廃NG。**21:00閉店後の無人だが清潔で活気ある夜の遊園地**へ再生成（構図維持・非常口の歪みのみ異物として残置） |
| v2 一括改訂（2026-06-15） | 著者FB（タッチのバラつき／実在地未再現／09のビート違い／10チープ）を根本原因まで特定し**8枚を再生成**。①**タッチ正典＝hl_01に固定**（05/06/07/08/10を暖色絵画調へ統一）②**実在コスモワールド（コスモクロック21）を再現**＝Web検索で実写取得→DNAカード化（03/04/09）③**09を「現実への帰還」に再設計**。01/02は基準として据え置き |
| 背景プレート化＋区分（2026-06-15） | 著者方針＝背景は人物なしプレートを基盤に、キャラは別参照で合成（両方保存）。**背景のみプレート10枚を `outputs/plates/` に生成**。**現実世界／ダンジョンの事前区分**を導入（現実=実写準拠で構図再現／ダンジョン=改変可だが元構図維持）。レイヤー方針・区分を stage-background/seedance スキルに明文化 |
