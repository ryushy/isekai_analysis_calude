from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


BASE = Path("outputs/mio_minatomirai_station_battle_sheet_base.png")
OUT = Path("outputs/mio_minatomirai_station_battle_sheet_v1.png")


def main() -> None:
    img = Image.open(BASE).convert("RGBA")
    scale = 2
    img = img.resize((img.width * scale, img.height * scale), Image.Resampling.LANCZOS)
    width, height = img.size
    draw = ImageDraw.Draw(img)

    font_paths = [
        Path("C:/Windows/Fonts/meiryo.ttc"),
        Path("C:/Windows/Fonts/YuGothM.ttc"),
        Path("C:/Windows/Fonts/msgothic.ttc"),
    ]

    def pick_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
        candidates = []
        if bold:
            candidates.append(Path("C:/Windows/Fonts/meiryob.ttc"))
        candidates.extend(font_paths)
        for path in candidates:
            if path.exists():
                return ImageFont.truetype(str(path), size)
        return ImageFont.load_default()

    f_title = pick_font(42, True)
    f_head = pick_font(28, True)
    f_body = pick_font(23)
    f_small = pick_font(20)
    f_tiny = pick_font(18)

    bg = (16, 20, 24, 230)
    bg_light = (8, 13, 18, 188)
    line = (203, 164, 96, 230)
    text = (238, 232, 218, 255)
    sub = (193, 208, 214, 255)
    red = (220, 96, 82, 255)
    gold = (238, 190, 104, 255)

    def box(xy, fill=bg, outline=line, radius=10) -> None:
        draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=2)

    def fit_lines(value: str, font_obj, max_width: int) -> list[str]:
        lines: list[str] = []
        for para in value.split("\n"):
            if not para:
                lines.append("")
                continue
            cur = ""
            for ch in para:
                test = cur + ch
                if draw.textlength(test, font=font_obj) <= max_width or not cur:
                    cur = test
                else:
                    lines.append(cur)
                    cur = ch
            if cur:
                lines.append(cur)
        return lines

    def write(x: int, y: int, value: str, font_obj, max_width: int, fill=text, line_gap: int = 7) -> int:
        for line_value in fit_lines(value, font_obj, max_width):
            draw.text((x, y), line_value, font=font_obj, fill=fill)
            bbox = draw.textbbox((x, y), line_value or " ", font=font_obj)
            y += (bbox[3] - bbox[1]) + line_gap
        return y

    def label_box(x1: int, y1: int, x2: int, y2: int, title: str, body: str, accent=gold, body_font=None) -> None:
        box((x1, y1, x2, y2))
        draw.text((x1 + 22, y1 + 16), title, font=f_head, fill=accent)
        write(x1 + 22, y1 + 58, body, body_font or f_body, x2 - x1 - 44, fill=text, line_gap=8)

    box((26, 26, 850, 110), fill=(7, 11, 16, 228))
    draw.text((48, 42), "澪 バトルシーン・デザインシート", font=f_title, fill=text)
    draw.text((48, 88), "横浜みなとみらい線風・地下鉄駅構内 / 単一点を作って撃つ", font=f_small, fill=sub)

    box((880, 26, 1178, 110), fill=(7, 11, 16, 228))
    draw.text((902, 44), "使用衣装", font=f_head, fill=gold)
    draw.text((902, 78), "light crimson functional v1", font=f_small, fill=text)

    box((1208, 26, width - 32, 110), fill=(7, 11, 16, 228))
    draw.text((1230, 44), "シーン核", font=f_head, fill=gold)
    draw.text((1350, 47), "駅に溶けた敵は最初、撃つべき一点を持たない。澪は退いて観察し、弱点の光を一点化して射抜く。", font=f_small, fill=text)

    box((52, 148, 620, 270), fill=bg_light)
    draw.text((74, 166), "キャラ設計", font=f_head, fill=gold)
    write(74, 204, "澪：現時点の支援射手。射程200〜300m。近距離と“点のない混沌”に弱い。", f_small, 520, fill=text, line_gap=6)

    box((690, 290, 1120, 430), fill=bg_light)
    draw.text((712, 308), "敵デザイン", font=f_head, fill=red)
    write(712, 346, "黒い雨水、改札影、通勤者の輪郭、ガラス片が混ざる駅構内アノマリー。声はなく、駅ノイズで圧を出す。", f_small, 386, fill=text, line_gap=6)

    box((672, 1460, 1232, 1550), fill=bg_light)
    draw.text((694, 1478), "台詞", font=f_head, fill=gold)
    write(790, 1482, "澪「逃げない。まず一点を作る」\n澪「……そこ。戻り標、見えた」", f_small, 410, fill=text, line_gap=4)

    label_box(
        30,
        1608,
        1268,
        1788,
        "設定 / アクション制約",
        "場所：横浜みなとみらい線風の地下駅。濡れた床、改札、柱、ホームドア、赤い非常灯。\n"
        "澪：軽量赤衣装。片肩・腕巻き・ブーツで走る、伏せる、柱に隠れる動作を優先。\n"
        "戦術：敵に単一点がないため即射できない。退いて距離を作り、反射・改札光・水滴の揺れから弱点を探す。",
        accent=gold,
        body_font=f_small,
    )

    label_box(
        1320,
        1608,
        2050,
        1788,
        "ショットリスト 1-9",
        "1 駅構内に黒い雨水が滲む / 2 澪が柱裏で気配を読む / 3 敵が複数輪郭へ分裂 / "
        "4 近距離を嫌って退く / 5 ホームドア枠で姿勢固定 / 6 弱点の小さな光が出る / "
        "7 矢は一本だけ番える / 8 短い局所発光で命中 / 9 残心、敵は水へ崩れる",
        accent=gold,
        body_font=f_tiny,
    )

    label_box(
        2060,
        1608,
        2572,
        1788,
        "カメラ / 動き",
        "カメラは低く滑る。床反射を前景に、柱の裏から澪へ寄り、敵の圧で一度後退。中盤は手持ち風の揺れ。射撃時だけ静止し、矢の後は敵ではなく澪の呼吸へ戻す。",
        accent=gold,
        body_font=f_tiny,
    )

    label_box(
        2600,
        1608,
        width - 32,
        1788,
        "照明 / 音 / 動画要素",
        "照明：冷白色の駅灯、青緑の反射、赤い非常灯、矢は淡金で局所のみ。\n"
        "音：水滴、改札エラー音、電車の低い風圧、弓弦の短い鳴り。\n"
        "禁止：連続レーザー、巨大ビーム、実在ロゴ、読める駅名。",
        accent=gold,
        body_font=f_tiny,
    )

    beats = [
        (1218, 126, "01 発生"),
        (1932, 126, "02 発見"),
        (2590, 126, "03 点がない"),
        (1218, 610, "04 退く"),
        (1870, 610, "05 固定"),
        (2468, 610, "06 弱点"),
        (1218, 1095, "07 一本"),
        (1932, 1095, "08 命中"),
        (2584, 1095, "09 残心"),
    ]
    for x, y, value in beats:
        draw.rounded_rectangle((x, y, x + 156, y + 38), radius=8, fill=(5, 8, 12, 185), outline=(203, 164, 96, 170), width=1)
        draw.text((x + 12, y + 7), value, font=f_tiny, fill=text)

    box((2630, 1416, width - 76, 1512), fill=(8, 13, 18, 190))
    draw.text((2652, 1436), "カメラ軌道：低速ドリー → 後退 → 柱越し寄り → 射撃で静止", font=f_tiny, fill=text)
    draw.line((2670, 1484, width - 130, 1484), fill=gold, width=4)
    draw.polygon([(width - 130, 1484), (width - 158, 1470), (width - 158, 1498)], fill=gold)

    img.convert("RGB").save(OUT, quality=95)
    print(OUT.resolve())
    print(f"{width}x{height}")


if __name__ == "__main__":
    main()
