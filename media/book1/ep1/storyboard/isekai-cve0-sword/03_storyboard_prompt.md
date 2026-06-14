# バトル「剣のひと」15秒ストーリーボード方針

保存先: `outputs/storyboards/storyboard_v1.png`

このファイルは画像生成前の確認用。codex はこのプロンプトを**一切変更せず**画像生成に使う（創作的追加・解釈変更は禁止）。

## Storyboard

```text
Create one 16:9 image containing a 3x3 grid of nine storyboard frames, numbered 1 to 9 in the corner of each frame. Modern cinematic anime style, near-future action anime look, moody but NOT horror, clean line art with atmospheric lighting and rain. Every frame is composed for a vertical 9:16 short-video crop inside the grid cell. Keep consistent character design, location, and color palette across all nine frames.

Characters: (A) Nagi, a 16-year-old half-Japanese half-Western boy. Light ash-blond / dirty-blond layered tousled hair with long side-swept bangs over the forehead, shorter sides; large striking light eyes (blue to blue-green); fair skin; refined, slightly androgynous features that read as MIXED heritage — mostly Western but with a subtle East-Asian softness around the eyes (clearly hapa / half-Japanese); slim build. White-and-gold on-ear headphones around his neck; light casual modern clothes (dark tee, denim). (B) a calm full-Japanese teenage boy of the same age, dark hair and dark eyes (clearly contrasting with Nagi), with a glowing blue line sword tattoo on his right forearm. Location: the third floor of a dungeon where a strange rain always falls; mossy stone, faintly glowing bioluminescent fungus, cool blue-grey light. On the ground there is a dry pale circle about two meters wide where the rain has been erased.

IMPORTANT visual rule: the boy's sword is NOT real steel; it is a symbol of power made of glowing blue lines/light that slides out of his arm tattoo. It is a manifestation of ability, not a metal weapon.

Frame 1: Nagi stands catching his breath after a fight; at his feet a dry pale white patch of ground; rain falls all around but that patch stays dry.
Frame 2: From within the rain, a calm boy of the same age walks toward him; a glowing blue line sword tattoo on his right forearm faintly shines.
Frame 3: The boy points at the dry patch of ground and asks something; Nagi tenses, wary.
Frame 4: A faint pale-blue presence (no face, no robot, just light) hovers by Nagi's ear; Nagi presses his lips shut, tense.
Frame 5: The boy sweeps his right arm; the blue line slides out of his tattoo and forms a full-length sword made of glowing blue light, clean and deliberate.
Frame 6: Nagi flinches into a guard, but the light-sword is NOT aimed at him; its tip lightly touches the ground instead.
Frame 7: Where the sword touches, the dry two-meter patch ripples and warps; the erased dryness unravels and the rain returns, droplets falling back onto the ground.
Frame 8: Nagi catches his breath in awe; the boy lowers the sword and the blue light slides back into his arm tattoo; the boy gives a soft, slightly apologetic expression.
Frame 9: The two boys face each other quietly; the boy looks gentle, but the faint pale-blue presence beside Nagi dims and sinks low, an uneasy mood. Bittersweet, ominous calm.

Avoid readable text, captions, subtitles, numbers inside scenes other than the storyboard frame numbers, logos, UI elements, HUD digits, gauges, modern phones or computers, robots or android faces, realistic metal weapons, gore, horror lighting, runes, magic circles, giant emblems. Cinematic, atmospheric, rain-soaked but clear.
```

## 生成後チェック（Claude Code が画像を見て確認）

- [ ] 9コマすべてが `01_highlight.md` の1-9と一致している
- [ ] 各コマが縦9:16構図で設計されている
- [ ] 場所（雨のダンジョン）・2人のキャラデザイン・色調が9コマで一貫している
- [ ] **剣が金属でなく青い光の具現**になっている（力の象徴）
- [ ] カット7：剣が地面に触れ、乾いた地面が歪んで雨が戻る（魔法vs剣＝能力層）が伝わる
- [ ] FAB が人型・顔・ロボットになっていない（淡い光のみ）／末尾の不穏が出ている
- [ ] 番号以外の読める文字・数字・HUD が入っていない
