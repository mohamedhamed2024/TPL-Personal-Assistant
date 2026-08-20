# Document template — Pattern Data daily progress

## File naming

- Progress: `Daily Progress/pattern-data-delivery-progress-YYYY-MM-DD.md`
- Standup transcript: `Transcript/ChartSwap Daily Stand up/ChartSwap-Daily-Stand-up-YYYY-MM-DD.docx`
- Austin meeting transcript: `Transcript/Austin Meeting/Pattern-Data-Austin-YYYY-MM-DD.docx`
- Actions: `Daily Actions/daily-actions-YYYY-MM-DD.md` (optional — not used as source for the progress report)

## Header

```markdown
# Pattern Data — delivery progress

**Feature:** [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) · **As of:** YYYY-MM-DD  
**Targets:** UAT sandbox **2026-08-31** · Production **2026-09-30**

## How to read this report

*Audience: delivery managers and stakeholders.*

| If you see… | It means… |
| --- | --- |
| **PD Sandbox finalize** | Dev team finishing and testing features on the Pattern Data development sandbox (pddev) |
| **UAT Sandbox deploy** | Approved features being moved **one at a time** to the pre-production UAT environment |
| **Deploy packages** | Salesforce outbound **changesets** — bundled code/config uploaded between environments (Forward + Rollback + optional Settings per feature) |
| **UAT-ready (N/M)** | **N** of **M** features have passed all gates to promote to UAT (code merged, packages validated, client wordings approved) |
| **Pending approval** (wordings) | Client copy/labels not yet signed off — blocks attaching text to the deploy package |
| **Deployment plan (Austin)** | Current feature promotion order and scope — set by engineering manager Austin; may change after each Austin meeting |
```

Include the **How to read this report** block in every progress file (after the header, before Status at a glance). Do **not** link to `.cursor/` paths in the deliverable — keep glossary inline only.

**Do not use wave / Wave 1 / Wave 2 language** anywhere in progress reports — retired delivery model.

## What to update from transcripts

| Section | Update when |
|---------|-------------|
| **Deployment plan (Austin)** | **Austin meeting transcript** — priority order, scope in/out, next environment target; replace table when Austin changes plan |
| **Status at a glance** — all phase rows | Standup **or** Austin meeting: closed subtasks, CS uploads, deploy decisions, **Forecast slips**. Do **not** accumulate historical bullets across days. |
| **Feature delivery tracker** | Re-sync from Jira before editing; append `**Update YYYY-MM-DD:**` in Next step when standup or Austin adds detail |
| **Team focus** | Michael/Sarah from Jira assignees; **Islam** from standup (default: RequestShare / LNI-3763); **exclude Youssef Yahia** subtasks |
| **Path to UAT & Production** | Recompute `N/M features UAT-ready` from tracker; adjust target dates only when **Austin** or standup confirms a slip |
| **Risks & challenges** | Keep the **two standing risks** unless user adds new ones; condition → consequence → mitigation format |
| **Standup action items** | Replace entirely from today's standup and/or Austin meeting (last section) |

**Do not include:** Open delivery blockers (OC bugs), Client release plan, Flow to be retested, Pre-UAT provider matrix, or "Other in-flight work".

**Do not edit** the plan file if user attached one for reference only.

## Writing style — manager audience

The primary readers are **delivery managers**, not Salesforce developers. Apply these rules in every progress file:

- **Spell out or explain jargon** on first use in each report (see *How to read this report* block after the header).
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
- **Forecast** — bold date; only change when **Austin meeting** or standup calls a slip

---

## Deployment plan (Austin)

Engineering manager **Austin** sets which features deploy next and may change the plan frequently. Place this section **after Status at a glance**, before Feature delivery tracker.

```markdown
## Deployment plan (Austin)

*Engineering manager **Austin** sets deployment order and scope — this may change after each Austin meeting. Update this block from the latest Austin meeting transcript when provided.*

| Priority | Feature / story | Environment | Status |
| --- | --- | --- | --- |
| 1 | [LNI-3137](...) Payment Management | UAT sandbox | Upload in progress |
| 2 | [LNI-3223](...) AutoPay | pddev | Next per Austin — TBD |

*Last plan input:* [Pattern-Data-Austin — YYYY-MM-DD](../Transcript/Austin%20Meeting/Pattern-Data-Austin-YYYY-MM-DD.docx)*
```

