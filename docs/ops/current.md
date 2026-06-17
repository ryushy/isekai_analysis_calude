# 現状スナップショット（中断復旧用）

> 「いま中断するなら、再開時にここから始めよ」を**最小限**で表す。
> セッション開始時にまず読み、終了時に必ず更新する。詳しい運用は [README.md](README.md)。

---

## 最終更新：2026-06-17

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
7. ✅ **第2ブロック B1-06〜10 話数配分＝提案 v0.1 作成**（2026-06-17）：[book1_skeleton §1.6](../plot/book1_skeleton.md)。go dark成立は第3ブロック決着のため、第2ブロックは「答え（go dark）に手を伸ばすが届かない」5話＝核到達の危険／削れの誘惑／澪を巻き込む足跡、の三すくみ。**著者確認待ち＝①go darkの糸口を第6話で出すか②道化（管轄外）を第2ブロックで動かすか③澪の露見を上司/鵜飼直接どちらから④6話で足りるか**（＝ここが現在の blocker）。
8. ✅ **第2ブロック4分岐＝著者確定**（2026-06-17）：go dark糸口＝第6話／道化＝第2ブロックで共有宿題／澪露見＝鵜飼が直接／6話のまま。skeleton §1.6 確定マーク。
9. ✅ **第6話プロット v0.1→4レビュー→v0.2**（2026-06-17）：[ep6_plot.md](../plot/ep6_plot.md)「帰り方」＝go darkの糸口（核に降りて種を持ち帰る＝足跡を断つ帰り方／核到達は深層の危険で手が届かない）＋削れ誘惑の再燃（延命↔根治の二択）＋鵜飼の包囲継続＋澪の守りの連携。[synthesis](../review/ep6_plot_synthesis.md)＝必須4（二択を同じ軸に／保留を意志的決断＋ナギの能動／核入口を能動の溜め／因果を体感化）＋推奨3を反映。引き＝核の気配で確定。**全員マージ可水準**。
10. ✅ **第6話 本文 v0.2＝完成**（2026-06-17）：[06_kaerikata.md](../manuscript/book1/06_kaerikata.md)「帰り方」（約5,525字・NG0/WARN0）。v0.1執筆→4レビュー（[synthesis](../review/06_synthesis.md)＝[九条](../review/06_kawahara.md)条件付き可/[夏目](../review/06_tsukikage.md)条件付き可/[読者3](../review/06_readers.md)7-8-9/[霧島](../review/06_actor.md)可）→必須3＋推奨を反映（核入口の順序逆転＝FABの前に自分で決める／引きの助走圧縮／二択独白の反復削減→澪の対話へ／勝ちの余韻・温もり前借り）。全員マージ可水準・開示違反なし。
11. ✅ **第5レビュアー `screen-review`（久遠灯＝映像クリエイター）新設**（2026-06-17 著者要望）：プロット作成時に映像化を想定し、戦闘・移動の描写を「画・カメラ・光・空間の地理・運動の重さ」で繊細化する（本文に乗らなくても執筆時に意識／storyboard・seedance への橋渡し）。[SKILL](../../.claude/skills/screen-review/SKILL.md)＋[ペルソナ](../../.claude/skills/screen-review/personas/kuon_akari.md)。CLAUDE.md レビュー行に登録（**プロット時は5レビューで回す**）。**初適用＝第6話**（[ep6_plot_screen](../review/ep6_plot_screen.md)）→本文の守りの連携の空間の地理＋核へ降りる移動の重さを **v0.3** で繊細化。
12. ✅ **第7話プロット v0.1→5レビュー→v0.2**（2026-06-17）：[ep7_plot.md](../plot/ep7_plot.md)「管轄外」＝道化の気配を二人で追う共有の宿題（B1は気配のみ）／澪の「登録＝安全」観のひび／点vs面の攻めの共闘。**screen-review（久遠）初の本格運用**＝[synthesis](../review/ep7_plot_synthesis.md)。必須4（達成の確定＝挙動の法則へ付け替え＋次の一片を持ち帰る／澪の縦糸の身体化／戦闘の"面"を三速度で身体化／登録外＝体制が扱えない因果）＋推奨3を反映。引き＝火の粉が本牧へ（気配のみ）。全員マージ可水準。
13. ✅ **第7話 本文 v0.2＝完成**（2026-06-17）：[07_kankatsugai.md](../manuscript/book1/07_kankatsugai.md)「管轄外」（約5,657字・NG0/WARN0）。舞台＝**根岸森林公園＋旧競馬場の廃馬見所**（固有現象＝終わらないレースの歓声＝群衆の記憶・喪失の鏡＝[C-037](../series/canon_log.md)）。v0.1執筆→**4レビュー（[synthesis](../review/07_synthesis.md)＝[九条](../review/07_kawahara.md)条件付き可/[夏目](../review/07_tsukikage.md)条件付き可/[読者3](../review/07_readers.md)8-8-9/[霧島](../review/07_actor.md)条件付き可）→必須3＋推奨2を反映**（A 引きの圧縮＝火の粉の溜め三段→一撃／B FABの素振りの解説削減＝一拍の遅れと光で語らせる・7巻種は気配のみ／C 澪の手が下がる橋渡し＝射る一点も埋める空欄もどちらも無い／D 弓＝棒の重複一本化／E ナギの静止に反動）。全員マージ可水準・開示違反なし。**道化の楽団（C-028）B1初の再来＝気配のみ**。
14. ✅ **第8話プロット v0.2＝完成**（2026-06-17）：[ep8_plot.md](../plot/ep8_plot.md)「露見」＝第2ブロックの山＝**澪の報告保留が体制に露見・鵜飼が澪に直接迫る**（通告と既視感＝鏡像／抹消申請は澪の証言が確定の鍵＝澪が勝利条件の鍵を布石）＋ナギの巻き込んだ罪悪感＋削れの天秤が傾く山場（速さで澪を連れ去る＝鵜飼と同じ罪＝呑まず核へ）。go darkはまだ手が届かない（第9話）。引き＝鵜飼の「期限（あと三日）」＝第9話への時計。**5レビュー（[synthesis](../review/ep8_plot_synthesis.md)＝[九条](../review/ep8_plot_kawahara.md)条件付き可/[夏目](../review/ep8_plot_tsukikage.md)可/[読者3](../review/ep8_plot_readers.md)7-8-7/[霧島](../review/ep8_plot_actor.md)条件付き可/[久遠](../review/ep8_plot_screen.md)可）→必須7反映**（刃を双務に／削れ却下を澪軸で／露見トリガー一本化＋抹消対象接続／既視感を沈黙化・マッチカット／罪悪感を身体トリガー／澪「答えません」を残心の能動所作／引きに目盛り＋画で締める）。全員マージ可水準。
15. ✅ **第8話 本文 v0.2＝完成**（2026-06-17）：[08_roken.md](../manuscript/book1/08_roken.md)「露見」（約5,502字・NG0/WARN0）。**著者決定＝引き＝ナギ視点＋澪を画で／タイトル＝「露見」**。v0.1執筆→**4レビュー（[synthesis](../review/08_synthesis.md)＝[九条](../review/08_kawahara.md)条件付き可/[夏目](../review/08_tsukikage.md)条件付き可/[読者3](../review/08_readers.md)8-8-9/[霧島](../review/08_actor.md)条件付き可）→必須3＋推奨1を反映**（A 引きの決意独白を研ぎ最終カットを澪の手に／B 既視感の澪側を症状に揃える＝鵜飼の過去の推量を削る／C 中盤の内面二段を圧縮／推奨＝鵜飼退場後に澪の素の半句で緩の谷）。全員マージ可水準・開示違反なし・プロット必須収束①〜⑦全達成。**第2ブロックの山（露見）＝本文化完了**。
16. ✅ **第9話プロット v0.2＝完成**（2026-06-17）：[ep9_plot.md](../plot/ep9_plot.md)「核へ」＝go dark本番＝**隠れ家の幻の駅の核（master の心臓＝終わらない終着駅＝喪失の鏡）へ潜りシードを読む**（第8話の「あと三日」を回収）。削れに頼るか自力か＝**自力（削れは喪失を食う＝核＝喪失とは自滅）**・あざが熱で拒む身体接地／澪が一緒に潜る＝踏み越えの予兆（"見逃すと決めたなら見届ける"＝規律の進化）／核＝喪失の鏡（待っていた目・気配のみ）。**本話はシード一歩手前で引く**（go dark成立＝第3ブロック）。**5レビュー（[synthesis](../review/ep9_plot_synthesis.md)＝[九条](../review/ep9_plot_kawahara.md)条件付き可/[夏目](../review/ep9_plot_tsukikage.md)可/[読者3](../review/ep9_plot_readers.md)7-8-7/[霧島](../review/ep9_plot_actor.md)条件付き可/[久遠](../review/ep9_plot_screen.md)可）→必須6反映**（削れ却下の身体接地／シード一歩手前を質的前進で／澪の踏み越えを規律の進化で／go dark＝根治の対比／あと三日を降下中も／喪失の鏡の言語化を1ビートに絞り身体符合で）。全員マージ可水準。
17. ✅ **第9話 本文 v0.2＝完成**（2026-06-17）：[09_kaku_e.md](../manuscript/book1/09_kaku_e.md)「核へ」（検査値約5,461字・NG0/WARN0）。**著者決定＝引き＝ナギ視点＋"待っていた目"の一像＋時計一拍の二段引き／タイトル＝「核へ」**。v0.1執筆→**4レビュー（[synthesis](../review/09_synthesis.md)＝[九条](../review/09_kawahara.md)条件付き可/[夏目](../review/09_tsukikage.md)可/[読者3](../review/09_readers.md)8-8-9/[霧島](../review/09_actor.md)条件付き可）→必須3反映**（A 章末二段引きの後段を研ぐ＝数字の繰り上がりを無音で／B 喪失の鏡の同化の起点を半歩の所作で／C 降下中盤の反復圧縮＋抽象独白の二重を一重に）。全員マージ可水準・開示違反なし・プロット必須収束7項目全達成。**go dark本番＝核の心臓に手は届いたが、読むには払うものがある＝シード一歩手前で引く（成立は第3ブロック）**。**字数注記＝検査値はヘッダ（設計メモ）を含むため物語本文は約1,100字少（ep6等と同条件）**。
18. ✅ **第10話プロット v0.2＝完成**（2026-06-17）：[ep10_plot.md](../plot/ep10_plot.md)「足跡の手前」＝第2ブロック最終話＝クライマックス前夜＝**go darkを一歩手前で挫く（喪失だけは渡さない芯＝種も読めない）＋鵜飼の決定的接触（戻り標に手＝包囲が点から面へ）＋澪の踏み越えの直前（様式を閉じる＝抹消申請の裏取りが崩れる＝不可逆の第一手）＋ナギの転回＝逃げない（追われる側から向き合う側へ）**。削れの天秤は未決のまま第3ブロックへ。**5レビュー（[synthesis](../review/ep10_plot_synthesis.md)＝[九条](../review/ep10_plot_kawahara.md)条件付き可/[夏目](../review/ep10_plot_tsukikage.md)可/[読者3](../review/ep10_plot_readers.md)8-8-8/[霧島](../review/ep10_plot_actor.md)条件付き可/[久遠](../review/ep10_plot_screen.md)条件付き可・平均8.0）→必須7反映**（"逃げない"を不可逆の行動で＝溜飲の生命線／go dark挫きを順序逆転＋深化／天秤を能動へ／澪の閉じる直前にナギを見る／転回を二拍に割る／鵜飼の接触＝凍りつき＋秩序の面／機構接続）。引きの視点＝ナギ視点で確定。**第2ブロック（B1-05〜10）の設計＝全話プロット完成・本文は5〜9話まで v0.2 完成**。
19. ✅ **第10話 本文 v0.2＝完成**（2026-06-17）：[10_ashiato_no_temae.md](../manuscript/book1/10_ashiato_no_temae.md)「足跡の手前」（検査値約5,513字・NG0/WARN0）。**引き＝ナギ視点・背中→正面の振り返り一像／タイトル＝「足跡の手前」**（working title 採用）。v0.1執筆→**4レビュー（[synthesis](../review/10_synthesis.md)＝[九条](../review/10_kawahara.md)条件付き可/[夏目](../review/10_tsukikage.md)条件付き可/[読者3](../review/10_readers.md)8-8-9/[霧島](../review/10_actor.md)条件付き可）→必須4反映**（A ナギの転回の引き金の二重を解消＝詰みを追認に回し澪の踏み出し一本に／B ビート7〜引きの「逃げ」反復を圧縮＋決着の予告／C 鵜飼が標に手をかけた直後の説明を圧縮／D 前半の低温にFABの短い誘い＋澪の一言で温度の谷）。全員マージ可水準・開示違反なし・プロット必須収束7項目全達成・**最重要検証＝溜飲が下がる三者クリア**。**第2ブロック（B1-05〜10）＝本文 v0.2 全話完成・設計完結**。
20. **【次の一手】第3ブロック（B1-11〜16＝出し抜く決着）の構想・第11話プロット**。第10話の申し送り＝**初手で「澪が閉じた様式が、鵜飼の手続きをどう軋ませるか」の線を動かす**（点vs面＋囮＋go dark/シードの組み合わせで出し抜く決着＝[antagonist §3](../settings/antagonist_ukai_core.md)）。**プロットは5レビューで回す**。要・著者構想（第3ブロックの話数配分・go dark成立の置き場・喪失の"払うもの"の顕在化）。
21. 任意：巻1の縦糸（削れの天秤／監視／澪の仲間化／喪失／道化の気配）の出し入れを第2〜巻末ブロックで配分（[book1_skeleton.md §2](../plot/book1_skeleton.md)）。
22. 任意：ストーリーボード（隠れ家establishing は確定済アセットあり／点vs面の共闘絵は第4話／鵜＝白い光の意匠／第7話＝点vs面の攻めの三速度／第8話＝既視感のマッチカット／第9話＝核へ降りる漆黒・待っていた目／第10話＝戻り標に手がかかる・整然と同期した白い目の面・ナギの背中→正面の振り返り）。
23. 任意：**字数計測の是正検討**＝check_manuscript.py が本文字数にヘッダ（`>`設計メモ）を含む件。物語本文のみを測るなら `>` 行も除外する改修を検討（過去回との整合に注意）。

> 進捗：**第2ブロック（B1-05〜10）＝本文 v0.2 全話完成・設計完結**（鵜飼人物設計＋戻り標/シード機構C-036＋ep5-10プロット＋第5〜10話本文）。**本セッションで第7話本文化＋第8話プロット＋第8話本文化＋第9話プロット＋第9話本文化＋第10話プロット＋第10話本文化まで完了**（8ユニット・全レビュー収束反映・著者決定反映・main マージ済）。第2ブロックは「追われる→go dark本番（核へ）→挫く＋鵜飼の決定的接触＋澪の不可逆の第一手＋ナギの転回＝逃げない（追われる側から向き合う側へ）」で完結。次は第3ブロック（B1-11〜16＝出し抜く決着）の構想＝初手で「澪が閉じた様式が鵜飼の手続きを軋ませる線」を動かす。

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
