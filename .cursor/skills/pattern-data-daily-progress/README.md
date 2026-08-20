# Pattern Data Daily Progress

Build or update the Pattern Data delivery progress report from ChartSwap standup transcripts, **Austin engineering-manager meeting transcripts**, and live Datavant Jira on feature DVI-1086.

## Use Cases

- **Daily progress report** — Create or update today's `pattern-data-delivery-progress-YYYY-MM-DD.md`
- **Standup sync** — Extract standup docx, sync Jira on DVI-1086, update all report sections
- **Austin meeting sync** — Update deployment plan, dates, and scope from Austin meeting transcript
- **Bootstrap new day** — Copy prior day's report and update header/sync dates
- **Testing alignment** — Optionally sync `Testing Updates.md` after progress update

## How to Use

1. **Run daily sync**: *"Update today's progress report"* or *"Standup sync"*
2. **After Austin meeting**: *"Sync from Austin meeting transcript"* — attach or reference `Pattern-Data-Austin-YYYY-MM-DD.docx`
3. **Bootstrap today**: *"Create today's pattern-data-delivery-progress file"*
4. **With transcript**: Attach or reference standup or Austin meeting `.docx`
5. Invoke from chat: `/pattern-data-daily-progress` (or ask for a daily progress update)

## Workflow

1. Determine today's date and bootstrap the progress file (copy prior day or open existing)
2. Extract standup and/or Austin meeting transcript via `scripts/extract_standup.py`
3. Update **Deployment plan (Austin)** when Austin transcript is available
4. Sync DVI-1086 hierarchy from Datavant Jira (epics → stories → subtasks)
5. Parse story comments for PR and changeset status
6. Extract Islam focus from standup (default: RequestShare / LNI-3763 testing); exclude Youssef legacy subtasks
7. Update report sections per template
8. Compute Path to UAT/Prod progress (N/M features UAT-ready)
9. Extract action items and append **Standup action items** table as the last section
10. Optionally sync `Testing Updates.md`
11. Delete temp files and remind user to post full `.md` to Teams

## Features

### Transcript extraction
- Arabic/English mixed `.docx` transcripts (standup + Austin meetings)
- `scripts/extract_standup.py` writes UTF-8 output (avoids Windows console encoding issues)

### Austin deployment plan
- Engineering manager **Austin** sets feature promotion order — may change frequently
- **Deployment plan (Austin)** section updated from meeting transcripts
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
| `Transcript/Austin Meeting/Pattern-Data-Austin-*.docx` | Austin engineering-manager meeting |
| `Testing Updates.md` | Testing tracker to align (optional) |
| Jira feature DVI-1086 | Story/subtask status source of truth |

## Skill Info

| Field | Value |
|-------|-------|
| **Skill Name** | `pattern-data-daily-progress` |
| **Location** | `.cursor/skills/pattern-data-daily-progress/` |
| **Source** | Project (local) |
| **Installed** | 2026-06-09 |
| **Revamped** | 2026-08-19 — DVI-1086 feature-delivery model; 2026-08-20 — Austin plan, no waves |
