# 現状スナップショット（中断復旧用）

> 「いま中断するなら、再開時にここから始めよ」を**最小限**で表す。
> セッション開始時にまず読み、終了時に必ず更新する。詳しい運用は [README.md](README.md)。

---

## 最終更新：2026-06-16

**フェーズ**：**Phase 0（舞台装置の設計）＝ほぼ完了**。設定の主要レイヤー（世界・戦闘・装備・成長・人物・勢力・連作）を規格書化し、第1話の核（喪失・容姿・10巻受容）まで確定。第1話の試作3本＋ストーリーボード3枚を作成。動画ワークフロー（storyboard/seedance スキル）と**管理基盤（ops/series/レビュースキル）を本セッションで導入**。

## いま走っているもの

- ✅ 設定規格書：[battle_system](../settings/battle_system.md)／[digital_tattoo](../settings/digital_tattoo.md)／[anomaly_mark](../settings/anomaly_mark.md)／[dungeon_design](../settings/dungeon_design.md)／[fab_persona](../settings/fab_persona.md)／[factions](../settings/factions.md)／[protagonist_core](../settings/protagonist_core.md)
- ✅ 第1話試作3本：[prototypes/](../manuscript/prototypes/)（静止した雨／剣のひと／ひと晩寝かせる）
- ✅ **第1話 本文 v0.6**：[manuscript/book1/01_modori_jirushi.md](../manuscript/book1/01_modori_jirushi.md)「戻り標」（横浜＝学校:山手／**ダンジョン:コスモワールドの非常口**＝SEKAI NO OWARI〈炎と森のカーニバル〉着想。**第1ダンジョンを駅→遊園地へ移設・固有現象＝記録の雨は維持**・空白除き約6,000字）。**敵＝道化の楽団を「謎集団」に格上げ**＝native＝獣／Ep1はバグ介入で道化集団が上書き侵入（FABの一言＋違和感で開示安全に伏線化＝[canon_log C-028](../series/canon_log.md)・[disclosure §2](../series/disclosure_ledger.md)）。**4レビュー（霧島/速水/縞田/九条/夏目）がL109密度過多＋道化の伏線弱に収束→園内3カット化＋遠くのオルガン先植えで解消**。レビュー＝[review/01_*](../review/)
- ✅ 第1話ハイライト（確定容姿v2）：[../../media/book1/ep1/highlights/](../../media/book1/ep1/highlights/)（旧 storyboard を highlights へ再編・剣/バトル）
- ✅ 制作スキル：`storyboard`／`seedance`（codex MCP・Higgsfield 確認済）
- ✅ 管理基盤：ops三層・series台帳（canon/timeline/disclosure/episode_id）・レビュースキル3（reader-personas/editor-kawahara/editor-tsukikage）
- ✅ **第2話 本文 v0.4**：[manuscript/book1/02_mirareteita.md](../manuscript/book1/02_mirareteita.md)「見られていた」（篠宮澪 初登場・見逃しの三本足場・点vs面・コスチューム変身・ラッキースケベの緩・**4レビュー収束3点反映**＝章末の引き一撃化/イレギュラー発生トリガー/突破に一拍のつまずき・約6,100字＝NG0/WARN0）。
- ✅ **第2話 4レビュー検証完了（全員マージ可・必須修正なし）**：[kawahara](../review/02_kawahara.md)（構造）／[tsukikage](../review/02_tsukikage.md)（テンポ・ラッキースケベ採用維持）／[readers](../review/02_readers.md)（3読者）／[actor](../review/02_actor.md)（役者）。
- ✅ **キャラクターシート**：[character_sheet_mio.md](../settings/character_sheet_mio.md)（澪＝顔/体型写真2枚・森脇リリカ参照・ラッキースケベ§3.5・§7ビジュアル仕様）／[character_sheet_nagi.md](../settings/character_sheet_nagi.md)（ナギ・§7）。生成補助＝`character-sheet` スキル。
- ✅ **レビュースキル追加**：[actor-review](../../.claude/skills/actor-review/SKILL.md)（演出家・霧島怜＝役者目線で行動の妥当性／唐突さ/キャラブレ検出）。reader-personas/editor-kawahara/editor-tsukikage と並ぶ第4のレビュアー。
- ✅ Git運用：ブランチ運用＋フック（pre-commit/commit-msg/post-commit＋Claude SessionStart/Stop）＋`git-flow`スキル。**第2話プロット・ヒロイン設定・学校確定まで main へマージ済**。**本セッション分（ヒロイン確定v0.2・ep2_plot v0.3・第2話本文v0.2・コスチューム機構C-027・文体ルールv0.2）は未コミット**。

## 次のアクション（優先順）— ★ここから再開する

