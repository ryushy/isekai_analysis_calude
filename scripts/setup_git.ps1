<#
CVE-0 Git セットアップ（PowerShell）
  - core.hooksPath を scripts/git-hooks に設定（事前・事後フックを有効化）
  - 改行・既定ブランチの設定
  - ローカル user 設定（任意）
実行: cd <repo>; .\scripts\setup_git.ps1
#>
param()

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "git が見つかりません。先に git をインストールしてください。" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path ".git")) {
    Write-Host ".git がありません。git init を実行します。" -ForegroundColor Yellow
    git init
    git symbolic-ref HEAD refs/heads/main 2>$null
}

# フック有効化（バージョン管理された scripts/git-hooks を使う）
git config core.hooksPath scripts/git-hooks
git config core.autocrlf false
git config init.defaultBranch main
Write-Host "core.hooksPath = $(git config --get core.hooksPath) を設定しました" -ForegroundColor Green

# ローカル user 設定（任意）
$name = Read-Host "user.name（Enterでスキップ）"
if ($name -ne "") { git config --local user.name "$name" }
$email = Read-Host "user.email（Enterでスキップ）"
if ($email -ne "") { git config --local user.email "$email" }

Write-Host "完了。運用は docs/guides/git_workflow.md を参照。" -ForegroundColor Cyan
Write-Host "main 直コミットは禁止です。作業は: git switch -c feature/<topic>" -ForegroundColor Yellow
