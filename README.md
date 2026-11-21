[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/ccxiaoba555/makefun-news-image-21/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/ccxiaoba555/makefun-news-image-21/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# news-image-20261121 — Saturday, 21 November 2026

Built for [make.fun](https://make.fun/bounty/news-image-20261121)'s "Sum up 21 November's world news in one image" bounty ($100 in USDC).

One image summing up the world news of Saturday 21 November 2026, drawn as a dense newspaper front page (1024×1024 PNG). The date is named at the top; 38 stories, each verified against that day's reporting, plus two evening developments in the ticker:

1. **Russia fires 400+ drones and 110 missiles at Ukraine — two land in Poland** — at least eight die in Kyiv; Poland calls it a deliberate provocation. (France 24 · CBS News · El País)
2. **S&P 500 falls 3.7% as AI rout wipes out the year's gains** — Nvidia plunges ~14% on an SEC accounting probe; Anthropic falls 11% a day after its record IPO. (BBC · The Guardian)
3. **World court rules Myanmar committed genocide against the Rohingya** — the ICJ's first-ever genocide ruling against a state. (PBS NewsHour · Sky News)
4. Iran says it downed a US MQ-9 drone; tankers hit near Hormuz. (Japan Times)
5. Trump defends ties with Putin and Xi after the Shenzhen peace summit. (BBC)
6. Pancreatic cancer pill makes tumours undetectable in trial. (The Guardian)
7. Saudi-led coalition intercepts three Houthi missiles over Riyadh. (Al Jazeera)
8. COP31 runs past deadline; protests as fossil fuels are cut from the draft. (Reuters)
9. GTA VI books a record $3.79bn on day one, 32.5m copies pre-sold. (Reuters)
10. Anthropic's record $81bn IPO briefly tops $2tn in value. (Evertiq)
11. Claude said to help prove the Riemann hypothesis — unverified. (The Hindu)
12. Magnitude 6.7 quake shakes central Peru; no deaths reported. (TRT World)
13. Two tankers hit by unknown projectiles leaving the Strait of Hormuz. (UKMTO)
14. FBI crime database reportedly hacked for the second time. (CNN)
15. Nvidia crashes ~14%; Trump wants ousted CEO Huang back. (Argus)
16. Denmark expels a Russian diplomat over an 'assassination plot'. (Al Jazeera)
17. Estonia to shut five road crossings with Russia from Dec 1. (Euronews)
18. UK and EU sign the biggest post-Brexit deal on food and carbon. (BBC)
19. Gen Z protests erupt in 25 countries over costs and arms. (BBC)
20. Indian man gets 19 years over a plot to kill a Sikh leader in the US. (The Hindu)
21. Israeli strikes kill six in Gaza; settler attacks top 400. (Al Jazeera)
22. US loses measles-free status after 7,700 cases and 13 deaths. (The Guardian)
23. Kane tears an ankle ligament; out for about three months. (AI Eye)
24. Ronaldo scores his 986th career goal in an Al Nassr defeat. (AllSports)
25. Trump orders contractors to alert the White House before Congress. (ANews)
26. China holds loan rates for an 18th month; Hang Seng falls 1.9%. (Argus)
27. Singapore PM Wong meets Li Qiang; 20+ deals due at the JCBC. (ChinaTechNews)
28. BepiColombo enters Mercury orbit after 8 years and 10bn km. (The Guardian)
29. Storm in Brazil kills 3 and wrecks about 5,000 homes. (Izvestia)
30. Judge approves Bayer's $7.25bn Roundup settlement. (Le Monde)

Ticker: Spain votes Nov 29 · Bolsonaro in hospital · Iraq retakes Jurf al-Sakhar · Nigeria boat capsizes (~30 dead) · 'Chapo Isidro' captured · Seoul moves to impeach the top judge · CERN sees ultra-rare decay · Voyager 1 now 24 light-hours away · Trump puts Iran strikes on hold · Trump tells Europe to defund Ukraine.

## Entry

`entry.png` (1024×1024, ~184 KB) is rendered by `render21.py` (Python 3 + Pillow, deterministic — no timestamps, no randomness) and copied to the grader's output by `main.ts` (Node 22, standard library only, no network), so repeated runs write identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# writes out/entry.png (byte-identical to entry.png in this repo)
```

To re-render the image from scratch:

```sh
python3 render21.py entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · Referral: https://make.fun/r/gxmh0hrp</sub>
