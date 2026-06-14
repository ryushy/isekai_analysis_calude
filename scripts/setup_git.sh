#!/bin/sh
# CVE-0 Git セットアップ（Git Bash / sh）
# 実行: sh scripts/setup_git.sh
set -e

command -v git >/dev/null 2>&1 || { echo "git が見つかりません。" >&2; exit 1; }

if [ ! -d .git ]; then
  echo ".git がありません。git init を実行します。"
  git init
  git symbolic-ref HEAD refs/heads/main 2>/dev/null || true
fi

git config core.hooksPath scripts/git-hooks
git config core.autocrlf false
git config init.defaultBranch main

# フックに実行権限（Unix系のみ意味を持つ。Windows では sh 実行のため任意）
chmod +x scripts/git-hooks/* 2>/dev/null || true

echo "core.hooksPath = $(git config --get core.hooksPath) を設定しました"
echo "完了。運用は docs/guides/git_workflow.md を参照。"
echo "main 直コミットは禁止です。作業は: git switch -c feature/<topic>"
