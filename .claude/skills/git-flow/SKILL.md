---
name: git-flow
description: CVE-0 のブランチ運用（作業ブランチで作成→ main へマージ）でコミット・マージを行うスキル。日本語プレフィックス規約・フック（pre-commit/commit-msg）に準拠し、main への直接コミットを避け、作業ブランチを切ってコミットし、完了後に --no-ff で main へマージする。コミット/ブランチ/マージ/「git管理」依頼時に使う。
argument-hint: <"start <topic>" | "commit <message>" | "merge" | "status" | 質問>
allowed-tools: Bash, Read, Glob, Grep
---

# git-flow — ブランチ運用でのコミット／マージ

CVE-0 の Git 運用：**作業ブランチで作成 → main へマージ**。フック（[../../../scripts/git-hooks/](../../../scripts/git-hooks/)）が main 直コミット・リンク破損・巨大ファイル・プレフィックス欠落をブロックする。

## 前提（初回のみ）

- フックを有効化：`git config core.hooksPath scripts/git-hooks`（[../../../scripts/setup_git.ps1](../../../scripts/setup_git.ps1) / `.sh` でも可）。
- 既定ブランチは `main`。

## 標準ワークフロー

1. **作業開始（ブランチを切る）**：main 上にいるなら必ず分岐する。
   ```bash
   git switch main && git pull --ff-only 2>/dev/null; git switch -c feature/<topic>
   ```
   ブランチ名：`feature/<topic>`（機能）／`fix/<topic>`（修正）／`docs/<topic>`／`chore/<topic>`。
2. **コミット**：**対象ファイルを個別ステージング**（`git add .` で無関係差分を巻き込まない）。日本語プレフィックス必須。
   ```bash
   git add <files>
   git commit -m "feat: <日本語の要約>"
   ```
   - 末尾に必ず付ける共著トレーラ：
     ```
     Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
     ```
3. **マージ（完了時）**：レビュー後に main へ `--no-ff` でマージし、ブランチを掃除。
   ```bash
   git switch main && git merge --no-ff feature/<topic> && git branch -d feature/<topic>
   ```
4. **プッシュ**：ユーザーが明示的に求めた時のみ。

## プレフィックス規約（commit-msg フックが強制）

`feat:`（機能）／`fix:`（修正）／`docs:`（文書）／`refactor:`／`test:`／`chore:`／`style:`／`perf:`。

## フックがブロックする事象（[../../../scripts/git-hooks/](../../../scripts/git-hooks/)）

| フック | 内容 |
|---|---|
| pre-commit | main 直コミット禁止／25MB超ファイル／Markdownリンク破損 |
| commit-msg | プレフィックス欠落 |
| post-commit | 作業ブランチなら main へのマージ手順を表示 |

> 例外的に main へ直接コミットする時のみ `ALLOW_COMMIT_ON_MAIN=1 git commit ...`。

## 引数

| 引数 | 動作 |
|---|---|
| `start <topic>` | main から `feature/<topic>` を切る |
| `commit <message>` | 変更を確認し、対象を個別ステージングして日本語プレフィックス付きでコミット |
| `merge` | 現ブランチを main へ `--no-ff` マージしブランチ削除 |
| `status` | `git status` ＋現ブランチ＋未コミット差分の要約 |
| （空・質問） | 現状を見て次の一手を提案 |

## 原則

- **コミット/プッシュはユーザーが求めた時に行う**。ただし本スキルが呼ばれた＝コミット意思とみなす。
- 破壊的操作（reset --hard / push --force / checkout -- 等）は安全な代替を優先し、必要時のみ。
- フック（hooks）はスキップしない（`--no-verify` を使わない）。失敗したら原因を直す。
