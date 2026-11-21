#!/usr/bin/env python3
"""Render the 21 November 2026 news image: a dense 1024x1024 newspaper
front page. Masthead + hero + two second stories + 27 dense items with
sources + an 'ALSO' ticker carrying the last 10 items.

38 stories researched from that day's reporting (see news-20261121.md),
plus two evening developments folded into the ticker. Every headline is
verified against its source; nothing is invented.

Layout is flow-based: each block's height follows its content, so no text
ever overlaps the line below it.

Usage: render21.py <out.png>
Deterministic: no timestamps, no randomness, fixed fonts.
"""
import sys
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (246, 241, 231)
NAVY = (15, 42, 74)
RED = (178, 34, 34)
INK = (24, 24, 24)
GREY = (90, 86, 78)
CARD = (255, 255, 255)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_fitted(draw, xy, text, fnt_path, size, width, fill,
                leading=1.15, max_lines=None, shrink_to=12, label=""):
    """Draw wrapped text, shrinking the font until it fits max_lines.
    Returns the y just below the last line."""
    x, y = xy
    sz = size
    while True:
        fnt = font(fnt_path, sz)
        lines = wrap(draw, text, fnt, width)
        if max_lines is None or len(lines) <= max_lines or sz <= shrink_to:
            break
        sz -= 1
    if sz < size:
        print(f"  [fit] {label}: shrank {size}->{sz} ({len(lines)} lines)")
    for line in lines[:max_lines] if max_lines else lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += int(sz * leading)
    return y


def tag_chip(draw, x, y, label, size=17):
    f = font(SANS_B, size)
    w = int(draw.textlength(label, font=f)) + 20
    h = size + 11
    draw.rounded_rectangle([x, y, x + w, y + h], radius=5, fill=RED)
    draw.text((x + 10, y + 4), label, font=f, fill=(255, 255, 255))
    return w, h


HERO = ("WAR IN UKRAINE · MISSILES LAND IN POLAND",
        "Russia fires 400+ drones and 110 missiles at Ukraine — two land in Poland",
        "At least eight die in Kyiv as bridges and rail stations are hit. "
        "Poland calls it a deliberate provocation.",
        "France 24 · CBS News · El País")

SECOND = [
    ("MARKETS · AI SELL-OFF",
     "S&P 500 falls 3.7% as AI rout wipes out the year's gains",
     "Nvidia plunges ~14% on an SEC accounting probe; Anthropic falls 11% "
     "a day after its record IPO.",
     "BBC · The Guardian"),
    ("JUSTICE · THE HAGUE",
     "World court rules Myanmar committed genocide against the Rohingya",
     "The ICJ's first-ever genocide ruling against a state orders returns "
     "and reparations; Myanmar calls it unfair.",
     "PBS NewsHour · Sky News"),
]

# 27 dense items (research items 4-30): (headline, source)
DENSE = [
    ("Iran says it downed a US MQ-9 drone; tankers hit near Hormuz", "Japan Times"),
    ("Trump defends ties with Putin and Xi after peace summit", "BBC"),
    ("Pancreatic cancer pill makes tumours undetectable in trial", "The Guardian"),
    ("Saudi-led coalition intercepts three Houthi missiles over Riyadh", "Al Jazeera"),
    ("COP31 runs past deadline; protests as fossil fuels cut from draft", "Reuters"),
    ("GTA VI books record $3.79bn on day one, 32.5m copies pre-sold", "Reuters"),
    ("Anthropic's record $81bn IPO briefly tops $2tn in value", "Evertiq"),
    ("Claude said to help prove the Riemann hypothesis — unverified", "The Hindu"),
    ("Magnitude 6.7 quake shakes central Peru; no deaths reported", "TRT World"),
    ("Two tankers hit by unknown projectiles leaving the Strait", "UKMTO"),
    ("FBI crime database reportedly hacked for the second time", "CNN"),
    ("Nvidia crashes ~14%; Trump wants ousted CEO Huang back", "Argus"),
    ("Denmark expels Russian diplomat over 'assassination plot'", "Al Jazeera"),
    ("Estonia to shut five road crossings with Russia from Dec 1", "Euronews"),
    ("UK and EU sign biggest post-Brexit deal on food and carbon", "BBC"),
    ("Gen Z protests erupt in 25 countries over costs and arms", "BBC"),
    ("Indian man gets 19 years over plot to kill Sikh leader in US", "The Hindu"),
    ("Israeli strikes kill six in Gaza; settler attacks top 400", "Al Jazeera"),
    ("US loses measles-free status after 7,700 cases, 13 deaths", "The Guardian"),
    ("Kane tears ankle ligament; out for about three months", "AI Eye"),
    ("Ronaldo scores his 986th career goal in Al Nassr defeat", "AllSports"),
    ("Trump orders contractors to alert White House before Congress", "ANews"),
    ("China holds loan rates for 18th month; Hang Seng falls 1.9%", "Argus"),
    ("Singapore PM Wong meets Li Qiang; 20+ deals due at JCBC", "ChinaTechNews"),
    ("BepiColombo enters Mercury orbit after 8 years, 10bn km", "The Guardian"),
    ("Storm in Brazil kills 3 and wrecks about 5,000 homes", "Izvestia"),
    ("Judge approves Bayer's $7.25bn Roundup settlement", "Le Monde"),
]

