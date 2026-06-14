# media/ — トランスメディア（ストーリーボード・画像・動画）

> CVE-0 のショート動画／画像展開の制作物と手順。**設定・本文は [../docs/](../docs/)、制作スキルは [../.claude/skills/](../.claude/skills/)**。

---

## 1. 構造

```text
media/
├── README.md
├── storyboard/                  … 案件（シーン）ごとのストーリーボード
│   └── <case-slug>/
│       ├── README.md            … 案件概要・進行表
│       ├── 01_highlight.md      … 15秒9カット（原文引用つき）   ← Claude が作成
│       ├── 03_storyboard_prompt.md … 3x3グリッド生成プロンプト   ← Claude が作成
│       ├── 04_seedance_prompt.md … 動画化プロンプト（任意）       ← Claude が作成
│       ├── outputs/storyboards/ … 生成ボード画像（codex）
│       ├── outputs/seedance/    … 生成動画（codex/Higgsfield）
│       ├── references/          … 案件固有の参照画像
│       └── reviews/             … レビュー用フレーム
└── 参考画像/                    … 主人公など共通キャラの参照画像
```

既存案件：`storyboard/isekai-cve0-battle-rain/`（静止した雨）／`storyboard/isekai-cve0-sword/`（剣のひと）。
※ 特訓「ひと晩寝かせる」は別リポジトリ `C:\project\home\entertaiment\ストーリーボード\cases\isekai-cve0-training\` にある（先行作成のため）。

---

## 2. 役割分担（重要）

| 主体 | 役割 |
|---|---|
| **Claude Code** | 台本（ハイライト・各プロンプト）の作成、本文準拠チェック、画像/動画レビュー。**テキストと検証の全て** |
| **codex（MCP）** | **画像生成のみ**（ストーリーボードPNG）。台本・プロンプトの創作はさせない |
| **codex + Higgsfield MCP** | Seedance による**動画生成**（`seedance-short-video` スキル経由） |

---

## 3. ワークフロー（2スキル）

1. **画像まで**：スキル [storyboard](../.claude/skills/storyboard/SKILL.md) を使う。
   ハイライト→ストーリーボードプロンプト作成→codex で 3x3 画像生成→レビュー。
2. **画像OK後、動画へ**：スキル [seedance](../.claude/skills/seedance/SKILL.md) を使う。
   クリーンなキーフレーム準備→Seedanceプロンプト作成→codex(Higgsfield)で動画生成→レビュー。

> **画像が問題なければ Seedance に進む**、というゲートを必ず挟む。番号付きグリッドのまま Seedance に渡さない（数字・枠が動画に映る）。

---

## 4. 固定ルール

- 縦9:16（3x3グリッドの各コマ内構図）／one continuous take 想定。
- **読める文字・数字・HUD を画面に出さない**（git 用語は世界観上も非表示）。
- 主人公の容姿は [../docs/settings/protagonist_core.md §0.1](../docs/settings/protagonist_core.md) と `参考画像/` に準拠。
- FAB は淡い光のみ（人型・顔・ロボット禁止）。武器＝力の象徴（金属でなく光の具現）。
- トーンはライトな現代アニメ調。

---

## 5. セットアップ（CLI / MCP）

詳細は [../.claude/skills/seedance/references/setup.md](../.claude/skills/seedance/references/setup.md)。要点：

- **codex CLI** が PATH にあること（`codex --version`）。
- **Claude→codex の MCP**：`.mcp.json`（リポジトリ直下）に `codex` サーバを宣言済み。`claude mcp list` で `codex ... ✔ Connected` を確認。
- **codex→Higgsfield の MCP**：codex 側に Higgsfield MCP と `seedance-short-video` スキルが必要（Seedance動画生成に使用）。
