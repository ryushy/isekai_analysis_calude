# highlights/runs/

ハイライト画像を複数回生成したときの候補を残す場所です。

```text
runs/
└── run-YYYYMMDD_HHMMSS/
    ├── prompt.md
    ├── outputs/
    ├── plates/
    ├── contact_sheet.jpg
    └── review.md
```

採用版だけを `../outputs/` に置きます。過去候補は比較や再生成の参照に使うため、すぐ削除しません。
