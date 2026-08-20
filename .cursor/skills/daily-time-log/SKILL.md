---
name: daily-time-log
description: >-
  Build the OC project daily time log markdown from live Jira subtask worklogs.
  Use when the user asks for a daily time log, work log report, Daily-Time-Log
  update, yesterday's logged time on OC subtasks, time spent by assignee, or to
  create or refresh Daily-Time-Log-YYYY-MM-DD.md in Daily TimeLog.
disable-model-invocation: true
---

# OC Daily Time Log

Build `Daily TimeLog/Daily-Time-Log-YYYY-MM-DD.md` from live Jira worklogs on OC **Sub-task** issues.

## Project paths

- `Daily TimeLog/Daily-Time-Log-YYYY-MM-DD.md` — primary deliverable
- Jira cloud ID: `0ace3b78-4a29-418f-8997-c353db285ca8` (Ontellus; see `AGENTS.md`)

## Workflow

Copy this checklist and track progress:

```
- [ ] 1. Determine target date (default: yesterday)
- [ ] 2. Search Jira for OC subtasks with worklog on that date
- [ ] 3. Fetch worklogs and sum time per task (target date only)
- [ ] 4. Build totals-by-assignee and detail tables
- [ ] 5. Write or overwrite Daily-Time-Log-YYYY-MM-DD.md
```

### Step 1 — Target date

- **Default:** previous calendar day relative to when the skill runs (`YYYY-MM-DD`).
- **Slash override:** if invoked via `/daily-time-log YYYY-MM-DD`, use that date.
- **Chat override:** use an explicit date if the user names one (e.g. “for June 15”).
- File name always uses that date: `Daily-Time-Log-YYYY-MM-DD.md`.

### Step 2 — Jira search

Use **user-atlassian** MCP (`searchJiraIssuesUsingJql`). Read tool schema before calling.

Use a **two-day `worklogDate` window** around the target date. Jira indexes `worklogDate` in the logger’s timezone, which can differ from the calendar date in the worklog `started` timestamp (e.g. a `-0500` entry on 15 Jun indexed as 16 Jun for an Egypt-timezone user). A single-day `worklogDate =` query misses those issues.

**Default target (yesterday, run the following calendar day):**

```text
project = OC AND issuetype = Sub-task AND worklogDate >= startOfDay(-1d) AND worklogDate < startOfDay(1d) ORDER BY key ASC
```

**Explicit target date `YYYY-MM-DD`:** compute the next calendar day (`YYYY-MM-DD+1`) and use:

```text
project = OC AND issuetype = Sub-task AND worklogDate >= YYYY-MM-DD AND worklogDate <= YYYY-MM-DD+1 ORDER BY key ASC
```

- Request `fields`: `summary`, `assignee`, `key`.
- `maxResults`: 100; paginate with `nextPageToken` if needed.

JQL is a **candidate list only** — the window adds false positives (issues indexed on the day after with no `started` on the target). Always verify in Step 3.

### Step 3 — Worklog extraction and time math

For each candidate issue, call `getJiraIssue` with `fields`: `summary`, `assignee`, `worklog`.

**Include a worklog only when** the `started` timestamp’s calendar date equals the target date (parse the ISO date before `T`).

**Assignee column:** issue `assignee.displayName`; if null, use the worklog `author.displayName`.

**Sum** all matching worklogs per issue into one row. Multiple loggers on the same task → separate rows (one per assignee/worklog author grouping).

**Time conversion — critical:** treat **1d = 7h**, not Jira’s default 8h. Parse each worklog’s `timeSpent` string (`Nd`, `Nh`, `Nm`); do **not** use `timeSpentSeconds` when the string contains `d` (Jira stores 1d as 28800s). See [references/time-conversion.md](references/time-conversion.md).

**Exclude** issues with zero converted time on the target date.

### Step 4 — Build tables

Order and layout: see [references/document-template.md](references/document-template.md).

1. **Daily total by assignee** — sum detail rows per assignee; add **All** row.
2. **Detail by task** — columns: Assignee | Task | Time spent (D Mon).

Sort detail rows by assignee name, then issue key.

Task column format: `[OC-XXXX](https://ontellus.atlassian.net/browse/OC-XXXX) — {summary}`

### Step 5 — Write file

Create `Daily TimeLog/` if missing. Write or overwrite the dated file. Do not append.

If no subtasks have time on the target date, still write the file with empty tables and a one-line note that no work was logged.

## When done

Reply with:

1. The file path created or updated
2. The **Daily total by assignee** table from the file
3. A one-line note if any JQL candidates were excluded because they had no work on the target date

## Hook follow-up

When this skill is run via `/daily-time-log`, the **work-log-report-hook** (`.cursor/hooks/work-log-report-hook.ps1`) chains **send-daily-timelog** on agent stop: generate per-assignee `.eml` files, full team reports (`all-salah`, `all-hussein`, `all-nabawy`), and send via Outlook. No extra prompt is required unless the user asks to skip sending.

## Additional resources

- [references/document-template.md](references/document-template.md) — markdown structure and example
- [references/time-conversion.md](references/time-conversion.md) — 1d = 7h parsing rules
- [references/jira-worklog-query.md](references/jira-worklog-query.md) — MCP tools, JQL, edge cases
