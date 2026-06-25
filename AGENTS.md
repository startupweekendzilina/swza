# AGENTS.md — Startup Weekend Žilina #13

## Pravidlá perzistencie
- Všetky dôležité learningy a pravidlá zapisuj aj sem (súbor = source of truth) + memory
- ~~Pozor na nekonzistenciu: oficiálne FAQ hovorí vek 12-14, plagát SWZA Kids má 10-14 — riešiť so Zuzkou~~ → VYRIEŠENÉ 23.6.2026

## SWZA Kids — kľúčové dáta (jún 2026, finálne)
- **Vek 2026: 12–14 rokov** — hlavne tento rozsah (podľa grantu). Minulé roky bol rozsah širší 10–14.
- Plagát má stále 10–14 — treba zaktualizovať! (aktualizujem v ďalšom kroku)
- **Mentori: 2 kid mentori na 1 detský tím** = 6 kid mentorov dokopy na celý víkend (3 tímy × 2)
- Zatiaľ nemáme žiadnych kid mentorov — treba aktívne hľadať
- Kapacita: 3 tímy × 5 detí = 15 detí
- Program: sobota + nedeľa, 9:00–17:00 (skrátený režim)
- Metodika: Lean Canvas, prototyp, finále, prieskum trhu, prezentácia
- **Kids koordinátorka (key person): Dominika Bieliková** — bielikova.dominika@gmail.com, 0904 987 322
- Sprievod: 10 € (strava, káva)

## SWZA Kids — stav projektov (jún 2026)
- FAQ po víkende: DONE ✅ (doplnená motivácia + Inovia, link v Drive)
- Media Kit: DONE ✅ (veku 12-14 sedí, doplnený odsek o 6 kid mentorech)
- Plagát: PDF s textom "10-14" — stále need update na "12-14" (rok 2026 podľa grantu)

## Najbližšie akcie
- Aktualizovať plagát SWZA Kids — vek 10-14 → 12-14 (PDF)
- Pokračovať v nájdení kid mentorov (cieľ: 6 na celý víkend)

## Nábor mentorov (SWZA Kids)
- Hľadáme 6 kids mentorov (2 na tím × 3 tímy)
- Priorita: majú radi deti, nevadí im s nimi pracovať, vedia udržať focus, motivujú deti
- Skúsenosti s prácou s deťmi sú plus, ale nie podmienka
- Vedia smerovať deti bez toho, aby za nich riešili veci

## Ciele Media Kitu SWZA Kids
- Partneri: financie na prototypovanie, materiál, mentori, mediálny priestor
- Mentori: ľudia čo majú radi deti, ochota pracovať s nimi, motivujú deti, udržiavajú focus
- Školy: nábory šikovných detí (partnerstvá so školami, emaily na učiteľov)
- Médiá: šírenie povedomia

## Komunikačné priečinky (Google Drive)
- Komunikacia (FAQ): 1vyjCdy03T1XHdCd16kdD4b15h8TPD4JH
  - FAQ podpriečinok: 1vTiZDyNvhoGBMS9Sz4tG6rGIPQW1Cj-T
    - FAQ pre novinárov: 1oELnqq0aLwgxDQizN267iidP8u8vtysUxcovLWKV38U
    - FAQ pre účastníkov SWZA #13: 1w6G2UnV7AzouhlRMqs4KuO8DjdHqhcjIJSRslp5jxOo
- 02_Media Kit (SWZA KIDS): 1z7Fme-WEhVVZPpWOHwKjYEOASXpq3W0S
  - Plagát SWZA Kids: 1I0DULNii_O1Qj3i8m_inQNmFG1OrICcf
- Komunikačný materiál SWZA: 1UQhyU40cexenwWv65NK73YZ9INUGYrf4
- 00_Media Kit (všeobecný): 1e7m-ElxKd5Z9OJ0gyrQpyf6_leXXlt1m

## SWZA tasks (TASKS sheet) — FINÁLNE STAVY (potvrdené Zuzkou 23.6.2026)
- **Master sheet**: `MASTER SWZA 2026` (oficiálny názov, ID: `14wTR5XREjKxSXi6B4R81x669ITJ9fPYDl9vrNwM435s`)
- **Tabuľka úloh**: hárok `TASKS` (gid `2099318786`) — NIKDY viac `TASKS_v2`! Premenovanie z `TASKS_v2` → `TASKS` 22.6.2026 je FINÁLNE
- Žiadne ďalšie premenovávanie. Toto je teraz tak. Toto sa zmenilo, takto to je.
- **Emaily vlastníkov**: v Org.Team
- **NIKDY `+append`!** Vždy `values update` s explicitným range `TASKS!A{riadok}:J{riadok}` + `USER_ENTERED`
- **Cron reminder** (job `80b6ff061606`): beží 22:00 daily cez `scripts/swza_task_notify.py` — používa `SHEET_NAME = "TASKS"` (správne, commit `e6b9a53` opravil). Posiela email ak je úloha stale > 4 dní. Zapisuje dátum do J stĺpca.
- **DVOJITÁ KOPIA (25.6.2026 fix)** — script existuje na 2 miestach a MUSIA byť v sync:
  - `/home/node/swza/scripts/swza_task_notify.py` (git repo, source of truth)
  - `/home/node/.hermes/scripts/swza_task_notify.py` (kam chodí cron `80b6ff061606`)
  - **Pri každej zmene** v `swza/scripts/` musíš manuálne `cp` aj do `~/.hermes/scripts/` — git sa tam nepoužíva. 25.6.2026 o 22:00 cron padol práve preto, lebo som opravil len `swza/scripts/` a zabudol na sync. **Pravidlo: po commite vždy `diff` oboch súborov. Ak sa líšia, okamžite kopíruj.**
  - V `~/.hermes/scripts/` je `assert SHEET_NAME == "TASKS"` — ak sa niekedy vráti `TASKS_v2`, script okamžite spadne (fail-loud) namiesto tichého posielania 0 remindrov.
- **n8n workflow** (`workflows/swza-task-notify-v1.json`): opravený 23.6.2026 — všetky `TASKS_v2` → `TASKS` (predtým error `Unable to parse range: TASKS_v2!A1:J1000`)
- "Priraď na mňa" = OKAMŽITÝ zápis
- Default deadline PR/marketing: 2026-09-15 (mesiac pred eventom 23-25.10.2026)
- gws CLI: `+read`/`+append` NEEXISTUJÚ → raw Discovery API, output do `/tmp/x.json`
- "Toto je hotovo, archivuj thread" = projektová archivácia