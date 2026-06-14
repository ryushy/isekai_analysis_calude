# docs/ 配下の地図

> 異世界×能力バトル企画「CVE-0（仮）」の **設定・物語・規約** を集約する。
> 設定の正本は [stage_device_design.md](stage_device_design.md)、企画概要は [proposal.md](proposal.md)。
> 動画・画像（トランスメディア）はリポジトリ直下 [../media/](../media/)、制作スキルは [../.claude/skills/](../.claude/skills/)。

---

## 1. 一目で分かる構造

```text
docs/
├── README.md               ← 本ファイル（地図）
├── proposal.md             ← 企画書（ピッチ・USP・比較）
├── project_handover.md     ← 作品コンセプト・著者要件・設計原則（時系列非依存）
├── project_roadmap.md      ← フェーズ・タスクID規約・1話ワークフロー
├── stage_device_design.md  ← 世界設定の正本（git＝作者側エンジン）
│
├── settings/   … 舞台装置の規格書（相互に密結合。一体で運用）
├── plot/       … 連作構成（全10巻・敵の階段・開示スケジュール）
├── manuscript/ … 執筆・試作（prototypes/ に第1話の試作）
├── guides/     … 執筆規約（文体）
├── ops/        … 作業状態管理（中断復帰：current/backlog/worklog/snapshots）
├── series/     … 連作横断台帳（canon/timeline/disclosure/episode_id）
└── review/     … レビュー結果（reader-personas/editor-*）

../media/        … トランスメディア（ストーリーボード・参考画像・動画）※docs外
../.claude/skills/ … 制作スキル（storyboard/seedance）＋レビュースキル（reader-personas/editor-kawahara/editor-tsukikage）
```

> **セッション開始時に読む**：[ops/current.md](ops/current.md) → [ops/backlog.md](ops/backlog.md)。構造的決定の前に [project_handover.md](project_handover.md)。

---

## 2. 各ディレクトリの責務

### 2-1. トップ層（直下2ファイル）

| ファイル | 役割 | いつ読む |
|---|---|---|
| [proposal.md](proposal.md) | 企画書。ログライン・USP・10巻構想・比較（アクセルワールド等） | 全体像を掴む時 |
| [stage_device_design.md](stage_device_design.md) | **世界設定の正本**。git＝作者側の整合エンジン。物理(append-only)・政治(偽origin/4学派)・経済(OSS遺産/タトゥー)・メディア(GitHub=ソース)・主人公/FAB | 設定の根拠を辿る時 |

### 2-2. [settings/](settings/) — 舞台装置の規格書（密結合・一体運用）

執筆・映像化で**描写がブレないための規格**。相互参照が密なため1ディレクトリで運用する。

| ファイル | 内容 |
|---|---|
| [settings/battle_system.md](settings/battle_system.md) | 戦闘・特訓（加速/二層/deploy/crash/心意級/成長＝積み上げ§3.5/飛躍§3.5-4） |
| [settings/ability_progression.md](settings/ability_progression.md) | **力の背骨**（記述の編集＝編集層の深化。しょぼい技→重力→ブラックホール→01/量子。徐々に開放） |
| [settings/digital_tattoo.md](settings/digital_tattoo.md) | 能力装備＝デジタルタトゥー（レア度/相性4分類/彫師ギルド/形見の継承） |
| [settings/anomaly_mark.md](settings/anomaly_mark.md) | あざ（自然・複製不可）／タトゥー（人工）の現象学 |
| [settings/locations.md](settings/locations.md) | **ロケーション**（自宅/学校/訓練/ダンジョン。表層×深層・移動） |
| [settings/dungeon_design.md](settings/dungeon_design.md) | ダンジョン設計（故人repo/固有現象/**実在地基盤・潜行・インスタンス生成**） |
| [settings/protagonist_core.md](settings/protagonist_core.md) | **主人公の核**（喪失と願い・容姿確定・10巻＝受容） |
| [settings/fab_persona.md](settings/fab_persona.md) | 相棒AI FAB の声・動機・嘘・削れ段階表 |
| [settings/factions.md](settings/factions.md) | マスターオリジン4学派＝組織と代表キャラ |

### 2-3. [plot/](plot/) — 連作構成

| ファイル | 内容 |
|---|---|
| [plot/series_arc_draft.md](plot/series_arc_draft.md) | 全10巻・3大弧・敵の階段・X伏せ開示・続編(upstream編) |

### 2-4. [manuscript/](manuscript/) — 執筆・試作

| パス | 内容 |
|---|---|
| [manuscript/prototypes/](manuscript/prototypes/) | 第1話の試作（規格書検証用）：[ep1_battle](manuscript/prototypes/prototype_ep1_battle.md)「静止した雨」／[ep1_sword](manuscript/prototypes/prototype_ep1_sword.md)「剣のひと」／[ep1_training](manuscript/prototypes/prototype_ep1_training.md)「ひと晩寝かせる」 |

### 2-5. [guides/](guides/) — 執筆規約

| ファイル | 内容 |
|---|---|
| [guides/writing_style_notes.md](guides/writing_style_notes.md) | 文体（ライトな現代口語・難語/造語回避・git非表示） |

### 2-6. [../media/](../media/) — トランスメディア（docs外）

ストーリーボード（3x3×9コマ）・参考画像・動画。制作手順は [../media/README.md](../media/README.md)。

---

### 2-7. 管理基盤（naro_novel から移植）

| ディレクトリ | 役割 |
|---|---|
| [ops/](ops/) | **中断復帰**。[current](ops/current.md)（進行スナップショット）／[backlog](ops/backlog.md)（優先タスク）／[worklog](ops/worklog.md)（履歴）／[snapshots/](ops/snapshots/) |
| [series/](series/) | **連作横断台帳**。[canon_log](series/canon_log.md)（確定事実）／[story_timeline](series/story_timeline.md)（年表）／[disclosure_ledger](series/disclosure_ledger.md)（**伏線・開示段階**）／[episode_id_convention](series/episode_id_convention.md)（ID規約） |
| [review/](review/) | レビュー結果の保存先（`reader-personas`／`editor-kawahara`／`editor-tsukikage`） |
| [project_handover.md](project_handover.md) | 作品コンセプト・著者要件・設計原則（時系列非依存） |
| [project_roadmap.md](project_roadmap.md) | フェーズ・タスクID規約・1話ワークフロー |

---

## 3. 新規ファイルの置き場所（迷ったら）

- **世界の根本ルール** → settings/ の該当規格書（無ければ stage_device_design に追記）
- **人物・勢力** → settings/（protagonist_core / fab_persona / factions）
- **巻構成・開示** → plot/
- **本文・試作** → manuscript/（試作は prototypes/）
- **文体・命名規約** → guides/
- **ストーリーボード・画像・動画** → ../media/
- **再構成が要るとき** → [../scripts/restructure_docs.py](../scripts/restructure_docs.py)（移動＋リンク自動張替え）

---

## 4. メンテナンス

- 各規格書は末尾に**改訂履歴**と**残課題**表を持つ。確定したら残課題を打ち消し線＋✅で更新。
- ファイル移動は [../scripts/restructure_docs.py](../scripts/restructure_docs.py) を使うとMarkdownリンクが自動で張り替わる（`--dry-run`で確認可）。
