# SWZA Agent Session — 2026-05-23

## Initial Context

**User:** Zuzka Kloskova — technically savvy, uses `gws` CLI (Google Workspace CLI) on another machine for Gmail/Drive. Prefers official Google tools.

**Project:** SWZA — Startup Weekend Žilina #13 (October 2026, 23.-25.)

### Repository & Automation
- **GitHub:** github.com/startupweekendzilina/swza (origin remote set)
- **n8n MCP:** connected at `https://api.n8n-mcp.com` via opencode.json — API key in `.env`
- **n8n instance:** healthy (ID: 910e1abd-cbec-4dac-81dc-814e378e465f), 1 workflow exists
- **Notion:** workspace integration ready

### Key People (from ROLES.md)
| Role | Person |
|------|--------|
| Main organizer / co-org | Baška |
| Venue & logistics | Adam J., Tadeas J. |
| Partners, mentors, judges | Tina |
| Marketing, PR, content | K. Janigova, Tadeas J. |
| Tickets, Discord | Dominik Kloska |
| Automation, n8n | Daniel Harcek |
| Catering | Veronika S. |
| KIDS program | J. Valová + Dominika B. |

### Event Timeline (from website)
- SWZA 2025 (12th edition) — completed
- SWZA 2026 (13th edition) — **October 23-25, 2026**
- Tootoot ticketing: tootoot.fm/en/events/6a084221cf42dac50e2d94ca

### SWZA Folder Structure
```
/home/node/swza/
├── AGENTS.md          # Entry point for agents
├── CHANGELOG.md
├── README.md
├── opencode.json      # MCP config (n8n + Notion)
├── .env               # API keys (gitignored)
├── .gitignore
├── docs/
│   ├── STAV.md        # Current state
│   ├── ROLES.md       # Roles and owners
│   ├── PHASES.md      # 5 phases of organization
│   ├── TOOLS.md       # Tools and platforms
│   ├── TROUBLESHOOTING.md
│   ├── MEMORY.md      # Context preservation rules
│   ├── DECISIONS.md   # Decision archive
│   ├── MCP_SETUP.md   # n8n MCP configuration guide
│   └── PARA/          # PARA folders (empty, needs population)
│       ├── 0_DAILY/
│       ├── 1_KNOWLEDGE/
│       ├── 2_PROJECTS/
│       └── 3_AREA/
└── workflows/
    └── swza-read-tasks.json
```

### Git Status
- Branch: `main`
- Working tree: clean
- Remote: origin (github.com/startupweekendzilina/swza)
- 2 commits in history

### n8n Workflow
- **SWZA - Read Tasks from Sheet** (ID: DkncUqSUxZ66xcZv) — inactive, reads from MASTER COPY SWZA 2026 Google Sheet, 3 nodes (Manual Trigger → Google Sheets → Code)

## TODO
- [ ] Explore online resources about past SWZA events (YouTube, media coverage)
- [ ] Build out PARA/ folders with event knowledge
- [ ] Consider what automation workflows are needed for SWZA #13
- [ ] Investigate SWZA #12 (2025) outcomes and winning teams

## Links to Explore
- https://www.startupweekendzilina.sk/
- https://linktr.ee/startupweekendzilina
- https://tootoot.fm/en/events/6a084221cf42dac50e2d94ca
- https://www.youtube.com/channel/UCh7F5i8Cx28FEMAT6CHMvuQ
- Media: ŽilinaK, SP21, StartItUp, Touch4IT