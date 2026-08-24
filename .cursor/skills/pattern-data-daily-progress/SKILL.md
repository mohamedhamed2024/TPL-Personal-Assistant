---
name: pattern-data-daily-progress
description: >-
  Build or update the Pattern Data daily delivery progress report from ChartSwap
  standup transcripts, Austin engineering-manager meetings, PD Review with Austin
  transcripts, and live Datavant Jira on feature DVI-1086. Use when the user asks
  for a daily progress report, standup sync, Austin meeting sync, PD Review sync,
  pattern-data-daily-progress update, PD delivery plan update, or to copy/create
  today's progress markdown from a transcript.
disable-model-invocation: true
---

# Pattern Data — Daily Progress Report

Build or update the dated delivery progress markdown from standup transcripts, **Austin-class transcripts** (Austin meeting **or** PD Review with Austin), and live Jira on feature [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086).

## Project paths

- `Daily Progress/pattern-data-delivery-progress-YYYY-MM-DD.md` — primary deliverable
- `Transcript/ChartSwap Daily Stand up/ChartSwap-Daily-Stand-up-YYYY-MM-DD.docx` — daily standup transcript
- `Transcript/PDReviewWithAustin/PDReviewWithAustin-YYYY-MM-DD` — **PD Review with Austin** (primary Austin-class source; plain text, `.txt`, or `.docx`)
- `Transcript/Austin Meeting/Pattern-Data-Austin-YYYY-MM-DD.docx` — shorter Austin engineering-manager meeting (same class as PD Review)
- `Daily Actions/daily-actions-YYYY-MM-DD.md` — optional separate action tracker (not used as source for the progress report table)
- `Testing Updates.md` — optional sync after progress update

## Engineering manager — Austin

**Austin** is the engineering manager and **owns deployment order and scope**. He may change the plan or next deployment frequently.

**Austin-class transcripts** (treat the same; use the **latest dated** file):

| Source | Typical file | Use for |
| --- | --- | --- |
| **PD Review with Austin** | `Transcript/PDReviewWithAustin/PDReviewWithAustin-YYYY-MM-DD` | Long review — deployment order, scope, implementation direction, next-up work after wrap-up |
| **Austin meeting** | `Transcript/Austin Meeting/Pattern-Data-Austin-YYYY-MM-DD.docx` | Shorter EM meeting — same fields |

When either is provided:

1. Extract **deployment priority**, **scope in/out**, **date changes**, and **implementation direction**
2. Update **Deployment plan (Austin)**, **Status at a glance** (Forecast / Notes), **Feature delivery tracker** Next step, and **Path to UAT** targets if Austin changed them
3. Add Austin-driven action items to **Standup action items** (or a dated note in that section) with owner **Austin**, **Team**, **Hamed**, or **Nabawy** as appropriate
4. If the transcript **jumps timestamps** (e.g. 1 min → 1h23) or is otherwise incomplete, do **not** invent the missing middle. Note the gap in *Last plan input* and backfill only from Jira comments titled **Austin requirement sync** on that date whose `Call / source` is **PD Review**

**Do not use wave / Wave 1 / Wave 2 language** — retired delivery model. Use **feature-by-feature** promotion per Austin's current plan.

## Workflow

Copy this checklist and track progress:

```
- [ ] 1. Determine today's date (YYYY-MM-DD)
- [ ] 2. Bootstrap file (copy prior day OR open today's file)
- [ ] 3. Extract standup transcript (if provided)
- [ ] 3b. Extract Austin-class transcript (PD Review with Austin and/or Austin meeting) — update deployment plan first
- [ ] 4. Sync Datavant Jira: DVI-1086 → epics → open stories → open subtasks (exclude Youssef Yahia)
- [ ] 5. Parse story comments for PR + changeset status
- [ ] 6. Extract Islam focus from standup (default: LNI-3763 RequestShare testing); exclude Youssef subtasks
- [ ] 7. Update all report sections per template (Austin plan overrides static assumptions)
- [ ] 8. Compute Path to UAT/Prod checklist counts (N/M features UAT-ready)
- [ ] 9. Replace Standup action items table at end of file
- [ ] 10. Optionally sync Testing Updates.md
- [ ] 11. Delete temp extract files
- [ ] 12. git fetch origin before opening a PR (rebase onto default branch if needed; do not push to main)
- [ ] 13. Post Teams Adaptive Card (full report inlined) via post_progress_to_teams.py
```

### Step 1 — Bootstrap

**Target date:** use **today** (current calendar day) unless the user invokes `/pattern-data-daily-progress YYYY-MM-DD` or names another date in chat.

**Morning automation (Jira-only):** a weekday Cursor Automation may run before standup transcripts exist. If today's ChartSwap standup `.docx` and Austin-class transcript are missing, skip transcript extraction (checklist 3 / 3b). Keep Austin's last deployment plan. Do **not** invent standup action items. Default Islam to RequestShare / LNI-3763. Still bootstrap today's file and sync Jira. See [references/automation-prompt.md](references/automation-prompt.md).

**If today's file does not exist:** copy the most recent `Daily Progress/pattern-data-delivery-progress-*.md` and rename to today's date. Update only:
- `**As of:**` header
- Jira sync date line in Feature delivery tracker
- Standup / Austin plan input dates

Leave historical event dates unchanged (e.g. when a CS was uploaded).

**If today's file exists:** update in place from standup + Austin-class transcript + Jira.

### Step 2 — Extract transcripts

Transcripts may be Arabic/English mixed `.docx` **or** plain text (PD Review files often have **no extension**). Run from the skill directory (write UTF-8 temp file; do not print to console on Windows):

