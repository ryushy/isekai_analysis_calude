# プロジェクトロードマップ（フェーズ・タスクID規約）

> 全体の進行指針とタスクID命名規則（naro_novel から移植）。進行状況の現在地は [ops/current.md](ops/current.md)、優先順位は [ops/backlog.md](ops/backlog.md)。

---

## 1. フェーズ

| フェーズ | 名称 | 内容 | 状態 |
|---|---|---|---|
| **Phase 0** | 舞台装置の設計 | 世界・戦闘・装備・成長・人物・勢力・連作の規格書化、第1話の核確定 | **ほぼ完了** |
| **Phase 1** | 第1話の実証 | 第1話プロット＋本文（試作の統合・昇格）、多角レビュー | 進行予定 |
| **Phase 2** | 大弧I 執筆 | B1〜B3（覚醒・特訓・最初の仲間・4学派登場） | 未着手 |
| **Phase 3** | 大弧II 執筆 | B4〜B7（学派政治・deploy倫理・偽origin・7巻裏切り） | 未着手 |
| **Phase 4** | 大弧III 執筆 | B8〜B10（起源・黒幕・中心の誘惑・10巻受容） | 未着手 |
| **Media** | トランスメディア | ストーリーボード／短尺動画（バトルイメージ先行） | 随時並走 |

---

## 2. タスクID命名規約

形式：`P{フェーズ}-{種別}-{連番2桁}`（フェーズ非依存の運用系は接頭辞のみ）。

| 種別 | 意味 | 例 |
|---|---|---|
| `SET` | 設定・規格書 | `P0-SET-03` |
| `PT` | プロット・章アウトライン | `P1-PT-01` |
| `CC` | 本文執筆（章/話） | `P1-CC-01` |
| `REV` | レビュー（読者/編集者） | `REV-02` |
| `MED` | メディア（画像/動画） | `MED-01` |
| `OPS` | 運用・基盤 | `OPS-02` |

- 話単位のアドレスは **ID規約**（[series/episode_id_convention.md](series/episode_id_convention.md)）の `B{巻}-{章}-{話}` を使う（タスクIDとは別系統）。
- バックログの各タスクに ID・状態（todo/wip/done/blocked）・依存 を付ける。

---

## 3. ワークフロー（執筆1話あたりの標準）

1. **章アウトライン**（PT）：[series/disclosure_ledger.md](series/disclosure_ledger.md) で開示可否を確認しながら章の引き・伏線配置を決める。**各ビートに、出来事だけでなく「五感・内面・会話・戦闘の手触り」の素を1つずつ書き込む**（あっさり防止・[guides/writing_style_notes.md §4.5](guides/writing_style_notes.md)）。1話の目安＝5,500〜6,500字。
2. **本文執筆**（CC）：[guides/writing_style_notes.md](guides/writing_style_notes.md) 準拠。git 非表示・ライト口語・失敗の描写。**プロットで仕込んだ四要素（五感/内面/会話/手触り）を各シーンに展開**。
3. **機械検査＋密度チェック**：`python scripts/check_manuscript.py <原稿>` で AI 執筆の癖（git語露出・地の文太字・難語・早出し語 等）を NG ゼロに（[guides/ai_writing_pitfalls.md](guides/ai_writing_pitfalls.md)）。あわせて**字数（目安内か）と密度（四要素が各シーンにあるか）**を確認。
4. **台帳更新**：確定事実→[series/canon_log.md](series/canon_log.md)、開示実績→disclosure_ledger。
5. **レビュー**（REV）：機械検査の後に `reader-personas`→`editor-kawahara`/`editor-tsukikage`。指摘を改稿に反映。
6. **メディア**（MED・任意）：`storyboard`→`seedance`。
7. **ops 更新**：current.md を更新、worklog に追記。

---

## 改訂履歴

| 日付 | 内容 |
|---|---|
| 2026-06-14 初版 | フェーズ（0設計〜4大弧III＋Media）・タスクID規約・1話標準ワークフローを整備 |
