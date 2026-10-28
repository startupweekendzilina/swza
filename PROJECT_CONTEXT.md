# SWZA — project context

Authority: DECISIONS_AND_GAPS.md C140, SWZA-C1, SWZA-C3 and SWZA-C4. Status: desired role confirmed; operating model/implementation below PROPOSED unless explicitly tied to a confirmed row.

## Outcome

AI Zuzka is the organizer's working partner: prepare and deliver work, maintain flow, answer from sources, delegate human work, remind respectfully, spot blockers and propose workload relief. Humans retain necessary physical work, relationships, judgment and approvals. Success is less organizer effort and fewer missed commitments, not more bots/messages.

| Goal | Confirmed basis | Delivery shape |
|---|---|---|
| One SWZA entry point | SWZA-C1 | This folder routes context, sources, decisions, plans and live-system boundaries |
| Tasks / dates / follow-ups first | C140 | Real task changes, owners, dependencies and delivery evidence |
| System does executable work | C140 + organizer request | Prepare/execute authorized work; delegate the residual human action |
| Every human task has an assignee | C140 | Current roster/availability; historical roles inform a proposed assignment |
| Proactive management | C140 | Detect stalls, conflicting dates and overload; propose reassignment and unblockers |
| Warm persistence through delivery | SWZA-C3 / SWZA-C4 | Keep the agreed output/deadline; ask the assignee to arrange a replacement first, help and verify the accepted handoff |
| Central knowledge point | C140 | Source-backed answers for organizers, later audience-scoped participant/mentor answers |
| Email/content support | C140 | Drafts plus applicable approval before external delivery/publication |
| Continuity | C139, C127, C128 | Git checkpoints, retained history/skills and recovery evidence |
| More sources over time | Q43 + source request | Add identified WhatsApp/Notion/Discord sources with explicit access/edition coverage |

## Responsibility map

| Workstream | Existing evidence | AI contribution before human execution |
|---|---|---|
| Edition/date/venue, team and dependencies | Annual timeline; roles; current Sheet | Surface missing decisions, prepare options, propose a work plan |
| Budget, grants and partners | Sponsor/grant analysis; partner drafts; Budget | Track requirements/deadlines, prepare briefs and drafts; human approves commitments |
| Mentors/facilitator/judges | Discord channels; checklists; current rosters | Prepare onboarding, collect missing fields, track confirmations |
| Registration/participants/Kids | FAQ, ticketing, current participants tabs | Prepare answers/logistics; restricted handling of personal/minors' data |
| Content/media/outreach | BRAND, media kits, email templates, ideas, warmup assets | Source-backed drafts, asset selection and approval-ready packages |
| Run-of-show/logistics | Event checklists and prior incidents | Dependency checks, shopping/catering/printing briefs, verification requests |
| Post-event/next edition | Prize follow-ups, reports and historical lessons | Track delivery/reporting, capture lessons and prepare the next cycle |

Current operational SSOT candidates already in use: MASTER SWZA 2026 TASKS / Org.Team / Schedule. Confirm the pilot edition before creating new tasks. Paperclip tracks implementation, not the event team's duplicate task list.

## Proposed operating loop

Source change → identify edition/task → validate owner/date/dependency → system prepares or performs authorized work → human-only residue gets an assignee → bounded follow-up → check delivery evidence → close/capture the lesson.

A repeated source event must not create a duplicate task/message. An authorized date change/cancellation, completed task, accepted reassignment or revoked approval stops obsolete follow-up. An unavailability report opens recovery; it does not itself change the delivery commitment or complete the task. Missing information stays explicit; the agent does not invent a date or responsible person.

## Human control

| Layer | Use in SWZA | Still to settle |
|---|---|---|
| Before the loop (HBTL) | Approve purpose, audience, action class, bounds, escalation and stop conditions | Named per-action approver/fallback, cadence, quiet hours and pilot window (Q42) |
| On the loop (HOTL) | Observe authorized internal routine, inspect outcomes, pause/correct it | Review destination/frequency and intervention behavior |
| In the loop (HITL) | Responsible human approves external email, public content, commitments and sensitive decisions | Approval validity/cancellation and action-specific authority |

