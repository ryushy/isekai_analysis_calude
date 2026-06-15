# 第1話ハイライト codex プロンプト集（直接生成用・コピペ）

> **用途**：codex で**直接**画像生成するための、全10カットの①背景プロンプト②キャラ込みプロンプト。
> 台本＝[01_highlights_script.md](01_highlights_script.md)。生成・レビューはユーザー側。
> **方針**：キャラ入りの静止画は**一発生成**（背景プレートに後乗せ＝合成はトーンがなじまず違和感が出るため不可）。背景のみが欲しい時は①、観賞用キャラ入りが欲しい時は②を使う。

## 共通ルール（全カット）

- **タッチ正典＝`outputs/hl_01_morning.png`**：柔らかい暖色の絵画調アニメイラスト・やわらかい光・**黒つぶれを作らない**。暗い重いフォトリアルに寄せない。
- **16:9・1920x1080**／**背景重視・人物は小さく**。
- **表現規則**：読める文字／数字／ロゴ／HUD／実在固有名なし。FAB・戻り標・能力＝**淡い光のみ**（人型/顔/ロボット不可）。武器＝金属でなく**光の象徴**。流血・グロなし。
- **背景区分**：**現実世界**（01/02/03/04/09/10）＝実写ベースで**構図を再現・改変しない**。**ダンジョン**（05/06/07/08）＝**改変可だが元構図はできるだけ維持**。
- **キャラ正典（ナギ）**：`Nagi — a tall, slim 16-year-old half-Japanese half-Western boy. Light ash-blond layered tousled hair with long side-swept bangs; white-and-gold on-ear headphones around his neck (a faint blue line glows on them only at the awakening moment); dark tee and denim, plain white sneakers; quiet, slightly melancholic.`（寄せ参照＝`media/common/characters/character-nagi/outputs/ref_sheet_v1.png`）
- **道化（敵・06/07のみ）**：`a tall thin DRIPPING CLOWN, skull-white theatrical painted face with a huge torn grin (makeup, NOT gore), a faded washed-out red costume dripping water; eerie but no blood, no real blade.`
- **実在地参照（03/04/09で必ず渡す）**：`media/common/reference/locations/yokohama-cosmoworld/cosmoclock21_2006_05_21.jpg`（昼の全景）／`media/book1/ep1/reference/コスモワールド2.png`（夜の虹色）／`コスモワールド1.png`（俯瞰）。コスモクロック21の固有性＝中心ハブの時計（数字なし）・全周の虹色ネオン・基部を巻いて水へ落ちる赤いコースター・基部の建物・運河の小島・背後にMM高層。

---

## 01 朝の下宿（現実世界）

**① 背景** → `outputs/plates/hl_01_morning_plate.png`
```
Interior of an old Japanese seaside boarding-house kitchen in early morning, warm steam rising from a pot of miso soup, a small ceramic dish of glossy brown simmered food on the table, soft golden window light, the hillside slope and a hint of distant rusty sea through the window. Absolutely NO people, empty room. Soft warm painterly anime-leaning illustration matching hl_01_morning.png's touch, no crushed blacks, 16:9, background plate. No text/numbers/logos/HUD.
```
**② キャラ込み** → `outputs/hl_01_morning.png`
```
Interior of an old Japanese boarding-house kitchen on a seaside hillside in early morning. Warm steam rising from a pot of miso soup, a small ceramic dish of glossy brown simmered food on the table, soft golden window light, the slope and a hint of a distant rusty sea through the window. A tall slim ash-blond boy with white-and-gold headphones around his neck sits SMALL near the window. Quiet domestic warmth; the temperature of ordinary daily life. Painterly cinematic semi-real anime illustration, 16:9, background-dominant, figure small. No text/numbers/logos/HUD.
```

## 02 煉瓦の校舎・誘い（現実世界）

