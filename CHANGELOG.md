# CHANGELOG.md

## [0.7.4] — 2026-06-25

### Fixed
- `scripts/swza_task_notify.py` — **zoskupené remindre po osobe** (commit `076c64a`):
  - Pravidlo Zuzky 25.6.2026: ak má vlastník 2+ stale úloh, pošle sa **JEDEN email so všetkými úlohami v odrážkach**, nie 2+ samostatné emaily.
  - Pred: pre každú úlohu sa odosielal samostatný email. Vlastník s 3 úlohami dostal 3 emaily naraz.
  - Po: 2-fázová logika: (1) `reminder_events[email] = list of (row_idx, task)`, (2) jeden `send_email()` / email so všetkými úlohami.
  - Subject dynamický: `1× úloha čaká` vs `3× úloha čaká`.
  - J stĺpec sa updatne len pre úlohy, ktoré sa reálne odoslali (ochrana pred polovičným J update).
  - **Toto pravidlo sa nesmie meniť — je to anti-spam zábrana** (zapísané v AGENTS.md).

### Diagnostika
- 24.6.2026 cron `80b6ff061606` skončil s `last_status: error` (príčina neidentifikovaná — potrebný log).
- 25.6.2026 ráno script spustený manuálne — 12 remindrov odoslaných, J stĺpce updatnuté na 2026-06-25.
- Nasledujúci cron (25.6. 22:00) by mal zbehnúť úspešne s novou logikou, alebo o 4 dni (29.6.) kedy sa J stĺpce stanú stale.

## [0.7.3] — 2026-06-23

### Fixed
- `scripts/swza_task_notify.py` — `SHEET_NAME` opravené z `TASKS_v2` na `TASKS` (commit `e6b9a53`)
  - 22.6.2026 bol hárok `TASKS_v2` premenovaný na `TASKS`, ale script stále používal staré meno.
  - Dôsledok: cron `80b6ff061606` zlyhával od 22.6.2026 s `Unable to parse range: TASKS_v2!A1:J1000`. Žiadne remindre sa neposielali 20.6, 21.6, 22.6, 23.6.
  - Opravené manuálne v súbore + commitnuté.
- `workflows/swza-task-notify-v1.json` — všetky výskyty `TASKS_v2` → `TASKS` (5 zmien: 2× `sheetName`, 2× node name, 1× v `jsCode` komentároch, 1× v connections)
  - Rovnaký problém: n8n workflow mal v kóde staré meno. Ak by sa deployoval, mal by rovnaký error.

### Added
- Nová úloha **SWZA-043** v TASKS (riadok 37): *"Draft oslovovacieho mailu pre školy + zoznam škôl (formálny výstup grantu) + metodika oslovovania znevýhodnených ľudí"*
  - Owner: `z.bojkova@gmail.com` (Zuzka), Oblasť: `participants`, Status: `todo`, Priorita: `medium`
  - Deadline: prázdny (Zuzka: "budem to robiť niekedy neskôr")
  - ID pridelené: posledné existujúce v TASKS bolo SWZA-042 → 043
  - Súvisí so SWZA-038 (znevýhodnené skupiny do 30 rokov) a SWZA-011 (newsletter pre školy)

### Documentation
- `AGENTS.md` — sekcia "SWZA tasks (TASKS sheet)" rozšírená o finálne stavy potvrdené Zuzkou 23.6.2026:
  - Master sheet = `MASTER SWZA 2026`
  - Hárok úloh = `TASKS` (gid `2099318786`)
  - NIKDY viac `TASKS_v2`! Žiadne ďalšie premenovávanie.

## [0.7.2] — 2026-06-22

### Changed
- `swza_task_notify.py` — **email templaty upravené** pre assignment / status / reminder notifikácie (Zuzka, 22.6.2026):
  - Odstránená duplicita: link na TASKS sheet sa teraz nachádza **len raz** na konci každého emailu (pred podpisom), nie dvakrát.
  - Link zvýraznený emodži 👉 a vyzývajúcim textom pred ním ("Prosím, aktualizuj status priamo v Sheete tu:" / "Pozri si zmeny a prípadne ďalej reaguj v Sheete:" / "Prosím aktualizuj status alebo daj vedieť, ak potrebuješ pomoc.").
  - Link ostáva rovnaký (`gid=2099318786`) — používatelia sa vedia z emailu prekliknúť priamo do TASKS sheetu a updatnúť stav úlohy.

## [0.7.1] — 2026-06-18

