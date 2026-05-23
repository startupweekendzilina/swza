# CHANGELOG.md

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