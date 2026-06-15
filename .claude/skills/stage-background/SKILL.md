---
name: stage-background
description: Use this when the user wants to create CVE-0 stage / dungeon BACKGROUND images (深層インスタンスの背景・舞台) via codex — from a real location/reference image OR from imaginative text. The same place keeps its 固有現象 (master's identity) while the ENVIRONMENT is rolled randomly (time of day, weather, mood/energy, terrain mutation like 森化/水中, stage trait like cyberpunk) per dungeon_design §1.5-3. Claude authors the prompt (scene identity + rolled variant), codex generates the image only. Use for 背景/ステージ/ダンジョン/環境/舞台画像 requests. Do NOT use for character model sheets (=`character-sheet`) or 9-frame storyboards (=`storyboard`).
---

# Stage Background（背景・ステージ画像作成）

CVE-0 の**深層ステージ（実在地ベースのダンジョンインスタンス）の背景画像**を codex で起こす。
**役割分担：Claude が台本（シーン同一性＋環境バリアント）、codex は画像生成のみ**（台本の創作はさせない）。`character-sheet` と同じ作法。

## 中核アイデア（正典の根拠）

> 同じ口でも入るたびに別インスタンス＝**「固有現象（同一性）は保ち、天候・時間・歪み方はランダム」**（[dungeon_design.md §1.5-3](../../../docs/settings/dungeon_design.md)）。これを画にする。

- **同一性（保持）**：場所の実在地ベース（[locations.md](../../../docs/settings/locations.md)＝本牧/山手/みなとみらい/幻の地下鉄駅 等）＋その master の**固有現象**（記憶のにじみ＝そのダンジョンの癖）。
- **可変（ロール）**：時間帯・天候・トーン/エネルギー・**地形変容（森化・水没＝水中・氷結 等）**・**ステージ特性（サイバーパンク化・記録の雨 等）**を毎回振る（[references/variants.md](references/variants.md)）。
- **演出原則＝「現実にありえない一点」**：実在地を歪めるとき、現実では起こりえない要素を1つ置き「ここは現実じゃない」を**台詞なしで**伝える（例＝地下なのに雨／止まった人波／天井へ伸びる階段）。
- **現実世界／ダンジョンを事前に区分する**：
  - **現実世界**（表層・実在地）＝**実写ベースで構図を忠実に再現**。改変しない（建築・配置・象徴物を写真どおり）。実写が無ければ [reference-fetch.md](references/reference-fetch.md) で取得。
  - **ダンジョン**（深層インスタンス）＝**ご都合主義で改変可**（何でもあり＝森化・水没・サイバーパンク化・固有現象）。**ただし元（実在地／前バージョン）の構図はできるだけ維持**し、無秩序にしない。

## 前提

- codex MCP 接続済み（`claude mcp list` に `codex ... ✔ Connected`）。未接続なら [seedance/references/setup.md](../seedance/references/setup.md) を案内。
- 入力は2系統：**(A) 実在地・参考画像**（locations の実在地／`media/common/reference/`／著者提示の参考画像）を歪めた深層版／**(B) 創造上のテキスト**（幻の地下鉄駅・未踏の場所など表層に無い場所）。
- **(A) で参考写真が無い／不足なら、手で用意せず [references/reference-fetch.md](references/reference-fetch.md) のフロー**（Web検索→`Special:FilePath`でcurl取得→分析→`media/common/reference/locations/<slug>/REFERENCE.md` に DNA をキャッシュ）で入手・再利用する。既にカードがあれば再取得しない。
- 表現規則は storyboard と共通：縦横は用途で選ぶ（establishing＝16:9 シネマ／seedance 連携＝縦9:16）。**読める文字・数字・HUD を出さない／git・専門語は世界観上も非表示／FAB＝淡い光のみ**。

## ワークフロー

1. **案件フォルダ**を `media/{common|book{N}/ep{M}}/backgrounds/<location-slug>/` に作る（`outputs/`・`references/`・`scene_input.md`）。slug は英数字とハイフン。
2. **STEP1 シーン同一性** `scene_input.md`：場所を決める。①**実在地ベース**（どの実在地か＝locations 準拠）②**固有現象**（誰の repo のにじみ＝そのステージの癖・同一性）③**ありえない一点**。入力が参考画像なら Read で見て構図・要素を文章化（画像は入力。生成物と区別）。
3. **STEP2 環境バリアントをロール** `scene_input.md` 内に記録：[references/variants.md](references/variants.md) の各軸（時間帯／天候／トーン／地形変容／ステージ特性／アートスタイル）を**ランダムに振る**（`bash` で `shuf`／`$RANDOM`）か、ユーザー指定（例「夜」「荒廃」「森と化す」「水中」）を採用。同じ場所で複数バリアントを出すと「毎回違う姿」を可視化できる。
4. **GATE 表現規則**：読める文字/数字/HUD なし／git・専門語を画面と説明に出さない／FAB＝光のみ／実在の固有名・ロゴを描かない／**同一性（実在地＋固有現象）が保たれているか**／ありえない一点が入っているか。
5. **STEP3 背景プロンプト**：英語で1枚分を作る。構成＝`Scene(同一性) + Variant(時間/天候/トーン/地形変容/特性) + Art style + Strict rules(no text/number/HUD)`。複数バリアントを1枚に並べる「バリアントシート」も可（隅に番号のみ）。
6. **STEP4 codex で生成**：codex MCP（`mcp__codex__codex`）に**生成だけ**依頼（プロンプト一字一句変えず）。`cwd`=リポジトリ直下／`sandbox`=workspace-write／`approval-policy`=never。参考画像で寄せる場合は**案件の `references/` に取り込んでから**渡す（外部パス＝OneDrive 等はサンドボックス外で読めないことがある）。出力＝`outputs/<location>_<variant>_vN.png`。
7. **レビュー**：生成PNGを Read で確認し、同一性・ありえない一点・表現規則を点検。案件 README/`scene_input.md` に v 記録。直すならプロンプト修正→ v+1。
8. **動画化**：背景OKなら `seedance`（縦9:16・1ショット）へ。キャラを乗せるなら `character-sheet` の正典ブロックを併用。

## レイヤー方針（既定）＝背景プレートとキャラは分離する

> CVE-0 の画像は**「背景プレート（人物なし）」＋「キャラ（[character-sheet](../character-sheet/SKILL.md) の正典）」を別レイヤー**で持ち、動画化（[seedance](../seedance/SKILL.md)）時に**それぞれ別参照として指定して合成**する。理由＝背景は使い回せる／キャラは差し替え・action系は何度も試せる。

- **背景プレートには人物（主人公・敵キャラ含む）を描かない**（純粋な舞台・環境のみ）。再利用の基盤。
- 制作順＝**①背景プレートを先に作る → ②その上にキャラを載せた版を作る → 両方を保存**（`outputs/`＝キャラ込み／`outputs/plates/`＝背景のみ、等で分離）。
- 動画時は seedance で「この画像が背景／この画像がキャラ」と**役割を明示**して渡す。
- 例外＝1枚絵の観賞用などキャラを焼き込みたい時は、**背景プレートを基にキャラ版を追加**する（プレートは必ず残す）。

## 固定ルール

- **codex には生成だけ依頼**（プロンプト・シーンの創作をさせない）。生成手段が使えない場合 codex は課金せず正直に報告する旨を依頼文に明記。画像生成はユーザーが明示的に望んだ時のみ。
- 読める文字/数字/HUD を出さない／**git・専門語は非表示**／FAB＝淡い光のみ／武器・能力＝光の象徴。
- **同一性を壊さない**：環境をどれだけ振っても、実在地ベースと固有現象（そのステージの癖）は保つ（無秩序にしない＝§1.5-3 の balance）。
- 実在の固有名・ロゴ・実在人物は描かない（モチーフ化）。日本語で記述。
