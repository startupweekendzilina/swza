# SWZA — StartupWeekend Žilina #13

## Entry Point

Tento projekt je organizácia podujatia StartupWeekend Žilina #13. Pozri `docs/STAV.md` pre aktuálny stav a potom `docs/ROLES.md` pre rozhodnutia ohľadom štruktúry.

## Quick Start pre nového agenta

1. Prečítaj `docs/STAV.md` — aktuálny stav
2. Prečítaj `docs/ROLES.md` — kto vlastní čo
3. Prečítaj `docs/PHASES.md` — čo sa deje kedy
4. Prečítaj `docs/TOOLS.md` — aké nástroje používame
5. Máš otázky? Pozri `docs/MEMORY.md` alebo eskaluj na hlavného organizátora (Baška)

## Core Principle: Context Preservation

**Pravidlo:** Po KAŽDOM turn agent uloží do projektovej pamäte cokolvek dôležité:
- Aktuálny stav úloh
- Rozhodnutia a dohody
- Zmeny v plánoch
- Čo bolo dokončené / čo zostáva

Použi skill `para-memory-files`. Pozri `docs/MEMORY.md`.

## Communication & Handoff

- Pred začiatkom novej práce: skontroluj `docs/STAV.md`
- Po dokončení tasku: aktualizuj `docs/STAV.md`
- Pri nejasnostiach: konzultuj s vlastníkom role (viď `ROLES.md`)
- Kritické rozhodnutia: eskaluj na hlavného organizátora

## Error Handling

Pri problémoch:
1. Zaloguj chybu do projektu
2. Informuj vlastníka role
3. Ak je kritické: eskaluj na hlavného organizátora
4. Dokumentuj riešenie do `docs/TROUBLESHOOTING.md`

## Dokumentačné pravidlá

**Každé pravidlo musí byť explicitne zdokumentované.** Nikdy sa nespoliehať na domyslanie alebo ústnu dohodu. Čo nie je napísané, neexistuje.

- Nové pravidlo = pridaj do AGENTS.md alebo do príslušného `.md` súboru
- Zmena pravidla = aktualizuj existujúci záznam, nepridávaj nový bez kontextu
- Pravidlo bez dokumentácie sa nepoužíva

## Rozhodnutia a dohody

**Čokoľvek na čom sa dohodneme, sa zaznamenáva ihneď.**

- Rozhodnutie = zapíš do `docs/DECISIONS.md` alebo priamo do AGENTS.md ak je to pravidlo
- Ak treba detaily k rozhodnutiu, pýtaj si ich pred zápisom
- Čo nie je zapísané, neexistuje — nespoliehame sa na pamäť

**Príklady:**
- "Používame n8n nie Make" → `DECISIONS.md`
- "Každý agent po turn uloží kontext" → `AGENTS.md` (už je)
- "Štruktúra dokumentov = docs/ROLES, PHASES, ..." → `AGENTS.md`

## CHANGELOG

Každá zmysluplná zmena sa zaznamenáva do `CHANGELOG.md`.

**Kedy commitnúť:**
- Po dokončení funkcie alebo jej incrementu
- Po akejkoľvek zmene konfigurácie (MCP, tools, atď.)
- Po každom bugfixe alebo refaktorovaní

**Formát commit správy:** `type: short description`

Príklady:
- `docs: add CHANGELOG.md tracking project evolution`
- `security: add strict .env handling rules to AGENTS.md`
- `feat: add n8n MCP server connection via opencode.json`

**Verzovanie:** `[MAJOR.MINOR.PATCH]` podľa zmien (nová funkcia = MINOR, breaking = MAJOR, bugfix = PATCH)

## PERMANENTNE PLATIACE PRAVIDLÁ — KRITICKÉ

### ⭐ Jazyk (cross-session)
**VŽDY odpovedz v SLOVENSKOM jazyku.** Žiadne čínske znaky ani iné neslovenské písmená.
Uložené v: `memory` + `swza/AGENTS.md`.

### ⭐ Perzistencia pravidiel (cross-session)
**AKUKOLVEK instrukciu ali dôležité pravidlo (learning, dohodu, rozhodnutie) OKAMŽITE zapisuj do súboru.**
- Primárne: príslušný `.md` súbor v projekte (`AGENTS.md`, `DECISIONS.md`, atď.)
- Sekundárne: `memory` (Hermes persistent)
- Pravidlo súboru = source of truth — platí aj po zmazaní memory ali strate session contextu
- Toto pravidlo samo o sebe je PERMANENTNE uložené v: `memory` + `swza/AGENTS.md`

## Quick Start pre nového agenta

**Kritické pravidlo:** Subory obsahujúce secrets (`.env`, atď.) sa NIKDY nečítajú cez tools a nepristupujú sa k nim priamo.

- Všetky API kľúče a secrets sú v `.env` — pristupuje sa k nim len cez environment variables
- MCP connections používajú `${VARIABLE_NAME}` placeholder v `opencode.json` — reálne hodnoty nikdy nie v konfiguračných súboroch
- `opencode.json` referencuje `${N8N_MCP_API_KEY}` zo `.env`
- `.env` je v `.gitignore` — nikdy sa necommituje

Pri podozrení na exposed secret: okamžite informuj a eskaluj na hlavného organizátora.

## Chyby a zaseky — Dokumentačné pravidlo

**Každú chybu alebo zasek, ktorý stretneme, zaznamenáme do `docs/TROUBLESHOOTING.md` spolu s riešením.**

- Problém bez dokumentácie = zaseknutý problém
- Ak nemáš dostatok detailov o riešení, vypýtaj si ich od osoby ktorá to vyriešila
- Záznam slúži ako referenčná príručka pre budúce podobné situácie

**Formát:**
- Dátum, problém, príčina, riešenie, kto vyriešil