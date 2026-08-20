# Document template — Daily Time Log

## File path

`Daily TimeLog/Daily-Time-Log-YYYY-MM-DD.md`

## Structure (order is required)

1. Title + intro paragraph
2. **Daily total by assignee** table
3. **Detail by task** table

Totals **before** detail.

## Title and intro

```markdown
# OC Daily Time Log — D Mon YYYY

Subtasks in the OC project with work logged on **D Mon YYYY**. Time reflects worklog entries for that day only (not cumulative task totals). **1d = 7h.**
```

Use the same calendar date in the title, intro, and filename.

## Daily total by assignee

```markdown
## Daily total by assignee

| Assignee | Total |
|----------|-------|
| {Name} | {Xh} |
| **All** | **{Xh}** |
```

- One row per assignee from the detail table (sorted alphabetically).
- **All** = sum of assignee totals.
- Use the same hour formatting as detail rows (e.g. `17h`, `1h 30m`).

## Detail by task

```markdown
## Detail by task

| Assignee | Task | Time spent (D Mon) |
|----------|------|---------------------|
| {Name} | [OC-XXXX](https://ontellus.atlassian.net/browse/OC-XXXX) — {summary} | {Xh} |
```

- **Time spent** column header uses short date without year: `(15 Jun)`.
- Only time logged on the target day — never the issue’s cumulative `timeSpent`.

## Empty day

```markdown
# OC Daily Time Log — D Mon YYYY

Subtasks in the OC project with work logged on **D Mon YYYY**. Time reflects worklog entries for that day only (not cumulative task totals). **1d = 7h.**

No OC subtasks had worklog time on this date.

## Daily total by assignee

| Assignee | Total |
|----------|-------|
| **All** | **0h** |

## Detail by task

| Assignee | Task | Time spent (D Mon) |
|----------|------|---------------------|
| — | — | — |
```

## Worked example (2026-06-15)

See `Daily TimeLog/Daily-Time-Log-2026-06-15.md` in the repo.
