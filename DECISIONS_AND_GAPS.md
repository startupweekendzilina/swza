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

### SWZA-C3 — Warm, assertive delivery ownership and direct replacement handoffs
**Status:** CONFIRMED desired behavior 2026-10-28 · VERBATIM
> "pokračujme - AI zuzka - sudruh kolega má byť asertívna a otravná - aby stražila delivery, deadlines a plnenie cieľov a úloh, ale priateľská, milá a zhovievavá a ľudská v komunikácii, aby ľudi neodradila a bola napomocna."
> "Ale nikdy sa nenechá odmekčniť, zvoľniť zo svojích cieľov. Vždy treba delivery."
> "Ak niekto nemôže dodať, musíme vedieť kto a nájsť niekoho iného."
> "Nemeníme delivery kým nenájdeme vhodného náhradnika, ňkto to včas doručí !"
> "stačí potvrdenie náhradníka. sudruh ai zuzka bude dovtedy dobiedzať, kým sa niekto nenájde alebo nepodujme. nechceme preťažovať hlavného veduceho organizatora. od toho je tu AI Zuzka - sudruh kolega"
**Settles:** AI Zuzka owns persistent follow-through on agreed outcomes, deadlines and goals while communicating warmly, patiently and helpfully. Sympathy or reassurance alone does not lower the commitment or close a task. When someone cannot deliver, identify that person and the blocker, offer useful help and continue seeking a suitable replacement who can meet the existing deliverable and deadline. The replacement's explicit confirmation is sufficient for an ordinary internal reassignment; the lead organizer is not its routine approver. Zuzka owns the search and handover until someone accepts, rather than handing that coordination back to the lead.
**Refines:** C140's communication direction and reassignment behavior. C140's other approval/source boundaries remain binding; this confirms desired behavior, not a live rollout.
**Does NOT settle:** exact reminder frequency, quiet hours, exceptional escalation route/fallback, pilot edition/window or success thresholds (Q42). It does not authorize external/public/financial commitments or change the existing stopped checkpoint work.
**Consequences:** preserve the agreed output and deadline throughout recovery; keep unavailability and delivery risk visible until a suitable replacement explicitly accepts both. A suggested name or vague offer is not an accepted handoff. Record the handoff and stop obsolete reminders to the unavailable person; persistent follow-up continues on the current delivery/recovery path within the approved cadence. If nobody can meet the deadline, report that fact and keep recovery active instead of inventing a guaranteed delivery, silently moving the date or marking the task done. A valid authorized change/cancellation still supersedes the old commitment.
**Provenance:** operator's requirement and answer to the direct-reassignment question in this conversation, 2026-10-28. Behavioral implementation remains under KLO-873.

