# 夏の住宅街アニメ質感：プロンプト根本ルール

> 目的：X投稿動画のような「明るい夏の住宅街を、軽く走り抜けるアニメ背景」のタッチを、澪の画像生成に転用するための指示ルール。
> 注意：特定投稿・特定作者を名指しで模倣させるのではなく、観察した視覚特徴を一般化して指定する。

## 0. 一文で指定するなら

```text
soft painterly modern anime still, bright summer Japanese residential street, watercolor-like bloom, sun-washed cream concrete, pale blue sky, vivid green foliage, selective clean character linework, simplified background edges, airy motion, high-key daylight, no video compression artifacts
```

日本語なら：

```text
明るい夏の日本の住宅街を、柔らかい水彩寄りの現代アニメ背景として描く。白〜クリーム色の壁、淡い青空、強い夏光、鮮やかな緑、背景の線は溶かし、人物だけは静止画として読める程度に締める。
```

## 1. このタッチの核

この動画の質感は、次の組み合わせで成立している。

1. **夏光で飛んだ白い住宅壁**
   - クリーム色〜白いコンクリート壁を高輝度にする。
   - 壁面の汚れや凹凸は描くが、写実的なザラつきにはしない。
   - 影は黒でなく、青灰色・緑灰色で置く。

2. **低いカメラと斜め導線**
   - 道路、階段、手すり、塀、電線を斜めに走らせる。
   - カメラは子ども〜胸くらいの高さ、または地面すれすれ。
   - 画面に「走って通過する」方向を必ず作る。

3. **前景の葉・柱・手すりで速度を出す**
   - 前景の植え込み、手すり、壁端を少しだけ流す。
   - 背景全体をぼかすのではなく、近いものだけを柔らかくする。
   - 静止画ではブラーを控えめにし、葉は面でまとめる。

4. **人物だけは少し締める**
   - 顔、目、髪の輪郭、制服の襟・リボン・手は読みやすくする。
   - ただし線を硬くしすぎず、背景と同じ光に包む。
   - キャラだけ高精細な別絵にならないよう、影色を背景と合わせる。

5. **日常の狭さ**
   - 大きな観光地やランドマークではなく、住宅街、坂、階段、駐輪場、路地、塀、電線、ベンチ、植木鉢、自販機など。
   - 生活感はあるが、看板の文字やロゴは読ませない。

## 2. 画面設計ルール

### 構図

- 16:9の横長が基本。
- 画面の奥に抜ける細い道を作る。
- 斜めの主線を1本決める。
  - 例：手すり、坂道、塀、道路の白線、階段。
- 人物は中央に置きすぎない。
  - 右三分割か左三分割に寄せる。
  - 走っている方向に余白を少し残す。
- 前景に葉・手すり・壁端を入れて、奥行きを作る。

### カメラ

- 低めの追走カメラ。
- 画角はやや広角。
- 遠景より、近景・中景の生活物を大きく見せる。
- 上から俯瞰する時も、影と道の形で動きを見せる。

### 背景密度

- 手前：葉や手すりは大きな面、少し柔らかい。
- 中景：人物と接する建物・階段・壁は読める。
- 奥：窓や看板は簡略化。文字は描かない。
- 空：淡い青の抜けを小さく入れる。雲は少なめ。

## 3. 色と光のルール

### 基本パレット

| 要素 | 色の方向 |
|---|---|
| 壁 | 白、アイボリー、クリーム、薄ベージュ |
| 影 | 青灰、緑灰、淡いシアン寄りの暗部 |
| 空 | 淡い水色、白に近い青 |
| 葉 | 黄緑、夏の明るい緑、暗部は深緑 |
| 金属手すり | 温かいベージュ、薄い金茶、白いハイライト |
| アクセント | 制服の青、猫や小物のオレンジなど少量 |

### ライティング

- 主光源は上左か左前からの強い太陽光。
- ハイライトは少し飛ばす。
- 影を黒くしない。
- 木漏れ日を壁や制服に落とすと、このタッチに寄る。
- 逆光ではなく、横〜斜め前の夏光が向く。

## 4. 線・塗り・質感のルール

### 線

- 背景線は薄く、ところどころ溶かす。
- 人物線は背景より少し濃く、ただし細く柔らかい。
- 髪の外形と目元だけは綺麗に締める。
- 建物の直線を完全に定規的にしない。少し手描き感を残す。

### 塗り

- 背景は水彩・ガッシュ風の面で塗る。
- 葉は一枚ずつ描かず、光の当たる塊と影の塊で描く。
- 制服や髪は、背景より少しだけ情報量を増やす。
- 影の境界は柔らかいが、全部をぼかさない。