### Fixed
- `AGENTS.md` — opravený workflow pre TASKS_v2 (Poučenie #3): `gws sheets +append` je nebezpečný, lebo neapenduje na koniec TASKS_v2 ale na prvé voľné miesto v tabuľkovej štruktúre v inom sheet-e (incident: SWZA-027 skončil v `Základne INFO!A8`).
- Workflow aktualizovaný: použi `gws sheets spreadsheets values update` s explicitným range `TASKS_v2!A{riadok}:H{riadok}` a vždy over výsledok cez `+read`.

### Added
- Nová úloha **SWZA-027** v TASKS_v2 (riadok 31): *"Prepojiť credentials v n8n na Instagram a Facebook pre Ivetku"*
  - Owner: `iveta.sinalova78@gmail.com`
  - Oblasť: `social`, Status: `todo`, Priorita: `medium`
  - Deadline: prázdny (Zuzka ho nepovedala)
  - ID pridelené: posledné existujúce v TASKS_v2 bolo SWZA-026 → 027
  - Špecifikácia: Prepojiť Instagram a Facebook účty SWZŽ na Ivetkin osobný prístup, vytvoriť/editovať credentials v n8n UI, odovzdať Ivetke prístupové inštrukcie

## [0.7.0] — 2026-06-18

### Documentation
- `AGENTS.md` — pridané pravidlo **"Toto je hotovo, archivuj thread"** (Daniel)
  - Význam: projektová archivácia (zápis do STAV.md + AGENTS.md update), NIE mazanie Discord správ
  - Workflow v tom istom turn-e: overiť scope → STAV.md sekcia + tabuľka → AGENTS.md update ak treba → CHANGELOG → report
  - Anti-pattern: nepýtať sa, nehovoriť len "ok", nepreskakovať overenie scope
- `docs/STAV.md` — pridaná sekcia 18.6.2026 (LinkedIn + Facebook page data export hotovo, thread 1509288026524881129 archivovaný)
  - FB: manuálne stiahnuté cez Page Insights
  - LinkedIn: Page admin Analytics export (cesta A)
  - Apify scraper (cesta B2): neimplementované, zdokumentované v session 20260606_124648_c1f3f457 pre prípadnú potrebu v budúcnosti
- `memory` — aktualizovaný záznam o pravidle pre "archivuj thread"

## [0.6.0] — 2026-06-14

### Documentation
- `AGENTS.md` — pridané **Poučenie #2** (Druhé porušenie pravidla "priraď na mňa" v tej istej session-i)
  - Workflow (definitívny): grep → gws +read Org.Team → zisti posledné ID → gws +append
  - Anti-pattern: "Nemám email" / "Aký je názov?" / "Priradil som" bez akcie
  - Pravidlo: prečítať AGENTS.md v každom turn-e, nie len pamätať
- `memory` — aktualizovaný záznam o TASKS_v2 s workflow krokmi

## [0.5.0] — 2026-05-18

### Added
- `docs/TROUBLESHOOTING.md` — rozšírený o 3 nové záznamy (n8n MCP tool errors, Google Sheets columns, Google OAuth 403)

### Documentation
- Pridané prevention pravidlá pre opakovanie chýb
- n8n MCP tool JSON parsing issue dokumentovaný
- Code node stĺpce (A/C vs skutočné názvy) vysvetlené

## [0.2.0] — 2026-05-18

### Added
- `AGENTS.md` — sekcie "Dokumentačné pravidlá" a "CHANGELOG" s explicitnými pravidlami

### Documentation Rules
- Každé pravidlo musí byť explicitne zdokumentované
- Nikdy sa nespoliehať na domyslanie alebo ústnu dohodu
- Nové pravidlo = pridať do AGENTS.md alebo príslušného .md súboru

### CHANGELOG Rules
- Zaznamenáva sa každá zmysluplná zmena
- Verzovanie: [MAJOR.MINOR.PATCH]
- Commit po dokončení funkcie, zmeny konfigurácie, bugfixe

## [0.1.1] — 2026-05-18

### Updated
- `AGENTS.md` — pridaná sekcia Security s pravidlami pre .env a secrets

## [0.1.0] — 2026-05-18

### Added
- `AGENTS.md` — root entry point s Core Principle: Context Preservation
- `docs/STAV.md` — šablóna pre aktuálny stav projektu
- `docs/ROLES.md` — všetky roly, vlastníci, oblasti a úlohy ([J], [P], [E])
- `docs/PHASES.md` — 5 fáz organizácie od prípravy po post-event
- `docs/TOOLS.md` — nástroje, platformy a automatizovateľné tasky
- `docs/MEMORY.md` — context preservation pravidlá + Self-Contained Rule
- `docs/PARA/` — PARA folder štruktúra pre para-memory-files
- `opencode.json` — MCP server config pre n8n (`https://api.n8n-mcp.com`)
- `.env.example` — placeholder pre N8N_MCP_API_KEY
- `.gitignore` — ignoruje `docs/PARA/`, `.env`, `*.md.bak`, `.DS_Store`
- `CHANGELOG.md` — história zmien projektu

### Security
- `.env` s reálnym API key nikdy nepristupovať cez tools
- Všetky secrets idú len cez environment variables