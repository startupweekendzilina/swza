# SWZA — runtime and repository boundary

## Ownership

| Plane | Home | Role |
|---|---|---|
| Canonical project context | /home/ubuntu/projects/SWZA | Product decisions, vision, source map, reviewed knowledge, brand, roadmap |
| Live project working tree | Zuzka_Oracle-24GB:/home/ubuntu/swza | Existing bot project Git/docs/campaigns; preserve its history and dirty work |
| Live Hermes runtime | Zuzka_Oracle-24GB:/home/ubuntu/workspaces/hermes-swza/data | SOUL.md, skills/, memories/, state.db and runtime state |
| Deployment / restore | /home/ubuntu/ai-stack/hermes-swza/ | Host-managed DR configuration; operational README remains there |
| Host monitoring / reaper | /home/ubuntu/ai-stack/fleet/zuzka/ | Shared host operations, not the event team's task state |
| Content executor | /home/ubuntu/projects/social-publisher/ | Shared generator and Notion integration; SWZA BRAND/SOURCES paths are adapters to this project |

Paths in the first two rows are on different machines. Opening this local folder does not change the running bot's context or mounts.

Container mount mapping observed 2026-10-22: Zuzka /home/ubuntu/swza → /home/node/swza; Hermes data → /home/node/.hermes; named volume hermes-swza-home → /opt/data. Live-root existence and Git identity were rechecked 2026-10-23. Current image/model selection remains host infrastructure's responsibility; do not copy model slugs into project policy.

## Read-only entry

ssh Zuzka_Oracle-24GB
git -C /home/ubuntu/swza status --short --branch
podman exec --user 10000 hermes-swza gws sheets spreadsheets values get --params '{"spreadsheetId":"14wTR5XREjKxSXi6B4R81x669ITJ9fPYDl9vrNwM435s","range":"Org.Team!A1:AI1"}'

The latter commands run on Zuzka. Do not invoke run.sh for a read: startup overwrites runtime configuration and can start another gateway. Never print a token-bearing remote URL. Full Discord-history permission remains unverified.

Hermes does not automatically load the master's ai-stack/AGENTS.md or this local folder. Its context is SOUL.md, its skills and the mounted project. A later deployment must explicitly map approved project rules there and prove loading/behavior without discarding runtime-learned work.

## Git / continuity

A local context repository is initialized at this root with the existing SWZA Git identity measured on Zuzka. Raw/private exports and runtime stores are excluded by .gitignore; commit explicit reviewed context paths only.

The existing Zuzka repository and this local context Git are not yet unified. No origin, remote push, scheduled sync or live path/mount change is configured here. KLO-873 owns repository/history mapping and delivery; C139 already approves after-work plus daily checkpoints, so do not ask that preference again. Its earlier PreToolUse DENY [credentials] remains stopped.

Before wiring publication: identify the intended private repository, reconcile existing history/dirty ownership, replace unsafe authentication under the existing operator boundary, choose context/source vs runtime projection and prove a no-change/repeated checkpoint. No force push, unrelated-history overwrite or raw runtime-store commit.

Local backup inclusion is visible in ai-stack/maintenance/ip-backup.sh (projects/SWZA file enumeration). That proves selection in source code, not a successful off-host backup/restore. Q43 requires an isolated restore test. Snapshot reaper horizon for the upgrade copies is 2026-11-18.

## Open runtime defects

- KLO-820: startup arguments and hardcoded/token-bearing Git authentication; operator rotation remains part of KLO-484's existing deferred decision.
- KLO-824: startup overwrites runtime-learned configuration; named-volume part was addressed, remaining preservation behavior still open.
- KLO-874: current recipient lookup instructions disagree with the roster schema.
- Master-only KLO-825/KLO-826 belong to ai-stack, not this project's rollout backlog.

Use the shared host runbooks for operations; this consolidation performs no restart, send, permission change or credential rotation.
