# Document template — Pattern Data daily progress

## File naming

- Progress: `Daily Progress/pattern-data-delivery-progress-YYYY-MM-DD.md`
- Standup transcript: `Transcript/ChartSwap Daily Stand up/ChartSwap-Daily-Stand-up-YYYY-MM-DD.docx`
- PD Review with Austin: `Transcript/PDReviewWithAustin/PDReviewWithAustin-YYYY-MM-DD.docx` (Microsoft Word; legacy plain text without extension still supported)
- Austin meeting transcript: `Transcript/Austin Meeting/Pattern-Data-Austin-YYYY-MM-DD.docx`
- Actions: `Daily Actions/daily-actions-YYYY-MM-DD.md` (optional — not used as source for the progress report)

## Header

```markdown
# Pattern Data — delivery progress

**Feature:** [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) · **As of:** YYYY-MM-DD  
**Targets:** UAT sandbox **2026-08-31** · Production **2026-09-30**
```

Do **not** include a separate glossary block. Spell out jargon on first use in section text (see Writing style). Do **not** link to `.cursor/` paths in the deliverable.

**Do not use wave / Wave 1 / Wave 2 language** anywhere in progress reports — retired delivery model.

## What to update from transcripts

| Section | Update when |
|---------|-------------|
| **Daily update from Austin** | **Austin-class transcript** (PD Review with Austin or Austin meeting) — priority order, scope in/out, next-up after wrap-up; replace table when Austin changes plan |
| **Status at a glance** — all phase rows | Standup **or** Austin-class: closed subtasks, CS uploads, deploy decisions, **Forecast slips**. Do **not** accumulate historical bullets across days. |
| **Feature delivery tracker** | Re-sync from Jira before editing; append `**Update YYYY-MM-DD:**` in Next step when standup or Austin adds detail |
| **Team focus** | Michael/Sarah from Jira assignees; **Islam** from standup (default: RequestShare / LNI-3763); **exclude Youssef Yahia** subtasks |
| **Path to UAT & Production** | Recompute `N/M features UAT-ready` from tracker; adjust target dates only when **Austin** or standup confirms a slip |
| **Risks & challenges** | Keep the **two standing risks** unless user adds new ones; condition → consequence → mitigation format |

**Do not include:** Open delivery blockers (OC bugs), Client release plan, Flow to be retested, Pre-UAT provider matrix, Other in-flight work, or **Standup action items** (use `Daily Actions/` for action tracking if needed).

**Standup action items section vs standup-driven content:** Dropping `## Standup action items` means **only** that section is omitted from the markdown and Teams card. You must still extract the standup transcript and update **Status at a glance**, **Team focus**, **Feature delivery tracker** Next step, **Daily update from Austin** (day-to-day), and **Risks** from standup content. If a morning Jira-only report was written before the standup `.docx` existed, update again when the transcript is available — replace carry-forward / "no transcript yet" notes with today's standup bullets.

**Do not edit** the plan file if user attached one for reference only.

## Writing style — manager audience

The primary readers are **delivery managers**, not Salesforce developers. Apply these rules in every progress file:

- **Spell out or explain jargon** on first use in each report (e.g. deploy packages, UAT-ready, pddev).
- Prefer **Deploy packages** over bare **CS** in tables and Notes; use `Forward · Rollback · Settings` instead of cryptic `Feature ✓ · Rollback ✓ · Properties ✓` when the report is manager-facing (either format OK if a legend is present).
- **Notes** columns and phase rows: plain English — what changed, what blocks the date, who owns the escalation.
- **Next step** column: one outcome a manager can track (not internal dev shorthand).
- **Risks**: always fill **Mitigation** with actionable bullets — never leave empty.
- **PM / escalation owners:** **Hamed** and **Nabawy** (not Salah) — client access, Austin follow-ups, timeline risk.

---

## Status at a glance

Three phases: **PD Sandbox finalize**, **UAT Sandbox deploy**, **Production**.

Use HTML lists inside table cells. **Keep each cell concise — plan-affecting updates only.**

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **PD Sandbox finalize** | Team | In progress | `<li>` today's completed dev/QA items on pddev | `<ul><li>` open features still being coded or retested | Rolling | — | Dev team finishing Pattern Data features on the **development sandbox** before any UAT move |
| **UAT Sandbox deploy** | Team | Not started / In progress | `<li>` features with deploy packages validated on UAT | `<ul><li>` remaining features queued; **one feature per release** | **2026-08-31** | — | Each feature needs Forward + Rollback packages (and Settings if applicable) tested on UAT |
| **Production** | Team | Not started | — | `<ul><li>` UAT sign-off; production deploy packages per feature | **2026-09-30** | — | Live release after UAT sign-off per Austin's deployment plan |

