# Teams post — Power Automate webhook

The morning Cursor Automation writes today's progress markdown, opens a PR, then POSTs a summary card to **Power Automate**. The flow is bound to the Teams channel — the agent never needs the channel name.

**Do not commit the HTTP URL.** Store it as:

- Cloud Agent environment secret `TEAMS_WEBHOOK_URL` (for the weekday automation)
- Repo-root `.env.local` for local manual runs (`TEAMS_WEBHOOK_URL=...`). That file is gitignored.

## One-time: create the flow

1. Open [Power Automate](https://make.powerautomate.com) (or Teams **Workflows**).
2. **Create** → **Instant cloud flow**.
3. Trigger: **When an HTTP request is received**.
4. Paste this JSON schema into **Request Body JSON Schema** (root **must** be an Adaptive Card):

```json
{
  "type": "object",
  "properties": {
    "type": { "type": "string" },
    "$schema": { "type": "string" },
    "version": { "type": "string" },
    "body": { "type": "array" },
    "actions": { "type": "array" }
  }
}
```

5. Add action **Post adaptive card in a chat or channel** (Teams):
   - **Post as:** Flow bot
   - **Post in:** Channel
   - **Team / Channel:** the Pattern Data progress channel Amr uses
   - **Adaptive Card:** `string(triggerBody())`  
     The HTTP body **is** the card (`"type": "AdaptiveCard"`). Do **not** use `triggerBody()?['adaptiveCard']` and do **not** pass a Teams `"type": "message"` wrapper.
6. Save the flow. Copy the **HTTP POST URL**.
7. In [Cursor Cloud Agents](https://cursor.com/dashboard/cloud-agents) → this repo's environment → **Secrets**, add:

   | Name | Value |
   |------|--------|
   | `TEAMS_WEBHOOK_URL` | the HTTP POST URL from step 6 |

## Existing flow — fix *Property 'type' must be 'AdaptiveCard'*

The flowbot received JSON whose root `type` was `message` (or a nested field), not `AdaptiveCard`.

1. Open the **Post adaptive card** action.
2. Set **Adaptive Card** to **`string(triggerBody())`**.
3. Save.
4. Re-run `post_progress_to_teams.py` (the script now POSTs the card as the entire body).

## What the script sends

The POST body **is** the Adaptive Card:

```json
{
  "type": "AdaptiveCard",
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "version": "1.2",
  "body": [ ]
}
```

Teams Adaptive Cards cannot attach a `.md` or HTML file. The script **inlines** the full progress report as TextBlocks under **Full report** (HTML lists/tables flattened to text). If the card would exceed ~25 KB, the report text is truncated.

Keep **Adaptive Card** = `string(triggerBody())`.

## Test locally (no post)

From the repo root (Windows: `py -3` if `python` is not on PATH):

```bash
python .cursor/skills/pattern-data-daily-progress/scripts/post_progress_to_teams.py --dry-run
```

Point at a specific file / date / PR:

```bash
python .cursor/skills/pattern-data-daily-progress/scripts/post_progress_to_teams.py --dry-run --date 2026-08-23 --pr-url "https://github.com/example/TPL-Personal-Assistant/pull/1"
```

Post for real (requires `TEAMS_WEBHOOK_URL` in the environment or `.env.local`):

```bash
python .cursor/skills/pattern-data-daily-progress/scripts/post_progress_to_teams.py --pr-url "<PR url>"
```

Exit codes: `0` success · `2` missing webhook or missing report file · `1` HTTP / parse error.

## Optional later

A true file in the channel **Files** tab still needs a SharePoint **Create file** action (not the Adaptive Card).
