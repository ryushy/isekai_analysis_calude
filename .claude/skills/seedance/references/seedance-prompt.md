# Seedance プロンプト雛形と codex 依頼文

## 04_seedance_prompt.md（連続ショット）

```markdown
# <シーン名> Seedance プロンプト v1

保存先動画: outputs/seedance/<project>_<scene>_vertical_final_vN.mp4
使用キーフレーム（番号・グリッドなし）: references/<keyframe>.png ／ ../../参考画像/<char>.png

## Video Prompt（codex はこれを使う）

​```text
Use the reference images: keep [character identity, hair, eyes, white headphones] from the character reference; use [dungeon / inn, lighting, atmosphere, palette] from the background reference.
Create a 15-second cinematic modern-anime video in ONE continuous take, vertical 9:16.
The camera [route and movement: slow push-in / handheld follow / arc].
Nagi [main action], causing [visible change: rain freezes / dry patch spreads / blue light sword forms].
End with [final hero framing].
Visual style: [lighting, palette, mood], light tone, not horror.
No cuts, no montage, no text, no subtitles, no numbers, no grid, no logos, no UI, no readable symbols, no extra characters; FAB only as a faint pale-blue light; weapons as glowing blue light, not metal.
​```

## Avoid（CVE-0 固定ネガティブ）
番号・グリッド・字幕・読める文字・HUD・魔法陣・ルーン・ロボット顔・流血・実在ロゴ。
```

## Seedance パラメータ目安（codex 側）

| 用途 | model | mode | resolution | aspect | duration | count |
|---|---|---|---|---|---|---|
| テスト | seedance_2_0 | fast | 720p | 16:9 | 4-8s | 1 |
| 最終（縦ショート） | seedance_2_0 | std | 1080p | 9:16 | 15s | 1 |

## codex 依頼文（雛形）

`mcp__codex__codex` を `cwd`=リポジトリ直下, `sandbox`=workspace-write, `approval-policy`=never で呼ぶ。`prompt`：

```text
あなた（codex）の `seedance-short-video` スキル（Higgsfield MCP）を使って動画を生成してください。台本・プロンプトの創作はしないこと。

- Seedanceプロンプト: media/book{N}/ep{M}/storyboard/<case>/04_seedance_prompt.md の「## Video Prompt」コードブロックをそのまま使用
- 参照画像（役割を明示）: <character ref> = 主人公の顔/髪/ヘッドホン、<keyframe> = 背景/構図。番号付きグリッドは使わないこと
- 手順: media_upload(presigned)→ローカルPUT→media_confirm→generate_video を get_cost:true で見積り→（コストを報告し）本生成→job_display をポーリング
- 設定: 最終は std/1080p/9:16/15s/count1（テストは fast/720p/16:9/4-8s）
- 保存: media/book{N}/ep{M}/storyboard/<case>/outputs/seedance/<project>_<scene>_vertical_final_vN.mp4
- 生成後: ffprobe で 9:16・尺を確認し、ffmpeg でコンタクトシートを reviews/<run-id>/ に出力

アップロードや生成手段（鍵/Higgsfield MCP）が使えない場合は課金せず、不足物を日本語で報告すること。完了したら保存パス・job/media ID・コスト・所感（縦9:16/読める文字や枠の有無/スライドショー化していないか/キャラ容姿）を日本語で報告すること。
```

## よくある不具合の対処

- スライドショー化 → `one continuous take, no cuts, no montage`。
- 番号・枠・文字が映る → 参照に番号付きグリッドを使っている。クリーンなキーフレームに差し替え。
- 朝が夜になる → `bright morning, no night, no stars`。
- キャラがブレる → 髪・目・ヘッドホン・服を明示し、専用キャラ参照を使う。
- 光の記号・魔法陣が出る → 参照/プロンプト汚染。記号なしキーフレーム＋ネガティブ強化で再生成。
