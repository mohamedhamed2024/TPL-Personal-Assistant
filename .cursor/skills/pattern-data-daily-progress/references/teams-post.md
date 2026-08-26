# Teams post — incoming webhook (Adaptive Card)

After today's progress markdown is on **main**, post a **full-width Adaptive Card** to the Teams channel using **`TEAMS_WEBHOOK_URL`** (Power Automate incoming webhook). Do **not** use Lokka / Microsoft Graph for Teams posting.

## One-time setup

1. Create a Power Automate flow: **When a Teams webhook request is received** → post the Adaptive Card (or use the project's existing manual webhook).
2. Set `TEAMS_WEBHOOK_URL` in gitignored `.env.local` (repo root). Never commit or print it.
3. Cloud Automations: store `TEAMS_WEBHOOK_URL` as an environment secret.

`TEAMS_CHANNEL_ID` is **not** required for webhook posting (the flow already targets the channel).

## Each run (after the report exists)

Read `Daily Progress/pattern-data-delivery-progress-YYYY-MM-DD.md`.

### 1. Build and POST the Adaptive Card

From repo root (Windows: `py -3` if `python` is missing):

```bash
py -3 .cursor/skills/pattern-data-daily-progress/scripts/post_progress_to_teams.py --date YYYY-MM-DD
```

The script:

- Maps the full report to Adaptive Card **1.5** (`targetWidth: VeryWide`, `msteams.width: Full`)
- Includes **all** report sections: Status at a glance, Daily update from Austin, Feature tracker, Team focus, Path to UAT & Production, Risks & challenges
- **Skips** legacy **How to read this report** and **Standup action items** if still in older files
- Uses native **`Table`** elements for markdown pipe tables
- Splits into multiple webhook messages at **## section** boundaries when the payload exceeds the ~28 KB cap
- Waits **2 seconds** between parts (configurable with `--post-delay`) so Teams receives them in order

Preview without posting:

```bash
py -3 .cursor/skills/pattern-data-daily-progress/scripts/post_progress_to_teams.py --date YYYY-MM-DD --dry-run
```

Export card JSON only:

```bash
py -3 .cursor/skills/pattern-data-daily-progress/scripts/post_progress_to_teams.py --date YYYY-MM-DD --export-card
```

Never print `TEAMS_WEBHOOK_URL` or paste it into chat.

### 2. Markdown → card mapping

| Markdown | Teams card |
| --- | --- |
| `#` / `##` / `###` | Heading `TextBlock` |
| `**bold**` · `_italic_` · `[label](url)` | TextBlock markdown |
| `-` / `1.` lists | TextBlock lists |
| `- [ ]` / `- [x]` | ☐ / ☑ checklist lines |
| pipe tables | Native Adaptive Card **`Table`** |
| `>` quotes | Emphasis `Container` |
| ` ``` ` fences | `CodeBlock` |
| `---` | Separator |

## If posting fails

- Confirm `TEAMS_WEBHOOK_URL` is set in `.env.local` or the Cloud Agent secret.
- Run `--dry-run` and check each part is under the size cap.
- If HTTP 400, the Power Automate flow may expect a raw Adaptive Card root instead of `type: message` — the script retries automatically.

Do **not** upload the `.md` to channel Files unless the user asks — the card is the channel deliverable.
