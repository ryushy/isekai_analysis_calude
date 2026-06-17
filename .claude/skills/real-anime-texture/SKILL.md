---
name: real-anime-texture
description: Create prompts and image-generation direction for a hybrid live-action-realism plus soft anime illustration texture. Use when the user asks for images with realistic everyday urban details, cars, vending machines, storefronts, street furniture, documentary-like camera angles, or "実写とイラストが融合した質感", while still keeping characters as polished anime/illustration. Especially useful for Mio Shinomiya style tests, storyboard frames, and urban slice-of-life or chase-scene backgrounds.
---

# Real Anime Texture

Create image prompts that blend **real-world urban specificity** with **soft painterly anime characters**.

Use this skill for:

- "実写とイラストが融合した質感" images.
- Anime characters placed in realistic-feeling Japanese streets, parking lots, storefronts, train areas, or residential slopes.
- Prompts that need concrete everyday objects: cars, vending machines, menu boards, shop glass, utility poles, railings, bicycle parking, potted plants, street lamps.
- Day/night variants where the light source logic matters.

Do not ask the model to copy a specific artist, post, or screenshot. Generalize the observed visual grammar.

## Core Rule

Always combine these three layers:

1. **Realistic location skeleton**: believable camera, architecture, street furniture, vehicles, light sources, object scale.
2. **Painterly anime simplification**: softened background edges, watercolor/gouache bloom, simplified unreadable signs, leaf masses instead of every leaf.
3. **Clean character readability**: face, hands, hair silhouette, outfit, and pose remain crisp enough for a still image.

One-line style block:

```text
hybrid live-action realism and soft painterly modern anime still, realistic everyday Japanese urban details, documentary-like camera angle, believable cars and street furniture, watercolor-like bloom, simplified background edges, crisp character face and silhouette, clean still-image finish, no video compression artifacts
```

## Workflow

1. Identify the **camera pattern**:
   - elevated bench looking down into a street
   - low parking-lot view with vending machine and cars
   - storefront steps with menu board and potted plants
   - residential slope with diagonal handrail
   - narrow alley with walls close to camera

2. Add at least **two everyday reality anchors**:
   - cars, vending machine, menu board, shop glass, potted plants, utility wires, railings, parked bicycles, street lamps, traffic mirrors, concrete tire stops.

3. Set the **time-of-day lighting**:
   - Day: sun-washed cream walls, pale blue sky, yellow-green foliage, blue-grey shadows.
   - Midnight: blue-black ambient shadows plus real local lights: vending-machine glow, fluorescent tubes, street lamps, shop-window glow, apartment windows, car reflections.

4. Protect still-image quality:
   - Keep the character face, hands, hair silhouette, outfit, and key object edges clear.
   - Use softness only on foreground leaves, far background, light bloom, or motion-adjacent edges.
   - Avoid "screenshot blur" unless the user explicitly wants video-frame degradation.

5. Remove unwanted artifacts:
   - No readable signs, no logos, no watermark, no captions, no UI/HUD, no exact screenshot recreation.

For detailed prompt modules, read [references/urban-real-anime-texture.md](references/urban-real-anime-texture.md).

## Prompt Pattern

Use this structure:

```text
Subject: <character identity, outfit, pose, expression>
Scene/backdrop: <realistic everyday Japanese location with concrete objects>
Camera/composition: <height, lens feel, foreground/midground/background, diagonal lines>
Lighting/time: <day or midnight light logic>
Texture: hybrid live-action realism and soft painterly modern anime still; realistic object geometry; watercolor-like bloom; simplified background edges; crisp character face and silhouette; clean still-image finish.
Constraints: no readable text, no logos, no watermark, no exact screenshot recreation, no video compression artifacts, no muddy blur.
```

## Mio Defaults

When applying this to Mio Shinomiya, preserve her canon:

- 16-year-old fictional Japanese kyudo heroine.
- Glossy jet-black long hair in a high ponytail.
- Petite slender build, rounded youthful face, calm dark eyes.
- Surface look: navy Catholic mission-school uniform, rounded collar, small ribbon, soft short bolero, white blouse sleeves, knee socks, loafers.
- Include her slim cloth bow-wrap only when it naturally fits the scene.
- Keep movement "quietly fast" or composed. Avoid fanservice and awkward cropping.

## Quick Examples

Daytime vending-machine scene:

```text
Mio Shinomiya leans beside a red vending machine in a small Japanese covered parking lot, parked compact cars receding into the left background, metal roof beams and fluorescent tubes above, concrete floor with tire stops and soft reflections. Hybrid live-action realism and soft painterly modern anime still, believable vending machine geometry and car reflections, watercolor-like daylight bloom at the garage exit, crisp Mio face and navy uniform, simplified unreadable drink labels, no logos, no readable text, no watermark.
```

Midnight storefront scene:

```text
Mio Shinomiya sits on low steps outside a closed neighborhood cafe at midnight, menu board and potted plants beside her, dark glass door behind, quiet narrow street receding right with utility poles and a few apartment windows. Hybrid live-action realism and soft painterly modern anime still, blue-black ambient shadows, warm shop-window and menu-board glow, crisp face and hair silhouette, softened background edges, no readable signs, no watermark, no video compression artifacts.
```
