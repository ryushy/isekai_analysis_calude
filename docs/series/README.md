# series/ — 連作横断の台帳

> 巻をまたいで管理する「事実・時系列・開示・ID」の正本群（naro_novel から移植）。

| ファイル | 役割 | 可変性 |
|---|---|---|
| [canon_log.md](canon_log.md) | **確定事実の追記式正本**（C-NNN）。撤回も新行で記録 | append-only |
| [story_timeline.md](story_timeline.md) | 世界・主人公の**年表**。整合性チェックの基準 | 低頻度更新 |
| [disclosure_ledger.md](disclosure_ledger.md) | **伏線・隠蔽の開示段階**（誰が/読者が/いつ知ったか）。執筆前後に必ず照合 | 可変（現在状態） |
| [episode_id_convention.md](episode_id_convention.md) | **物語全体→Book→章→話** のID規約 | 規約 |

## 使い分け

- 「これはもう確定した事実か？」→ canon_log
- 「この章でこれを書いていいか？（まだ伏せるべきか）」→ disclosure_ledger
- 「いつの出来事か・矛盾しないか」→ story_timeline
- 「このシーンのアドレスは？」→ episode_id_convention
