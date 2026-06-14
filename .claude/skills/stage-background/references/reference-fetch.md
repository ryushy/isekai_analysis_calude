# 実在地リファレンス自動取得フロー（Web検索→分析→キャッシュ）

実在地ベースの背景／ハイライトを描くとき、参考写真を**毎回手で用意せず**、Web検索で取得・分析して**ロケーション別カードに一度だけ蓄積**し、以後は再利用する。

## いつ使うか

- 背景・ハイライト・ストーリーボードで**実在地**（みなとみらい、本牧、山手 等）を再現したいが、案件フォルダに実写参照が無い／不足しているとき。
- 既に `media/common/reference/locations/<slug>/REFERENCE.md` があれば**それを使う**（再取得しない＝煩雑回避の要）。

## 手順

1. **ロケーション特定**：実在地の正式名（例「横浜コスモワールド コスモクロック21」）と、絵に要る要素（全景／近接／夜景／俯瞰）を決める。slug を付ける（例 `yokohama-cosmoworld`）。
2. **キャッシュ確認**：`media/common/reference/locations/<slug>/REFERENCE.md` があれば終了（そのDNA＋実写を使う）。無ければ続行。
3. **Web検索（自由ライセンス優先）**：`WebSearch` を `allowed_domains:["commons.wikimedia.org"]` 等で叩き、`File:...` ページURLを集める（Wikimedia Commons＝直リンク可・ライセンス明確）。
4. **ダウンロード**：`media/common/reference/locations/<slug>/` を作り、Commons の **`Special:FilePath`** からオリジナルを取得（リダイレクト追従 `-L`）。
   ```bash
   curl -sL -A "Mozilla/5.0 (CVE-0 reference fetch)" \
     "https://commons.wikimedia.org/wiki/Special:FilePath/<FILE_NAME>" -o "<slug>/<out>.jpg"
   ```
5. **検収**：`file *` で**HTMLエラーページ（数KBの偽jpg）を除去**。本物のJPEG/PNGのみ残す。`Read` で1枚ずつ見て中身を確認。
6. **DNA抽出**：`Read` した画像から**固有性（保つべき要素）を箇条書き**で言語化（建物配置・象徴物・色・周辺地形）。`REFERENCE.md` に「実写一覧（出典URL付き）＋ビジュアルDNA＋表現規則」を書く（カードの雛形＝既存の `yokohama-cosmoworld/REFERENCE.md`）。
7. **生成に渡す**：codex には **(a) キャッシュした実写ファイル** と **(b) DNA箇条書き** の両方を渡す。深層化するなら固有現象を上乗せしつつDNAは保つ。

## 注意

- **ライセンス**：Commons 優先（自由利用・要出典）。出典URLを必ずカードに残す。著者手置きの実写と併用可。
- **表現規則**：生成側は読める文字／数字／ロゴ／実在固有名を出さない（時計＝読めない光、看板無地）。実写は**入力**であり生成物と区別する。
- **再利用**：同じ実在地は次回からカードを読むだけ。要素が足りなければ追補取得してカードに追記。
- `WebFetch` は本文をmarkdown化して読む用途。**画像バイナリの取得は `curl`（Bash）** を使う。
