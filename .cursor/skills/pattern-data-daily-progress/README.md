# Pattern Data Daily Progress

Build or update the Pattern Data delivery progress report from ChartSwap standup transcripts, **Austin-class transcripts** (PD Review with Austin or Austin meeting), and live Datavant Jira on feature DVI-1086.

## Use Cases

- **Daily progress report** — Create or update today's `pattern-data-delivery-progress-YYYY-MM-DD.md`
- **Standup sync** — Extract standup docx, sync Jira on DVI-1086, update all report sections
- **Austin meeting / PD Review sync** — Update deployment plan, dates, and scope from Austin-class transcript
- **Bootstrap new day** — Copy prior day's report and update header/sync dates
- **Testing alignment** — Optionally sync `Testing Updates.md` after progress update
- **Weekday morning job** — Jira-only report + PR + Teams Adaptive Card (see below)

## How to Use

1. **Run daily sync**: *"Update today's progress report"* or *"Standup sync"*
2. **After PD Review or Austin meeting**: *"Sync from Austin transcript"* — attach or reference `PDReviewWithAustin-YYYY-MM-DD` or `Pattern-Data-Austin-YYYY-MM-DD.docx`
3. **Bootstrap today**: *"Create today's pattern-data-delivery-progress file"*
4. **With transcript**: Attach or reference standup `.docx` or Austin-class file (plain text or `.docx`)
5. Invoke from chat: `/pattern-data-daily-progress` (or ask for a daily progress update)

## Workflow

1. Determine today's date and bootstrap the progress file (copy prior day or open existing)
2. Extract standup and/or Austin-class transcript via `scripts/extract_standup.py` (`.docx` or plain text)
3. Update **Deployment plan (Austin)** when a PD Review or Austin meeting transcript is available
4. Sync DVI-1086 hierarchy from Datavant Jira (epics → stories → subtasks)
5. Parse story comments for PR and changeset status
6. Extract Islam focus from standup (default: RequestShare / LNI-3763 testing); exclude Youssef legacy subtasks
7. Update report sections per template
8. Compute Path to UAT/Prod progress (N/M features UAT-ready)
9. Extract action items and append **Standup action items** table as the last section
10. Optionally sync `Testing Updates.md`
11. Delete temp files
12. `git fetch origin` before opening a PR; rebase onto the default branch if needed
13. Post a Teams Adaptive Card (summary + full report text) via `scripts/post_progress_to_teams.py` when `TEAMS_WEBHOOK_URL` is set

## Features

### Transcript extraction
- Arabic/English mixed `.docx` (standup + Austin meeting) and **plain-text PD Review** files (often no extension)
- `scripts/extract_standup.py` writes UTF-8 output (avoids Windows console encoding issues)

### Austin deployment plan
- Engineering manager **Austin** sets feature promotion order — may change frequently
- **Deployment plan (Austin)** section updated from PD Review or Austin meeting transcripts
- No wave-based release language — feature-by-feature per Austin's current plan

### Jira Integration (Datavant)
- Queries [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) → LNI epics → stories → open subtasks via Atlassian MCP
- Parses story comments for Bitbucket PRs and Salesforce changeset URLs
- Michael and Sarah auto-populated from Jira assignees; Islam from standup (default: RequestShare testing on LNI-3763)
- Youssef Yahia assignments excluded — off project, legacy Jira items

### Report Sections
- Status at a glance (PD Sandbox finalize, UAT Sandbox deploy, Production)
- **Deployment plan (Austin)** — current promotion priority
- Feature delivery tracker (per epic: PR, changesets, wordings, sandbox columns)
- Team focus (Michael · Sarah · Islam); PM actions → Hamed / Nabawy
- Path to UAT & Production (checklist + N/M progress)
- Risks & challenges (**two standing risks** — Islam Jira access, client wordings)
- Standup action items (Owner × Action — **open actions only**)

### MCP Tools Used
- `searchJiraIssuesUsingJql` — fetch DVI-1086 hierarchy
- `getJiraIssue` — story comments for PR/changeset parsing

## Configuration Sources

| File | What It Provides |
|------|-----------------|
| `Daily Progress/pattern-data-delivery-progress-*.md` | Prior report to bootstrap or update |
| `Transcript/ChartSwap Daily Stand up/ChartSwap-Daily-Stand-up-*.docx` | Daily standup transcript |
| `Transcript/PDReviewWithAustin/PDReviewWithAustin-*` | PD Review with Austin (plain text or `.docx`) |
| `Transcript/Austin Meeting/Pattern-Data-Austin-*.docx` | Shorter Austin engineering-manager meeting |
| `Testing Updates.md` | Testing tracker to align (optional) |
| Jira feature DVI-1086 | Story/subtask status source of truth |

## Weekday morning automation → Teams

A Cursor Automation can run this skill on a weekday morning from **Jira only** (skip missing transcripts), open a PR, and POST a summary Adaptive Card to Power Automate → a Teams channel.

| Piece | Where |
|-------|--------|
| Power Automate + secret | [references/teams-post.md](references/teams-post.md) |
| Automation prompt | [references/automation-prompt.md](references/automation-prompt.md) |
| Post script | [scripts/post_progress_to_teams.py](scripts/post_progress_to_teams.py) |

Create the live job in the **Agents Window** (`/automate`) or at [cursor.com/automations](https://cursor.com/automations). Store `TEAMS_WEBHOOK_URL` as a Cloud Agent secret — never commit it.

## Skill Info

| Field | Value |
|-------|-------|
| **Skill Name** | `pattern-data-daily-progress` |
| **Location** | `.cursor/skills/pattern-data-daily-progress/` |
| **Source** | Project (local) |
| **Installed** | 2026-06-09 |
| **Revamped** | 2026-08-19 — DVI-1086 feature-delivery model; 2026-08-20 — Austin plan, no waves; 2026-08-23 — PD Review with Austin source |
