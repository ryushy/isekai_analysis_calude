# isekai-cve0-battle-rain（バトル看板：静止した雨）

第1話バトル「静止した雨」を15秒9カットのショートに起こすケース。**出力はすべて claude プロジェクト内**に配置。フォーマットはストーリーボードリポジトリ（`chapter_short_pipeline_v3`）の規約を踏襲。

- 原稿（本文）: [docs/prototype_ep1_battle.md](../../../../../docs/manuscript/prototypes/prototype_ep1_battle.md)
- 設定参照: [docs/settings/battle_system.md](../../../../../docs/settings/battle_system.md)（§1 加速・二層／§4 deploy・crash／§9 短尺仕様）、[docs/settings/anomaly_mark.md](../../../../../docs/settings/anomaly_mark.md)（あざ）、[docs/settings/fab_persona.md](../../../../../docs/settings/fab_persona.md)、[docs/writing_style_notes.md](../../../../../docs/guides/writing_style_notes.md)

## このケースの一点

雨が空中で静止した世界で、ナギが雨粒に触れ、獣の頭上だけ「降らなかったこと」にする——半径2mの地面が十年ぶりに白く乾く deploy の瞬間。**バレットタイム×現実改変×あざの発光**という本作の看板ビジュアル。

## 成果物

| STEP | 成果物 | 担当 | 状態 |
|---|---|---|---|
| STEP1 ハイライト | [01_highlight.md](01_highlight.md) | Claude Code | ✅ |
| STEP3 ストーリーボードプロンプト | [03_storyboard_prompt.md](03_storyboard_prompt.md) | Claude Code | ✅ |
| STEP4 ストーリーボード画像 | **[outputs/storyboards/storyboard_v2.png](outputs/storyboards/storyboard_v2.png)（確定容姿・正）** ／ v1＝旧容姿 | codex（生成のみ） | ✅ |

## 固定ルール

1. 縦9:16構図（3x3グリッドの各コマ内）
2. 読める文字・数字・HUD を画面に出さない（**git 用語は世界観上も非表示**）
3. ライトな現代アニメ調・ムーディだがホラーにしない
4. FAB は淡い光のみ（人型・顔・ロボット禁止）／あざは前髪の下で淡く発光

## v1 所感・リテイク候補

- ◎ カット5（静止した雨）・カット7（指先と雨粒の接点）・カット1（発光菌糸の青いダンジョン）が特に良好。色調も9コマ一貫。
- △ カット6：あざの発光がやや弱い → 前髪の下の印をもう少し明確に。
- △ カット8：乾いた円が「ポータル」風に見える → 「空が乾く／地面が白くむき出し」をより明確化したい。