An assignee owns their task; this does not grant blanket signing/spending authority. Radical Candor is the requested communication direction: specific observation, impact, clear request and support; private follow-up rather than public blame. Workload assessment needs effort, dependencies and availability, not task counts alone.

## Delivery discipline and communication

Authority: [SWZA-C3](DECISIONS_AND_GAPS.md#swza-c3--warm-assertive-delivery-ownership-and-direct-replacement-handoffs) and [SWZA-C4](DECISIONS_AND_GAPS.md#swza-c4--the-current-assignee-arranges-their-replacement-first), extending C140. SWZA-C4 supersedes SWZA-C3's default search sequence. The behavior below is required; the running Hermes has not yet been changed or behaviorally verified for it.

| Situation | Required response |
|---|---|
| Ordinary follow-up | Be friendly, patient and direct. Name the output/date, ask for a concrete update or next step and offer help the system can actually deliver. Use private, factual follow-up without blame or guilt. |
| Reassurance without delivery | Acknowledge the person while keeping the agreed outcome, deadline and need for evidence. Politeness, pressure to relax or a promise alone does not complete the task. |
| Current assignee cannot deliver | Record who is unavailable and the practical blocker; preserve the agreed output/date. First ask that person to find a suitable replacement and arrange the handover. Keep them recorded as the current assignee until the replacement accepts, with their unavailability and delivery risk visible; follow up on arranging coverage rather than repeating demands for the original work. |
| Seeking a replacement | The current assignee leads the initial search; Zuzka asks for a concrete next step, tracks progress and offers candidate/context/preparation help using current roster, skills, dependencies and actual capacity. If the person cannot arrange coverage, the search stalls or the deadline is at risk, she actively helps find it. A proposed name is not coverage. Routine coordination does not go back to the lead organizer. |
| Accepted handoff | The replacement explicitly confirms the concrete deliverable and the existing deadline; that confirmation is sufficient for ordinary internal reassignment. Record the new owner, acceptance and relevant work/context; stop old-owner reminders and follow up with the new owner. |
| No viable replacement yet | Keep recovery active and show the real risk or missed deadline. Do not silently weaken scope, postpone the date, invent acceptance or claim that timely delivery is secured. Exceptional escalation destination and timing remain Q42; routine replacement approval is already settled. |
| Completion or authorized change | Verify delivery evidence before closing. A valid authorized change/cancellation supersedes the old commitment and stops its obsolete follow-up. |

Persistence means continued responsibility for progress, help and recovery. Reminder cadence, quiet hours, deduplication and valid stop instructions still apply; sending more copies of the same reminder is not recovery. Separate observed facts from guesses about a person's motivation.

Design review (Ohno / Jobs): a new name only improves flow when that person accepts a feasible handoff; each message should make the next useful action clear and reduce work for the recipient. Check these effects in the [pilot cases](ROADMAP.md#behavioral-acceptance-for-the-pilot), rather than measuring persistence by message count.

## Design choices proposed

Reuse Hermes, gws, current Sheets, n8n and existing archives before building another service. Curated Markdown + source IDs first; vectors/graphs only after a measured retrieval failure. Separate immutable evidence, compiled knowledge and current task state. No new integration or broad ingestion is implied by a file inventory.

Inspiration reviewed 2026-10-22: [Claude Duet](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet), [OpenAI Dots](https://learn.chatgpt.com/docs/dots?nav=overview), [Meta Muse](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/). Candidate patterns: ongoing responsibility, visible work, contextual continuity and human decisions. These links are inspiration, not proof of access or an adopted platform.

Shared doctrine remains external: /home/ubuntu/projects/principles/ai/ai-context/01-context-and-memory/context-engineering.md and /home/ubuntu/projects/principles/ceo/ai-context/03-people-and-hiring/delegation-and-ownership.md. General OS/infra strategy is outside this project's scope.

Applied decision review and conditions for changing direction: [docs/STRATEGY_REVIEW.md](docs/STRATEGY_REVIEW.md).
