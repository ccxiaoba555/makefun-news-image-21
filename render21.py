#!/usr/bin/env python3
"""Draw the 21 November 2026 front page: one 1024x1024 PNG.

Layout is computed by a small flow engine: every block measures its wrapped
text first, then draws, then advances the cursor, so no two lines can
overlap. Headline, deck and grid copy is written fresh for this day.
"""
import hashlib
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
MARGIN = 36
COLW = W - 2 * MARGIN  # 952

PAPER = (247, 243, 234)
INK = (24, 24, 24)
RED = (172, 32, 32)
NAVY = (16, 36, 64)
GREY = (112, 108, 100)
RULE = (186, 180, 168)
LIGHT = (238, 233, 222)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def load(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_MAST = load("DejaVuSerif-Bold.ttf", 44)
F_DATE = load("DejaVuSans-Bold.ttf", 15)
F_KICK = load("DejaVuSans-Bold.ttf", 14)
F_HERO = load("DejaVuSerif-Bold.ttf", 30)
F_DECK = load("DejaVuSans.ttf", 16)
F_SRC = load("DejaVuSans.ttf", 12)
F_SUBKICK = load("DejaVuSans-Bold.ttf", 13)
F_SUBHEAD = load("DejaVuSerif-Bold.ttf", 20)
F_SUBBODY = load("DejaVuSans.ttf", 13)
F_SECT = load("DejaVuSans-Bold.ttf", 13)
F_CELL = load("DejaVuSans-Bold.ttf", 12)
F_CELLSRC = load("DejaVuSans.ttf", 10)
F_TICK = load("DejaVuSans.ttf", 13)
F_TAG = load("DejaVuSans-Bold.ttf", 13)


def wrap(draw, text, font, width):
    """Greedy word wrap; returns a list of lines that fit width."""
    words = text.split()
    lines = []
    cur = ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, x, y, lines, font, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


def centre(draw, y, text, font, fill):
    w = draw.textlength(text, font=font)
    draw.text(((W - w) / 2, y), text, font=font, fill=fill)
    return y + font.size + 4


def rule(draw, y, weight=1):
    draw.line([(MARGIN, y), (W - MARGIN, y)], fill=RULE, width=weight)
    return y + weight + 4


# ---------------------------------------------------------------- content

HERO = {
    "kicker": "TOP STORY  ·  WAR IN EUROPE",
    "head": "Russia's largest air assault on Ukraine yet - missiles land in Poland",
    "deck": ("More than 400 drones and 110 missiles strike Ukraine; at least eight "
             "are killed in Kyiv as bridges and rail stations are hit. Two Russian "
             "missiles and a suspected drone come down in Poland. Prime Minister "
             "Tusk calls it a deliberate provocation; NATO calls it a serious "
             "airspace violation and scrambles jets."),
    "src": "Sources: France 24  ·  CBS News  ·  El Pais",
}

SECONDARY = [
    {
        "kicker": "MARKETS",
        "head": "AI sell-off drags Wall Street into correction",
        "body": ("The S&P 500 falls 3.7% to 6,910.39 and the Dow enters correction; "
                 "the Nasdaq erases its 2026 gains. Nvidia plunges about 14% as "
                 "Reuters reports an SEC accounting inquiry, and Anthropic drops "
                 "11% a day after listing. Gold falls about 4% and bitcoin about 4%."),
        "src": "Sources: BBC  ·  UPI  ·  The Guardian",
    },
    {
        "kicker": "JUSTICE",
        "head": "World court finds Myanmar guilty of genocide",
        "body": ("The International Court of Justice rules Myanmar committed genocide "
                 "against the Rohingya - the first time the court has held a state "
                 "responsible. It orders the displaced to be allowed home and "
                 "compensation to be paid. Myanmar calls the ruling unfair."),
        "src": "Sources: PBS NewsHour  ·  Sky News",
    },
]

# 27 dense briefs: (headline, source). Headlines kept under ~80 chars so
# each fits two lines in a ~300 px column at 13 px bold.
DENSE = [
    ("US-Iran war: Hormuz attacks go on; Iran says it downed a US drone",
     "Japan Times  ·  Middle East Eye"),
    ("After Shenzhen summit, Trump defends ties with Putin and Xi",
     "BBC  ·  Le Monde"),
    ("Pancreatic cancer drug hailed as biggest advance in decades",
     "The Guardian  ·  BBC"),
    ("Saudi-led coalition intercepts Houthi missiles aimed at Riyadh",
     "Al Jazeera"),
    ("COP31 talks run past deadline in fossil-fuel deadlock",
     "Channel News Asia  ·  Reuters"),
    ("GTA VI books record $3.79bn on its first day",
     "Reuters  ·  CNN"),
    ("Anthropic IPO, the largest ever, tops $2tn in value",
     "Evertiq"),
    ("Claude said to help prove the Riemann hypothesis",
     "The Hindu"),
    ("Magnitude 6.7 earthquake strikes central Peru",
     "TRT World"),
    ("Two tankers hit by unknown projectiles off Hormuz",
     "UKMTO  ·  Outlook India"),
    ("FBI crime database reportedly hacked",
     "CNN  ·  The Straits Times"),
    ("Nvidia plunges 14%; Trump wants ousted CEO Huang back",
     "Argus"),
    ("Denmark expels Russian diplomat over murder plot",
     "Al Jazeera  ·  BBC"),
    ("Estonia to shut five road crossings with Russia",
     "Al Jazeera  ·  Euronews"),
    ("UK and EU sign biggest post-Brexit deal",
     "BBC  ·  RFI"),
    ("Gen Z protests sweep 25 European countries",
     "Al Jazeera  ·  BBC"),
    ("Indian man jailed 19 years over US murder-for-hire plot",
     "The Hindu  ·  BBC"),
    ("Gaza strikes kill six as West Bank violence goes on",
     "Middle East Eye  ·  Al Jazeera"),
    ("US loses its measles-free status after 7,700 cases",
     "The Guardian"),
    ("Kane tears ankle ligament, out for three months",
     "AI Eye"),
    ("Ronaldo scores career goal No. 986 in Al Nassr defeat",
     "AllSports"),
    ("Trump orders contractors to alert White House first",
     "ANews"),
    ("China holds loan rates for 18th month; Hang Seng down 1.9%",
     "Argus"),
    ("Singapore PM Wong meets Li Qiang in Beijing",
     "ChinaTechNews"),
    ("BepiColombo enters orbit around Mercury",
     "The Guardian  ·  BBC"),
    ("Brazil storm kills three, wrecks 5,000 homes",
     "Izvestia"),
    ("Judge approves Bayer's $7.25bn Roundup settlement",
     "Le Monde  ·  ANSA"),
]

TICKER = [
    "Spain votes on 29 November; conservatives lead",
    "Bolsonaro in hospital with bowel blockage",
    "Iraq retakes Jurf al-Sakhar after 12 years",
    "Nigeria boat capsizes: ~30 dead, 300 missing",
    "FBI-wanted 'Chapo Isidro' captured in Mexico",
    "Seoul moves to impeach top court chief",
    "CERN sees first evidence of ultra-rare decay",
    "Voyager 1 now 24 light-hours from Earth",
    "COP31 extended with no deal; Addis Ababa to host COP32",
    "Trump postpones Iran strike; 41 killed in Yemen raid",
]

BAND_H = 76


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    y = 20

    # ---- masthead ------------------------------------------------------
    y = centre(d, y, "THE WORLD TODAY", F_MAST, INK)
    y = centre(d, y + 2, "SATURDAY, 21 NOVEMBER 2026  ·  WORLD NEWS IN ONE PAGE",
               F_DATE, INK)
    y += 6
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=INK, width=3)
    y += 6
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=INK, width=1)
    y += 12

    # ---- hero ----------------------------------------------------------
    d.text((MARGIN, y), HERO["kicker"], font=F_KICK, fill=RED)
    y += 20
    head_lines = wrap(d, HERO["head"], F_HERO, COLW)
    assert len(head_lines) <= 2, head_lines
    y = draw_lines(d, MARGIN, y, head_lines, F_HERO, INK, 36)
    y += 4
    deck_lines = wrap(d, HERO["deck"], F_DECK, COLW)
    assert len(deck_lines) <= 4, deck_lines
    y = draw_lines(d, MARGIN, y, deck_lines, F_DECK, INK, 20)
    y += 4
    d.text((MARGIN, y), HERO["src"], font=F_SRC, fill=GREY)
    y += 18
    y = rule(d, y, 1)
    y += 6

    # ---- two secondary stories ----------------------------------------
    gap = 24
    col_w = (COLW - gap) // 2
    sub_tops = []
    for i, story in enumerate(SECONDARY):
        x = MARGIN + i * (col_w + gap)
        yy = y
        d.text((x, yy), story["kicker"], font=F_SUBKICK, fill=RED)
        yy += 19
        lines = wrap(d, story["head"], F_SUBHEAD, col_w)
        assert len(lines) <= 2, lines
        yy = draw_lines(d, x, yy, lines, F_SUBHEAD, INK, 24)
        yy += 3
        body = wrap(d, story["body"], F_SUBBODY, col_w)
        assert len(body) <= 5, body
        yy = draw_lines(d, x, yy, body, F_SUBBODY, INK, 18)
        yy += 3
        d.text((x, yy), story["src"], font=F_SRC, fill=GREY)
        yy += 16
        sub_tops.append(yy)
    # vertical divider between the two columns
    mid_x = MARGIN + col_w + gap // 2
    d.line([(mid_x, y), (mid_x, max(sub_tops))], fill=RULE, width=1)
    y = max(sub_tops)
    y = rule(d, y, 1)
    y += 6

    # ---- section header -------------------------------------------------
    d.text((MARGIN, y), "THE DAY IN BRIEF", font=F_SECT, fill=INK)
    right = "27 STORIES  ·  SOURCES NAMED"
    rw = d.textlength(right, font=F_SECT)
    d.text((W - MARGIN - rw, y), right, font=F_SECT, fill=GREY)
    y += 18
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=INK, width=1)
    y += 8

    # ---- dense 3x9 grid -------------------------------------------------
    cols = 3
    cell_gap = 18
    cell_w = (COLW - (cols - 1) * cell_gap) // cols
    grid_top = y
    for row in range(9):
        trio = DENSE[row * 3:(row + 1) * 3]
        wrapped = []
        row_h = 0
        for head, src in trio:
            lines = wrap(d, head, F_CELL, cell_w)
            assert len(lines) <= 2, (head, lines)
            h = len(lines) * 14 + 12 + 3
            wrapped.append((lines, src))
            row_h = max(row_h, h)
        for i, (lines, src) in enumerate(wrapped):
            x = MARGIN + i * (cell_w + cell_gap)
            yy = draw_lines(d, x, y, lines, F_CELL, INK, 14)
            d.text((x, yy), src, font=F_CELLSRC, fill=GREY)
        y += row_h + 4
        if row < 8:
            d.line([(MARGIN, y - 3), (W - MARGIN, y - 3)], fill=LIGHT, width=1)
    grid_bottom = y
    print("grid: top", grid_top, "bottom", grid_bottom)
    assert grid_bottom <= H - BAND_H - 8, grid_bottom

    # ---- ticker band ----------------------------------------------------
    band_y = H - BAND_H
    d.rectangle([(0, band_y), (W, H)], fill=NAVY)
    tag = "LATEST"
    tw = d.textlength(tag, font=F_TAG)
    tag_x, tag_y = 18, band_y + (BAND_H - 26) // 2
    d.rectangle([(tag_x, tag_y), (tag_x + tw + 16, tag_y + 26)], fill=RED)
    d.text((tag_x + 8, tag_y + 5), tag, font=F_TAG, fill=(255, 255, 255))
    tx = tag_x + tw + 16 + 14
    tlines = wrap(d, "  •  ".join(TICKER), F_TICK, W - MARGIN - tx)
    assert len(tlines) <= 4, tlines
    ty = band_y + (BAND_H - len(tlines) * 17) // 2
    draw_lines(d, tx, ty, tlines, F_TICK, (235, 235, 230), 17)

    img.save(OUT, format="PNG")
    size = os.path.getsize(OUT)
    digest = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
    print("saved", OUT, size, "bytes")
    print("sha256", digest)
    print("size ok (<1MiB):", size < 1048576)
    return size, digest


if __name__ == "__main__":
    build()