> 直近の流れ：第2話本文化 → **本セッション：第3話プロット設計 → 著者決定で再構成＝「拠点獲得説明会」回を新第3話に挿入し、特訓＋削れ＋澪共闘を第4話へ繰り下げ**。背景アセット[honmoku_station_hideout_night_v1.png](../../media/common/backgrounds/honmoku-phantom-station-hideout/outputs/honmoku_station_hideout_night_v1.png)（温かい隠れ家化）を物語化。

- ✅ **第3話プロット v0.2**：[ep3_plot.md](../plot/ep3_plot.md)「終わらない終着駅」＝**拠点獲得＋説明会**（再アクセス→当たりインスタンス→**タグ固定**→冷たい廃駅→温かい隠れ家）＋**初めてここで眠る＝削れの種（実害なし・予感のみ）**。固有現象＝終わらない終着駅（待ち続けて発てなかった人＝喪失の鏡）＝[canon_log C-029](../series/canon_log.md) 確定。澪は不在（共闘は第4話）。
- ✅ **第4話プロット v0.3**：[ep4_plot.md](../plot/ep4_plot.md)「眠っている間に」＝**特訓本番＋削れの代償（L1→L2・実害）＋澪共闘（点vs面の補完＝最初の仲間へ）**。第3話の"種"を実害で払う。
- ✅ **第3話・第4話プロットの4レビュー完了**：[synthesis](../review/ep3-4_plot_synthesis.md)（[九条](../review/ep3-4_plot_kawahara.md)/[夏目](../review/ep3-4_plot_tsukikage.md)/[読者3](../review/ep3-4_plot_readers.md)/[霧島](../review/ep3-4_plot_actor.md)）＝**収束8点を両プロットに反映済**（必須2＝削れ受容トリガー/FAB開示の推量化、推奨6＝説明会の体験化/引き一撃化/連携しくじり/澪違和感止まり＋コメディ重層/種＝受けかけて呑む/条件付き安全）。**両プロットともマージ可水準**。
- ✅ **第3話 本文 v0.2**：[03_owaranai_shuchakueki.md](../manuscript/book1/03_owaranai_shuchakueki.md)「終わらない終着駅」（拠点獲得＝タグ固定・スローライフ＋削れの種・**おばさんの口ぐせ「いってらっしゃい。寄り道は、ほどほどにね」を先植え**）。
- ✅ **第4話 本文 v0.2**：[04_nemutteiru_aida_ni.md](../manuscript/book1/04_nemutteiru_aida_ni.md)「眠っている間に」（特訓失敗・澪合流・点vs面の共闘・**澪に庇い返されて削れを受容＝口ぐせが消える**・澪が証人）。
- ✅ **第3話・第4話 本文の4レビュー完了→収束反映**：[synthesis](../review/ep3-4_honbun_synthesis.md)（[九条](../review/ep3-4_honbun_kawahara.md)/[夏目](../review/ep3-4_honbun_tsukikage.md)/[読者3](../review/ep3-4_honbun_readers.md)/[霧島](../review/ep3-4_honbun_actor.md)）＝**全員マージ可・開示違反なし**。**収束A〜Eを本文v0.2に反映**（必須＝澪の名乗り補完／第4話決壊の所作・密度回復、推奨＝庇い返しの身体先行／第3話の反復圧縮／FAB「たぶん」整理）。**未コミット**。先メモ＝今後「管轄じゃないもの」の宿題を次話で動かす／「あざの熱」締めは第5話で一度別の引きに。

- ✅ **ARC-01＝book1 全体構想 完了**（2026-06-15）：著者決定3点＝①**巻1は「最初の仲間（澪）確立＋当面の敵への初の決着」まで＝約18〜20話**②**巻1の当面の敵＝監視機構の末端（非致死の追跡者・撃破でなく出し抜く決着）**③**series_arc 10行表＝弧ビート（到達点）と再定義し二層化**。成果物＝[book1_structure.md](../plot/book1_structure.md)（分析・決定台帳）＋[book1_skeleton.md](../plot/book1_skeleton.md)（巻1正本＝4ブロック構成・縦糸5本）。[series_arc_draft.md](../plot/series_arc_draft.md) v0.2／canon C-032／[factions §4](../settings/factions.md) 反映済。

