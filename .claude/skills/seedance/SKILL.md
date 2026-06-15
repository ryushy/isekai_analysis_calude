---
name: seedance
description: Use this when CVE-0 storyboard images are already approved and the user wants to generate the actual short VIDEO with Seedance. Claude authors the Seedance prompt (one continuous shot, vertical 9:16) and delegates generation to codex's seedance-short-video skill (Higgsfield MCP) — uploading CLEAN keyframes (never the numbered grid), preflighting cost, generating, then reviewing frames. Use for video/動画/Seedance/シードダンス requests. For the storyboard image step, use the `storyboard` skill first.
---

# Seedance（動画化）

承認済みストーリーボードから **Seedance のショート動画** を作る。
**役割分担：Claude が Seedance プロンプト（テキスト）を作り、codex の `seedance-short-video` スキルが Higgsfield MCP 経由で動画生成**する。

## 前提（必ず確認）

1. **ストーリーボード画像が承認済み**（`storyboard` スキルの GATE B 通過）。未承認ならまず `storyboard` スキルへ。
2. codex MCP 接続済み（`claude mcp list` で `codex ... ✔ Connected`）。
3. **codex 側に Higgsfield MCP と `seedance-short-video` スキルがある**こと。確認・設定は [references/setup.md](references/setup.md)。

## ワークフロー

1. **⚠️ クリーン・キーフレーム準備（最重要）**：Seedance に**番号付き3x3グリッドを渡さない**（数字・枠・レイアウトが動画に焼き付く）。必要なキーフレーム（開始・中間・終端など）を、`storyboard` スキルで**番号・グリッドなしの単独画像**として別途生成し `references/` に置く（または既存の参照キャラ画像を使う）。
2. **STEP5 Seedanceプロンプト** `04_seedance_prompt.md`：**1つの連続ショット**として記述（スライドショーにしない）。開始構図／カメラの動き／主人公の動作／環境変化／終端フレーム／画風／avoid list。各参照画像に**役割を明示**（どれがキャラ／背景／小物を支配するか）。縦9:16。雛形は [references/seedance-prompt.md](references/seedance-prompt.md)。
3. **STEP6 codex で生成**：codex MCP を呼び、`seedance-short-video` スキル（Higgsfield MCP）で——
   - `media_upload`（presigned URL）で参照をアップ → `media_confirm`。
   - `generate_video` を **`get_cost:true` で見積り**してから本生成（テスト＝fast/720p/16:9/4-8s、最終＝std/1080p/9:16/15s）。
   - 出力 mp4 を `media/book{N}/ep{M}/storyboard/<case>/outputs/seedance/<descriptive>_vN.mp4` に保存、`job_display` をポーリング。
   - 依頼文の雛形は [references/seedance-prompt.md](references/seedance-prompt.md) 末尾。
4. **GATE B 動画レビュー** `06_video_review.md`：codex に `ffprobe`／`ffmpeg` でコンタクトシートを `reviews/<run-id>/` に出させ、縦9:16・尺・**読める文字や枠が無い**・スライドショー化していない・キャラ容姿・終端到達を確認。**＋ 環境整合（GATE B2）**＝現実/実在地ベースのシーンが実写の構図に沿い、建築・空間の動線（改札→階段→出口、坂の高低差 等）が破綻していないかも確認（[storyboard SKILL.md 環境レイヤー＆実写参照ゲート](../storyboard/SKILL.md)）。不合格なら 04 に追記して再生成。

## 固定ルール

- **番号付きグリッドを参照に渡さない**（焼き付き防止）。クリーンキーフレームを使う。
- **背景とキャラは別レイヤー・別参照で渡す**（既定）：背景＝人物なしプレート（[stage-background](../stage-background/SKILL.md) のレイヤー方針）／キャラ＝[character-sheet](../character-sheet/SKILL.md) の正典。各参照に「これは背景／これはキャラ」と役割を明示。
- one continuous take／縦9:16／読める文字・字幕・ロゴなし。
- 主人公の容姿＝[character-canon](../storyboard/references/character-canon.md) 準拠。FAB＝光のみ。武器＝光の象徴。
- **コスト**：`get_cost:true` で見積りし、本生成はユーザー承認の上で。

## コスト方針

- API/課金は**ユーザーが明示的に望んだ時のみ**。`get_cost` を必ず先に。
- アップロードや生成手段が使えない場合、codex は課金せず正直に報告する（依頼文に明記）。
