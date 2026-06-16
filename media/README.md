# media/ — トランスメディア（ストーリーボード・画像・動画）

> CVE-0 のショート動画／画像展開の制作物と手順。**設定・本文は [../docs/](../docs/)、制作スキルは [../.claude/skills/](../.claude/skills/)**。

---

## 1. 構造

**共通（複数話で使い回す）＝ `common/`／話固有＝ `book{N}/ep{M}/`** に分ける。各話固有フォルダは `backgrounds/`・`reference/`・`storyboard/` を任意に持つ。

```text
media/
├── README.md
├── common/                      … 共通（複数話で横断利用）
│   ├── backgrounds/             … 恒久ロケの深層背景（例：honmoku-phantom-station-hideout＝秘密基地）
│   │   └── <location-slug>/     … outputs/・references/・scene_input.md
│   ├── characters/              … 共通キャラ参照（モデル写真→候補生成→採用版）
│   │   ├── _incoming-model-photos/ … 未整理の実在モデル写真（原則ローカル）
│   │   └── <char-slug>/         … references/・prompts/・generations/・outputs/
│   └── reference/               … 共通の参考画像（背景・雰囲気）＋ README
└── book{N}/                     … 巻
    └── ep{M}/                   … 話固有
        ├── backgrounds/<location-slug>/  … その話のダンジョン／舞台背景（scene_input.md＋outputs/）
        ├── reference/                     … その話の実在地参照（例：コスモワールド・みなとみらい・山手学院）
        └── storyboard/<case-slug>/        … その話のストーリーボード案件
            ├── README.md            … 案件概要・進行表
            ├── 01_highlight.md      … 15秒9カット（原文引用つき）   ← Claude が作成
            ├── 03_storyboard_prompt.md … 3x3グリッド生成プロンプト   ← Claude が作成
            ├── 04_seedance_prompt.md … 動画化プロンプト（任意）       ← Claude が作成
            ├── runs/                … 複数回生成した候補・比較元
            ├── outputs/storyboards/ … 採用済み生成ボード画像（codex）
            ├── outputs/seedance/    … 生成動画（codex/Higgsfield）
            ├── references/          … 案件固有の参照画像
            └── reviews/             … レビュー用フレーム
```

既存：
- 共通背景＝`common/backgrounds/honmoku-phantom-station-hideout/`（幻の地下鉄駅＝秘密基地）。
- 第1話（`book1/ep1/`）＝背景 `backgrounds/cosmoworld-carnival-dungeon/`（炎と森のカーニバル）、ストーリーボード `storyboard/isekai-cve0-battle-rain/`（静止した雨）／`storyboard/isekai-cve0-sword/`（剣のひと）、参照 `reference/`（コスモワールド・みなとみらい）。
- 第2話（`book2`…ではなく `book1/ep2/`）＝参照 `reference/`（山手学院）。

※ 特訓「ひと晩寝かせる」は別リポジトリ `C:\project\home\entertaiment\ストーリーボード\cases\isekai-cve0-training\` にある（先行作成のため）。

---

## 2. 役割分担（重要）

| 主体 | 役割 |
|---|---|
| **Claude Code** | 台本（ハイライト・各プロンプト）の作成、本文準拠チェック、画像/動画レビュー。**テキストと検証の全て** |
| **codex（MCP）** | **画像生成のみ**（ストーリーボードPNG）。台本・プロンプトの創作はさせない |
| **codex + Higgsfield MCP** | Seedance による**動画生成**（`seedance-short-video` スキル経由） |

---

## 3. キャラクター制作ワークフロー

人物を作成する場合は、まず実在モデル写真を用意し、それを直接再現するのではなく、キャラクター設定へ変換してから使う。

1. 未整理写真は `common/characters/_incoming-model-photos/` に置く。
2. キャラが決まったら `common/characters/<char-slug>/references/model-photos/private/` に移す。
3. 生成に使ってよい写真だけ `approved/` に選ぶ。
4. キャラ化プロンプトを `prompts/` に保存する。
5. 候補は `generations/run-YYYYMMDD_HHMMSS/` に複数残す。
6. 採用した正典キャラシートだけ `outputs/ref_sheet_v*.png` に置く。

`private/` と `_incoming-model-photos/` は個人情報・権利保護のため Git には入れない。採用版・選抜済み参照だけを必要に応じて共有する。

## 4. 画像生成ワークフロー（複数候補→採用）

画像生成は一発採用を前提にしない。各案件で複数回生成し、良い候補を採用する。

```text
<case>/
├── prompts/ または 02_codex_prompts.md
├── runs/run-YYYYMMDD_HHMMSS/    # その回の候補・比較資料・レビュー
├── reviews/                     # 横断比較・コンタクトシート
└── outputs/                     # 採用版のみ
```

- `runs/` の候補は比較用に残す。
- `outputs/` は現在の採用版として、台本・動画化・他工程が参照する。
- 旧版を退避するときは `outputs_backup_*` ではなく、今後は `runs/run-*/outputs/` に入れる。

## 5. ワークフロー（2スキル）

1. **画像まで**：スキル [storyboard](../.claude/skills/storyboard/SKILL.md) を使う。
   ハイライト→ストーリーボードプロンプト作成→codex で 3x3 画像生成→レビュー。
2. **画像OK後、動画へ**：スキル [seedance](../.claude/skills/seedance/SKILL.md) を使う。
   クリーンなキーフレーム準備→Seedanceプロンプト作成→codex(Higgsfield)で動画生成→レビュー。

> **画像が問題なければ Seedance に進む**、というゲートを必ず挟む。番号付きグリッドのまま Seedance に渡さない（数字・枠が動画に映る）。

---

## 6. 固定ルール

- 縦9:16（3x3グリッドの各コマ内構図）／one continuous take 想定。
- **読める文字・数字・HUD を画面に出さない**（git 用語は世界観上も非表示）。
- 主人公の容姿は [../docs/settings/protagonist_core.md §0.1](../docs/settings/protagonist_core.md) と `common/characters/character-nagi/outputs/ref_sheet_v*.png`、必要に応じて `references/model-photos/approved/` に準拠。
- FAB は淡い光のみ（人型・顔・ロボット禁止）。武器＝力の象徴（金属でなく光の具現）。
- トーンはライトな現代アニメ調。

---

## 7. セットアップ（CLI / MCP）

詳細は [../.claude/skills/seedance/references/setup.md](../.claude/skills/seedance/references/setup.md)。要点：

- **codex CLI** が PATH にあること（`codex --version`）。
- **Claude→codex の MCP**：`.mcp.json`（リポジトリ直下）に `codex` サーバを宣言済み。`claude mcp list` で `codex ... ✔ Connected` を確認。
- **codex→Higgsfield の MCP**：codex 側に Higgsfield MCP と `seedance-short-video` スキルが必要（Seedance動画生成に使用）。
