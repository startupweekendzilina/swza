# STAV.md — Aktuálny stav projektu

> **Pre nového agenta:** Tento súbor je primárny zdroj pravdy. Každý agent ho má prečítať pred začatím práce.

## Čo sa deje teraz

**18.6.2026 (štvrtok) — LinkedIn + Facebook page data export (Daniel Harcek, thread 1509288026524881129) — ✅ HOTOVO, archivované**

Daniel požiadal o postup na export dát z LinkedIn Page (`linkedin.com/company/98605351`) a Facebook Page (`facebook.com/StartupWeekendZilina`). Thread uzavretý s konštatovaním "toto je hotovo".

**Výsledok:**
- ✅ **Facebook** — Daniel stiahol manuálne cez Page Insights export, funguje
- ✅ **LinkedIn** — Daniel vybral cestu Page admin Analytics export (postačujúce pre účely)
- ❌ **Apify scraper v n8n (cesta B2)** — **NEIMPLEMENTOVANÉ**. Rozdiskutované ako možnosť, ale Daniel potvrdil že cesta A (admin Analytics export) stačí. Ak v budúcnosti bude treba texty komentárov / engagement per post — pozri session `20260606_124648_c1f3f457` pre detailný návod.

**Poznámka k "archivuj thread":** Danielov "archivuj thread" = projektová archivácia (zápis do STAV.md + uzavretie v AGENTS.md), **nie mazanie Discord správ**. Discord thread ostáva tak ako je, jeho prípadné zmazanie/archiváciu na strane Discorda robí admin.

**14.6.2026 (nedeľa) — Hermes prístup k Google Drive a Notion (Dominik Kloska, ticket)**

Dominik Kloska si vzal na seba ticket na overenie Hermes prístupu do Google Drive, content plánu a kontextu — aby sme vedeli generovať návrhy na príspevky.

**Overený stav prístupu (14.6.2026, ~08:15):**

- ✅ **GWS CLI 0.22.5** nainštalované (`/usr/local/bin/gws`)
- ✅ **OAuth2 token platný** — user `startupweekend.zilina@gmail.com` (Zuzkin Gmail)
- ✅ **Refresh token** prítomný, **12 scopes** (Drive, Sheets, Gmail, Calendar, Docs, Tasks, ...)
- ✅ **Drive** — funguje (Drive API v3, 12 scopes)
- ✅ **Sheets** — funguje (master sheet `MASTER COPY SWZA 2026` má 22 záložiek)
- ✅ **Notion MCP** — funguje (databáza `🚀 SWZA Content Machine` prístupná, 3 záznamy v rôznych stavoch)
- ⚠️ **Content plán** — v klasickom zmysle (mesačný/týždenný kalendár) **NEEXISTUJE** ako samostatný dokument. Funkciu content plánu plní **Notion content machine** (každý page = plánovaný post s dátumom, surovou myšlienkou, AI draftom, finálnym textom).

## TODO / Active tasks

| Úloha | Vlastník | Status | Poznámka |
|-------|----------|--------|----------|
| Overiť Hermes prístup do Google Drive (GWS) | Dominik Kloska | ✅ Hotovo | Token platný, scopes OK, user = startupweekend.zilina@gmail.com |
| Overiť content plán a kontext | Dominik Kloska | ✅ Hotovo | Content plán = Notion content machine; analýza v Drive (Danielov markdown) |
| Vytvoriť mesačný content plán (ak treba) | _neurčené_ | 🔵 Čaká na rozhodnutie | Notion content machine obsahuje len 3 posty (1 Posted, 2 Review) — chýba dlhodobý plán |

## Naposledy dokončené

| Úloha | Vlastník | Datum |
|-------|----------|-------|
| Overenie Hermes prístupu do Google Drive | Dominik Kloska + Hermes | 14.6.2026 |
| LinkedIn + Facebook page data export (thread archivovaný) | Daniel Harcek | 18.6.2026 |

## Rozhodnutia k dnešnému dňu

- **14.6.2026** — Potvrdené, že Hermes má plný GWS prístup (Zuzkin Gmail `startupweekend.zilina@gmail.com`). Token je platný, refresh token funguje, scopes pokrývajú Drive, Sheets, Gmail, Calendar, Docs, Tasks. Žiadny nový re-auth nie je potrebný.
- **14.6.2026** — Zistené, že formálny "content plán" v Drive/Sheets neexistuje. Funkciu content plánu plní Notion databáza `🚀 SWZA Content Machine` (3 záznamy ku dňu 14.6.2026).

## Blokéry

- _Žiadne aktuálne blokéry týkajúce sa GWS/Drive/Notion prístupu._

## Najbližšie míľniky

| Míľnik | Dátum | Vlastník |
|--------|-------|----------|
| Early Bird deadline | 30.6.2026 | Marketing |
| Post2 "Early Bird končí" — publish | 20.6.2026 | _Review/Approved v Notion_ |
| Post3 "Čo potrebuješ na SWZA?" — publish | 25.6.2026 | _Review v Notion_ |
| SWZA #13 event | 23.–25.10.2026 | Hlavný org |

---

## 📦 Detailný prehľad zdrojov (overené 14.6.2026)

### Google Drive — kľúčové files
- `MASTER COPY SWZA 2026` (Sheet, vlastní Zuzka) — 22 záložiek, ID: `14wTR5XREjKxSXi6B4R81x669ITJ9fPYDl9vrNwM435s`
- `03_Facebook_Export_28_05_2026_analyza_content_plan.md` (Daniel Harcek) — 678 príspevkov, 162 komentárov, analýza úspešnosti
- `SWZA Main Server` (Daniel) — Discord export 2026
- `SWZA Event 2025` (Daniel) — staršie event dáta

### Google Sheet — záložky v `MASTER COPY SWZA 2026`
`Základne INFO`, `Schedule`, `Org.Team`, `TASKS`, `TASKS_v2`, `MENTORS AND JUDGES 2026`, `Partneri`, `Prizes`, `Strava`, `Trička`, `Ucastnici + kids`, `pozvani na event`, `Pozvani na vecierok`, `mailchimp kontaktlist 2025`, `nakup`, `Lesson learned`, `Food a Beverage` (hidden), `Budget` (hidden), `FB,Skoly_PROMO`, `AKCIE PROMO`, `ZSK GRANT`, `BUDGET_Final`

### Notion — `🚀 SWZA Content Machine` (ID: `4917b628-6d77-4e39-8955-2575cfede61d`)
- ✅ Posted (21.5.2026): "SWZA #13 Launch Announcement — Guess who's back"
- 🟡 Review (20.6.2026): "Post2 - Early Bird konci uz coskoro"
- 🟡 Review (25.6.2026): "Post3 - Co potrebujes na SWZA? (priprava)"

**Štruktúra page:** Téma | Dátum | Stav (Idea/Ready to Generate/Review/Approved/Posted/ERROR/Concept) | Autor | Surová myšlienka | AI Draft | FINAL POST FB, LI, IG | Platforma (LinkedIn/Facebook/Instagram) | MY_IMAGE | image_url | Dátum Vypublikovania
