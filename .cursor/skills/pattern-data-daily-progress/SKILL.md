---
name: pattern-data-daily-progress
description: >-
  Build or update the Pattern Data daily delivery progress report from ChartSwap
  standup transcripts, Austin engineering-manager meeting transcripts, and live
  Datavant Jira on feature DVI-1086. Use when the user asks for a daily progress
  report, standup sync, Austin meeting sync, pattern-data-daily-progress update,
  PD delivery plan update, or to copy/create today's progress markdown from a docx.
disable-model-invocation: true
---

# Pattern Data — Daily Progress Report

Build or update the dated delivery progress markdown from standup transcripts, **Austin meeting transcripts**, and live Jira on feature [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086).

## Project paths

- `Daily Progress/pattern-data-delivery-progress-YYYY-MM-DD.md` — primary deliverable
- `Transcript/ChartSwap Daily Stand up/ChartSwap-Daily-Stand-up-YYYY-MM-DD.docx` — daily standup transcript
- `Transcript/Austin Meeting/Pattern-Data-Austin-YYYY-MM-DD.docx` — Austin engineering-manager meeting transcript (deployment plan, scope, dates)
- `Daily Actions/daily-actions-YYYY-MM-DD.md` — optional separate action tracker (not used as source for the progress report table)
- `Testing Updates.md` — optional sync after progress update

## Engineering manager — Austin

**Austin** is the engineering manager and **owns deployment order and scope**. He may change the plan or next deployment frequently. When the user provides an Austin meeting transcript:

1. Extract **deployment priority**, **scope in/out**, **date changes**, and **implementation direction**
2. Update **Deployment plan (Austin)**, **Status at a glance** (Forecast / Notes), **Feature delivery tracker** Next step, and **Path to UAT** targets if Austin changed them
3. Add Austin-driven action items to **Standup action items** (or a dated note in that section) with owner **Austin**, **Team**, **Hamed**, or **Nabawy** as appropriate

**Do not use wave / Wave 1 / Wave 2 language** — retired delivery model. Use **feature-by-feature** promotion per Austin's current plan.

## Workflow

Copy this checklist and track progress:

```
- [ ] 1. Determine today's date (YYYY-MM-DD)
- [ ] 2. Bootstrap file (copy prior day OR open today's file)
- [ ] 3. Extract standup transcript (if provided)
- [ ] 3b. Extract Austin meeting transcript (if provided) — update deployment plan first
- [ ] 4. Sync Datavant Jira: DVI-1086 → epics → open stories → open subtasks (exclude Youssef Yahia)
- [ ] 5. Parse story comments for PR + changeset status
- [ ] 6. Extract Islam focus from standup (default: LNI-3763 RequestShare testing); exclude Youssef subtasks
- [ ] 7. Update all report sections per template (Austin plan overrides static assumptions)
- [ ] 8. Compute Path to UAT/Prod checklist counts (N/M features UAT-ready)
- [ ] 9. Replace Standup action items table at end of file
- [ ] 10. Optionally sync Testing Updates.md
- [ ] 11. Delete temp extract files
- [ ] 12. Remind user to post full .md to Teams after standup
```

### Step 1 — Bootstrap

**Target date:** use **today** (current calendar day) unless the user invokes `/pattern-data-daily-progress YYYY-MM-DD` or names another date in chat.

**If today's file does not exist:** copy the most recent `Daily Progress/pattern-data-delivery-progress-*.md` and rename to today's date. Update only:
- `**As of:**` header
- Jira sync date line in Feature delivery tracker
- Standup / Austin plan input dates

Leave historical event dates unchanged (e.g. when a CS was uploaded).

**If today's file exists:** update in place from standup + Austin meeting + Jira.

### Step 2 — Extract transcripts

Transcripts are Arabic/English mixed `.docx` files. Run from the skill directory (write UTF-8 temp file; do not print to console on Windows):