- **Priority 1** = next feature Austin directed for promotion or active UAT work
- Remaining rows = queue or "TBD until Austin meeting"
- If no Austin transcript: carry forward prior day's plan or infer from Jira UAT column + standup; note `*Last plan input:* baseline from Jira sync YYYY-MM-DD — no Austin meeting transcript on file yet.*`
- When Austin reprioritizes, **replace the table** — do not append stale priorities

---

## Feature delivery tracker

```markdown
## Feature delivery tracker

*Synced from [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) on YYYY-MM-DD (live).*

*Deploy packages = Salesforce changesets (Forward + Rollback + optional Settings per feature).*

### [LNI-#### — Epic title](https://datavant.atlassian.net/browse/LNI-####)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-####](...) | Michael | In Progress | In review (#220) | Forward ✓ · Rollback ✓ · Settings — | Pending approval | Tested | Upload in progress | Complete UAT package upload; get wordings approved |
```

One `### Epic` subsection per **active epic** under DVI-1086 (status In Progress or UAT). Table rows = **open stories** (`statusCategory != Done`) under that epic.

### Column rules

| Column | Rule |
| --- | --- |
| **Story** | Link `[LNI-####](https://datavant.atlassian.net/browse/LNI-####)` + short summary if space allows |
| **Assignee** | First name from Jira (`Michael`, `Sarah`) or `—` |
| **Jira status** | Live status name (In Progress, Code Review, QA, UAT, etc.) |
| **Code review (PR)** | Parse story comments — see [jira-sync.md](jira-sync.md). No open PR → **`Ready — finalize code review & deploy packages`** |
| **Deploy packages** | Three checks: `Forward ✓/Pending · Rollback ✓/Pending · Settings ✓/Pending/—` (Settings optional — show `—` when N/A). *Alias for devs: Feature / Rollback / Properties.* |
| **Client wordings** | `Pending approval` or `Approved — attach to package` (PATTERNDATA labels) |
| **PD sandbox** | `Not deployed` / `In progress` / `Tested` on **pddev** |
| **UAT sandbox** | `Not deployed` / `In progress` / `Tested` |
| **Next step** | One line; prefix `**Update YYYY-MM-DD:**` for standup deltas |

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

Standing note (assign to **Hamed** or **Nabawy** in action items when still open): **Follow up with Austin on Islam's Jira access**.

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
| Deployment order / next feature / scope cut | **Deployment plan (Austin)** + Status at a glance Forecast |
| Date slip or new target | Status at a glance Forecast + Path to UAT targets |
| Story/subtask progress | Feature delivery tracker Next step + Status at a glance |
| PR / changeset / deploy | Feature delivery tracker columns + Path to UAT |
| Islam QA / testing | Team focus (Islam row) only — not a Path to UAT gate |
| Austin / Jira access | Risks #1 + action items → **Hamed** or **Nabawy** |
| PATTERNDATA wordings | Feature delivery tracker wordings column + Risks #2 |
| Assigned next steps | **Standup action items** (last section) |
| Teams posting cadence | Remind user (not in doc) |

---

## Standup action items (last section)

Always the **final section** in the progress file. Extract from **today's standup transcript only** — not from `Daily Actions/` files or prior progress reports. Replace entirely on each sync.

```markdown
---

## Standup action items (YYYY-MM-DD)

*From [ChartSwap Daily Stand-up — YYYY-MM-DD](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-YYYY-MM-DD.docx).*

| Owner | Action |
| --- | --- |
| **Michael** | Finalize **PR #220** and upload apex CS to UAT for [LNI-3137](...) |
| **Sarah** | Continue **SAML SSO** refactor on pddev |
| **Islam** | Test **RequestShare** ([LNI-3763](https://datavant.atlassian.net/browse/LNI-3763)) on pddev — Sarah's implementation |
```

### Table rules

| Column | Rule |
| --- | --- |
| **Owner** | **Michael**, **Sarah**, **Islam**, **Team**, **Hamed**, or **Nabawy** (PM — client escalations, access, timeline) |
| **Action** | One clear outcome per row; bold key terms; avoid dev jargon without context |

- **Open actions only** — omit items completed in the meeting; put closures in Status at a glance *What's done* or tracker instead
- Link LNI keys: `[LNI-####](https://datavant.atlassian.net/browse/LNI-####)`
- Sort rows alphabetically by owner
- Omit section only when no standup transcript was available, or no open actions remain

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
