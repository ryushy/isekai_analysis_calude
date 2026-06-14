# Setting Analysis — Claude Code Project Memory

このファイルは Claude Code が毎セッション開始時に読む **永続記憶**。プロジェクトの全体像・現状・規約をここに集約する。


## プロジェクト目的

異世界転生・仮想世界作品の **「最高の舞台装置」を検討すること**。


C:\project\home\entertaiment\codex\isekai-world-engine-db_codex　は参照用として利用、改変等は禁止


私のアイディア以下を様々な視点で検討して、舞台装置を考えたい。

ある日を境に世界は一変 Claude Fable(disabled) 実は2000年にきっかけ
人1人について原則1プロジェクト　GitHubのような仕組みで各人の生きざまが記録されている。
世界の記録はGitHubのような仕組で管理されている
気が付いているのは、特殊な人のみ
特殊能力（ライブラリ）が突然現れる　ダンジョンを攻略するとライブラリをゲット（魔法や特殊武器、特殊能力が定義されている）
個人のリポジトリには限界があり、その容量の中で　ライブラリをロードする。


## セッション開始時に読む（中断復帰）

1. [docs/ops/current.md](docs/ops/current.md) … いまどこまで・次に何をするか
2. [docs/ops/backlog.md](docs/ops/backlog.md) … 優先タスク
3. 構造的決定の前に [docs/project_handover.md](docs/project_handover.md)（著者要件・設計原則）

執筆時：開示可否は [docs/series/disclosure_ledger.md](docs/series/disclosure_ledger.md)、確定事実は [docs/series/canon_log.md](docs/series/canon_log.md)、ID規約は [docs/series/episode_id_convention.md](docs/series/episode_id_convention.md)。
レビュー：`reader-personas`（読者目線）／`editor-kawahara`（川原礫＝構造）／`editor-tsukikage`（テンポ）。

## ディレクトリ構造（地図）

詳細は [docs/README.md](docs/README.md)。

- `docs/` … 設定・物語・規約。`stage_device_design.md`（正本）＋`settings/`（規格書）＋`plot/`＋`manuscript/prototypes/`＋`guides/`
- `media/` … トランスメディア。**共通＝`media/common/`**（backgrounds・characters・reference）／**話固有＝`media/book{N}/ep{M}/`**（backgrounds・reference・storyboard）。手順は [media/README.md](media/README.md)
- `.claude/skills/` … 制作スキル `storyboard`（画像）／`seedance`（動画）
- `scripts/restructure_docs.py` … ファイル移動＋Markdownリンク自動張替え

## 動画制作ワークフロー（Claude→codex→Seedance）

1. **画像**：スキル `storyboard` — Claude が台本（ハイライト＋プロンプト）を作り、**codex（MCP）が画像生成のみ**。
2. **動画**：画像OK後にスキル `seedance` — Claude が動画プロンプトを作り、**codex の `seedance-short-video`（Higgsfield MCP）が Seedance 生成**。
3. MCP：`.mcp.json` に `codex` 宣言済み（`claude mcp list` で確認）。Higgsfield は codex 側。設定詳細＝[.claude/skills/seedance/references/setup.md](.claude/skills/seedance/references/setup.md)。
4. 主人公の容姿正典＝[docs/settings/protagonist_core.md §0.1](docs/settings/protagonist_core.md)＋`media/common/characters/参考画像/`。
