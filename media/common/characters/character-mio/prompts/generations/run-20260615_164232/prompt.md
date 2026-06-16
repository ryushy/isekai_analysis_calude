# ref_sheet_v3_cute_uniform prompt

目的：`ref_sheet_v2_face_model_refined.png` の顔特徴と深層衣装を維持しつつ、表層制服の肩まわりを修正する。v2 は肩のリボン状パーツが外側へ張り、肩パッド/戦闘服のように見えたため、ミッション女子校らしい「かわいい・柔らかい・自然な肩」に寄せる。

入力参照：

- `media/common/characters/character-mio/outputs/ref_sheet_v2_face_model_refined.png`: 編集元。顔、髪、体型、深層衣装、シート構成を維持。

生成プロンプト要約：

```text
Edit the visible Mio Shinomiya reference sheet. Keep the v2 face, hairstyle, body proportions, expression set, sheet layout, deep-layer crimson archer outfit, pale-gold light bow, and overall anime rendering style. Change only the surface school uniform design in the top full-body row and the school-uniform close-up row: remove the stiff shoulder-pad look and make the uniform cuter, softer, and more feminine.

Replace the hard angular shoulder flaps/padded-looking shoulder bows with small rounded puff sleeves under a soft short navy bolero; add a modest cute rounded collar and a neat small navy chest ribbon/bow; keep the white blouse and navy jumper skirt, but make the silhouette gentle and school-uniform-like rather than armor-like. Shoulders should look narrow and natural, not broad, not padded, not military. Use soft curves, light fabric, and elegant girlish details.

Change only the surface school uniform elements; do not alter the deep-layer archer costume, face shape, hair, poses, background, or color family. No readable text, no numbers, no logos, no watermark, no signatures, no HUD.
```

出力：

- `media/common/characters/character-mio/outputs/ref_sheet_v3_cute_uniform.png`
