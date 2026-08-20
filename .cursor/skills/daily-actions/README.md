# Daily Actions

Extract standup or meeting action items into dated owner × category matrix tables.

## Use Cases

- **Daily actions file** — Create or update `daily-actions-YYYY-MM-DD.md`
- **Standup sync** — Extract transcript and list open + completed actions
- **Any project** — Derive owners and categories from the meeting; optional project profiles for recurring teams

## How to Use

1. **Generate today's actions**: *"Extract action items from today's standup"*
2. **With transcript**: Reference the meeting file path
3. Invoke from chat: `/daily-actions` (or ask for daily standup actions)

## Workflow

1. Determine today's date
2. Extract transcript (docx script or direct read)
3. Map actions to owners and categories
4. Split open vs completed/done
5. Write matrix tables with HTML bullet cells
6. Add Decisions section; delete temp files

## Output Format

| Aspect | Value |
| --- | --- |
| Rows | Owner |
| Columns | Category (from meeting themes) |
| Tables | Open actions + Completed / done |
| Cells | `<ul><li>` bullet lists |

## Skill Info

| Field | Value |
| --- | --- |
| **Skill Name** | `daily-actions` |
| **Location** | `.cursor/skills/daily-actions/` |
| **Source** | Project (local) |
