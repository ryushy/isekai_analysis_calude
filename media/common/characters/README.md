# common/characters/

複数話で使うキャラクター素材の置き場です。今後は「実在モデル写真を用意する → キャラ候補を複数生成する → 良いものを採用する」という流れで管理します。

## 導線

1. 実在モデル写真を置く
   - 作業前の未整理写真: `_incoming-model-photos/`
   - キャラ別の生写真: `character-*/references/model-photos/private/`
   - 生成に使ってよい選抜済み写真: `character-*/references/model-photos/approved/`
2. キャラ化プロンプトを作る
   - `character-*/prompts/`
3. 候補を複数生成する
   - `character-*/generations/run-YYYYMMDD_HHMMSS/`
4. 採用版だけを正典として出す
   - `character-*/outputs/ref_sheet_v*.png`

## フォルダの意味

```text
characters/
├── _incoming-model-photos/        # 未整理のモデル写真。原則コミットしない
├── character-nagi/
│   ├── references/
│   │   ├── model-photos/
│   │   │   ├── private/           # 生写真。原則コミットしない
│   │   │   └── approved/          # 生成に使ってよい選抜済み参照
│   │   └── style/                 # 衣装・髪型・雰囲気などの非人物参照
│   ├── prompts/                   # キャラシート生成・改訂プロンプト
│   ├── generations/               # 複数回生成した候補
│   └── outputs/                   # 採用済みの正典キャラシート
└── character-mio/
    └── ...
```

## 採用ルール

- `generations/` の候補は消さず、比較・再利用できるように残します。
- `outputs/` は各話の画像生成が参照する正典です。差し替える場合は旧版を `generations/` または `archive/` に残してから更新します。
- 実在人物の写真は、本人・権利者の許可があるもの、または制作上利用してよいものだけを `approved/` に移します。
