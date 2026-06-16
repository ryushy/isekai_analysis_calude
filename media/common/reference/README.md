# common/reference/ — 共通参考画像（背景・横断利用）

> 複数話で使い回す参考画像置き場（プロジェクト共通）。
> **話固有の実在地参照**（コスモワールド・みなとみらい・山手学院など）は `media/book{N}/ep{M}/reference/` に置く。
> **案件固有の参照**は各 `…/storyboard/<case>/references/` に置く。主人公・キャラの顔参考は `media/common/characters/<char-slug>/references/model-photos/approved/`、採用済みキャラシートは `media/common/characters/<char-slug>/outputs/` に置く。

## 収録（共通背景・雰囲気参照）

| ファイル | 内容 | 用途 |
|---|---|---|
| `image.png` | 著者提示の参考画像（地下鉄駅＝秘密基地イメージ） | 秘密基地（[../backgrounds/honmoku-phantom-station-hideout/](../backgrounds/honmoku-phantom-station-hideout/)）の歪ませ元。キャラ雰囲気の参照にも使用 |

## キャラ参照の移動先

澪の人物・衣装参照は `common/characters/character-mio/` に整理済み。

| 種別 | 移動先 |
|---|---|
| 顔・体型リファレンス | `../characters/character-mio/references/model-photos/approved/mio_model_ref_20260614_201207.png` |
| 顔・体型リファレンス（別カット） | `../characters/character-mio/references/model-photos/approved/mio_model_ref_20260614_201259.png` |
| 深層衣装リファレンス | `../characters/character-mio/references/style/mio_deep_layer_archer_costume_yoimiya_ref.png` |

## 命名規則

`<対象>_<出典メモ>.<ext>`（実在地は話固有フォルダ側で `<対象>_<出典メモ>.png`）。

> 背景・衣装・雰囲気の共通参照はここ、人物モデル写真とキャラシートは `common/characters/` に置く。storyboard / seedance / character-sheet / stage-background スキルが見た目の寄せに使える（[../../../docs/settings/locations.md](../../../docs/settings/locations.md) の実在地モチーフと対応）。
