# Jira worklog query — MCP and edge cases

## MCP server

Use **user-atlassian** (read tool schemas under `mcps/user-atlassian/tools/` before calling).

| Tool | Purpose |
|------|---------|
| `searchJiraIssuesUsingJql` | Find candidate subtasks |
| `getJiraIssue` | Fetch `worklog` for each issue |

## Parameters

- **cloudId:** `0ace3b78-4a29-418f-8997-c353db285ca8`
- **getJiraIssue fields:** `summary`, `assignee`, `worklog`

## JQL — two-day candidate window

Do **not** use `worklogDate = YYYY-MM-DD` alone. Jira indexes `worklogDate` in the logger’s timezone, which can land on the calendar day **after** the target when the `started` offset shows the target date (example: OC-9598 — `started` 2026-06-15 in `-0500`, indexed as 2026-06-16 for Egypt timezone).

**Default target (yesterday):**

```text
project = OC AND issuetype = Sub-task AND worklogDate >= startOfDay(-1d) AND worklogDate < startOfDay(1d) ORDER BY key ASC
```

**Explicit target `YYYY-MM-DD`:** use the next calendar day as the upper bound:

```text
project = OC AND issuetype = Sub-task AND worklogDate >= YYYY-MM-DD AND worklogDate <= YYYY-MM-DD+1 ORDER BY key ASC
```

Example for 2026-06-15: `worklogDate >= 2026-06-15 AND worklogDate <= 2026-06-16`.

## Work date filter (Step 3 — authoritative)

The JQL window produces **false positives** (issues indexed on target+1 with work only on other days) and must not be used for totals. After fetch, keep only worklogs whose **`started`** calendar date (ISO portion before `T`) equals the target `YYYY-MM-DD`.

## Assignee vs author

| Column | Source |
|--------|--------|
| Assignee | Issue assignee, else worklog author |

If two people log time on the same subtask the same day, output **two detail rows**.

## Pagination

- Search: up to 100 per page; follow `nextPageToken` until `isLast`.
- Worklog: default returns 20; if `total` > 20, note in skill run — re-request or paginate worklog API if MCP exposes it. For typical daily volume, the embedded worklog on `getJiraIssue` is sufficient.

## Issue type

Only **Sub-task** (`issuetype = Sub-task`). Do not include Story, Bug, Task, etc., unless the user explicitly expands scope.
