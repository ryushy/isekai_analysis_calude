# セットアップ（CLI / MCP）

動画ワークフローは **Claude Code →（codex MCP）→ codex →（Higgsfield MCP）→ Seedance** の2段。

## 1. codex CLI

- codex CLI が PATH にあること。確認：`codex --version`。
- codex の設定は `C:\Users\ryuya\.codex\config.toml`（model・信頼プロジェクト等）。

## 2. Claude → codex（MCP）

- リポジトリ直下 [.mcp.json](../../../../.mcp.json) に `codex` サーバを宣言済み：

  ```json
  { "mcpServers": { "codex": { "command": "cmd", "args": ["/c", "codex", "mcp-server"] } } }
  ```

- 確認：`claude mcp list` → `codex: cmd /c codex mcp-server - ✔ Connected`。
- 初回はプロジェクトの `.mcp.json` 承認ダイアログが出る場合がある（許可する）。
- 既にユーザースコープでも `codex` が登録されていれば、どちらでも動作する。

## 3. codex → Higgsfield（Seedance 動画生成）

- **Seedance 動画は codex 側の Higgsfield MCP** が実行する。Claude は codex に依頼するだけ。
- codex 側に必要なもの：
  - Higgsfield MCP（`media_upload` / `media_confirm` / `generate_video` / `job_display` ツール）。
  - codex グローバルスキル `seedance-short-video`（`C:\Users\ryuya\.codex\skills\seedance-short-video\`。`scripts/upload_to_presigned_url.py`・`download_url.py` 同梱）。
- 確認方法：codex セッションで「利用可能な Higgsfield MCP ツールを一覧して」と尋ねる、または `seedance-short-video` スキルの存在を確認させる。
- 見つからない場合：Higgsfield MCP の登録（codex 側）と認証が必要。動画ステップはそこが整うまで保留し、画像（storyboard）までで止める。

## 4. 画像生成について

- ストーリーボードの**静止画**は codex の内蔵画像生成で行う（`storyboard` スキル）。Higgsfield は不要。
- 動画化（`seedance` スキル）でのみ Higgsfield が要る。

## 5. 動作確認コマンド

```bash
codex --version
claude mcp list          # codex が ✔ Connected か
```
