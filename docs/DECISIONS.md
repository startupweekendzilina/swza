# DECISIONS.md — Archív rozhodnutí

## Formát záznamu

Každé rozhodnutie má:
- **Dátum:** Kedy bolo prijaté
- **Číslo:** DEC-001, DEC-002, ...
- **Popis:** Čo sme sa rozhodli
- **Dôvod:** Prečo táto voľba
- **Alternatívy:** Čo sme zvažovali

---

## DEC-001: Štruktúra dokumentov

**Dátum:** 2026-05-18
**Popis:** Dokumenty organizujeme do `/docs/` adresára podľa oblasti
**Dôvod:** Vyhnúť sa jednému veľkému súboru, ľahšia orientácia
**Alternatívy:** Jeden veľký AGENTS.md (zamietnuté)

**Detailná štruktúra:**
- `docs/STAV.md` — aktuálny stav
- `docs/ROLES.md` — roly a úlohy
- `docs/PHASES.md` — fázy projektu
- `docs/TOOLS.md` — nástroje
- `docs/MEMORY.md` — context preservation
- `docs/PARA/` — PARA folders pre pamäť

---

## DEC-002: MCP n8n integrácia

**Dátum:** 2026-05-18
**Popis:** Používame n8n MCP server cez opencode.json
**Dôvod:** Centralizovaná automatizácia workflow
**Alternatívy:** Make.com, priame API integrácie

---

## DEC-003: Konfigurácia MCP cez .env

**Dátum:** 2026-05-18
**Popis:** API keys v .env, opencode.json používa placeholder syntax ${VAR}
**Dôvod:** Bezpečnosť — nikdy necommitujeme secrets
**Alternatívy:** Priamy zápis API key do json (zamietnuté)