```bash
python scripts/extract_standup.py "Transcript/ChartSwap Daily Stand up/ChartSwap-Daily-Stand-up-YYYY-MM-DD.docx" -o _standup_extract.txt
python scripts/extract_standup.py "Transcript/Austin Meeting/Pattern-Data-Austin-YYYY-MM-DD.docx" -o _austin_extract.txt
```

Delete `_standup_extract.txt` and `_austin_extract.txt` when done.

**Priority when both exist:** Austin meeting sets **deployment plan and dates**; standup sets **day-to-day dev/QA progress** and action items.

### Step 3 — Sync Datavant Jira

Sync **before** editing the report. See [references/jira-sync.md](references/jira-sync.md) for JQL chain, cloud ID, PR/changeset parsing, and assignee mapping.

Also see [references/salesforce-deploy.md](references/salesforce-deploy.md) for changeset validation rules.

### Step 4 — Islam focus

**Islam** has no Jira account yet. Populate his Team focus row from the **standup transcript** when Islam is mentioned. If no standup or Islam not mentioned, use the standing default: **PD sandbox testing of [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare** (implemented by Sarah).

Standing item: **Hamed** or **Nabawy** follows up with **Austin on Islam's Jira access** (Risks + action items when still open).

### Step 4b — Exclude Youssef

**Youssef Yahia is off the project.** Do not list subtasks, stories, or Team focus rows for his Jira assignments — they are legacy. Filter out on every sync (see [references/jira-sync.md](references/jira-sync.md)).

### Step 5 — Extract action items

From **standup** and/or **Austin meeting** transcripts, capture only **assigned or agreed next steps**. Do **not** copy from `Daily Actions/daily-actions-*.md`.

**Include:** explicit assignments, blockers with owner, deadlines, deployment decisions, process commitments.

**Exclude:** pure status with no follow-up, items done in the meeting, leadership context-only decisions.

**Owners:** Michael, Sarah, Islam, Team, **Austin**, **Hamed**, **Nabawy** (PM — client escalations, access, delivery timeline). Do **not** use Salah as an action owner.

Use [references/document-template.md](references/document-template.md) for table format. Write for a **manager audience** — plain language, filled risk mitigations, deploy package glossary in each report. **Replace** the section on each sync.

### Step 6 — Update sections

Apply standup + Austin deltas to the progress report. See [references/document-template.md](references/document-template.md) for section structure, transcript mapping, and worked examples.

After all other sections are updated, add or replace **## Standup action items** as the **last section**.

### Step 7 — Domain decisions

Apply standing business rules. See [references/domain-decisions.md](references/domain-decisions.md).

### Step 8 — Testing Updates.md (optional)

Align phase summary with today's progress. Set `Last updated` and `Updated by: Standup sync (pattern-data-delivery-progress-YYYY-MM-DD)`.

### Step 9 — Post-update

Remind user: Amr requested the **full progress .md** posted to Teams after standup (with source file attached). This is manual.

## When done

Reply with:

1. The file path created or updated
2. **Status at a glance** — phase row summary (what changed today)
3. **Deployment plan (Austin)** — current priority if Austin transcript was applied
4. Feature tracker counts — stories in progress, ready-for-PR, UAT-ready (`N/M`)
5. Michael / Sarah / Islam focus one-liners
6. Path-to-UAT gate progress
7. Reminder to post the full progress `.md` to Teams after standup (Amr's request)
8. **Hamed / Nabawy:** Austin or Islam Jira access follow-up if still open

## Additional resources

- [references/document-template.md](references/document-template.md) — section templates, transcript mapping, worked examples
- [references/jira-sync.md](references/jira-sync.md) — Datavant JQL, DVI-1086 hierarchy, PR/CS parsing
- [references/salesforce-deploy.md](references/salesforce-deploy.md) — changeset 3-pack, sandbox gates, wordings
- [references/domain-decisions.md](references/domain-decisions.md) — delivery targets, Austin plan, team sources
