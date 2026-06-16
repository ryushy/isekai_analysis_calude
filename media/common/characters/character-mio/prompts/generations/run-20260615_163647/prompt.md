# ref_sheet_v2_face_model_refined prompt

目的：`references/model-photos/approved/` の2枚から、本人再現ではなく澪の顔特徴として「丸みのある輪郭・柔らかい頬・自然な小さめの口・落ち着いた大きな目・前髪の軽さ・凛と幼さの同居」を抽出し、v1 より汎用感の少ない設定画へ更新する。

入力参照：

- `media/common/characters/character-mio/outputs/ref_sheet_v1.png`: 既存レイアウト、制服、深層衣装、色、同一キャラ性の参照。
- `media/common/characters/character-mio/references/model-photos/approved/mio_model_ref_20260614_201207.png`: 凛とした表情、丸みのある若い顔、目元、前髪、静かな視線の参照。
- `media/common/characters/character-mio/references/model-photos/approved/mio_model_ref_20260614_201259.png`: 柔らかい笑顔、頬の丸み、自然な華奢さの参照。
- `media/common/characters/character-mio/references/style/mio_deep_layer_archer_costume_yoimiya_ref.png`: 緋色の和風射手装束モチーフの参照。

生成プロンプト要約：

```text
Recreate the existing character reference sheet for Mio Shinomiya with a less generic face, using the two approved model photos only as loose face/physique references, not as an exact portrait. Preserve Mio as a fictional 16-year-old Japanese kyudo archer heroine.

Mio Shinomiya, petite/slender Japanese girl, glossy jet-black long hair in a high ponytail with soft loose strands and airy bangs, fair skin, rounded youthful face, soft cheeks, delicate jawline, large calm dark-brown eyes with steady gaze but not overly generic, small natural nose, subtle mouth; composed and refined but with a childlike softness when she smiles.

Vertical character sheet with three bands: top band surface look turnaround in navy Catholic mission school uniform; middle band four close-up expressions: composed serious, gentle smile, flustered blush, focused archer gaze; bottom band deep-layer look turnaround in crimson Japanese archer costume with pale-gold light bow.

Polished modern anime character design sheet, clean production art, high detail, consistent face across every pose, soft painterly shading, plain warm light-gray studio background. No readable text, no numbers, no logos, no watermark, no metal weapon, no photorealism.
```

出力：

- `media/common/characters/character-mio/outputs/ref_sheet_v2_face_model_refined.png`
