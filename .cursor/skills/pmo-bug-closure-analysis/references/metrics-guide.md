# Lifecycle Metrics Guide

How to compute each metric from the tracker changelog and comments. With the Jira MCP (the worked
example), the changelog comes from `jira_get_issue` with `expand: "changelog"` (or
`jira_batch_get_changelogs` with `limit: -1`). Each changelog entry has an `author`, a `created`
timestamp, and `items` (field, fromString, toString). Status transitions are items where
`field == "status"`. Substitute the equivalent history API of your tracker.

**Golden rule:** if the changelog is unavailable or lacks the timestamps a metric needs, that metric
is **`Not Clear`** — never estimate.

## Table of Contents
- [Status model](#status-model)
- [Reopen frequency](#reopen-frequency)
- [Time to fix / cycle time](#time-to-fix--cycle-time)
- [Time in progress](#time-in-progress)
- [Time to first response / triage](#time-to-first-response--triage)
- [Resolution time (created → resolved)](#resolution-time-created--resolved)
- [Formatting durations](#formatting-durations)

## Status model

Map your tracker's workflow statuses to three categories. Read your board's status/workflow config
and classify each status; a typical mapping looks like:

- **To Do:** backlog / to-do / not-yet-started statuses
- **In Progress:** in-progress / analysis / blocked / code-review / product-review statuses
- **Done:** closed / done / resolved statuses

A bug is "resolved/closed" when it reaches a **Done** category status.

## Reopen frequency

Count the number of times the issue transitioned **out of** a Done-category status **back into** a
To Do or In Progress status.

```
reopens = count of status transitions where
            fromString ∈ Done-category statuses AND
            toString  ∈ (To Do ∪ In Progress) statuses
```

- If the changelog is present and no such transition exists → **`0`**.
- If there is no changelog → **`Not Clear`**.
- Also note the dates of each reopen in the report (useful signal of an unstable fix).

## Time to fix / cycle time

**Cycle time** = time from when work *started* to when the bug *reached Done*.

```
work_start  = timestamp of the FIRST transition into an In Progress status
done_time   = timestamp of the LAST transition into a Done status
cycle_time  = done_time − work_start
```

- If the bug never entered an In Progress status (e.g., went straight backlog → closed) → use
  Resolution time instead and note that cycle time is `Not Clear` (no in-progress record).
- If reopened, use the **last** Done transition as `done_time` (total cycle including rework). Also
  report the first-fix cycle time separately if useful.

## Time in progress

Sum the durations the issue actually spent in In Progress statuses (excludes time sitting in
the backlog or Blocked if Blocked is treated separately).

```
time_in_progress = Σ (interval where current status ∈ In Progress, excluding Blocked)
```

Walk the status transitions in order, tracking the current status and the time spent in each before
the next transition. Sum the In Progress intervals. If transitions are missing → `Not Clear`.

## Time to first response / triage

```
first_response = (earliest of: first comment timestamp,
                                first transition out of the backlog) − created
```

Use whichever signal exists. If neither comments nor transitions are available → `Not Clear`.

## Resolution time (created → resolved)

```
resolution_time = done_time − created
```

`created` is the issue's creation timestamp; `done_time` as defined above. This is the simplest
end-to-end metric and is usually computable whenever the changelog exists.

## Formatting durations

- Express durations in the largest sensible unit with one decimal where helpful:
  `3h`, `1.5d`, `6d`, `2w 1d`.
- Prefer **business-day awareness only if** working-calendar data is available; otherwise use
  wall-clock elapsed time and state it is wall-clock.
- Always show the two timestamps you computed from in the local report (not in the comment) so the
  math is auditable.
