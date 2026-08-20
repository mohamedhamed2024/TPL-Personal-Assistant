# Document template — daily actions

## File naming

- Actions: `Daily Actions/daily-actions-YYYY-MM-DD.md`
- Transcript: user-provided; link in header when available

## Header

```markdown
# Daily Actions

**Source:** [Meeting name — YYYY-MM-DD](relative/path/to/transcript) · **As of:** YYYY-MM-DD

---
```

Add an optional project line when context helps:

```markdown
**Project:** Pattern Data · **Epic:** [OC-9223](https://ontellus.atlassian.net/browse/OC-9223)
```

## Table layout

Two tables with the **same column structure**:

1. **Open actions** — pending, blocked, or scheduled work
2. **Completed / done** — finished or largely complete items from the meeting

| Dimension | Rule |
| --- | --- |
| **Rows** | Owner (first name by default) |
| **Columns** | Category (meeting themes) |
| **Cells** | `<ul><li>` bullet lists; one bullet per distinct action |
| **Empty** | `—` |

### Owners

- Derive from the meeting attendees and assignees.
- Use **first names** unless two people share a name.
- Use a **Team** row for whole-team commitments with no single owner.
- When two people share an action, put the bullet in **both** owner rows (same category column).
- Sort rows consistently (alphabetical by first name, or team lead first — pick one order per file).

### Categories

- Derive columns from **recurring themes** in the meeting (e.g. testing, bugs, process, access, leadership).
- Keep the same column headers in both tables for a given file.
- Add a column when a **new recurring theme** appears; do not drop empty columns mid-file (keeps tables aligned).
- For Pattern Data standups in this workspace, use the standard column set in [project-profiles/pattern-data.md](project-profiles/pattern-data.md).

## Cell formatting

```markdown
<ul><li>Fix <strong>ShareCare sandbox cost / full-film</strong> today</li><li>Retry <strong>6/16</strong></li></ul>
```

- Bold **key terms**: areas, dates, ticket keys, decisions, blockers
- Link ticket keys when mentioned (Jira, Azure DevOps, etc.)
- Keep bullets concise — one clear outcome per `<li>`

## Completed vs open — examples

| Meeting signal | Table |
| --- | --- |
| "Transaction comments done", "validation working" | Completed — owner / relevant category |
| "Pushed unit tests to the branch" | Completed — owner / testing category |
| "Will fix X today" | Open — owner / relevant category |
| "Demo before deploy" | Open — owner / demo or testing category |
| "Decision: code in PRs not tickets" | Completed — leadership owner / process category |
| "Forecast slipped to 6/17" | Decisions (not an action row) |

## Decisions section

After both tables:

```markdown
## Decisions (context — not new actions)

- **Topic:** One-line agreement or status change from the meeting.
```

Include: forecast rebaselines, deprioritizations, policy decisions, date moves. Exclude items already listed as open actions.

## Full skeleton

```markdown
# Daily Actions

**Source:** [Meeting — YYYY-MM-DD](...) · **As of:** YYYY-MM-DD

---

## Open actions

| Owner | Category A | Category B | Category C |
| --- | --- | --- | --- |
| **Alex** | <ul><li>…</li></ul> | — | … |
| **Team** | — | <ul><li>…</li></ul> | — |

---

## Completed / done

| Owner | Category A | Category B | Category C |
| --- | --- | --- | --- |
| **Alex** | <ul><li>…</li></ul> | — | — |

---

## Decisions (context — not new actions)

- …
```

## Reference example (this workspace)

Pattern Data standup: `Daily Actions/daily-actions-2026-06-15.md`
