# Urban Real-Anime Texture Reference

Use this reference when constructing detailed prompts for the hybrid real-world/anime texture.

## Visual Grammar

The target look is not pure watercolor anime and not photorealism. It is a layered mix:

- **Real-world skeleton**: objects must feel measured and plausible.
- **Anime simplification**: signs, leaves, windows, crowds, and distant shop detail are simplified.
- **Still-image polish**: character identity is clean and readable.

## Required Ingredients

### Camera

Use one clear camera logic:

- Elevated stair landing looking down into a shopping street.
- Low-to-mid camera beside a vending machine, with cars and roof beams in perspective.
- Ground-level view of storefront steps, menu board, potted plants, and receding street.
- Residential slope with diagonal railings and close apartment walls.

Prefer:

- 16:9 horizontal composition.
- Low or chest-height camera.
- One dominant diagonal line: handrail, stair, street edge, roof beam, curb, or wall.
- Foreground, midground, and background all present.

### Reality Anchors

Add two or more:

- parked compact cars
- red vending machine
- drink rows behind glass with unreadable labels
- menu board with food photos but no readable text
- potted plants
- shop glass door and reflections
- concrete steps
- metal handrails
- utility poles/wires
- bicycle parking
- street lamps
- convex traffic mirror
- roof beams
- fluorescent tubes
- concrete tire stops

### Day Palette

- sun-washed cream concrete
- pale blue sky
- yellow-green foliage
- blue-grey shadows
- warm beige railings
- simplified distant shop colors

Prompt words:

```text
high-key summer daylight, sun-washed cream concrete, pale blue sky, yellow-green foliage, blue-grey soft shadows, watercolor-like bloom, believable everyday urban details
```

### Midnight Palette

- blue-black ambient shadow
- warm vending-machine or shop-window glow
- cool fluorescent tubes
- amber street lamps
- dark car reflections
- damp-looking concrete sheen even without rain

Prompt words:

```text
midnight blue-black ambience, warm local light sources, vending-machine glow, fluorescent tubes, streetlamp pools, shop-window reflections, quiet after-hours mood
```

## Line And Paint Handling

Background:

- Simplify edges.
- Keep object geometry readable.
- Avoid hard photoreal concrete grain.
- Merge leaf clusters into light/dark masses.
- Make signs and labels decorative blocks, not text.

Character:

- Keep face, eyes, hands, hair silhouette, outfit, and pose clear.
- Let the same light hit the character and background.
- Use slightly cleaner linework on the character than on the background.
- Do not make the character look pasted onto a photo.

## Static Image Adjustment

When adapting from a video-like reference, include:

```text
clean still-image finish, no video compression artifacts, selective softness only on foreground leaves and distant background, crisp face and hands, clean hair silhouette, background edges simplified but not muddy
```

Avoid:

```text
low-resolution screenshot, overcompressed video frame, heavy blur on face, muddy background, readable labels, exact screenshot recreation
```

## Scene Recipes

### Bench Above Shopping Street

```text
weathered wooden bench at an elevated stair landing, old stone paving, paired street-lamp posts, notice boards with unreadable paper blocks, shopping street descending behind, small crowds and compact cars in the distance, summer daylight or quiet midnight street lamps
```

### Vending Machine And Parking Lot

```text
red vending machine on the right, rows of colorful drinks simplified behind glass, compact cars in a covered parking area on the left, metal roof beams, fluorescent lights, concrete floor, tire stops, convex safety mirror, real reflections but no readable labels
```

### Storefront Steps

```text
small neighborhood cafe entrance, dark glass door, tiled or brick column, grey concrete steps, black handrail, menu board with food-photo shapes but no text, potted plants, narrow street receding to the side
```

### Residential Slope

```text
close apartment buildings, cream walls, grey-green glass, diagonal warm beige handrails, dense green tree canopy, foreground hedge, pale blue sky gap with utility wires, summer bloom
```

## Negative Block

Use this unless the task requires otherwise:

```text
no readable text, no logos, no watermark, no captions, no UI, no HUD, no exact screenshot recreation, no video compression artifacts, no low-resolution screenshot, no muddy blur, no cyberpunk neon overload, no fantasy ruins, no photorealistic hard texture, no fanservice, no panty shot
```