```bash
python scripts/extract_standup.py "Transcript/ChartSwap Daily Stand up/ChartSwap-Daily-Stand-up-YYYY-MM-DD.docx" -o _standup_extract.txt
python scripts/extract_standup.py "Transcript/PDReviewWithAustin/PDReviewWithAustin-YYYY-MM-DD" -o _austin_extract.txt
python scripts/extract_standup.py "Transcript/Austin Meeting/Pattern-Data-Austin-YYYY-MM-DD.docx" -o _austin_extract.txt
```

Prefer **PD Review with Austin** when both Austin-class files exist for the same date. Delete `_standup_extract.txt` and `_austin_extract.txt` when done.

**Priority when both standup and Austin-class exist:** Austin-class sets **deployment plan and dates**; standup sets **day-to-day dev/QA progress** and action items.

### Step 3 — Sync Datavant Jira

Sync **before** editing the report. See [references/jira-sync.md](references/jira-sync.md) for JQL chain, cloud ID, PR/changeset parsing, and assignee mapping.

Also see [references/salesforce-deploy.md](references/salesforce-deploy.md) for changeset validation rules.

### Step 4 — Islam focus

**Islam** has no Jira account yet. Populate his Team focus row from the **standup transcript** when Islam is mentioned. If no standup or Islam not mentioned, use the standing default: **PD sandbox testing of [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare** (implemented by Sarah).

Standing item: **Hamed** or **Nabawy** follows up with **Austin on Islam's Jira access** (Risks + action items when still open).

### Step 4b — Exclude Youssef

**Youssef Yahia is off the project.** Do not list subtasks, stories, or Team focus rows for his Jira assignments — they are legacy. Filter out on every sync (see [references/jira-sync.md](references/jira-sync.md)).

### Step 5 — Extract action items

From **standup** and/or **Austin-class** transcripts (PD Review or Austin meeting), capture only **assigned or agreed next steps**. Do **not** copy from `Daily Actions/daily-actions-*.md`.

**Include:** explicit assignments, blockers with owner, deadlines, deployment decisions, process commitments.

**Exclude:** pure status with no follow-up, items done in the meeting, leadership context-only decisions.

**Owners:** Michael, Sarah, Islam, Team, **Austin**, **Hamed**, **Nabawy** (PM — client escalations, access, delivery timeline). Do **not** use Salah as an action owner.

Use [references/document-template.md](references/document-template.md) for table format. Write for a **manager audience** — plain language, filled risk mitigations, deploy package glossary in each report. **Replace** the section on each sync.

### Step 6 — Update sections

Apply standup + Austin-class deltas to the progress report. See [references/document-template.md](references/document-template.md) for section structure, transcript mapping, and worked examples.

After all other sections are updated, add or replace **## Standup action items** as the **last section**.

### Step 7 — Domain decisions

Apply standing business rules. See [references/domain-decisions.md](references/domain-decisions.md).

### Step 8 — Testing Updates.md (optional)

Align phase summary with today's progress. Set `Last updated` and `Updated by: Standup sync (pattern-data-delivery-progress-YYYY-MM-DD)`.

### Step 9 — Fetch before PR

When opening a pull request (automation or when the user asks for a PR):

1. `git fetch origin` (or the remote that tracks the default branch)
2. Rebase the working branch onto the latest default branch if it has moved
3. Then open the PR

Do **not** push to the default branch. Do **not** force-push.

### Step 10 — Post-update

Amr requested the progress report in Teams.

**Cursor Automation / when `TEAMS_WEBHOOK_URL` is set:** after the markdown exists (and after the PR URL is known, if opening a PR), run:

```bash
python .cursor/skills/pattern-data-daily-progress/scripts/post_progress_to_teams.py --pr-url "<PR url if any>"
```

The Adaptive Card includes a summary **and** the full report text (markdown flattened; Teams flowbot cannot attach a file or render HTML). Never print or commit the webhook URL. Setup: [references/teams-post.md](references/teams-post.md).

**Interactive chat:** if the webhook is not configured, remind the user to post the **full progress `.md`** to Teams after standup (with source file attached).

## When done

Reply with:

1. The file path created or updated
2. **Status at a glance** — phase row summary (what changed today)
3. **Deployment plan (Austin)** — current priority if an Austin-class transcript was applied
4. Feature tracker counts — stories in progress, ready-for-PR, UAT-ready (`N/M`)
5. Michael / Sarah / Islam focus one-liners
6. Path-to-UAT gate progress
7. Teams: PR URL + whether `post_progress_to_teams.py` succeeded; otherwise remind the user to post the full `.md` to Teams (Amr's request)
8. **Hamed / Nabawy:** Austin or Islam Jira access follow-up if still open

## Additional resources

- [references/document-template.md](references/document-template.md) — section templates, transcript mapping, worked examples
- [references/jira-sync.md](references/jira-sync.md) — Datavant JQL, DVI-1086 hierarchy, PR/CS parsing
- [references/salesforce-deploy.md](references/salesforce-deploy.md) — changeset 3-pack, sandbox gates, wordings
- [references/domain-decisions.md](references/domain-decisions.md) — delivery targets, Austin plan, team sources
- [references/teams-post.md](references/teams-post.md) — Power Automate webhook and `TEAMS_WEBHOOK_URL`
- [references/automation-prompt.md](references/automation-prompt.md) — weekday-morning Cursor Automation prompt
- [scripts/post_progress_to_teams.py](scripts/post_progress_to_teams.py) — POST Adaptive Card summary to Teams
