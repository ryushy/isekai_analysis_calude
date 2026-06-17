---
name: x-post-fetch
description: X/Twitter の公開投稿URLから本文、メタデータ、画像・動画を取得してローカル保存するスキル。ユーザーが X 投稿、tweet、status URL、x.com/twitter.com の動画取得、投稿内容の保存、参考動画の取得を依頼したときに使う。ログイン壁・非公開投稿・削除済み投稿・権限が必要な投稿は回避せず、取得可能な公開情報だけを扱う。
allowed-tools: Bash, Read, Glob, Grep, WebFetch, WebSearch
---

# X Post Fetch

X/Twitter の公開投稿を、制作・参照用にローカル保存する。

## 基本方針

- 公開投稿だけを対象にする。ログイン壁、非公開、削除済み、年齢制限、地域制限、権限が必要な投稿を回避しない。
- パスワードや認証コードは求めない。Cookie を使う必要がある場合は、ユーザーが明示的にローカル cookie ファイルを指定した時だけ使う。
- 動画・画像は原則 `tmp/x-post-fetch/<status_id>/` に保存する。Git 管理したい時だけ、ユーザーに確認してから `media/` などへ移す。
- 投稿本文は短く要約し、必要なら短い引用だけにする。取得したメディアの再配布可否は判断せず、参照用途として扱う。

## 推奨ワークフロー

1. URL から `status_id` を確認する。
2. まず `scripts/fetch_x_post.py <URL>` を実行する。
3. 生成された `summary.md` と `summary.json` を読む。
4. 必要なら `ffprobe` で動画仕様を確認する。
5. ユーザーへ、投稿本文・作者・投稿日・保存パス・動画仕様・取得できなかった項目を報告する。

## コマンド

```powershell
python .claude/skills/x-post-fetch/scripts/fetch_x_post.py "https://x.com/<user>/status/<id>"
```

出力先を変える場合：

```powershell
python .claude/skills/x-post-fetch/scripts/fetch_x_post.py "https://x.com/<user>/status/<id>" --out tmp/x-post-fetch
```

ローカル cookie ファイルをユーザーが明示した場合のみ：

```powershell
python .claude/skills/x-post-fetch/scripts/fetch_x_post.py "https://x.com/<user>/status/<id>" --cookies path/to/cookies.txt
```

## 取得できない時

- `yt-dlp` が無い：`python -m yt_dlp --version` を試す。両方無ければインストールが必要と報告する。
- X 側でブロック：ログイン不要で取得できないことを報告し、スクリーンショット、投稿本文の貼り付け、またはユーザー指定 cookie ファイルの提供を選択肢として示す。
- 動画が無い：本文・サムネ・メタデータだけ保存できたか確認する。
- 出力が文字化け：PowerShell では `$env:PYTHONIOENCODING='utf-8'` を設定して再実行する。

## 報告フォーマット

```text
取得できました。

- 投稿URL:
- 投稿者:
- 投稿日:
- 本文:
- 保存先:
- 動画:
- サムネ:
- メタデータ:
- 注意:
```
