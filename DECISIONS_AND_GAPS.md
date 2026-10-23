# DECISIONS AND GAPS - SWZA

> Canonical SWZA authority. Operator quotes are binding; proposals and unanswered choices are not. Legacy C127/C128/C139/C140 and Q42/Q43 were relocated VERBATIM from ai-stack on 2026-10-23; IDs remain stable within their original provenance. Shared host rules remain in ai-stack.

## CONFIRMED

### SWZA-C1 — SWZA-specific context belongs to this project
**Status:** CONFIRMED 2026-10-23 · VERBATIM
> "máme v projects priečinok SWZA, poprosím všetko tam, čo súvisí so SWZA."
> "všeobecné, kloski os, agentic company, stack, infra, host v ai-stack, prípadne kloski-agentic-company v projects."
> "Všetko SWZA specivic v SWZA."
> "Aby keď otvoríme priečinok SWZA sme presne vedeli, ako , prečo a čo ďalej"
**Settles:** /home/ubuntu/projects/SWZA is the canonical project home for SWZA goals, strategy, source review, brand, decisions, knowledge and continuation. Shared host/OS/infra and company-wide context retain their own homes. Related executors keep adapters/pointers rather than a second SWZA knowledge copy.
**Does NOT settle:** new account access, publishing, live mount/context cutover, campaign mode, any guard bypass, or the unanswered pilot/action-policy choices.
**Consequences:** preserve source provenance and historical bytes, relocate SWZA-specific register content verbatim, reconcile active readers and make the project start from AGENTS.md/README.md.
**Provenance:** operator request in this conversation, 2026-10-23.

### C127 — SWZA Hermes v0.22.2 upgrade: nothing the agent built may be lost; tirith goes, Always Approve stays
**Status:** CONFIRMED 2026-10-19 · VERBATIM (chat + two selected answers)
> "Dokážeme upgradnuť SWZA hermes na latest hermes a latest minimax model - M3.1 flash - xhigh, aby agent neprišiel o dáta, skills, context a všetko čo si vybudoval ?"
> "Upgrade bez tirith (Recommended)"
> "Nechať bez pýtania (Recommended)"
**Settles:** hermes-swza (zuzka) moves to upstream image v0.22.2 + `MiniMax-M3.1-Flash` @ `agent.reasoning_effort: xhigh`. Acceptance = sessions, messages, memories, skills, cron, scripts, task state and gws/mcp credentials survive (counted, not assumed). Tirith pre-exec scanning is dropped (upstream removed it, no replacement); `approvals.destructive_slash_confirm` stays `false` as users set it in Discord.
**Does NOT settle:** session retention (kept forever via `sessions.auto_prune: false` until decided), GH_TOKEN in terminal (v0.22.2 blocks its passthrough), KLO-820 secrets on the podman command line, the master-host hermes-gateway (still v2026.9.24 with tirith).
**Provenance:** current interactive operator messages, 2026-10-19 (resume of session `3584295d`); tickets KLO-818, KLO-819.

### C128 — SWZA skill curator stays on; the agent picked 365 idle days under operator delegation
**Status:** CONFIRMED 2026-10-20 · VERBATIM delegation (chat), choice DERIVED by the agent
> "to je natívna funkcionalita hermes? Prečo to vypínať? 3etrí to kontext? Prečo navrhuješ vypnúť? Aké sú plusy a mínusy ?"
> "tak aby to dávalo zmysel a fungovalo, simplify, optimize, fine-tune, improve, continue &finish"
**Settles:** hermes-swza keeps the native curator; `curator.archive_after_days: 365` (upstream 30) so event-seasonal skills survive the gap between events. Chosen over pinning the 5 skills because it also covers skills created later and is one DR-tracked config line.
**Does NOT settle:** restoring the 3 skills archived 2026-10-16 (left archived: consolidated into `swza` / `n8n-workflow-builder`); thread → session link retention (stays 90 days, not configurable via config.yaml in v0.22.2).
**Provenance:** current interactive operator messages, 2026-10-20; operator may veto (pins instead).

### C139 — SWZA Git checkpoints after work and daily
**Status:** CONFIRMED 2026-10-22 · VERBATIM
> "Pushnime a pushujme pravidelne zmeny, changes..."
> "Oboje"
**Settles:** the SWZA workflow must commit/push after completed agent work and run an automatic daily checkpoint. The selected "Oboje" answered those two explicit options; it authorizes that recurring SWZA workflow, not pushes from unrelated repos.
**Does NOT settle:** publishing runtime stores or private account data to Git, history rewrites, any bypass of the stopped implementation guard, or a general relaxation of the interactive push rule. No checkpoint automation was deployed.
**Provenance:** operator's opening request and exact interactive selection in this conversation, 2026-10-22. Inventory, stopped delivery and next actions: Paperclip KLO-873.