### 静止画向け調整

動画キャプと同じにすると、静止画では「ぼけた」「圧縮された」絵に見えやすい。静止画では次を必ず入れる。

- **no video compression artifacts**
- **clean still-image finish**
- **selective softness only in foreground leaves and distant background**
- **clear face, clear hands, clean hair silhouette**
- **background edges simplified but not muddy**

逆に避ける語：

- heavy motion blur
- blurry character
- low resolution screenshot
- noisy video frame
- smeared face
- overcompressed

## 5. 澪に適用する時のルール

### 表層・制服

澪をこのタッチで描く場合、もっとも相性が良いのは表層制服。

必須：

- 黒髪ハイポニーテール。
- 紺のミッション校制服。
- 白ブラウス、丸襟、小さな胸リボン、柔らかい短ボレロ。
- 弓巻は肩掛けか背中に細く固定。
- 表情は焦りすぎず、静かな集中。

動き：

- 走る、階段を上がる、手すりに軽く触れる、坂を駆ける。
- 派手な跳躍より、静かに速い動き。
- 髪とスカートは風で動かすが、過度にめくれさせない。

### 深層・緋色装束

深層装束にも使えるが、動画の生活感とは少し距離が出る。

- 背景は現実寄り住宅街を維持し、装束だけが異物として映える形にする。
- 光の弓は出しすぎない。出すなら背中・手元に小さく。
- 射線ビームは描かない。

## 6. コピペ用プロンプト骨格

### 背景だけ

```text
A bright summer Japanese residential street on a narrow slope or outdoor stairway between close apartment buildings, soft painterly modern anime background, watercolor-like bloom, sun-washed cream concrete walls, pale blue sky gap with thin utility wires, vivid green tree canopy and foreground hedge, warm beige handrails cutting diagonally through the frame, high-key daylight from upper left, blue-grey soft shadows, simplified background edges, airy nostalgic chase-scene mood, clean still-image finish. No people, no animals, no readable text, no logos, no watermark, no video compression artifacts.
```

### 澪入り・表層制服

```text
Mio Shinomiya, a petite 16-year-old Japanese kyudo heroine with glossy jet-black long hair in a high ponytail, soft rounded youthful face, calm dark eyes, wearing a navy Catholic mission-school uniform with rounded collar, small chest ribbon, white blouse sleeves, soft short bolero, knee socks, loafers, and a slim cloth bow-wrap over one shoulder. She runs lightly uphill along a warm beige handrail in a bright summer Japanese residential slope between close apartment buildings. Soft painterly modern anime still, watercolor-like bloom, sun-washed cream concrete, pale blue sky, vivid green foliage, blue-grey shadows, selective softness on foreground hedge and distant buildings, clear face and clean hair silhouette, airy motion but crisp still-image finish. No readable text, no logos, no watermark, no animals, no video compression artifacts, no fanservice, no panty shot.
```

### 澪入り・深層を少し混ぜる

```text
Mio Shinomiya in her crimson Japanese archer deep-layer costume, still current-era and not final form, moving quietly through a bright summer Japanese residential slope that remains grounded in everyday reality. Cream concrete walls, pale blue sky, green tree canopy, diagonal beige handrails, soft painterly anime background, watercolor-like bloom, high-key daylight, blue-grey shadows. Her pale-gold light bow is subtle and contained near her hand or back, with no visible beam and no continuous target line. Keep the scene clean, airy, and still-image crisp, with only foreground leaves softly blurred.
```

## 7. ネガティブ指定

```text
no watermark, no readable text, no captions, no logo, no exact screenshot recreation, no white-haired original girl, no copied character, no video compression artifacts, no heavy blur on face, no muddy background, no photorealistic hard texture, no cyberpunk, no fantasy ruins, no night, no rain, no over-detailed signage, no fanservice, no panty shot
```

## 8. 良し悪し判定

良い出力：

- 白い壁と緑が夏光で明るい。
- 手すり・坂・階段などの斜め導線がある。
- 背景は柔らかいが、澪の顔と制服は読める。
- 生活感があるのに、文字やロゴで画面が汚れていない。
- 「静かに速い」感じが出ている。

悪い出力：

- キャラだけ別の硬い美少女絵になっている。
- 背景が写実的すぎる、またはサイバーパンク・廃墟になる。
- 全体がぼけて静止画として弱い。
- 葉が細かすぎて画面がうるさい。
- 看板や文字が読める。
- 元動画の人物・猫・透かしをそのまま再現しようとしている。