- **What's done** — `<li>` bullets: **today's** closed subtasks, CS uploads validated, stories marked ready
- **What's left** — `<ul><li>` bullets: open stories, pending CS, wordings approval, UAT promotion queue
- **Notes** — only constraints that **change scope, dates, or capacity** (e.g. feature-by-feature deploy, Austin decision)
- **Forecast** — bold date; only change when **Austin-class transcript** or standup calls a slip

---

## Daily update from Austin

Engineering manager **Austin** sets what ships next and may change direction frequently. Place this section **after Status at a glance**, before Feature delivery tracker.

```markdown
## Daily update from Austin

*What Austin directed — deployment priority, scope, and what's next. Updated from PD Review or Austin meetings; may change day to day.*

| Priority | Feature / story | Environment | Status |
| --- | --- | --- | --- |
| 1 | [LNI-3137](...) Payment Management | UAT sandbox | Upload in progress |
| 2 | Approved Fee overhaul | pddev | Next after current wrap-up (Austin) |

*Last Austin input:* [PD Review with Austin — YYYY-MM-DD](../Transcript/PDReviewWithAustin/PDReviewWithAustin-YYYY-MM-DD.docx)*
```

- **Priority 1** = next feature Austin directed for promotion or active UAT work
- Remaining rows = queue or "TBD until Austin meeting"
- If no Austin-class transcript: carry forward prior day's table or infer from Jira UAT column + standup; note `*Last Austin input:* baseline from Jira sync YYYY-MM-DD — no Austin meeting or PD Review transcript on file yet.*`
- Prefer **PD Review with Austin** over `Pattern-Data-Austin` when both exist for the same date
- PD Review source is a **Word `.docx`** file (`PDReviewWithAustin-YYYY-MM-DD.docx`). The file may contain both meeting transcript and embedded reference docs (e.g. wordings tracker) — use transcript for deployment plan; wordings sections for Risks and delivery gates
- If the PD Review file jumps timestamps, note the gap and cite Jira **Austin requirement sync** comments from that date as the backfill source
- When Austin reprioritizes, **replace the table** — do not append stale priorities

Legacy heading `## Deployment plan (Austin)` in older files is the same section — rename when editing.

---

## Feature delivery tracker

```markdown
## Feature delivery tracker

*Synced from [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) on YYYY-MM-DD (live).*

*Deploy packages = Salesforce changesets (Forward + Rollback + optional Settings per feature).*

### [LNI-#### — Epic title](https://datavant.atlassian.net/browse/LNI-####)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-####](...) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#220)</li><li><strong>Packages:</strong> Forward ✓ · Rollback ✓ · Settings —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> Tested</li><li><strong>UAT sandbox:</strong> Upload in progress</li></ul> | Complete UAT package upload; get wordings approved |
```

One `### Epic` subsection per **active epic** under DVI-1086 (status In Progress or UAT). Table rows = **open stories** (`statusCategory != Done`) under that epic.

### Column rules

| Column | Rule |
| --- | --- |
| **Story** | Link `[LNI-####](https://datavant.atlassian.net/browse/LNI-####)` + short summary if space allows |
| **Assignee** | First name from Jira (`Michael`, `Sarah`) or `—` |
| **Jira status** | Live status name (In Progress, Code Review, QA, UAT, etc.) |
| **Delivery gates** | One cell, HTML `<ul><li>` bullets — **PR**, **Packages** (Forward · Rollback · Settings), **Wordings**, **PD sandbox**, **UAT sandbox**. See [jira-sync.md](jira-sync.md) for PR/CS parsing. |
| **Next step** | One line; prefix `**Update YYYY-MM-DD:**` for standup deltas |

Legacy wide tables (separate PR / packages / wordings / sandbox columns) are still accepted; the Teams card script merges them automatically.

### Open subtasks (below each epic table)

When open subtasks exist under in-progress stories in that epic:

```markdown
*Open subtasks*

| Sub-task | Assignee | Status | Notes |
| --- | --- | --- | --- |
| [LNI-####](...) | Michael | In Progress | ... |
```

Include only subtasks with `status != Done`. **Exclude** subtasks assigned to **Youssef Yahia** (off project — legacy Jira items). Omit subsection when none remain after filtering.

### UAT-ready count

A story counts **UAT-ready** when all of:
- PR merged or no open PR (code complete)
- Feature + Rollback CS validated on pddev
- Properties CS validated on pddev (or N/A)
- PATTERNDATA wordings approved
- UAT sandbox column = `Validated`

