# Jira sync — Pattern Data daily progress (Datavant)

## Project context

| Field | Value |
|-------|-------|
| Feature | [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) — PatternData SSO |
| Cloud ID | `eade365b-968b-4bd2-ad93-66539cfaeb93` |
| Site | `https://datavant.atlassian.net` |
| Primary deliverable | `Daily Progress/pattern-data-delivery-progress-YYYY-MM-DD.md` |

Use Atlassian MCP on **Datavant only**. Ontellus OC-9223 is not synced (historical reports may still reference OC keys).

## MCP workflow (before editing the report)

Run steps in order. Re-fetch on each daily sync — do not reuse prior-day Jira snapshots.

### Step 1 — Epics under feature

```jql
parent = DVI-1086 AND statusCategory != Done ORDER BY status ASC, key ASC
```

Collect epic keys (e.g. LNI-2309 … LNI-3216). Include epics in **In Progress** or **UAT** status.

### Step 2 — Open stories under epics

```jql
parent in (LNI-2309, LNI-2310, LNI-2311, LNI-2312, LNI-2313, LNI-3141, LNI-3216) AND issuetype = Story AND statusCategory != Done ORDER BY parent ASC, status ASC, key ASC
```

Replace `parent in (...)` with keys from Step 1. Paginate with `nextPageToken` if needed.

### Step 3 — Open subtasks

```jql
parent in (<story keys from Step 2>) AND issuetype = Sub-task AND status != Done ORDER BY parent ASC, key ASC
```

**Exclude Youssef Yahia:** after fetch, drop any subtask whose assignee is **Youssef Yahia**. He is off the project — remaining Jira assignments are legacy and must not appear in the report, Team focus, subtask tables, or action counts.

### Step 4 — Story detail fetch

For each story in the feature tracker, call `getJiraIssue`:

```json
{
  "cloudId": "eade365b-968b-4bd2-ad93-66539cfaeb93",
  "issueIdOrKey": "LNI-####",
  "fields": ["summary", "status", "assignee", "comment", "parent"],
  "responseContentFormat": "markdown"
}
```

Parse **comments** (newest first) for PR links, changeset URLs, and wordings status.

When a **PD Review with Austin** transcript is incomplete (timestamp jump) or thin on decisions, also scan story comments for headings **`Austin requirement sync — YYYY-MM-DD`** whose `Call / source` is **PD Review**. Use those bullets to fill **Daily update from Austin** and tracker Next step — do not invent the missing transcript middle.

## Assignee mapping

| Jira displayName | Report row |
| --- | --- |
| Michael Girgis | Michael |
| Sarah Hassaan | Sarah |
| **Youssef Yahia** | **Exclude** — off project; ignore stories/subtasks assigned to him |
| Unassigned / other | Notes column only; do not add to Team focus unless standup names them |

## PR status heuristics (from story comments)

Scan comment bodies for Bitbucket URLs matching `bitbucket.org/.../pull-requests/`:

| Signal in comments | PR status column |
| --- | --- |
| `Open PR`, `pull-requests/new`, or recent PR link + story still In Progress / Code Review | **In progress** (include PR # if found, e.g. `#220`) |
| `Merged`, `supersedes`, PR closed + story advancing to QA/UAT | **Merged** |
| No `pull-requests/` URL in recent comments and story not Done | **Ready — finalize code review & deploy packages** |
| Explicit "no pending PR" / "dev complete" in standup | Override with standup note in Next step |

Prefer the **most recent** comment mentioning a PR.

## Changeset heuristics (from story comments)

Scan for Salesforce outbound changeset URLs (`changemgmt/outboundChangeSetDetail`) or keywords:

| Signal | Changesets column |
| --- | --- |
| `apex CS`, `code set`, `Feature CS`, `② (code)` uploaded/validated | Feature ✓ |
| `rollback CS`, `Rollback` uploaded/validated | Rollback ✓ |
| `properties CS`, `Objects:` properties set | Properties ✓ |
| `Properties CS` not applicable / code-only feature | Properties — |
| No CS mention | Feature Pending · Rollback Pending · Properties Pending |

Also note **manual CS steps** in Next step (e.g. "PayflowSettingsService add before UAT deploy").

## Sandbox column heuristics

| Signal | PD sandbox / UAT sandbox |
| --- | --- |
| `pddev`, `PD sandbox`, validated on pddev | PD sandbox → Validated or In progress |
| `Uploaded to UAT`, `UAT sandbox`, UAT validation | UAT sandbox → In progress or Validated |
| No deploy mention | Not deployed |

Cross-check with standup for same-day deploy events.

## PATTERNDATA wordings

| Signal | Column value |
| --- | --- |
| `wordings approved`, `PATTERNDATA approved` | Approved — attach to CS |
| Default | Pending approval |

## Recurring Jira keys

| Key | Topic |
| --- | --- |
| DVI-1086 | Feature — PatternData SSO |
| LNI-2309 | Epic — Payment Management |
| LNI-2310 | Epic — AutoPay Submission Flow |
| LNI-2311 | Epic — SAML SSO (Sarah) |
| LNI-2312 | Epic — Status Sync / Webhooks (Michael) |
| LNI-2313 | Epic — Patient Prefill API (Michael) |
| LNI-3141 | Epic — Invoice Upload to S3 (Michael) |
| LNI-3216 | Epic — General (Michael + Sarah) |
| LNI-3137 | Story — Payment Management |
| OC-9223 | Historical Ontellus epic (not synced) |

## Sync date line

Every Feature delivery tracker must include:

```markdown
*Synced from [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) on YYYY-MM-DD (live).*
```

Use the calendar date of the sync, not the story's `updated` timestamp.