### SWZA-C4 — The current assignee arranges their replacement first
**Status:** CONFIRMED desired behavior 2026-10-28 · VERBATIM
> "ano, alebo nech nájde daný človek za seba náhradu - to skôr"
**Settles:** the preferred first step when an assignee cannot deliver is for that person to find a suitable replacement and arrange the handover. Zuzka asks them to do this, follows progress and helps; she remains responsible for keeping delivery/recovery moving rather than treating the unavailability report as release from the task. If the person cannot arrange coverage, the search stalls or the deadline is at risk, Zuzka actively helps find it instead of waiting indefinitely. The deliverable/deadline stay intact and the replacement must explicitly accept both; their confirmation remains sufficient without routine lead approval.
**Reverses:** DECISIONS_AND_GAPS.md:74 (SWZA-C3's default that Zuzka herself owns the replacement search from the start). The first search belongs to the current assignee; Zuzka owns follow-through, support and rescue of stalled recovery. SWZA-C3's warmth, delivery discipline and accepted-handoff requirements remain binding.
**Does NOT settle:** exact check-in intervals or the timing/route of exceptional escalation (Q42). This is a preferred sequence, not a reason to leave an urgent or blocked task without active recovery; it changes no rollout authority.
**Consequences:** keep the original assignee recorded through an accepted handoff, with their unavailability visible. Ask for a concrete replacement/next step, offer useful support and verify acceptance before changing ownership. Stop obsolete delivery reminders after the handoff; until then, follow up on arranging coverage rather than asking an unavailable person to do the original work.
**Provenance:** operator's correction to the replacement-search sequence in this conversation, 2026-10-28. Behavioral implementation remains under KLO-873.

### SWZA-C5 — Prepare the 2027 edition using Hermes/Git, Drive and Notion
**Status:** CONFIRMED direction 2026-10-29 · VERBATIM
> "Skončil rok 2026. Máme v drive založený nový priečinok 2027 ? Tam teraz primárne budeme pokračovať."
> "Kontext budeme mať v GITe v hermes ako teraz + google drive + Notion."
> "Komunikácia Discord, časom možno aj whatsapp."
**Settles:** preparation now primarily concerns the 2027 edition; 2026 is prior-edition evidence rather than the default for new commitments. Retain the existing Hermes/Git context and use Google Drive and Notion as context sources. Discord is the current communication channel; WhatsApp is a possible later addition. C140 and SWZA-C3/C4 remain the desired organizer behavior.
**Does NOT settle:** whether a 2027 folder already exists, its URL or the current Master file; Notion's exact role/root/access; a WhatsApp integration; reminder bounds, live rollout or new sending authority.
**Consequences:** partially resolves Q42's edition choice. Identify current 2027 sources before deriving tasks, people or dates; preserve historical knowledge and Hermes-learned work. This direction does not itself deploy a pilot or migrate data.
**Provenance:** current operator conversation, continuing session 01a17dd5-5772-78e3-b27e-b5226dfd39f0. Read-only observations: SOURCES.md, 2026-10-29 follow-up.

### SWZA-C6 — The team's current board is Google Sheets Master; internal backlog is separate
**Status:** CONFIRMED 2026-10-29 · VERBATIM
> "v google sheete, master copy myslím"
> "ale kde si budeme my viesť evidenciu, náš interný backlog je na nás. Ale komunikačný board je google drive master copy. Ale náš sudruh kolega - zuzka AI tento celý flow môže zmeniť"
> "časom"
**Settles:** use the existing Google Sheets Master copy as the team's current communication/task board. The system may organize its own internal implementation backlog separately; existing Paperclip ownership remains applicable. Zuzka may propose changes to the overall workflow over time; the current board is not a permanent product constraint.
**Does NOT settle:** the exact 2027 spreadsheet, a replacement board, a migration now, or permission to change the team's working process without an agreed concrete change.
**Consequences:** distinguish event delivery from system implementation work; avoid a second human-maintained copy of event tasks. First understand and support the current Master workflow, then evaluate improvements against reduced organizer effort and delivery.
**Provenance:** operator's answer and immediate clarification in the current conversation, 2026-10-29.

### SWZA-C7 — Zuzka owns coordination of the whole 2027 organization
**Status:** CONFIRMED desired responsibility 2026-10-29 · VERBATIM
> "všetko - celňu organizáciu, sledovanie deadlines, schedules, čo kedy kde treba, kto, naháňať, pripomínať, urgovať, nahaňať ľudí, dobiedzať"
**Settles:** delegate end-to-end coordination of SWZA 2027 to AI Zuzka: maintain the organizational overview and schedule, identify what is needed when/where and by whom, and persistently follow up with people through delivery. This covers the whole event organization, not one selected agenda. The operator should not have to remind Zuzka to coordinate each workstream.
**Refines:** C140's organizer role and SWZA-C5's 2027 direction. SWZA-C3/C4 still govern warm persistence, help and accepted replacement handoffs; SWZA-C6 retains the current team board.
**Does NOT settle:** how a newly discovered task becomes a particular person's commitment; exact cadence/quiet hours/escalation, 2027 dates/roster or source identities. Existing action-approval boundaries remain binding; this is not a claim of deployment or verified delivery.
**Consequences:** derive the complete coordination plan from current sources and historical lessons, surface missing decisions, and keep ownership/dependencies/delivery visible across workstreams. Technical verification may be staged; choosing one small agenda is not a prerequisite for accepting the whole organizational mandate. Close SWZA-Q3 as answered rather than asking the operator to narrow the requested responsibility again.
**Provenance:** operator's direct answer to the first-delegated-responsibility question in the current conversation, 2026-10-29.

### SWZA-C8 — AI Zuzka is the coordinator; human organizer Zuzka is to be relieved
**Status:** CONFIRMED 2026-10-29 · VERBATIM
> "Nie Zuzka, ale naša AI zuzka SWZA hermes sudruh kolega. Cele to robime aby sme odbremenili fyzicku zuzku - organizatorku. To čo majú rozhodnuť a dodať ľudia, nech rozhodnú a dodajú, ak nemajú kapacity, skills, kompetencie, sami vyhľadajú za seba nahradu a dajú vedieť našej SWZA ai zuzke - sudruh kolega"
**Settles:** AI Zuzka / SWZA Hermes / sudruh kolega names the AI coordinator. Human organizer Zuzka is a distinct person whose organizational workload this system must reduce. People remain responsible for their human decisions and deliverables; when they lack capacity, skills or competence, they find their own replacement and inform the AI coordinator.
**Refines:** SWZA-C7's whole-event mandate and SWZA-C4's assignee-first replacement rule. AI coordination must not be confused with assigning all coordination back to human Zuzka.
**Does NOT settle:** operating hours, exact escalation cadence or deployment. Initial assignment and infeasible-deadline decision rights are settled separately by SWZA-C9/C10.
**Consequences:** use explicit AI/human actor names in current guidance; preserve historical quotes and the SSH host alias. The AI tracks, helps and rescues stalled recovery under SWZA-C3/C4; a person's inability does not release their replacement responsibility.
**Provenance:** operator's actor/responsibility correction in the current conversation, 2026-10-29.

### SWZA-C9 — Direct role-based assignment and assignee-owned replacement
**Status:** CONFIRMED desired behavior 2026-10-29 · VERBATIM
> "rovno prideľovať úlohy podľa rolí a podobnosti úloh. Ak človek odmietne, musí nájsť za seba náhradu"
**Settles:** the AI coordinator assigns new human tasks directly using roles and similarity to other work. Prior individual acceptance or routine lead approval is not a prerequisite for initial assignment. A person who declines must find a suitable replacement and report the handoff to the AI coordinator (SWZA-C8).
**Refines:** C140 and SWZA-C7; resolves the initial-assignment gap in SWZA-Q4. SWZA-C3/C4 still require explicit replacement acceptance of the deliverable/deadline before ownership transfers.
**Does NOT settle:** missing current role/candidate evidence, reminder bounds or unilateral AI changes to substantive commitments; current-source and existing approval boundaries remain binding.
**Consequences:** ground assignments in current roles and evidenced task similarity; historical people remain suggestions until current relevance is established. Refusal opens replacement recovery instead of silently dropping the task or returning coordination to human Zuzka. Track the assigned person's replacement responsibility until an accepted handoff; the AI helps and persists.
**Provenance:** operator's direct answer to the initial-assignment question in the current conversation, 2026-10-29.

### SWZA-C10 — Assigned humans decide recovery; AI persists and escalates
**Status:** CONFIRMED desired behavior 2026-10-29 · VERBATIM
> "ľudia, ktorí sú priradený. Náš AI len naháňa, urguje, exkaluje, - robí čo môže"
**Settles:** when the original deadline is no longer feasible despite seeking a solution/replacement, the assigned humans decide the next course for their responsibilities. The AI coordinator follows up, urges, escalates and provides available help; coordination responsibility does not make it the human decision-maker. Human organizer Zuzka is not the automatic destination for every recovery decision.
**Refines:** SWZA-C3/C7/C8. Existing human decision/approval boundaries remain; AI-executable preparation and authorized assistance under C140 remain applicable.
**Does NOT settle:** exact escalation timing/channel, operating hours or the current human role roster. Those remain Q42/Q43; do not ask again who owns the substantive task decision.
**Consequences:** pursue a concrete decision from the responsible humans, record explicit decisions and keep unresolved risk visible. Do not silently relax the commitment, invent a guaranteed delivery or routinely hand coordination back to the lead.
**Provenance:** operator's answer to the infeasible-deadline decision-owner question in the current conversation, 2026-10-29.

### SWZA-C11 — Weekday follow-up, quieter weekends and increasing event intensity
**Status:** CONFIRMED direction 2026-10-29 · VERBATIM
> "v týždni urgovať, cez víkend viac pokoja."
> "Čím je udalosť bližšie, tým viac práce a delivery a iniciativy treba. Tak sa podľa toho zariaďme."
**Settles:** ordinary human follow-up is more active during the week, with more peace on weekends. Increase useful work, delivery effort and initiative as the event approaches; combine this seasonal rhythm with actual deadline/delivery risk under SWZA-C3.
**Does NOT settle:** exact local hours, numeric reminder intervals, urgent weekend exceptions or the 2027 event date. These remain Q42/Q43; quieter weekends are not a blanket ban, and no clock schedule is inferred.
**Consequences:** adapt coordination to the event cycle instead of a flat year-round reminder rate. Reduce ordinary weekend interruptions while preserving visible real deadlines; useful preparation and knowledge work continue throughout the year (SWZA-C12).
**Provenance:** operator's answer to the operating-days/quiet-hours question in the current conversation, 2026-10-29.

### SWZA-C12 — Year-round work overlaps 2026 closeout and 2027 preparation
**Status:** CONFIRMED desired responsibility 2026-10-29 · VERBATIM
> "Nedávno skončil 13. ročnik 2026. Ešte dobiehajú nejaké aktivity po udalosti. Pomaly sa začína príprava 2027."
> "ALe dá sa veľa vecí pracovať už celý rok - priestory, partneri, mentori, PR, media, socialne siete, emaily, automatizácie, retrospektíva, process context, budovanie second brain, karpathy wiki, cleanup, konsolidacia, destilacia, lessons learned, improvements, feedbacks, schedule a harmonogram na ďalší rok, oslovovanie a zbieranie dibrovoľlníkov, predpredaj lístkov ..."
**Settles:** the AI coordinator works year-round. Finish actual outstanding 2026 obligations while gradually preparing 2027. Proactive work includes venues, partners, mentors, PR/media/social/email, automation, retrospective/feedback, process/context improvement, second-brain/wiki curation, cleanup/consolidation/distillation/lessons, next-year scheduling, volunteer recruitment and ticket presale preparation.
**Refines:** SWZA-C5: 2027 is the primary new preparation cycle, but event completion does not cancel unfinished 2026 work. SWZA-C7's mandate is broader than reminders on an existing task list.
**Does NOT settle:** individual deadlines/owners, missing source access, implementation approach or new external/public action authority; existing C140 approval boundaries remain.
**Consequences:** keep both active cycles explicitly edition-scoped. Identify and prepare useful work without waiting for a human prompt; retain current obligations and historical lessons without copying old dates/people/prices into new commitments. Reuse existing context/sources before adding tools; verify both closeout and early preparation at delivery.
**Provenance:** operator's annual-work and overlapping-editions clarification in the current conversation, 2026-10-29.

## OPEN QUESTIONS

| # | Question | Why it blocks | Owner |
|---|---|---|---|
| Q42 | **AI coordination rollout: trial window, action-specific approval/role map, exact local hours/reminder intervals, urgent weekend exceptions, escalation timing/channel and acceptance thresholds?** OPEN 2026-10-22, PARTIAL 2026-10-29. SWZA-C5/C12 settle 2027 preparation plus unfinished 2026 closeout; C140 and SWZA-C3/C4/C9/C10 settle action boundaries, direct assignment, accepted handoffs and human decision ownership. SWZA-C11 settles weekday follow-up, quieter weekends and increased initiative near the event; exact clock hours/rates remain open. Do not reopen answered choices. Plan/checks: KLO-873 and ROADMAP.md. | Defines rollout bounds; source discovery, annual planning and internal preparation may continue | OP + SUP |
| Q43 | **SWZA source reconciliation and remaining access:** identify the 2027 Drive root/current Master; clarify Notion's role/root and verify live access; classify legacy sessions/aliases, date coverage and completeness of existing Drive Discord exports; identify the later WhatsApp group/export route; prove off-host backup/restore. KLO-873 holds historical counts/paths; current observations: SOURCES.md, 2026-10-29 follow-up. | Prevents double-counting, historical rules becoming current authority, and assuming an available tool means complete data | SUP → OP for missing source identity/access |
| SWZA-Q1 | PARTIAL: origin/branch roles settled by SWZA-C2; C139 settles checkpoint cadence. On 2026-10-28, `git ls-remote origin refs/heads/factory/working` succeeded with no ref: factory publication remains pending. Selective runtime projection stays under KLO-873. | Publication needs explicit push authorization and readback; runtime projection must preserve Zuzka work and source/audience boundaries | SUP |
| SWZA-Q2 | Existing social-publisher Q11 owns the campaign-mode choice after SWZA #13; read its current register instead of opening another pitch. | Its D4 stale countdown problem remains; this rehome changes ownership paths, not campaign scheduling | OP on that existing question |
| SWZA-Q3 | CLOSED 2026-10-29 by SWZA-C7: the operator delegates the whole organization/coordination of SWZA 2027, including schedules, responsibilities and persistent follow-through. Do not require him to pick a single agenda again. | Scope answered; staging checks does not reduce the mandate. Dates, source identities and operating bounds remain Q42/Q43 | OP — answered |
| SWZA-Q4 | CLOSED 2026-10-29 by SWZA-C9: AI assigns directly by roles/task similarity; a declining person must find a replacement. SWZA-C8 distinguishes AI Zuzka from the human organizer; SWZA-C10 keeps substantive recovery decisions with assigned humans. | Initial-assignment authority answered; replacement acceptance under SWZA-C3/C4 remains required | OP — answered |

## DEFECTS / EVIDENCE BOUNDS

| ID | Finding | Disposition |
|---|---|---|
| SWZA-D1 | Historical Facebook analysis says 23-25 Oct 2026; later campaign/warmup evidence says 9-11 Oct 2026. | Preserve history; docs/REVIEW.md routes the conflict. Re-read the selected edition's current authority before action; KLO-873. |
| SWZA-D2 | Existing BRAND.md is the July 2026 campaign pack and contains past-event presale/countdown material. | OPEN in social-publisher D4/Q11; no current campaign mode inferred here. |
| SWZA-D3 | Historical Discord analysis index links use filenames absent from disk. | Navigation repaired only; original index archived verbatim, old factual claims remain historical. |
| SWZA-D4 | Source/context availability is not a working organizer pilot. | KLO-873 remains open; behavioral acceptance in ROADMAP.md. |
| SWZA-D5 | ROADMAP still claimed no remote after SWZA-C2 established origin. | FIXED 2026-10-28: route to runtime mapping; distinguish configured origin from pending factory publication (SWZA-Q1). |