Use for Path to UAT progress line: `**N/M features UAT-ready**`.

---

## Team focus (Michael · Sarah · Islam)

```markdown
## Team focus

| Member | Focus |
| --- | --- |
| **Michael** | [LNI-3223](...) AutoPay refactor; [LNI-3137](...) UAT CS upload — from Jira |
| **Sarah** | [LNI-3224](...) SAML SSO provisioning — from Jira |
| **Islam** | PD sandbox testing — [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare (Sarah's implementation) |
```

| Member | Source |
| --- | --- |
| **Michael** | Jira: all open stories/subtasks assigned to Michael Girgis |
| **Sarah** | Jira: all open stories/subtasks assigned to Sarah Hassaan |
| **Islam** | **Standup transcript** when Islam is mentioned; **default (no standup):** testing **RequestShare** [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) on pddev — feature implemented by Sarah |
| **Youssef** | **Never include** — off project; exclude his Jira assignee rows and subtasks |

Standing note (assign to **Hamed** or **Nabawy** in Risks mitigations when still open): **Follow up with Austin on Islam's Jira access**.

---

## Path to UAT & Production

```markdown
## Path to UAT & Production

**UAT-ready progress:** N/M features UAT-ready (see Feature delivery tracker)

### To reach UAT sandbox (target 2026-08-31)

- [ ] All in-scope stories finalized/refactored on **pddev**
- [ ] Each feature: **Forward + Rollback** deploy packages built (Settings package if needed)
- [ ] Each package uploaded and **tested on pddev**, then promoted to **UAT sandbox** (one feature at a time)
- [ ] **Client wordings (PATTERNDATA)** approved and attached to each package
- [ ] Code review complete — pull request merged for each feature

### To reach Production (target 2026-09-30)

- [ ] UAT validation complete for every feature
- [ ] Austin / client sign-off on UAT completion (per current deployment plan)
- [ ] Production deploy packages built per feature (same 3-pack pattern)
- [ ] Production release + smoke test
```

Check boxes reflect gate completion (checked when all tracker rows satisfy that gate, or standup confirms).

---

## Risks & challenges

Numbered table. Each risk: **condition → consequence**. Mitigation as `<ul><li>` list. Severities: High / Medium / Low.

**Maintain exactly these two standing risks** unless the user explicitly adds or replaces rows:

| # | Risk | Severity |
| --- | --- | --- |
| 1 | **Islam Jira access** — cannot log defects or update Jira; QA progress invisible in tracker | Medium |
| 2 | **Client wordings (PATTERNDATA) pending** — blocks deploy package finalization and UAT promotion | Low |

Mitigation owners: **Hamed / Nabawy** escalate to **Austin** where noted. Do **not** reintroduce wave-based mitigations.

**Do not add** retired risks (SSO metadata, webhook dependency, manual CS steps, feature-by-feature coordination) unless the user asks to expand the table.

---

## Transcript → section mapping

| Transcript topic | Where it goes |
|------------------|---------------|
| Deployment order / next feature / scope cut / next-up after wrap-up | **Daily update from Austin** + Status at a glance Forecast |
| Approved Fee overhaul / PCI cart / account flag | **Daily update from Austin** + tracker Next step |
| Date slip or new target | Status at a glance Forecast + Path to UAT targets |
| Story/subtask progress | Feature delivery tracker Next step + Status at a glance |
| PR / changeset / deploy | Feature delivery tracker columns + Path to UAT |
| Islam QA / testing | Team focus (Islam row) only — not a Path to UAT gate |
| Austin / Jira access | Risks #1 mitigations → **Hamed** or **Nabawy** |
| PATTERNDATA wordings | Feature delivery tracker wordings column + Risks #2 |
| Assigned next steps | Tracker **Next step**, Status at a glance, or Risks mitigations |
| Teams posting cadence | Post Adaptive Card via `TEAMS_WEBHOOK_URL` (not in the progress doc itself) |

---

## Worked example (feature tracker row)

Payment Management with partial CS progress:

```markdown
### [LNI-2309 — Payment Management](https://datavant.atlassian.net/browse/LNI-2309)

| Story | Assignee | Jira status | PR status | Changesets | PATTERNDATA wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) | Michael | In Progress | In progress (#220) | Feature ✓ · Rollback ✓ · Properties ✓ | Pending approval | Validated | In progress | **Update 2026-08-19:** Upload final apex CS to UAT; wordings pending |

*Open subtasks*

| Sub-task | Assignee | Status | Notes |
| --- | --- | --- | --- |
| [LNI-3238](https://datavant.atlassian.net/browse/LNI-3238) | — | In Progress | UI/UX Design — Payment Management Page |
```