### C140 — AI Zuzka: proactive organizer, human task owners and bounded autonomy
**Status:** CONFIRMED desired behavior 2026-10-22 · VERBATIM
> "Robíme AI agentic Zuzku."
> "Pripomína, priradzuje, deleguje, kontroluje, naháňa, urguje, predpripravuje, odpovedá na otázky."
> "Centrálny bod- knowledgebase pre všetkých organizátorov a potencionálne aj účastnikov, mentorov a všetkých."
> "Vie s čím treba pomôcť, kto nestíha, nedoručuje, navrhuje preradiť na niekoho iného. Vie kto má toho najviac, skúša odbremeniť ..."
> "každá úloha, ktorú má plniť človek a nie systém, má svojeho assignee. Podľa kontextu, minulých ročníkov. Úlohu vieme preradiť."
> "Riadenie úloh, termínov a follow-upov (odporúčam)"
> "Áno, interná rutina automaticky; vonkajšie a citlivé kroky schvaľovať (odporúčam)"
**Settles:** build toward a central proactive SWZA organizer/knowledge point that removes work from humans, prepares and delegates deliverables, answers/navigates, tracks dates/dependencies/delivery and proposes workload relief/reassignment. Human-only work has a named assignee grounded in available context/past editions and may be reassigned. First pilot: tasks, dates and follow-ups. After its rules are approved, routine internal reminders may run automatically; external email, public posts and commitments require human approval.
**Does NOT settle:** named approvers/fallbacks per action; reminder cadence, quiet hours or escalation rules; pilot edition/window and numeric success thresholds; broad data ingestion, new account access, public exposure or runtime rollout. The operator named Radical Candor as the communication model; exact practice remains a design proposal. Assignee does not imply blanket financial/signing authority. Existing safeguards remain binding.
**Consequences:** reuse current sources and tools first; distinguish current facts from past-edition evidence; retain source/audience boundaries. Inventory and proposed phases/acceptance live on Paperclip KLO-873; this row is desired behavior, not a claim that the pilot exists.
**Provenance:** operator's organizer request and follow-up interactive answers in this conversation, 2026-10-22; no invented message IDs.

### SWZA-C2 — One origin, separate factory and runtime branches
**Status:** CONFIRMED 2026-10-23 · VERBATIM
> "dajme to aj na origin všetko, Iné branches"
> "je to ako fabrika a auto. Fabrika vyrába auto. Použivatelia potrebujú auto, nie fabriku. Na našom host v SWZA je fabrika. Hermes potrebuje auto. Dáva zmysel ?"
> "prístupy na origin su dané. To neriešme. Chcem len oddeliť runtime a working know how a pracovné, working stuff"
**Settles:** use the existing startupweekendzilina/swza origin with unchanged access. The master-host SWZA checkout is the factory: working context, maintenance know-how, evidence and source preparation. Keep it on factory/working; main remains the existing Hermes product/runtime branch. This is content separation, not a branch-level access boundary. Publish reviewed Git-suitable work only; raw/private data and runtime stores remain excluded.
**Does NOT settle:** new repositories or access changes, a live context rollout, bulk merge into main, raw-data publication, checkpoint automation or a workaround for the earlier stopped checkpoint implementation.
**Consequences:** preserve both existing histories and the Zuzka dirty work; promote only reviewed runtime knowledge/rules/skills to main. Git/path evidence and the publication check live in docs/RUNTIME.md; KLO-873 retains checkpoint/runtime delivery work.
**Provenance:** current operator conversation; continuation of session 01a1658a-f84e-77b2-a21a-6697306e2fc0.

## OPEN QUESTIONS

| # | Question | Why it blocks | Owner |
|---|---|---|---|
| Q42 | **SWZA C140 pilot: which edition/window, named approval route/fallback per action, cadence/quiet hours/escalation and acceptance thresholds?** OPEN 2026-10-22. Internal-routine vs external/sensitive boundary is already confirmed; do not reopen it. Candidate plan and checks: KLO-873. | Defines the rollout contract; planning/read-only inventory may continue | OP + SUP |
| Q43 | **SWZA source reconciliation and remaining access:** classify legacy sessions/aliases, date coverage and completeness of existing Drive Discord exports; verify Notion live access/root and identify the WhatsApp group/export route; prove off-host backup/restore. KLO-873 holds measured counts and exact paths. | Prevents double-counting, historical rules becoming current authority, and assuming an available tool means complete data | SUP → OP for missing source identity/access |
| SWZA-Q1 | PARTIAL 2026-10-23: origin and branch roles answered by SWZA-C2; existing startupweekendzilina/swza origin is configured locally. Publication and selective runtime projection remain under KLO-873. C139 already settles checkpoint cadence. | Factory publication needs a verified push; runtime projection must preserve Zuzka work and source/audience boundaries | SUP |
| SWZA-Q2 | Existing social-publisher Q11 owns the campaign-mode choice after SWZA #13; read its current register instead of opening another pitch. | Its D4 stale countdown problem remains; this rehome changes ownership paths, not campaign scheduling | OP on that existing question |

## DEFECTS / EVIDENCE BOUNDS

| ID | Finding | Disposition |
|---|---|---|
| SWZA-D1 | Historical Facebook analysis says 23-25 Oct 2026; later campaign/warmup evidence says 9-11 Oct 2026. | Preserve history; docs/REVIEW.md routes the conflict. Re-read the selected edition's current authority before action; KLO-873. |
| SWZA-D2 | Existing BRAND.md is the July 2026 campaign pack and contains past-event presale/countdown material. | OPEN in social-publisher D4/Q11; no current campaign mode inferred here. |
| SWZA-D3 | Historical Discord analysis index links use filenames absent from disk. | Navigation repaired only; original index archived verbatim, old factual claims remain historical. |
| SWZA-D4 | Source/context availability is not a working organizer pilot. | KLO-873 remains open; behavioral acceptance in ROADMAP.md. |
