---
name: daily-actions
description: >-
  Extract standup or meeting action items into dated daily-actions markdown
  using owner × category matrix tables. Use when the user asks for daily actions,
  standup action items, daily-actions update, or to create or refresh
  daily-actions-YYYY-MM-DD.md from a transcript or meeting notes.
disable-model-invocation: true
---

# Daily Actions

Extract action items from standup transcripts or meeting notes into `Daily Actions/daily-actions-YYYY-MM-DD.md` using the owner × category matrix format (open + completed tables).

## Project paths (defaults)

Adapt paths if the workspace uses different folders:

- `Daily Actions/daily-actions-YYYY-MM-DD.md` — primary deliverable
- Transcript source — user-provided path (commonly `.docx` under a `Transcript/` folder)
- Optional extractor: `.cursor/skills/pattern-data-daily-progress/scripts/extract_standup.py` (ChartSwap `.docx` transcripts in this workspace)

For **Pattern Data / ChartSwap** standups in this repo, see [references/project-profiles/pattern-data.md](references/project-profiles/pattern-data.md).

## Workflow

Copy this checklist and track progress:

```
- [ ] 1. Determine today's date (YYYY-MM-DD)
- [ ] 2. Extract transcript (if docx provided)
- [ ] 3. Identify action items, owners, and categories
- [ ] 4. Split open vs completed/done
- [ ] 5. Write or update daily-actions-YYYY-MM-DD.md
- [ ] 6. Delete temp extract files
```

### Step 1 — Bootstrap

**Target date:** use **today** (current calendar day) unless the user invokes `/daily-actions YYYY-MM-DD` or names another date in chat.

**If today's file does not exist:** create from template in [references/document-template.md](references/document-template.md).

**If today's file exists:** update in place; move items to **Completed / done** when the meeting confirms they are finished.

### Step 2 — Extract transcript

**`.docx` (ChartSwap standups in this workspace):** run from project root (UTF-8 temp file; do not print to console on Windows):

```bash
python .cursor/skills/pattern-data-daily-progress/scripts/extract_standup.py "PATH/TO/transcript.docx" -o _standup_extract.txt
```

**Other formats:** read the file directly (markdown, plain text, pasted notes).

Delete `_standup_extract.txt` when done.

### Step 3 — Extract actions

Capture only **assigned or agreed next steps** — not general discussion.

Include:
- Explicit assignments ("X will…", "Y to…")
- Blockers with a named owner or escalation path
- Deadlines and dependencies
- Process commitments the team agreed to follow

Exclude:
- Pure status with no follow-up
- Rhetorical questions without an owner
- Leadership monologue with no team action (unless a decision affects everyone → **Decisions** section)

Map each action to one **owner** and one **category**. Derive owners and categories from the meeting — use [references/document-template.md](references/document-template.md) for layout rules.

### Step 4 — Open vs completed

| Put in **Open actions** | Put in **Completed / done** |
| --- | --- |
| Pending, not started, blocked, retry scheduled | Explicitly **done**, **complete**, **pushed**, **validated**, **working** |
| "Will do today/tomorrow", investigate, discuss later | Notifications already sent, setup already finished |
| Demo/fix still outstanding | Decisions already made (policy → leadership owner) |

When one topic is partially done, **split**: completed bullets in the done table; remaining work stays open.

Use `—` for empty cells. Omit owner rows that have no items in that table.

### Step 5 — Write output

Follow [references/document-template.md](references/document-template.md):

- **Rows:** owner (first names unless full name needed for clarity)
- **Columns:** category (themes from the meeting)
- **Cells:** HTML bullet lists (`<ul><li>…</li></ul>`)
- **Sections:** Open actions → Completed / done → Decisions (context only)

### Step 6 — Decisions section

Add bullets for team agreements, forecast changes, deprioritizations, and policy decisions that are **context**, not assignable tasks. Do not duplicate open actions here.

## When done

Reply with:

1. The file path created or updated
2. Count of **open** vs **completed** action rows (owner rows with at least one bullet)
3. Any new or changed **Decisions** bullets added today

## Additional resources

- [references/document-template.md](references/document-template.md) — table layout, header, formatting, examples
- [references/project-profiles/pattern-data.md](references/project-profiles/pattern-data.md) — ChartSwap team owners and category columns for this workspace