TICKER = ("ALSO: Spain votes Nov 29 as conservatives lead · Bolsonaro in "
          "hospital · Iraq retakes Jurf al-Sakhar · Nigeria boat capsizes: "
          "~30 dead · 'Chapo Isidro' captured · Seoul moves to impeach top "
          "judge · CERN sees ultra-rare decay · Voyager 1: 24 light-hours "
          "away · Trump puts Iran strikes on hold · Trump tells Europe to "
          "defund Ukraine")


def render(out_path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 36

    # ---- Masthead: 0-132 ----
    d.rectangle([0, 0, W, 126], fill=NAVY)
    d.text((mx, 12), "WORLD NEWS  —  IN ONE IMAGE", font=font(SANS_B, 20),
           fill=(255, 214, 90))
    d.text((mx, 38), "SATURDAY, 21 NOVEMBER 2026", font=font(SERIF_B, 44),
           fill=(255, 255, 255))
    d.text((mx, 94), "The day's news in one image  ·  38 stories, as reported",
           font=font(SANS, 19), fill=(190, 205, 222))
    d.rectangle([0, 126, W, 132], fill=RED)

    # ---- Hero card: 142-338 (flow-laid, card sized to content) ----
    y = 142
    tag, head, summ, src = HERO
    # measure content height first
    tmp = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    hh = len(wrap(tmp, head, font(SERIF_B, 31), W - 2 * mx - 52))
    sh = len(wrap(tmp, summ, font(SANS, 18), W - 2 * mx - 52))
    card_h = 12 + 28 + 6 + hh * int(31 * 1.12) + 5 + sh * int(18 * 1.25) \
        + 6 + 17 + 8
    d.rounded_rectangle([mx, y, W - mx, y + card_h], radius=10, fill=CARD)
    d.rectangle([mx, y + 12, mx + 8, y + card_h - 12], fill=RED)
    tag_chip(d, mx + 26, y + 12, tag, size=17)
    yy = y + 12 + 28 + 6
    yy = draw_fitted(d, (mx + 26, yy), head, SERIF_B, 31,
                     W - 2 * mx - 52, INK, leading=1.12, max_lines=2,
                     label="hero headline")
    yy = draw_fitted(d, (mx + 26, yy + 5), summ, SANS, 18,
                     W - 2 * mx - 52, GREY, leading=1.25, max_lines=2,
                     label="hero summary")
    d.text((mx + 26, yy + 6), "Sources: " + src, font=font(SANS, 15),
           fill=GREY)
    y = y + card_h + 8

    # ---- Second row: two cards, flow-laid ----
    card_w = (W - 2 * mx - 20) // 2
    tops = []
    for i, (tag, head, summ, src) in enumerate(SECOND):
        x0 = mx + i * (card_w + 20)
        hh = len(wrap(tmp, head, font(SERIF_B, 23), card_w - 40))
        sh = len(wrap(tmp, summ, font(SANS, 15), card_w - 40))
        ch = 10 + 24 + 4 + hh * int(23 * 1.12) + 4 + sh * int(15 * 1.25) \
            + 5 + 15 + 8
        tops.append(ch)
    card_h = max(tops)
    for i, (tag, head, summ, src) in enumerate(SECOND):
        x0 = mx + i * (card_w + 20)
        d.rounded_rectangle([x0, y, x0 + card_w, y + card_h], radius=10,
                            fill=CARD)
        tag_chip(d, x0 + 20, y + 10, tag, size=13)
        yy = y + 10 + 24 + 4
        yy = draw_fitted(d, (x0 + 20, yy), head, SERIF_B, 23,
                         card_w - 40, INK, leading=1.12, max_lines=2,
                         label=f"second-{i} headline")
        yy = draw_fitted(d, (x0 + 20, yy + 4), summ, SANS, 15,
                         card_w - 40, GREY, leading=1.25, max_lines=2,
                         label=f"second-{i} summary")
        d.text((x0 + 20, yy + 5), "Sources: " + src,
               font=font(SANS, 13), fill=GREY)
    y = y + card_h + 8

    # ---- Dense grid: 3 columns x 9 rows, from y to 954 ----
    y0, y1 = y, 954
    cols, rows = 3, 9
    col_w = (W - 2 * mx - 2 * 20) // cols
    row_h = (y1 - y0) // rows
    print(f"  dense grid: y {y0}-{y1}, row_h {row_h}")
    for idx, (head, src) in enumerate(DENSE):
        r, c = divmod(idx, cols)
        x0 = mx + c * (col_w + 20)
        yy = y0 + r * row_h
        d.rectangle([x0, yy + 4, x0 + 4, yy + row_h - 8], fill=RED)
        tx = x0 + 14
        tw = col_w - 14
        y2 = draw_fitted(d, (tx, yy + 2), head, SANS_B, 15, tw, INK,
                         leading=1.12, max_lines=2, shrink_to=13,
                         label=f"dense-{idx}")
        d.text((tx, y2 + 1), "— " + src, font=font(SANS, 11), fill=GREY)

    # ---- Ticker footer: 962-1024 ----
    d.rectangle([0, 962, W, H], fill=NAVY)
    lines = wrap(d, TICKER, font(SANS_B, 15), W - 2 * mx)
    print(f"  ticker lines: {len(lines)}")
    ty = 968
    for tl in lines[:3]:
        d.text((mx, ty), tl, font=font(SANS_B, 15), fill=(255, 214, 90))
        ty += 19

    img.save(out_path, "PNG", optimize=True)
    print(out_path, img.size)


if __name__ == "__main__":
    render(sys.argv[1])