**① 背景** → `outputs/plates/hl_02_school_plate.png`
```
Exterior of an old red-brick mission school on a Yokohama hillside, ivy-clad walls, small bell tower, Western-style arched windows, late-afternoon slanting light and long shadows, an empty courtyard. Absolutely NO people. Soft warm painterly anime touch matching hl_01, no crushed blacks, 16:9, background plate. No text/numbers/logos/HUD.
```
**② キャラ込み** → `outputs/hl_02_school.png`
```
Exterior of an old red-brick mission school on a Yokohama hillside, ivy-clad walls, a small bell tower, Western-style arched windows, late-afternoon slanting light and long shadows. Two small student figures in the courtyard, one casually gesturing as if proposing a dare; a tall ash-blond boy with headphones among them, small in the frame. Ordinary afterschool calm with a faint thread of unease. Painterly cinematic semi-real anime illustration, 16:9, background-dominant, figure small. No text/numbers/logos/HUD.
```

## 03 裏手・非常口（現実世界／実在コスモワールド再現）

**① 背景** → `outputs/plates/hl_03_threshold_plate.png`
```
The REAL Yokohama Cosmoworld at night around 21:00 just after closing — clean, lively and fully lit but empty. Cosmo Clock 21 giant Ferris wheel (white-to-pale-pink frame) with a large round CLOCK at its hub (glowing, no readable digits) and its whole rim in vivid RAINBOW neon, pastel gondolas; a red roller-coaster wraps the base and plunges toward water; the wheel straddles a low building; the park sits on a small island with canals, water and a quay in the foreground, glass Minatomirai towers behind. On the right edge a small side building has a closed rusted steel rear emergency door with plain tape; the air around that one door warps faintly as if seen through water. Absolutely NO people. Soft warm painterly anime touch matching hl_01, no crushed blacks, 16:9, background plate. No readable text/numbers/logos/HUD.
```
**② キャラ込み** → `outputs/hl_03_threshold.png`
```
The REAL Yokohama Cosmoworld at night around 21:00 just after closing — clean, lively and fully lit but empty of visitors. The iconic Cosmo Clock 21 giant Ferris wheel (white-to-pale-pink frame) with a large round CLOCK at its central hub (clock face glows but shows no readable digits) and its whole rim lit in vivid RAINBOW neon; pastel multicolor gondolas. A red roller-coaster track wraps the base of the wheel and plunges toward the water; the wheel straddles a low building at its base. The whole park sits on a small island surrounded by canals — water and a quay in the foreground, glass Minatomirai skyscrapers glowing behind. On the right edge, a small side building has a closed rusted steel rear emergency door with plain blank tape; the air right around that ONE door warps faintly as if seen through water. A small ash-blond boy with white-and-gold headphones stands distant near that door. Soft warm painterly anime-leaning illustration matching hl_01_morning.png's touch, no crushed blacks, 16:9, background-dominant, figure small. No readable text, no numbers, no logos, no HUD.
```

## 04 越境（現実世界／実在コスモワールドの非常口）

**① 背景** → `outputs/plates/hl_04_crossing_plate.png`
```
At the rear emergency door of the REAL Yokohama Cosmoworld (rainbow Cosmo Clock 21 and red coaster across the canal behind, Minatomirai towers — match references), the threshold: the rusted steel doorway has gone pitch black and is swallowing inward, the world 'peeling' like a turned page with faint spatial warping around the frame, a soft BLUE glow pooling on the wet ground in front of the open dark door. Absolutely NO people, empty stage ready for a figure. Soft warm painterly anime touch matching hl_01, no crushed blacks, dim but luminous, 16:9, background plate. Magic as soft light only. No text/numbers/logos/HUD.
```
**② キャラ込み** → `outputs/hl_04_crossing.png`
```
At the rear emergency door of the REAL Yokohama Cosmoworld (the Cosmo Clock 21 rainbow Ferris wheel and red coaster visible across the canal behind, glass Minatomirai towers — match the real-location references), the threshold moment of crossing INTO another world: the rusted steel doorway has gone pitch black and is swallowing a figure, the world 'peeling' like a turned page with faint spatial warping around the frame, a soft BLUE glow pooling at the feet on the wet ground. A tall ash-blond boy with white-and-gold headphones seen small, from behind, half-stepping into the dark portal. Soft warm painterly anime-leaning illustration matching hl_01_morning.png's touch, no crushed blacks, dim but luminous, 16:9, background-dominant, figure small. Magic shown as soft light only. No readable text, numbers, logos, HUD.
```

