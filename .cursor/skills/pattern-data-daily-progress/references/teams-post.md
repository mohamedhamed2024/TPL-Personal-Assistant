# Teams post — Power Automate webhook

The morning Cursor Automation writes today's progress markdown, opens a PR, then POSTs a summary card to **Power Automate**. The flow is bound to the Teams channel — the agent never needs the channel name.

**Do not commit the HTTP URL.** Store it as:

- Cloud Agent environment secret `TEAMS_WEBHOOK_URL` (for the weekday automation)
- Repo-root `.env.local` for local manual runs (`TEAMS_WEBHOOK_URL=...`). That file is gitignored.

## One-time: create the flow

1. Open [Power Automate](https://make.powerautomate.com) (or Teams **Workflows**).
2. **Create** → **Instant cloud flow**.
3. Trigger: **When an HTTP request is received**.
4. Paste this JSON schema into **Request Body JSON Schema**:

```json
{
  "type": "object",
  "properties": {
    "title": { "type": "string" },
    "asOf": { "type": "string" },
    "uatReady": { "type": "string" },
    "glance": { "type": "string" },
    "teamFocus": { "type": "string" },
    "actions": { "type": "string" },
    "prUrl": { "type": "string" },
    "filePath": { "type": "string" },
    "text": { "type": "string" },
    "adaptiveCard": { "type": "string" }
  }
}
```

5. Add action **Post adaptive card in a chat or channel** (Teams):
   - **Post as:** Flow bot
   - **Post in:** Channel
   - **Team / Channel:** the Pattern Data progress channel Amr uses
   - **Adaptive Card:** `triggerBody()?['adaptiveCard']` — this is a **JSON string** starting with `{"type":"AdaptiveCard"`. Do **not** pass the whole `triggerBody()` (that fails with *Property 'type' must be 'AdaptiveCard'*).
6. Save the flow. Copy the **HTTP POST URL**.
7. In [Cursor Cloud Agents](https://cursor.com/dashboard/cloud-agents) → this repo's environment → **Secrets**, add:

   | Name | Value |
   |------|--------|
   | `TEAMS_WEBHOOK_URL` | the HTTP POST URL from step 6 |

8. Optional: add a second action **Post message in a chat or channel** with `triggerBody()?['text']` as a fallback if the Adaptive Card action fails.

## What the script sends

`scripts/post_progress_to_teams.py` POSTs:

- **`adaptiveCard`** — JSON **string** of the Adaptive Card (for **Post adaptive card in a chat or channel**)
- **`type` / `attachments`** — Teams Workflows webhook wrapper (if you used “When a Teams webhook request is received”)
- **`text` plus glance / teamFocus / actions** — fallback for **Post message in a chat or channel**

## If the HTTP request succeeds (202) but the flow fails

The trigger accepted the POST; the Teams action rejected the card.

1. Open the failed run → the **Post adaptive card** (or **Post card**) action → copy the error.
2. Set that action’s Adaptive Card field to **`triggerBody()?['adaptiveCard']`**, not the entire body.
3. If the field still shows as an object in the designer, use **`string(triggerBody()?['adaptiveCard'])`**.
4. Optional fallback: **Post message in a chat or channel** with `triggerBody()?['text']`.

Teams Adaptive Cards are size-capped (~28 KB). The card is a **summary** (glance, team focus, open actions). The full markdown lives on the PR (`prUrl`).

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

Add **Create file** (SharePoint / Teams Files) if you want the full `.md` attached in the channel. Keep the card + PR link as the first version — it is smaller and more reliable.
