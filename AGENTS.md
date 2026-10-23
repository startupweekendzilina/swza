# AGENTS.md — SWZA

Project home: /home/ubuntu/projects/SWZA. Read this card when working on Startup Weekend Žilina.

## Start
- Authority and unanswered decisions: [DECISIONS_AND_GAPS.md](DECISIONS_AND_GAPS.md). Legacy C127/C128/C139/C140 and Q42/Q43 retain their IDs after relocation from ai-stack.
- Purpose, responsibility and proposed operating model: [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md).
- Phase order and exit conditions: [ROADMAP.md](ROADMAP.md); next execution entry: [NEXT_SESSION.md](NEXT_SESSION.md).
- Sources/access/edition boundaries: [SOURCES.md](SOURCES.md); file-level evidence: [sources/catalog.jsonl](sources/catalog.jsonl).
- Existing material assessment: [docs/REVIEW.md](docs/REVIEW.md).
- Reusable lessons: [knowledgebase/INDEX.md](knowledgebase/INDEX.md).

## Ownership
- SWZA product context, brand, decisions, knowledge and plans live here.
- Shared host rules, model routing, services/DR, fleet and general second-brain architecture stay in /home/ubuntu/ai-stack. Company-wide strategy stays in /home/ubuntu/projects/kloski-agentic-company.
- Actionable implementation work stays on Paperclip: KLO-873 parent; KLO-874 roster; KLO-820 startup exposure; KLO-824 runtime-state loss. Read the actual ticket/comments before acting. Do not create a second task tracker in this folder.
- Live SWZA bot is on SSH host Zuzka_Oracle-24GB. Its /home/ubuntu/swza and Hermes data are deployment/runtime sources, not this master's working directory. Mapping: [docs/RUNTIME.md](docs/RUNTIME.md).

## Work rules specific to SWZA
- C140 confirms the desired role; the pilot and recurring Git checkpoint automation are not deployed.
- Internal routine becomes automatic only under the approved action policy. External messages, public posts and commitments need the responsible human's approval. Per-action approvers/cadence remain Q42.
- AI/tool-executable work should be delivered by the system. Human-only work gets one named assignee; historical role holders are suggestions, current Org.Team and availability decide.
- Org.Team recipient lookup uses the E-mail header, never a fixed column. KLO-874 remains open; inventory found stale instructions, not a proven bad send.
- Distinguish current authority from historical evidence. Source date, edition, audience and approval travel with a derived fact. Do not turn an old deadline/person/price into a current commitment.
- BRAND.md is the existing July 2026 campaign pack; its past-event countdown issue remains social-publisher D4/Q11. Read docs/REVIEW.md before drafting current content. Shared audience rules remain in social-publisher/brands/AUDIENCE_SK.md.
- Raw Discord exports, contact lists, budgets, children/participant data and runtime stores are restricted sources. Compiled answers follow the requester's audience. Do not put runtime stores or raw contact data in Git.
- Preserve operator-original presentations and historical source bytes. Existing outreach build scripts can rebuild/deploy artifacts; do not execute them as an inventory step.
- The earlier PreToolUse DENY [credentials] for checkpoint implementation remains stopped. No alternate-tool/account/agent workaround.

## Verification
- For this context: resolve links from this root, verify lossless relocations and the source catalog, inspect only explicit Git paths.
- For a future pilot: run the behavioral acceptance cases in ROADMAP.md at delivery; report failed/skipped/unavailable cases. A timer's existence is not acceptance.

Strategy decisions use [docs/STRATEGY_REVIEW.md](docs/STRATEGY_REVIEW.md); shared review methods stay in ai-stack.
