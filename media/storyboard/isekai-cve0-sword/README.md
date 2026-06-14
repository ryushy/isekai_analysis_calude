# isekai-cve0-sword（バトル：剣のひと／魔法vs剣）

第1話続き「剣のひと」を15秒9カットのショートに起こすケース。**出力はすべて claude プロジェクト内**に配置。フォーマットはストーリーボードリポジトリ（`chapter_short_pipeline_v3`）の規約を踏襲。

- 原稿（本文）: [docs/prototype_ep1_sword.md](../../../docs/manuscript/prototypes/prototype_ep1_sword.md)
- 設定参照: [docs/settings/battle_system.md](../../../docs/settings/battle_system.md)（§0 形と勝敗＝根本原則）、[docs/settings/digital_tattoo.md](../../../docs/settings/digital_tattoo.md)（剣型タトゥー・登録/野良）、[docs/settings/fab_persona.md](../../../docs/settings/fab_persona.md)、[docs/writing_style_notes.md](../../../docs/guides/writing_style_notes.md)

## このケースの一点

剣を持つ少年が現れる。だがその剣は斬る道具でなく「書かれたものを、なかったことにする」力。地面に触れただけで、ナギが乾かした2mが歪み雨が戻る。**剣＝力の象徴（金属でなく青い光）で、魔法vs剣が能力層で成立する**ことを画で実証するケース。

## 成果物

| STEP | 成果物 | 担当 | 状態 |
|---|---|---|---|
| STEP1 ハイライト | [01_highlight.md](01_highlight.md) | Claude Code | ✅ |
| STEP3 ストーリーボードプロンプト | [03_storyboard_prompt.md](03_storyboard_prompt.md) | Claude Code | ✅ |
| STEP4 ストーリーボード画像 | **[outputs/storyboards/storyboard_v2.png](outputs/storyboards/storyboard_v2.png)（確定容姿・正）** ／ v1＝旧容姿 | codex（生成のみ） | ✅ |

## 固定ルール

1. 縦9:16構図（3x3グリッドの各コマ内）
2. 読める文字・数字・HUD を画面に出さない（**git 用語・専門語は世界観上も非表示**）
3. **剣は金属でなく青い光の具現＝力の象徴**（現実の金属剣にしない）
4. FAB は淡い光のみ（人型・顔・ロボット禁止）

## v1 所感

- ◎ カット5（青い光の剣の具現）・カット7（剣が地面に触れ波紋＋雨が戻る）が看板原則「形は象徴／勝敗は能力層」を明確に画化。
- ◎ 雨の暗い青のダンジョン色調が9コマ一貫。FABの青い細い光も統一。
- 末尾カット9の不穏（FABの光が低く沈む）も出ており、「いい子だから報告する」の余韻に接続。
