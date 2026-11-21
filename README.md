# news-image-20261121 — The World Today

One image that sums up Saturday, 21 November 2026: a hand-drawn newspaper
front page, 1024 x 1024, built with PIL from the day's reported news.

## How it is made

- `render21.py` draws the page with PIL (DejaVu Serif / DejaVu Sans) and
  writes `entry.png`. Every block measures its wrapped text before drawing,
  so no two lines overlap.
- `main.ts` (Node 22, standard library only) copies `entry.png` to
  `/output/entry.png`, so the two grader runs write identical bytes.

Run it: `python3 render21.py`, then
`mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts`.

## Stories on the page (40)

### Top story

1. Russia's largest air assault on Ukraine yet — missiles land in Poland
   (France 24 / CBS News / El País)

### Secondary stories

2. AI sell-off drags Wall Street into correction (BBC / UPI / The Guardian)
3. World court finds Myanmar guilty of genocide (PBS NewsHour / Sky News)

### The day in brief (27)

4. US–Iran war: Hormuz attacks go on; Iran says it downed a US drone
   (The Japan Times / Middle East Eye)
5. After Shenzhen summit, Trump defends ties with Putin and Xi
   (BBC / Le Monde)
6. Pancreatic cancer drug hailed as biggest advance in decades
   (The Guardian / BBC)
7. Saudi-led coalition intercepts Houthi missiles aimed at Riyadh
   (Al Jazeera)
8. COP31 talks run past deadline in fossil-fuel deadlock
   (Channel News Asia / Reuters)
9. GTA VI books record $3.79bn on its first day (Reuters / CNN)
10. Anthropic IPO, the largest ever, tops $2tn in value (Evertiq)
11. Claude said to help prove the Riemann hypothesis (The Hindu)
12. Magnitude 6.7 earthquake strikes central Peru (TRT World)
13. Two tankers hit by unknown projectiles off Hormuz
    (UKMTO / Outlook India)
14. FBI crime database reportedly hacked (CNN / The Straits Times)
15. Nvidia plunges 14%; Trump wants ousted CEO Huang back (Argus)
16. Denmark expels Russian diplomat over murder plot (Al Jazeera / BBC)
17. Estonia to shut five road crossings with Russia
    (Al Jazeera / Euronews)
18. UK and EU sign biggest post-Brexit deal (BBC / RFI)
19. Gen Z protests sweep 25 European countries (Al Jazeera / BBC)
20. Indian man jailed 19 years over US murder-for-hire plot
    (The Hindu / BBC)
21. Gaza strikes kill six as West Bank violence goes on
    (Middle East Eye / Al Jazeera)
22. US loses its measles-free status after 7,700 cases (The Guardian)
23. Kane tears ankle ligament, out for three months (AI Eye)
24. Ronaldo scores career goal No. 986 in Al Nassr defeat (AllSports)
25. Trump orders contractors to alert White House first (ANews)
26. China holds loan rates for 18th month; Hang Seng down 1.9% (Argus)
27. Singapore PM Wong meets Li Qiang in Beijing (ChinaTechNews)
28. BepiColombo enters orbit around Mercury (The Guardian / BBC)
29. Brazil storm kills three, wrecks 5,000 homes (Izvestia)
30. Judge approves Bayer's $7.25bn Roundup settlement (Le Monde / ANSA)

### Latest ticker (10)

31. Spain votes on 29 November; conservatives lead
32. Bolsonaro in hospital with bowel blockage
33. Iraq retakes Jurf al-Sakhar after 12 years
34. Nigeria boat capsizes: ~30 dead, 300 missing
35. FBI-wanted 'Chapo Isidro' captured in Mexico
36. Seoul moves to impeach top court chief
37. CERN sees first evidence of ultra-rare decay
38. Voyager 1 now 24 light-hours from Earth
39. COP31 extended with no deal; Addis Ababa to host COP32
40. Trump postpones Iran strike; 41 killed in Yemen raid

## License

MIT — see LICENSE.
