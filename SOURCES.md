# SWZA — sources and access

Local audit: 2026-10-23; machine counts and file hashes: sources/catalog.jsonl and docs/REVIEW.md. The original external inventory is frozen at 2026-10-22; a separate 2026-10-29 follow-up appears below. Neither is a completeness claim.

## Authority by data kind

| Kind | Location | Authority / use |
|---|---|---|
| Product decisions / approved responsibility | DECISIONS_AND_GAPS.md | Binding operator words; unresolved rows stay open |
| Edition-specific work/people/schedule | Existing MASTER SWZA 2026 TASKS / Org.Team / Schedule; 2027 file/root remains Q43 | Re-read current fields; retain real 2026 closeout work while preparing 2027 (SWZA-C12) |
| Historical operations | extracted/Data Exports/01–06 Discord analyses | Candidate playbooks and prior-role evidence, not current assignments |
| Historical dialogue | extracted/Data Exports/SWZA Discord Export 2026/ | Citable message evidence; catalog has IDs/dates/counts |
| Historical content | Facebook Markdown exports/analyses, Content/, media kits | Voice/examples/FAQ; verify claims and edition before use |
| Brand | BRAND.md | Existing campaign pack; publisher D4/Q11 remains open |
| Files/media provenance | docs/archive/MARKETING_SOURCES-20260703.md | Historical acquisition/cleanup record, not proof of today's remote completeness |
| Runtime mappings | docs/RUNTIME.md | Connect this project's context to the live bot and shared host infrastructure |

The archive includes private lists and organizer/financial/Kids material. Default audience is internal organizers. Public answers must use a reviewed audience-safe extract, not the entire raw source. Historical checklist Wi-Fi access values are not copied into this context.

## External/live sources — observed 2026-10-22

| Source | Verified | Bounds / next work |
|---|---|---|
| SWZA Hermes state.db on Zuzka | 179 sessions / 13,550 messages; Discord 176 / 13,526 since 2026-05-23 | Saved bot context is not full Discord channel history |
| Upgrade snapshots | Each 174 / 12,455; IDs/message pairs present in live SWZA | Reaper horizon 2026-11-18; no additional unique DB evidence found in these two copies |
| Session JSON / legacy bot | Seven canonical IDs absent from live DB, 326 entries; legacy DB 19 sessions / 283 messages absent by ID | Resolve aliases/overlap and SWZA relevance before merging; exclude request dumps |
| Gmail via existing gws account | startupweekend.zilina@gmail.com; profile/search/message metadata read | Mailbox 1,525 messages / 1,195 threads; not all SWZA; search estimate is approximate |
| Drive | 954 name-matching items; native Sheet/Doc/Form/PDF/assets present | Name search is not recursive completeness; local/export overlap needs stable IDs/hashes |
| MASTER SWZA 2026 | 20 tabs; actual TASKS/Org.Team/Schedule reads | Sheet ID 14wTR5XREjKxSXi6B4R81x669ITJ9fPYDl9vrNwM435s; E-mail header was F, not the documented E |
| Calendars | SWZA primary + startupisti.zilina listed with owner access | Event-level read/write not tested |
| Notion | Content Machine reference d05eac70-cd6a-400f-b59c-a80459e4b8a4; data source 4917b628-6d77-4e39-8955-2575cfede61d | Live access and the main organizer wiki root unverified |
| WhatsApp | Requested as an additional group/source | Group identity, export/access route and coverage still Q43 |
| Live Discord REST | Existing gateway/history works; historical HTTP 40333 documented | Full-history permissions/coverage unverified; no denied-access workaround |

Master Hermes is a separate dataset: the earlier larger session count belongs to master, not SWZA. Classify relevance before importing any master sessions.

Drive references:
- Export/archive root: 1j_8NYsRys4-FoDVzWG4MsK3K4kXtgV8J.
- Main Server: 17rjCpTp2RsrJf_CoqeKvG8alVFQpE7Al.
- Event 2025: 1YS2GPS_Lje7H0K1qPFiNyiJ9iw43b9fC.
- Event 2023: 1tr7--FCQ4Mx_AO-8nCIbI5LFbxu7OERv.
- Older acquisition record cites 1MO7o8qnY9jMLJnVmqQIWM86ZRZV5bWLP; do not silently equate the roots without checking.

## Source record for the future ingest loop

Stable source ID + account/channel/file + source date range + edition + audience + owner + read/write authority + fetched-at/cursor/hash + derived-page links. Corrections supersede a dated fact; they do not erase its historical provenance. Use Discord message IDs to dedupe, not filenames or session counts.

Known coverage gap: local main-server exports end in February 2026; Hermes records begin in May 2026. Neither establishes channel completeness between or after those points. Current live sources must be reconciled rather than summed.

Native local search: rg -n -i '<topic>' knowledgebase docs extracted/Data\ Exports --glob '*.md'.
Read-only gws uses the running bot container (see docs/RUNTIME.md), not run.sh. A new source appearing is a source-registry update, not blanket approval to expose its contents.

## 2026-10-29 follow-up — 2027 discovery

Authority: DECISIONS_AND_GAPS.md SWZA-C5/C6. Read-only source/runtime observations; no source edit or outbound business message. Git context publication is separate.

| Surface | Observed | Bound / next step |
|---|---|---|
| Live Hermes | Container hermes-swza reports Up 9 days; SOUL.md, memories and state.db exist at the mapped runtime path | File presence is not restore or behavioral acceptance |
| Runtime project context | /home/ubuntu/swza/AGENTS.md and active project/swza skill still identify edition #13 / October 2026; SOUL.md contains generic Hermes guidance | New delivery behavior was not verified; preserve learned rules while preparing 2027 context |
| Existing email notifier | Job 80b6ff061606, SWZA Daily Task Notify: enabled=false, state=paused; last_run_at=2026-10-13T22:00:59.694562+00:00, last_status=ok | Not a newly enabled pilot; do not reactivate from this inventory |
| Drive | Existing 2026 folder and MASTER SWZA 2026 found; searches for accessible 2027 folders, including an exact 2026/2027 folder filter, returned no 2027 folder | Does not prove absence in another location/account; current 2027 root and Master URL remain Q43 |
| Notion | This session has no connected Notion tools; a Notion plugin is available but not connected. Hermes has a productivity/notion skill; the existing Content Machine reference remains in the historical inventory above | Neither live access nor the main organizer root/role was verified |
| Implementation backlog | KLO-873, KLO-874 and KLO-824 read with comments; all report backlog | No repair, task closure or rollout performed |

Selected runtime Git status remains main with modified AGENTS.md and untracked campaigns/. Preserve that work. No contact rows, memory contents or runtime stores were copied into Git.
