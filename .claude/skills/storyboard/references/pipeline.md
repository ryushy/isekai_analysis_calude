# ストーリーボード制作パイプライン（詳細）

> 参照元：ストーリーボードリポジトリ `chapter_short_pipeline_v3`（本文準拠ゲート付き）を CVE-0 用に簡約。

## 案件フォルダ構成

```text
media/storyboard/<case-slug>/
  README.md                  ← 案件概要・進行表・v記録
  01_highlight.md            ← STEP1（原文引用つき9カット）  ※Claude
  03_storyboard_prompt.md    ← STEP3（codex 用 3x3 プロンプト）※Claude
  04_seedance_prompt.md      ← STEP5（seedance スキルで作成・任意）
  outputs/storyboards/       ← 生成ボード画像（storyboard_vN.png）
  outputs/seedance/          ← 生成動画（seedance スキル）
  references/                ← 案件固有の参照
  reviews/                   ← レビュー用フレーム
```

## STEP1 ハイライト（01_highlight.md）テンプレ

```markdown
# <シーン名>15秒ハイライト v1
原稿: <docs/manuscript/prototypes/....md への相対パス>

## フォーカス（続きを読みたくなる一点）
<1〜2文。原文の山場から>

## 公開導線
- 勝ち記号: <映像の核1モチーフ・原文由来>
- 未読者への問い: <1文>
- 投稿文案: <原文に忠実なSNS文>

## 15秒9カット（全要素に原文引用必須）
| # | 秒 | 画 | 原文根拠（引用＋行番号） |
|---|---:|---|---|
| 1 | 0.0-1.7 | … | 「…」(L..) |
| … | … | … | … |
| 9 | 13.6-15.0 | … | 「…」(L..) |

## 創作補完（原文にない要素。ユーザ承認が必要）
| 要素 | 理由 | 承認 |
|---|---|---|

## 映像化しない原文要素と理由
- …
```

## STEP3 ストーリーボードプロンプト（03_storyboard_prompt.md）

`## Storyboard` 見出しの下の **英語コードブロック**が codex に渡す本体。冒頭固定文：

```text
Create one 16:9 image containing a 3x3 grid of nine storyboard frames, numbered 1 to 9 in the corner of each frame. Modern cinematic anime style, light tone (not horror). Every frame is composed for a vertical 9:16 short-video crop inside the grid cell. Keep consistent character design, time-of-day, and color palette across all nine frames.

Character: <character-canon.md の正典ブロックを貼る>

Frame 1: <カット#1の画>
...
Frame 9: <カット#9の画>

Avoid readable text, captions, subtitles, numbers other than the storyboard frame numbers, logos, UI, HUD digits, gauges, modern phones/computers, robots or android faces, gore, horror lighting, runes, magic circles, giant emblems.
```

## STEP4 codex 依頼文（そのまま使える雛形）

`mcp__codex__codex` を `cwd`=リポジトリ直下, `sandbox`=workspace-write, `approval-policy`=never で呼ぶ。`prompt`：

```text
ストーリーボード制作の役割分担に従い、あなた（codex）の役割は「画像生成のみ。台本やプロンプトの創作はしない」です。

次のプロンプトファイルの「## Storyboard」コードブロック内の英語プロンプトを一切変更せずに使い、3x3グリッド9コマの画像を生成して保存してください。
主人公の顔・髪・ヘッドホンは参考画像に寄せてください（同一人物。少しハーフ＝目元にわずかな東アジアの柔らかさ）。

- プロンプト: media/storyboard/<case>/03_storyboard_prompt.md
- 参考画像: media/参考画像/
- 保存先: media/storyboard/<case>/outputs/storyboards/storyboard_vN.png

プロンプト文言の追加・削除はしないこと。画像生成手段が使えない場合は課金せず、その旨と必要物を日本語で報告すること。生成できたら保存パスと所感（カット一致／縦9:16／読める文字の有無）を日本語で報告すること。
```

## GATE A チェック（生成前）

- [ ] 9カット全要素が原文引用に遡れる（創作補完は承認済み）
- [ ] 読める文字・数字・HUD を出さない指示が入っている
- [ ] git 用語が画面・台詞・技名に出ていない
- [ ] キャラ記述が character-canon.md と一致

## GATE B チェック（生成後・Read で確認）

- [ ] 9コマが 01_highlight と一致
- [ ] 各コマ縦9:16構図／時間帯・色調・キャラデザ一貫
- [ ] 主人公の容姿が正典・参考画像に寄っている
- [ ] 番号以外の読める文字なし
- [ ] 案件 README に vN を記録（正バージョンを明記）