1. ✅ **追跡者の人物設計＝完了**（2026-06-16）：著者決定3点（外見＝**中年の冷徹な実務官**／通称＝**「足取りの鵜飼」で確定**／芯＝**澪の未来の影**＝葛藤を職務で殺した先輩監察官＝澪が報告保留を続けた先の姿＝警告の鏡像）で核ドキュメント [antagonist_ukai_core.md](../settings/antagonist_ukai_core.md) を新設。skeleton §1.5（人物設計確定へ昇格）・[C-035](../series/canon_log.md)・[factions §4](../settings/factions.md)・[disclosure §2](../series/disclosure_ledger.md)（鵜飼の過去＝B1は既視感のみ）反映。
2. ✅ **第5話プロット v0.1＝作成**（2026-06-16）：[ep5_plot.md](../plot/ep5_plot.md)「足取り」＝第2ブロック開幕＝**追跡者「鵜飼」の初提示**（鵜＝白い光の気配→痕跡→初の顔出し＝静かな通告）。第1話「帰還の脆さ・戻り標」＋第3話「条件付き安全＝戻り標は残る」を**追跡能力として回収・脅威化**／**居場所が帰り道から読まれる恐怖**／**澪の報告保留が体制に露見し始める圧**／**鵜飼＝澪の未来の影の種＝既視感のみ**／点vs面が"撃てない"側に回る＝出し抜く決着の布石。**要・著者レビュー＋4レビュー**。
3. ✅ **機構更新＝ダンジョン再訪の二層化（[C-036](../series/canon_log.md)・2026-06-16 著者決定）**：**戻り標は時限で薄れる（永続しない）／シード値＝深層の核に到達して取得すれば戻り標なしで再訪＝足跡を断つ(go dark)**。「戻り標が永久に残る将来制約」を解消し、鵜飼を時間圧力のある追っ手に・**シード切替を出し抜く決着の機構**に格上げ。秘密基地＝**一発で当たりを引き核に到達してシード取得**（C-029「タグ固定」→「シード固定」読み替え）。[dungeon §1.5-6](../settings/dungeon_design.md)新設・[battle §1-3](../settings/battle_system.md)・[locations §4.5](../settings/locations.md)・[antagonist_ukai_core §2-3](../settings/antagonist_ukai_core.md)・[ep5_plot](../plot/ep5_plot.md) 反映。
4. ✅ **第5話プロット 4レビュー検証＝完了→v0.2 反映**（2026-06-16）：[synthesis](../review/ep5_plot_synthesis.md)（[九条](../review/ep5_plot_kawahara.md)条件付き可/[夏目](../review/ep5_plot_tsukikage.md)可/[読者3](../review/ep5_plot_readers.md)6-5-7/[霧島](../review/ep5_plot_actor.md)条件付き可）。**必須4＋推奨3を [ep5_plot.md](../plot/ep5_plot.md) v0.2 に反映**＝A 皮肉の因果を場所＋澪の体感で結ぶ／B 戻り標"薄れる"を第5話で自然初提示／C 鵜飼の通告を一本化＋所作で語る・名乗りは拾わせる／D 澪の既視感＝身体の引き金＋非対称／E 中盤を空間↔理屈で撃ち分け＋ナギの小さな能動／F「確認中です」を身体の事件に／G シード予感を欠落の問いへ。**全員マージ可水準**。
5. ✅ **第5話プロットの残課題＝確定**（2026-06-16 著者決定4点）：①顔出し＝**ラストで初顔出し＝通告**②引き＝**ナギ視点（入口の白い光）**③タイトル＝**「足取り」**④戻り標「薄れる」＝**第3話本文に一語足す軽微遡及**（[03](../manuscript/book1/03_owaranai_shuchakueki.md) 修正済）。ep5_plot §5 を確定マーク。
6. ✅ **第5話 本文 v0.2＝完成**（2026-06-17）：[05_ashidori.md](../manuscript/book1/05_ashidori.md)「足取り」（約5,573字・NG0/WARN0）。v0.1執筆→**4レビュー（[synthesis](../review/05_synthesis.md)＝[九条](../review/05_kawahara.md)条件付き可/[夏目](../review/05_tsukikage.md)条件付き可/[読者3](../review/05_readers.md)6-8-8/[霧島](../review/05_actor.md)可）→必須3＋推奨3を反映**（引きの一撃化／既視感を症状へ＝開示整合／二重説明・詭弁の地の文を薄める／「確認中です」を意思に反し先に／一瞥を一拍長く／包囲の手触り）。全員マージ可水準・開示違反なし。
7. **【次の一手】第2ブロック B1-06〜10 の話数配分・第6話プロット**：鵜飼の圧の段階・澪の露見の進度を割る。第6話＝白い光への対処の模索／go dark（シード）の糸口／鵜飼の二度目。
8. 任意：巻1の縦糸（削れの天秤／監視／澪の仲間化／喪失／道化の気配）の出し入れを第2〜巻末ブロックで配分（[book1_skeleton.md §2](../plot/book1_skeleton.md)）。
9. 任意：ストーリーボード（隠れ家establishing は確定済アセットあり／点vs面の共闘絵は第4話／鵜＝白い光の意匠）。