## 05 深層のカーニバル（ダンジョン／世界観の一枚）

**① 背景** → `outputs/plates/hl_05_carnival_plate.png`
```
The endless fire-and-forest carnival deep layer: a Ferris wheel turning with a frozen faceless human silhouette in each gondola (these are part of the eerie setting), rides half-swallowed by vines and young trees, stray fairy-lights like sparks of fire, record-rain suspended in the air. NO protagonist, no clown — empty stage. Soft warm painterly anime touch matching hl_01, gentle glow, no crushed blacks, dreamlike and uncanny but warm illustrative, 16:9, background plate. No text/numbers/logos/HUD.
```
**② キャラ込み** → `outputs/hl_05_carnival.png`
```
The endless fire-and-forest carnival deep layer KEEPING a warm soft touch (a Ferris wheel turning with a frozen human silhouette in each gondola, rides half-swallowed by vines and young trees, stray fairy-lights like sparks of fire, record-rain suspended in the air, a tiny ash-blond boy far below looking up). Soft warm painterly anime-leaning illustration matching hl_01_morning.png: gentle glow, NO crushed blacks, dreamlike and uncanny but warm and illustrative rather than dark photoreal. 16:9, background-dominant, figure tiny. No readable text, numbers, logos, HUD.
```

## 06 道化の登場（ダンジョン）

**① 背景** → `outputs/plates/hl_06_carousel_plate.png`
```
The carnival deep layer: a stopped, ornate merry-go-round half-swallowed by vines, a hand-cranked barrel organ beside it, ember fairy-lights, the Ferris wheel and forest behind, suspended record-rain. NO people, no clown — empty stage. Soft warm painterly anime touch matching hl_01, no crushed blacks, warm illustrative, 16:9, background plate. No text/numbers/logos/HUD.
```
**② キャラ込み** → `outputs/hl_06_clown.png`
```
In front of a stopped merry-go-round in the carnival deep layer, a tall thin dripping clown with skull-white theatrical makeup and a torn grin, faded washed-out red costume dripping, a hand-cranked barrel organ beside it; a small ash-blond boy with headphones faces it from the foreground. Soft warm painterly anime-leaning illustration matching hl_01_morning.png: gentle glow, NO crushed blacks, eerie and uncanny but warm and illustrative rather than dark photoreal horror; no gore, no blood, no real blade. 16:9, background-dominant, figure small. No readable text, numbers, logos, HUD.
```

## 07 《アンブレラ》で受ける（ダンジョン）

**① 背景** → `outputs/plates/hl_07_arena_plate.png`
```
The carnival deep layer, an open patch of wet ground in front of the stopped merry-go-round (clear foreground space ready for an action figure), ember lights, vines, the Ferris wheel behind, suspended record-rain, dynamic slightly low angle. NO people, no clown — empty stage. Soft warm painterly anime touch matching hl_01, no crushed blacks, 16:9, background plate. No text/numbers/logos/HUD.
```
**② キャラ込み** → `outputs/hl_07_umbrella.png`
```
Action moment in the carnival deep layer: a translucent half-dome shield of soft light raised by the boy (an umbrella of light, NOT metal), the dripping clown's jagged grin biting into the shield with straining sparks of light, a faint warm glow at the boy's chest, dynamic low angle. Soft warm painterly anime-leaning illustration matching hl_01_morning.png: gentle glow, NO crushed blacks, warm illustrative rather than dark photoreal. Abilities = symbolic light, not metal. 16:9. No readable text, numbers, logos, HUD.
```

## 08 雨が止まる（ダンジョン／覚醒）

