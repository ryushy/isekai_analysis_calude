---
name: storyboard
description: Use this when the user wants to turn a CVE-0 scene (a prototype in docs/manuscript/prototypes/ or a new scene) into a 3x3 nine-frame cinematic storyboard IMAGE for short video. Claude authors the highlight (with original-text citations) and the storyboard image prompt following project rules (git hidden, light tone, vertical 9:16, no readable text, canonical character design), then delegates image generation only to codex via the codex MCP. Use for storyboard/絵コンテ/ストーリーボード/画像/コマ割り requests. Do NOT use for video — that is the `seedance` skill.
---

# Storyboard（画像コンテ作成）

CVE-0 のシーンを **3x3＝9コマのストーリーボード画像** に起こす。
**役割分担：Claude が台本（テキスト）を作り、codex は画像生成のみ**（台本の創作はさせない）。

## 前提

- codex MCP が接続済み（`claude mcp list` に `codex ... ✔ Connected`）。未接続なら [references/setup.md](../seedance/references/setup.md) を案内。
- 主人公の容姿は [docs/settings/protagonist_core.md §0.1](../../../docs/settings/protagonist_core.md) と `media/common/characters/参考画像/` に準拠。
- 詳細手順は [references/pipeline.md](references/pipeline.md)、キャラ正典は [references/character-canon.md](references/character-canon.md)。

## ワークフロー

1. **案件フォルダ**を `media/book{N}/ep{M}/storyboard/<case-slug>/` に作る（`outputs/storyboards/`, `references/`, `reviews/` も）。slug は英数字とハイフン。
2. **STEP1 ハイライト** `01_highlight.md`：対象原稿（`docs/manuscript/prototypes/...`）を**直接読み**、15秒9カットに。**全ビジュアル要素に原文引用＋行番号**を付け、原文にない要素は「創作補完」欄に分離（要・ユーザー承認）。**各カットに環境レイヤー（現実／深層・実在地ベース／深層・純ファンタジー）を明記**。
3. **GATE A 本文準拠＋表現規則＋環境整合**：全カットが引用に遡れるか／読める文字・数字・HUD なし／git 用語は表に出さない／乳幼児写実・流血・実在物・模倣可能な危険手順を避ける。**＋ GATE A2（環境整合）**＝下記「環境レイヤー＆実写参照ゲート」を必ず通す。
4. **STEP3 ストーリーボードプロンプト** `03_storyboard_prompt.md`：英語で「1枚に3x3＝9フレーム、各コマ縦9:16構図、隅に番号1-9のみ」。キャラ記述は [references/character-canon.md](references/character-canon.md) の正典ブロックを使う。時間帯・色調・キャラデザの一貫を指定。
5. **STEP4 codex で生成**：codex MCP（`mcp__codex__codex`）を呼ぶ。テンプレは [references/pipeline.md](references/pipeline.md) の「codex 依頼文」。**プロンプトを一字一句変えず生成**、`media/common/characters/参考画像/` を見た目の寄せに使用、`outputs/storyboards/storyboard_vN.png` に保存。`cwd`=リポジトリ直下, `sandbox`=workspace-write, `approval-policy`=never。
6. **レビュー（GATE B）**：生成PNGを Read で確認し、`01_highlight.md` の各カットと一致するか点検。**＋ GATE B2（環境整合）**＝現実/実在地ベースのカットが実写の構図に沿い、建築・空間の動線が破綻していないかを確認。案件 README に v 記録。直すならプロンプト修正→v+1 で再生成。
7. **完了したら**：画像が問題なければ `seedance` スキルへ（動画化）。

## 環境レイヤー＆実写参照ゲート（GATE A2 / B2）【必須】

> 背景の「現実 vs 深層」を取り違えると破綻する（例：第2話 ep2 highlights 09＝現実寄りの幻の駅をダンジョン環境で描き、自動改札と階段の配置が崩壊）。これを生成前後で必ずチェックする。

- **STEP1 で各カットに環境レイヤーを明記**：
  - **現実**（地上・実在地＝自宅/学校/坂/街） … **実写参照 必須**
  - **深層・実在地ベース**（実在の場所が深層化＝幻の駅・歪んだ路地など。"ありえない一点"はあるが土台は実景） … **実写参照 必須**
  - **深層・純ファンタジー**（変身・時間崩壊・能力空間） … 実写参照 不要（想像で可）
- **GATE A2（生成前）**：
  - [ ] 実写参照が要るカットは **Web検索で実在の構図を確認**し、プロンプトに反映した（例：地下鉄駅＝ホーム→改札→階段→出口の動線／坂＝高低差／教会・煉瓦）。
  - [ ] **建築・空間の整合**を言語化した（要素の物理的な配置・動線を1行で。例「platform → ticket gates → ascending stairs → exit を一直線に」）。
  - [ ] 現実カットを**ダンジオン/ファンタジー廃墟の質感で描かない**指示を入れた（崩壊・苔・瓦礫の誤適用を防ぐ）。
- **GATE B2（生成後・Read で確認）**：
  - [ ] 実在地ベースのカットが**実写の構図**に沿っている（参照とかけ離れていない）。
  - [ ] **改札・階段・扉・通路・道路などの配置と動線が物理的に成立**している（宙に浮く/接続しない/方向が逆 が無い）。
  - [ ] 現実カットが意図せずダンジョン化していない。

## 固定ルール

- 縦9:16（各コマ内構図）／読める文字・数字・HUD を出さない／**git 用語は世界観上も非表示**。
- FAB＝淡い光のみ（人型・顔・ロボット禁止）。武器＝力の象徴（金属でなく光の具現）。
- トーン＝ライトな現代アニメ調。主人公の容姿＝正典準拠。
- **codex には生成だけ依頼**（プロンプト・台本の創作をさせない）。

## コスト方針

- 画像生成はユーザーが明示的に望んだ時のみ（このスキルの起動＝明示とみなす）。
- 生成手段が使えない場合、codex は課金せず正直に報告する旨を依頼文に明記する。
