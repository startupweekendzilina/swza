# AGENTS.md — Startup Weekend Žilina #13

## Current contact lookup and source preservation — 2026-10-29

Resolve recipients by the unique `E-mail` header in current `Org.Team`, not a fixed column letter. Missing/duplicate headers or an unknown person require clarification; never guess. Active caller verification remains KLO-874.

Personal contact rows are not versioned. The complete pre-publication notes are preserved locally at `/home/node/.hermes/private-context-archive/prepublish-2026-10-29-e9d610ba3e7d/AGENTS-original.md`; current roster data takes precedence. The material below concerns edition #13 / 2026, not automatic 2027 commitments.

## Pravidlá perzistencie
- Všetky dôležité learningy a pravidlá zapisuj aj sem (súbor = source of truth) + memory
- ~~Pozor na nekonzistenciu: oficiálne FAQ hovorí vek 12-14, plagát SWZA Kids má 10-14 — riešiť so Zuzkou~~ → VYRIEŠENÉ 23.6.2026

## 🔴 FINÁLNY TERMÍN SWZA #13 — 9.–11. október 2026 (potvrdené Zuzkou 13.7.2026)
- **Dátum podujatia: piatok 9. október – nedeľa 11. október 2026** (3 dni / 54 hodín)
- **Zmena z pôvodného 23.–25. októbra 2026** (dôvod: kolízia s komunálnymi voľbami — rozhodnutie z meetingu 6.7.2026)
- **Toto je jediný finálny dátum** — používaj VŠADE: v TASKS, copy, social media posts, emailey, dokumenty, media kit, plagáty, web, newslettre
- **Starý dátum 23.–25.10.2026 je NEPLATNÝ** — všetky referencie treba aktualizovať (úloha SWZA-053: Grafika/Web, Kubko, deadline 20.7.)
- Starý dátum sa mohol objaviť v starších commitoch/postoch — pre nové úlohy vždy píš **9.–11. október 2026**
- Týka sa aj: registračného linku (https://tootoot.fm/en/events/6a084221cf42dac50e2d94ca — link ostal rovnaký, len dátum v texte sa mení)

## 🔴 KRITICKÉ PRAVIDLO PRE MASTER SHEET (19.8.2026 — fail recovery!)
**Naučenie z incidentu 19.8.2026 — vymazala som dáta z Partneri hárku pri zápise Marcelkiných partnerov!**

- **NIKDY neprepisujem existujúce riadky** v MASTER SWZA 2026 sheetu (ID: `14wTR5XREjKxSXi6B4R81x669ITJ9fPYDl9vrNwM435s`)
- **Vždy INSERT (nové riadky) na koniec tabuľky**, nie UPDATE existujúcich
- **Ak potrebujem nahradiť existujúci riadok** → MUSÍM sa najprv opýtať Zuzky
- **Pred akýmkoľvek zápisom do tohto sheetu:**
  1. Stiahni aktuálny stav daného hárku cez `gws sheets values get`
  2. Over čo tam je
  3. Ak sa obsah môže prepísať → opýtaj sa Zuzky či môžeš prepísať
  4. Ak nie si istá → append na koniec (riadok číslo = existujúce riadky + 1)
- **Marcelkini partneri** sa vždy pridávajú **na koniec Partneri hárku**, nie na začiatok (za Tini partnerov)
- **Pri update hárkov (TASKS, Org.Team, Mentors)**: vždy použi `values update` s presným range `Hárok!A{row}:J{row}` pre jednotlivý riadok

---

## 📧 Pravidlo pre emaily ownerov (potvrdené Zuzkou 13.7.2026)
- **Vždy posielať emaily IBA na adresu osoby v poli E-mail (Org.Team), nájdenom podľa hlavičky** — nikdy nevymýšľať nové emaily
- Ak úloha patrí osobe, ktorá **nie je v Org.Team** → opýtať sa Zuzku, nehádať
- Ak sa v zápisnici/poznámke spomína iný email (napr. osobný vs pracovný) — prednosť má **Org.Team pole E-mail podľa hlavičky**
- Výnimka: ak Zuzka výslovne povie "pošli na X" — vtedy ten email, ale stále len 1 email/osobu/beh (pravidlo 1 email/osoba z 25.6.2026)

## SWZA Kids — kľúčové dáta (jún 2026, finálne)
- **Vek 2026: 12–14 rokov** — hlavne tento rozsah (podľa grantu). Minulé roky bol rozsah širší 10–14.
- Plagát má stále 10–14 — treba zaktualizovať! (aktualizujem v ďalšom kroku)
- **Mentori: 2 kid mentori na 1 detský tím** = 6 kid mentorov dokopy na celý víkend (3 tímy × 2)
- Zatiaľ nemáme žiadnych kid mentorov — treba aktívne hľadať
- Kapacita: 3 tímy × 5 detí = 15 detí
- Program: sobota + nedeľa, 9:00–17:00 (skrátený režim)
- Metodika: Lean Canvas, prototyp, finále, prieskum trhu, prezentácia
- **Kids koordinátorka (key person): Dominika Bieliková** — [contact in Org.Team], [phone in Org.Team]
- Sprievod: 10 € (strava, káva)

## SWZA Kids — stav projektov (jún 2026)
- FAQ po víkende: DONE ✅ (doplnená motivácia + Inovia, link v Drive)
- Media Kit: DONE ✅ (veku 12-14 sedí, doplnený odsek o 6 kid mentorech)
- Plagát: PDF s textom "10-14" — stále need update na "12-14" (rok 2026 podľa grantu)

## Najbližšie akcie
- Aktualizovať plagát SWZA Kids — vek 10-14 → 12-14 (PDF)
- Pokračovať v nájdení kid mentorov (cieľ: 6 na celý víkend)

## Meeting 18.8.2026 — zapísané do TASKS (R80-R99, 20 nových úloh)
- **Marcelka Barčáková** (nová členka) — `[contact in Org.Team]` (Zuzka potvrdila 18.8. cez Discord, nebola v Org.Team)
- **Tinka** (`[contact in Org.Team]`) — 10 úloh (mentori, partnerstvá, catering, marketing)
- **Karol** (`[contact in Org.Team]`) — 1 nová + update existujúcej (SWZA-064)
- **Zuzka** (`[contact in Org.Team]`) — 5 úloh (web, promo kódy, socials)
- **Tinka+Zuzka spoločne** — 1 úloha (Pronaila barter)
- Kľúčové deadline-y: 25.8. (web + social post), 30.8. (Kros faktúra, promo kódy), 31.8. (mentori), 1.9. (WhatsApp mentorov)
- Pravidlo: pri parsingu zápisníc cez Discord — **pýtať sa na email novej osoby** (Marcelka prípad). Neprevziať z textu zápisu, len z Org.Team.
- Update existujúcich: SWZA-003 deadline→31.8., SWZA-063 breakdown 50/30/10%, SWZA-066 Kros follow-up, SWZA-077 video-pozvánky follow-up

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

## SWZA lístky — oficiálny URL (potvrdené Zuzkou 30.6.2026)
- **Priamy link na registráciu/lístky:** `https://tootoot.fm/en/events/6a084221cf42dac50e2d94ca`
- VŽDY vkladaj túto presnú URL všade kde treba link na lístky (sociálne siete, copy-paste texty, emaily, dokumenty, media kit)
- NIKDY nepíš len `tootoot.fm` alebo `linktr.ee/startupweekendzilina` ako náhradu za priamy link na lístky — linktr.ee je všeobecný rozcestník, nie priamy link
- Všeobecné info: linktr.ee/startupweekendzilina (web/rozcestník)

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

## 📊 TASKS — oficiálne pickre v stĺpcoch (overené z dataValidation 5.8.2026)
- **D - Oblasť (9 hodnôt)**: `venue`, `partnerships`, `mentors`, `marketing`, `automation`, `logistics`, `volunteers`, `operations`, `finance`
- **F - Status (6 hodnôt)**: `todo`, `in_progress`, `blocked`, `done`, `postponed`, `cancelled`
- **G - Priorita (3 hodnoty)**: `high`, `medium`, `low` — ⚠️ `Critical` NIE JE v pickroch! Ak treba "najvyššiu" prioritu, dať `high`.
- **Majú byť lowercase** — case sa v pickroch neakceptuje. 5.8.2026 opravené 11 riadkov (`High`→`high`, `Medium`→`medium`, `Critical`→`high`) cez `batchUpdate` `TASKS!G2:G61`. Overené validáciou.
- **NEOPRAVENÉ (5.8.2026)**: 16 hodnôt Oblasť mimo pickrov (`Partneri`, `Partneri / UNIZA`, `marketing/PR`, `Catering`, `Grafika / Web`, atď.). Vyžaduje Danielovo rozhodnutie — niektoré sú evidentne rozdelenie partnerships (`Partneri / UNIZA`, `Partneri / Komunikácia`), iné sú samostatné (`Catering`, `Grafika / Web`). Rozšíriť pickre v dataValidation, nie prepisovať hodnoty.

## SSE Partnerstvo — SWZA-072 (pridané 5.8.2026 na žiadosť Daniela)
- **TASKS!A62:J62**: ID `SWZA-072`, Oblasť `partnerships`, Owner `[contact in Org.Team]`, Status `in_progress`, Priorita `medium`, Deadline `2026-09-15`
- Kontakt na SSE: **Michaela Kríva** — email zatiaľ **NEZISTENÝ** (nie je v Org.Team; treba opýtať sa). Podľa pravidla "Emaily ownerov" — nikdy nevymýšľať.
- Partneri sheet **R18 (SSE)** — stav `Negotiate` (5.8.2026 update z `Contact` po poslaní pripomienok), Zodpovedný `Daniel`, Kontaktná osoba: Michaela Kríva.

## Mesto Žilina partnerstvo — SWZA-061 (existujúce, aktualizované 5.8.2026)
- **TASKS R51** (SWZA-061): "Napísať mestu Žilina (STA, rozpočet, podpora)" — Owner: `[contact in Org.Team]`, Status: `in_progress`, Priorita: `high`, Deadline: `2026-07-26` (už prešiel)
- Poznámka: "Stretnutie 20.7.2026 — Daniel sa dohodol so STA. Mesto neodpoveda, prislubena odpoved, poslana pripomienka." + ďalšia pripomienka 5.8.2026
- Partneri sheet **R21 (Mesto Žilina)** — stav `Negotiate` (5.8.2026 update z `Contact` po poslaní pripomienok), Zodpovedný `Daniel`. Kontakt: Silvia (z Org.Team R31).
- SWZA-036 (iná Mesto Žilina uloha): "Dohodnúť mesto Žilina + radničné noviny" — Owner: `[contact in Org.Team]`, Status: `done` (cez Silviu).

## Partneri sheet — sales pipeline (5.8.2026)
- Statusy v Partneri stĺpci G: `Lead`, `Contact`, `Negotiate`, `Legal`, `Win`, `Lost`
- Logika prechodu: Lead → Contact (prvý kontakt) → Negotiate (posielajú sa pripomienky / aktívna komunikácia) → Legal (zmluva sa pripravuje) → Win/Lost
- Poznámka pri prechode z `Contact` na `Negotiate`: vždy keď Daniel manuálne pošle pripomienky partnerovi.

## 📭 Reminder pravidlá — kto dostane ping (potvrdené Zuzkou 14.7.2026)
- **PING** (posiela sa reminder po 4 dňoch): `in_progress`, `todo`
- **PRESKOČ** (žiadny email): `blocked`, `postponed`, `done`, `cancelled`, prázdny (`''`)
- Logika v `swza_task_notify.py`: `REMINDABLE_STATUSES = {"in_progress", "todo"}`. Ak status nie je v tejto množine → `continue`.
- Prázdny status = plánovaná úloha, NIE todo → nikdy nepinguje (pravidlo)
- `blocked` NEpíše sa preto, lebo na blocked úlohe sa bežne nič nezmení (čaká sa na externý dependency) a ping len otravuje
- Pri "priraď na mňa" / nová úloha dávam default `in_progress` (ak nie je blokovaná), aby owner dostal svoj prvý reminder ak zabudne
- Dôvod (14.7.2026): SWZA-048, 050, 051, 052 mali prázdny status a zbytočne by posielali ping; `blocked` úlohy (napr. LinkedIn Community API čakajúci na schválenie) nikdy neprogredujú samé od seba — ping je zbytočný

## SWZA Newsletter/Emailing pre bývalých účastníkov — July 1, 2026
- **Emailing mailchimp: 🚀 SWZA #13 Early Bird – Bývalí účastníci** (ID `1xsFy2CDnAnBlPtettp6N-Kdmu_fdA5AFa8t5ebZFiEQ`)
- Pôvodne vytvorený v `Komunikačný materiál SWZA / EMAILING (1b-HlsNi4qFMeVmDoAJbqtKeXO6Rjq1WU)`, **1.7.2026 Zuzka presunula do `02_Newsletter_bývalí_účastníci (1TRg7J1s99yLlTlQylk7ZbcOxWaYSsrYb)`** (správne cieľové miesto pre newslettery)
- Vizuálne spracované cez `docs.batchUpdate` (insertText + updateParagraphStyle + updateTextStyle) — dvojfázový postup podľa pravidla vyššie
- Štruktúra: Subject (sivý italic 10pt) → H1 hero (22pt modrý bold) → H3 dátum/miesto → 3× H2 sekcie (16pt modrý bold) → CTA button (H1 22pt oranžový bold) → URL link (13pt modrý bold) → bullet listy → urgentný text (12pt červený bold) → záver italic → linktree (10pt link) → podpis (12pt bold)
- 4 image placeholdery: [OBRÁZOK 1-4] — Zuzka vloží skutočné fotky/plagát v Google Docs UI manuálne (Zuzkin pokyn „nepotrebujes obrazky, daj tam dummies")
- `deleteContentRange` gotcha: endIndex NEMÔŽE zahŕňať newline na konci segmentu (vracia 400 error). Riešenie: endIndex = segment_end - 1

## SWZA Social Posts (partner copy-paste) — June 30, 2026
- Google Docs vytvorené pre Zuzku ako univerzálny promo text (Instagram/Facebook/LinkedIn), krátky aj dlhý variant
- **SWZA hlavný** (FINÁLNY): ID `1s71qAX-7sIOILDq4scbDa9flW8jLcDkN-eYSFl3sqOY`, name `SWZA_post_na_socialne_siete_partnerom`, v `00_Media Kit (všeobecný) (1e7m-ElxKd5Z9OJ0gyrQpyf6_leXXlt1m)`. Vytvorený cez `docs.documents.batchUpdate` s `insertText` (nie markdown upload — ten spôsobuje tofu emoji v prehliadačoch bez emoji fontu). Obsahuje: H1 titul, H2 KRÁTKA + DLHŠIA VERZIA, CTA vety (⚡), správny link `https://tootoot.fm/en/events/6a084221cf42dac50e2d94ca`. **Zmazané staré verzie**: 1KVY... (pôvodný môj), 1RsI... (predchádzajúci commit chybný), 1roPV... (Zuzkin prázdny).
- **SWZA Kids**: ID `1a3JH_sNvIrxAxGGj1GNiUc7g3lh0jQErlTcwkrPthLw`, v `02_Media Kit (SWZA KIDS) (1z7Fme-WEhVVZPpWOHwKjYEOASXpq3W0S)`, name `Social_post_swza_kids_partnerom` (starý formát, pred tofu-fixom)
- Hook text (Zuzkin favorit z TC): „Máš nápad, ktorý by mohol zmeniť svet? Alebo ťa zaujíma, ako vzniká úspešný startup? ... vyskúšať podnikanie na vlastnej koži, bez rizika a s podporou skúsených mentorov"
- Vynechané: kredit partnerov (formálnosť pre copy-paste), stará CTA veta „Už navždy sa budeš inak dívať na svet"
- Vek detí zjednotený na 12-14 (podľa grantu)
- Emoji set (len Unicode ≤2010): 🚀 📋 📅 📍 🎫 🌐 👉 ⚡ ✅ • — žiadne 🟢 (2019) ani 🎟 (2014) pre kompatibilitu so starými Chrome/Windows
- Linktree ako "Viac info" rozcestník (nie link na lístky) — linktr.ee/startupweekendzilina

## Drive upload cez gws (zistenie 30.6.2026)
- text/markdown mime type → Drive auto-importne ako Google Doc (`application/vnd.google-apps.document`)
- Súbor MUSÍ byť v cwd (nie /tmp) — inak validácia zlyhá "outside the current directory"
- Príklad: `cp subor.md ./ && gws drive files create --json '{...}' --upload ./subor.md --upload-content-type text/markdown`
- **batchUpdate API gotcha**: `updateParagraphStyle` rozšíri štýl na VŠETKY paragraphs ktoré sa prekrývajú s range. Po `insertText` potom treba **resetovať paragraphy ktoré omylom dostali HEADING/NORMAL_TEXT zlý štýl** cez ďalší `updateParagraphStyle` s `NORMAL_TEXT`. Štýl sa aplikuje na celý paragraph element (od \n po \n), nie len na text v range.
- **Dvojfázový prístup pre vytváranie dokumentov s nadpismi**: 1) `insertText` celý text, 2) `updateParagraphStyle` len na správne ranges, 3) tretí krok `updateParagraphStyle` s NORMAL_TEXT pre paragraphs ktoré boli zle ovplyvnené.

## Drive upload cez gws (zistenie 30.6.2026)
- text/markdown mime type → Drive auto-importne ako Google Doc (`application/vnd.google-apps.document`)
- Súbor MUSÍ byť v cwd (nie /tmp) — inak validácia zlyhá "outside the current directory"
- Príklad: `cp subor.md ./ && gws drive files create --json '{...}' --upload ./subor.md --upload-content-type text/markdown`
- Markdown upload VLOŽÍ emoji ako Unicode glyphs, ale **Google Docs ich NIEKEDY zobrazí ako tofu (štvorčeky)** — viditeľné najmä v prehliadačoch bez emoji fontu (Chrome na niektorých Linux/Win verziách)
- **Fix pre tofu emoji v existujúcom Google Doc**: cez `docs.documents.batchUpdate` prepísať odstavce s emoji cez `deleteContentRange` + `insertText` (rovnaký text). V batche ísť OD KONCA, aby nižšie indexy zostali platné. TabId je v `tabs[0].tabProperties.tabId` (napr. „t.0")
- Po editácii vždy overiť, že headings + bold ostali zachované (`get` → skontrolovať `paragraphStyle.namedStyleType`)