**① 背景** → `outputs/plates/hl_08_rainstop_plate.png`
```
The carnival deep layer in bullet-time: record rain FROZEN in mid-air, every droplet suspended and motionless, total stillness, a luminous quiet hush, the Ferris wheel and vine-covered rides behind. NO people — empty stage. Soft warm painterly anime touch matching hl_01, gentle luminous glow, no crushed blacks, dreamy, 16:9, background plate. No text/numbers/logos/HUD.
```
**② キャラ込み** → `outputs/hl_08_rainstop.png`
```
Bullet-time in the carnival deep layer: the record rain FROZEN mid-air, every droplet suspended, the carnival paused, the white-and-gold headphones around the boy's neck glowing a faint BLUE line, the boy's fingertip reaching toward a single suspended raindrop with a tiny point of light, a small ash-blond boy quiet and luminous. Soft warm painterly anime-leaning illustration matching hl_01_morning.png; keep the luminous blue accents but soften them, NO crushed blacks, dreamy hush rather than dark photoreal. 16:9, background-dominant, figure small. Glow = soft light only. No readable text, numbers, logos, HUD.
```

## 09 現実への帰還（現実世界／実在コスモワールドの夕方）

**① 背景** → `outputs/plates/hl_09_return_plate.png`
```
The REAL Yokohama Cosmoworld at orange dusk early evening, the rainbow Cosmo Clock 21 and red coaster across the canal just beginning to light up (match references), glass Minatomirai towers behind, water and quay in foreground. On the right, the rusted rear emergency door with plain blank cordon tape, a faint soft warm 'return-marker' light fading by the doorway. Absolutely NO people — empty stage ready for figures. Soft warm painterly anime touch matching hl_01, no crushed blacks, 16:9, background plate. Return-marker as soft light only. No readable text/numbers/logos/HUD.
```
**② キャラ込み** → `outputs/hl_09_sunbreak.png`
```
The RETURN to reality: the two boys tumble back out through the rear emergency door of the REAL Yokohama Cosmoworld, emerging from a fading soft warm 'return-marker' light back into the ordinary world — it is still early evening, the sky orange with dusk, the real Cosmo Clock 21 rainbow Ferris wheel and red coaster across the canal just beginning to light up (match the real-location references), glass Minatomirai towers behind. Plain blank cordon tape and the rusted door beside them. A tall ash-blond boy with headphones pulls the other boy by the arm out into the real dusk, both small, clearly coming BACK to reality, relief. Soft warm painterly anime-leaning illustration matching hl_01_morning.png's touch, no crushed blacks, 16:9, background-dominant, figures small. Return-marker shown as soft light only. No readable text, numbers, logos, HUD.
```

## 10 その夜・喪失（現実世界）

**① 背景** → `outputs/plates/hl_10_night_plate.png`
```
Night, a small simple Japanese boarding-house tatami room, a futon on the floor, white-and-gold on-ear headphones resting on the floor beside it, deep dark blue night sky and a moonlit seaside slope faintly visible through the window. Absolutely NO people, empty room. Rich soft warm painterly anime touch matching hl_01's interior and detail, no crushed blacks, 16:9, background plate. No text/numbers/logos/HUD.
```
**② キャラ込み** → `outputs/hl_10_night.png`
```
Night, a small simple Japanese boarding-house tatami room (same warm aesthetic and level of detail/quality as hl_01_morning.png's interior), a futon on the floor, deep dark blue night sky and the seaside slope faintly visible through the window. A tall slim ash-blond boy sits SMALL on the futon, staring at his own open hand; his white-and-gold headphones rest nearby on the floor. A faint warm glow rests under his bangs on his forehead (a birthmark holding faint heat). Quiet, intimate, a small hollow loneliness. Rich soft warm painterly anime-leaning illustration matching hl_01_morning.png's touch and detail, no crushed blacks, 16:9, background-dominant, figure small. Glow = soft light only. No readable text, numbers, logos, HUD.
```

---

## codex 依頼の定型（参考）

> cwd＝リポジトリ直下／sandbox＝workspace-write／approval-policy＝never。プロンプトは一字一句変えず使用。実在地カットは上記の実写参照を必ず渡す。中間ファイル（コンタクトシート等）はリポジトリに残さない。生成できない場合は課金せず正直に報告。
