# Git 運用ガイド（ブランチ作成 → main へマージ）

> 本プロジェクトの Git 管理。**作業ブランチで作成し、main へマージ**する。フックが規約を自動で強制する。
> スキル＝[../../.claude/skills/git-flow/SKILL.md](../../.claude/skills/git-flow/SKILL.md)。

---

## 1. セットアップ（初回のみ）

```powershell
# PowerShell
.\scripts\setup_git.ps1
```
```sh
# Git Bash
sh scripts/setup_git.sh
```
→ `core.hooksPath=scripts/git-hooks` を設定し、事前・事後フックを有効化する。

## 2. 基本サイクル

```bash
git switch -c feature/<topic>     # main から作業ブランチを切る
# …編集…
git add <files>                   # 対象を個別ステージング（git add . は避ける）
git commit -m "feat: <日本語要約>" # プレフィックス必須
git switch main && git merge --no-ff feature/<topic>
git branch -d feature/<topic>
```

- ブランチ名：`feature/` `fix/` `docs/` `chore/`。
- コミット末尾に共著トレーラ：`Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`。
- プッシュはユーザーが明示した時のみ。

## 3. フック（自動チェック）

### 事前（native git hooks＝[../../scripts/git-hooks/](../../scripts/git-hooks/)）

| フック | ブロック内容 |
|---|---|
| **pre-commit** | ① main/master 直コミット禁止 ② 25MB 超ファイル ③ Markdown リンク破損（`scripts/check_links.py`） |
| **commit-msg** | プレフィックス欠落（feat/fix/docs/refactor/test/chore/style/perf） |

### 事後

| フック | 内容 |
|---|---|
| **post-commit**（native） | 作業ブランチなら main へのマージ手順を表示 |
| **Stop**（Claude・[../../.claude/hooks/review_changes.py](../../.claude/hooks/review_changes.py)） | セッション終了時、本セッションで編集した未コミット変更を要約し、コミットを促す（再起動） |

### 復帰（事前・セッション開始）

| フック | 内容 |
|---|---|
| **SessionStart**（Claude） | `docs/ops/current.md` の先頭を表示し、ブランチ運用を再周知 |

## 4. 例外・トラブル

- どうしても main へ直接コミットする時のみ：`ALLOW_COMMIT_ON_MAIN=1 git commit ...`。
- フックはスキップしない（`--no-verify` 禁止）。失敗したら原因（リンク破損・巨大ファイル・プレフィックス）を直す。
- リンク破損の詳細：`python scripts/check_links.py`。

## 5. 改行・無視

- [../../.gitattributes](../../.gitattributes)：テキストは LF 固定、画像/動画は binary。
- [../../.gitignore](../../.gitignore)：`__pycache__`・`tmp/` 等のみ無視。**ストーリーボード画像は成果物として追跡**（動画を除外したい場合は .gitignore のコメント参照）。
