# AGENTS — Pattern Data Delivery Plan

AI workspace for tracking and reporting Pattern Data integration delivery progress. The agent maintains dated progress markdown, syncs with live Jira, extracts standup and Austin meeting transcripts, and aligns testing status — using project skills and Atlassian MCP integrations.

## Project Identity

| Field | Value |
|-------|-------|
| **Client** | Ontellus LLC |
| **Product** | ChartSwap — record ordering, tracking, and delivery portal |
| **Active feature** | [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) — PatternData SSO |
| **Go-live goal** | UAT sandbox **2026-08-31** · Production **2026-09-30** |
| **Jira cloud ID** | `eade365b-968b-4bd2-ad93-66539cfaeb93` (datavant.atlassian.net) |
| **Engineering manager** | **Austin** — sets deployment order and scope; plan may change frequently |
| **Delivery focus** | PD sandbox finalize → UAT sandbox (feature-by-feature, Austin-directed) → Production |
| **Historical epic** | [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) — prior Ontellus tracker (not synced) |

## Context Sources

Read these on demand when a task requires deeper context. Do not load them all preemptively.

| Path | Purpose |
|------|---------|
| `Daily Progress/pattern-data-delivery-progress-YYYY-MM-DD.md` | Dated delivery progress report (primary deliverable) |
| `Transcript/ChartSwap Daily Stand up/ChartSwap-Daily-Stand-up-YYYY-MM-DD.docx` | Daily standup transcript source |
| `Transcript/PDReviewWithAustin/PDReviewWithAustin-YYYY-MM-DD` | PD Review with Austin — primary Austin-class source (plain text or `.docx`) |
| `Transcript/Austin Meeting/Pattern-Data-Austin-YYYY-MM-DD.docx` | Shorter Austin engineering-manager meeting — deployment plan and dates |
| `Daily Actions/daily-actions-YYYY-MM-DD.md` | Standup action items (optional) |
| `Testing Updates.md` | Live testing tracker — sync after progress updates |
| `Daily TimeLog/Daily-Time-Log-YYYY-MM-DD.md` | OC subtask worklog summary for a calendar day |
| `Daily TimeLog/emails-YYYY-MM-DD/*.eml` | Per-assignee time log email drafts (see send-daily-timelog skill) |
| `.cursor/skills/pattern-data-daily-progress/references/document-template.md` | Report section templates and formatting rules |
| `.cursor/skills/pattern-data-daily-progress/references/jira-sync.md` | Datavant DVI-1086 JQL and PR/changeset parsing |
| `.cursor/skills/pattern-data-daily-progress/references/salesforce-deploy.md` | Changeset 3-pack rules and sandbox gates |
| `.cursor/skills/pattern-data-daily-progress/references/teams-post.md` | Lokka / Graph post of the progress `.md` to Teams |
| `.cursor/skills/pattern-data-daily-progress/references/automation-prompt.md` | Weekday-morning Cursor Automation prompt |
| `.cursor/skills/daily-time-log/references/document-template.md` | Daily time log table layout and 1d = 7h rules |
| `.cursor/skills/send-daily-timelog/references/recipient-map.md` | Integrant email addresses for time log reminders |
| `.cursor/skills/daily-actions/references/document-template.md` | Daily actions table layout, owners, categories |
| `.cursor/skills/daily-actions/references/project-profiles/pattern-data.md` | Pattern Data standup owners and category columns |

## Key Conventions

- **Jira is source of truth** for feature delivery — re-fetch DVI-1086 hierarchy (LNI epics → stories → subtasks) before each progress update.
- **Team focus:** Michael and Sarah from Jira assignees; Islam from standup (default: **RequestShare / LNI-3763** testing on pddev). **Exclude Youssef Yahia** — off project; legacy Jira subtasks are ignored.
- **Changesets:** each feature needs Feature + Rollback CS (+ optional Properties CS); validate on target sandbox; PATTERNDATA wordings must be approved before attach.
- **Austin (engineering manager)** sets deployment priority — update **Deployment plan (Austin)** from PD Review or Austin meeting transcript when provided; no wave-based release language.
- **UAT promotion** is feature-by-feature per Austin's plan, not one mega-changeset.
- **Teams** — after committing today's progress to **main**, post the `.md` via **Lokka-Microsoft-365** (sign in via Lokka connections; destination `TEAMS_CHANNEL_ID`). See `teams-post.md`. Do not open a PR for the daily report.
- **Delete temp files** — remove `_standup_extract.txt` and other extraction artifacts when done.

---

<skills_system priority="1">

## Available Skills

<!-- SKILLS_TABLE_START -->
<usage>
When users ask you to perform tasks, check if any of the available skills below can help complete the task more effectively. Skills provide specialized capabilities and domain knowledge.

How to use skills:
- Invoke from the **`/` menu** in chat (each skill has `disable-model-invocation: true` for explicit user trigger)
- Or ask in natural language — the agent loads matching skills from `.cursor/skills/<name>/SKILL.md`
- Read bundled `references/` and run `scripts/` relative to each skill directory when the workflow calls for them

Usage notes:
- Only use skills listed in <available_skills> below
- Do not load a skill that is already in your context
- Each skill invocation is stateless
</usage>

<available_skills>

<skill>
<name>daily-actions</name>
<description>>-</description>
<location>project</location>
</skill>

<skill>
<name>daily-time-log</name>
<description>>-</description>
<location>project</location>
</skill>

<skill>
<name>pattern-data-daily-progress</name>
<description>>-</description>
<location>project</location>
</skill>

<skill>
<name>pmo-bug-closure-analysis</name>
<description>>-</description>
<location>project</location>
</skill>

<skill>
<name>send-daily-timelog</name>
<description>>-</description>
<location>project</location>
</skill>

</available_skills>
<!-- SKILLS_TABLE_END -->

</skills_system>