> 進捗：第2ブロックの基盤（鵜飼人物設計＋戻り標/シード機構C-036＋第5話プロットv0.2＋第5話本文v0.2）まで main マージ済。第5話本文 v0.2＋レビュー5本は本セッションでマージ予定。

- **開示厳守**：重力/量子/4学派/Mythos/偽origin/喪失真相/"上"の正体は完全隠蔽（大弧I前半）。B2段階の上限＝[disclosure_ledger](../series/disclosure_ledger.md)。

## 引っかかり・判断待ち

- ✅ **第1話の漢字レベル是正＝完了**（v0.4＝LN相当・シールド統一・NG0/WARN0）。第1話・第2話の文体基準がそろった。
- **剣の少年＝温存**：後巻の近接ライバル候補（聖光モチーフ男子校）。当てる巻は series_arc 設計時。
- **イレギュラーの収束のさせ方[未決]**：第2話で誰が・何で鎮めたか（一過性の扱い）は本文で曖昧化したまま＝後で要設計（ep2_plot §5）。
- 主人公の正式名（現「ナギ」仮）・どの国の欧米ハーフか（あざ意匠と連動）＝[protagonist_core 残課題](../settings/protagonist_core.md)。
- 4学派の人物・組織名は全て仮（[factions 残課題](../settings/factions.md)）。

## 改訂履歴（直近5世代）

| 日付 | 更新概要 |
|---|---|
| 2026-06-15 | **ARC-01＝book1 全体構想 完了**。著者決定3点（巻1≈18〜20話・到達点＝最初の仲間確立＋当面の敵への初の決着＋削れの天秤起動／当面の敵＝監視機構の末端＝非致死の追跡者／series_arc 10行表＝弧ビート再定義し二層化）。[book1_structure.md](../plot/book1_structure.md)＋[book1_skeleton.md](../plot/book1_skeleton.md) 新設、series_arc v0.2・canon C-032・factions §4 反映。次の一手＝巻1第2ブロック設計（追跡者の人物設計→第5話プロット） |
| 2026-06-14 | 初版。Phase0 完了間際の状態＋管理基盤導入を記録 |
| 2026-06-14 | 第2話プロット作成→**剣の少年を弓道狙撃ヒロイン（監視役・見逃す葛藤型）へ置換**（[heroine_core.md](../settings/heroine_core.md) 新設）。**学校確定**（聖光/雙葉モチーフ・モチーフ化・C-025/C-026）。すべて main マージ済。**次の一手＝ヒロインのキャラ設計→第2話本文化** |
| 2026-06-14 | **キャラクターシート作成**（[mio](../settings/character_sheet_mio.md)＝顔/体型リファレンス写真2枚・ペルソナ森脇リリカ参照・**ラッキースケベ的接触§3.5**／[nagi](../settings/character_sheet_nagi.md)）。澪の容姿に**素の柔らかさ（凛↔柔の二面）**を追加。**役者目線レビュースキル [actor-review](../../.claude/skills/actor-review/SKILL.md)（演出家・霧島怜）を新設**＝行動の妥当性/唐突さ/キャラブレ検出。**第2話に適用**（[review/02_actor.md](../review/02_actor.md)）→検出「ナギが澪を庇う動機が薄い」を本文v0.3で補強＋ラッキースケベの緩を追加 |
| 2026-06-14 | **第2話を4レビュアーで検証**（kawahara/tsukikage/readers/actor＝全員マージ可・必須修正なし）。**収束3点を本文v0.4で反映**＝①章末の引きを一撃に②イレギュラー発生トリガー補強③突破に一拍のつまずき（インフレ回避）。`character-sheet` スキル＋§7ビジュアル仕様を追加。**main マージ→第3話へ** |
| 2026-06-14 | **ヒロイン確定**（篠宮澪／弓＝外付け支給品／聖稜学院・山手聖二葉女学院・容姿/口調/出自）。著者FB「葛藤が唐突」→**見逃しの三本足場**（手順/弓道の規律/**第3勢力＝ダンジョンのイレギュラー共闘**＝弓と相性悪い"点の無い混沌"・点vs面）でヒロイン§1.5・ep2_plot v0.3 を再設計。**第2話本文 v0.2 執筆**（NG0/WARN0）。著者FB反映＝**漢字レベルLN相当に是正（writing_style §1.1）**・《アンブレラ》＝**半透明のシールド**統一・**コスチューム変身機構**（digital_tattoo §6.5・C-027＝深層で能力外在化・澪=和風射手装束 mio_deep_layer_archer_costume_yoimiya_ref.png 黒髪版）。**未コミット**＝次は main マージ＋第2話レビュー |
