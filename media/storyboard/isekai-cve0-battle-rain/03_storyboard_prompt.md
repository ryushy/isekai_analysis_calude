# バトル「静止した雨」15秒ストーリーボード方針

保存先: `outputs/storyboards/storyboard_v1.png`

このファイルは画像生成前の確認用。codex はこのプロンプトを**一切変更せず**画像生成に使う（創作的追加・解釈変更は禁止）。

## Storyboard

```text
Create one 16:9 image containing a 3x3 grid of nine storyboard frames, numbered 1 to 9 in the corner of each frame. Modern cinematic anime style, near-future action anime look, moody but NOT horror, clean line art with atmospheric lighting and rain. Every frame is composed for a vertical 9:16 short-video crop inside the grid cell. Keep consistent character design, location, and color palette across all nine frames.

Character: Nagi, a 16-year-old half-Japanese half-Western boy. Light ash-blond / dirty-blond layered tousled hair with long side-swept bangs falling over the forehead, shorter sides; large striking light eyes (blue to blue-green); fair skin; refined, slightly androgynous features that read as MIXED heritage — mostly Western but with a subtle East-Asian softness around the eyes (clearly hapa / half-Japanese, hard to place); slim build; quiet, slightly melancholic. White-and-gold on-ear headphones resting around his neck; light casual modern clothes (dark tee, denim). Location: the third floor of a dungeon where a strange rain always falls but the ground never gets wet; mossy stone, faintly glowing bioluminescent fungus on the walls, cool blue-grey light. A recurring motif: a thin translucent protective membrane, a faint pale-blue glow, and a faint glowing birthmark under his bangs.

Frame 1: Wide shot of the rainy dungeon floor; Nagi calmly harvests glowing fungus from the wall into a pouch; everyday, relaxed mood; rain falls but the stone ground stays dry.
Frame 2: The rain sound cuts out; a fast mid-sized beast lunges at him from the gloom at impossible speed; sudden danger.
Frame 3: Nagi instantly raises a thin translucent protective membrane that catches the beast's fangs; the membrane strains and bends.
Frame 4: Close on Nagi behind the straining membrane; an unseen heavy weight presses it; the edges of his silhouette glow hot, he grimaces, near overflow.
Frame 5: Bullet-time: the rain freezes in mid-air; a falling droplet hangs still, the beast's fangs, splashed mud, and his white breath all frozen; total silence.
Frame 6: In the frozen world, the faint birthmark under Nagi's bangs glows warmly; a soft faint pale-blue presence (no face, no robot, just light) hovers near him.
Frame 7: Nagi's fingertip gently touches a single frozen raindrop; the contact point sparkles softly as understanding flows in.
Frame 8: Reality rewrites: above the beast a two-meter circle of sky goes dry, the rain there simply did-not-fall; the ground beneath turns dry and white, bared for the first time in ten years.
Frame 9: The world resumes motion; Nagi pushes off the dry white ground and slips sideways past the beast's charge; the birthmark still glows faintly; quiet awe.

Avoid readable text, captions, subtitles, numbers inside scenes other than the storyboard frame numbers, logos, UI elements, HUD digits, gauges, modern phones or computers, robots or android faces, gore, horror lighting, runes, magic circles, giant emblems. Cinematic, atmospheric, rain-soaked but clear.
```

## 生成後チェック（Claude Code が画像を見て確認）

- [ ] 9コマすべてが `01_highlight.md` の1-9と一致している
- [ ] 各コマが縦9:16構図で設計されている
- [ ] 場所（雨のダンジョン）・キャラデザイン・色調が9コマで一貫している
- [ ] カット5のバレットタイム（静止した雨）が明確に伝わる
- [ ] カット8の deploy（半径2mの地面が白く乾く）が画で伝わる
- [ ] FAB が人型・顔・ロボットになっていない（淡い光のみ）／あざが前髪の下で発光
- [ ] 番号以外の読める文字・数字・HUD が入っていない
