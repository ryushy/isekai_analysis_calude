# 運用基盤 README（中断からの即時復帰）

> 作業中断からの即時復帰を可能にする運用基盤（naro_novel から移植）。
> 本ディレクトリは「**作業状態の管理**」担当。設定（[../settings/](../settings/)）・物語（[../plot/](../plot/)）・台帳（[../series/](../series/)）・本文（[../manuscript/](../manuscript/)）とは役割が分離されている。

---

## 0. 層の責務分離

| 層 | 場所 | 担当 | 永続性 |
|---|---|---|---|
| **メモリ層** | `~/.claude/projects/.../memory/` | 横断知識・ユーザー像・進行スタイル・WHY | 全セッション永続（自動ロード） |
| **作業状態層** | `docs/ops/`（本ディレクトリ） | バックログ・進行中作業・完了履歴・節目スナップショット | Git 管理・永続 |
| **総括引き継ぎ層** | [../project_handover.md](../project_handover.md) | 作品コンセプト・著者要件・設計原則（時系列非依存） | Git 管理・永続 |
| **台帳層** | [../series/](../series/) | 確定事実・年表・伏線開示・ID | Git 管理・永続 |

**使い分け**：

- 「ユーザーはこう言うとこう判断する人だ」→ メモリ
- 「次にやるべき作業は○○、理由は△△」→ [backlog.md](backlog.md)
- 「いま中断するなら、再開時にここから始めよ」→ [current.md](current.md)
- 「日々の小さな完了の記録」→ [worklog.md](worklog.md)
- 「節目の凍結記録」→ [snapshots/](snapshots/)
- 「作品の不変のコンセプト・設計原則」→ [../project_handover.md](../project_handover.md)

**重複回避の鉄則**：

- 同じ事実は **1ファイル1箇所**。他からはリンク参照。スナップショットを current/worklog にコピペしない。
- スナップショットは凍結記録（作成後は基本編集しない。直したくなったら新規作成）。

---

## 1. ファイル構成

```text
docs/ops/
├── README.md   … 本ファイル
├── current.md  … 進行スナップショット（中断復旧の中核）
├── backlog.md  … 優先順位付きバックログ（タスクID・状態・依存）
├── worklog.md  … 完了タスクの履歴（追記式・時系列）
└── snapshots/  … 節目の凍結スナップショット（INDEX.md）
```

## 2. セッション運用

- **開始時**：[current.md](current.md) → [backlog.md](backlog.md) を読む。
- **終了時**：[current.md](current.md) を必ず更新。完了タスクは [worklog.md](worklog.md) に追記。
- **節目**：フェーズ完了時に [snapshots/](snapshots/) に凍結記録を作り INDEX に1行追加。

## 3. タスクID

[../project_roadmap.md](../project_roadmap.md) の命名規約に従う。例：`P0-SET-03`（Phase0・設定・3番）／`P1-CC-01`（Phase1・執筆・1番）／`MED-02`（メディア）／`OPS-01`（運用）。
