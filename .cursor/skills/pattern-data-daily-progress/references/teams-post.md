# Teams post — Power Automate webhook

The morning Cursor Automation writes today's progress markdown, opens a PR, then POSTs a summary card to **Power Automate**. The flow is bound to the Teams channel — the agent never needs the channel name.

**Do not commit the HTTP URL.** Store it as:

- Cloud Agent environment secret `TEAMS_WEBHOOK_URL` (for the weekday automation)
- Repo-root `.env.local` for local manual runs (`TEAMS_WEBHOOK_URL=...`). That file is gitignored.

## One-time: create the flow

1. Open [Power Automate](https://make.powerautomate.com) (or Teams **Workflows**).
2. **Create** → **Instant cloud flow**.
3. Trigger: **When an HTTP request is received**.
4. Paste this JSON schema into **Request Body JSON Schema** (Teams webhook envelope):

```json
{
  "type": "object",
  "properties": {
    "type": { "type": "string" },
    "attachments": { "type": "array" }
  }
}
```

5. Add action **Post adaptive card in a chat or channel** (Teams):
   - **Post as:** Flow bot
   - **Post in:** Channel
   - **Team / Channel:** the Pattern Data progress channel Amr uses
   - **Adaptive Card:** `triggerBody()?['attachments']?[0]?['content']`  
     Prefer the **When a Teams webhook request is received** template, which already loops `attachments`. Do **not** pass a raw Adaptive Card as the HTTP body (that is a common **400**).
6. Save the flow. Copy the **HTTP POST URL**.
7. In [Cursor Cloud Agents](https://cursor.com/dashboard/cloud-agents) → this repo's environment → **Secrets**, add:

   | Name | Value |
   |------|--------|
   | `TEAMS_WEBHOOK_URL` | the HTTP POST URL from step 6 |

## Existing flow — fix HTTP 400 / *Property 'type' must be 'AdaptiveCard'*

**400 from the webhook URL:** the HTTP body was a raw Adaptive Card. The script now sends `type: message` + `attachments`. Re-run `post_progress_to_teams.py`.

**Property 'type' must be 'AdaptiveCard'** in **Post adaptive card**: the action received the envelope (`type: message`) instead of the card. Set **Adaptive Card** to `triggerBody()?['attachments']?[0]?['content']` (or use the Teams webhook template).

1. Open the flow that owns `TEAMS_WEBHOOK_URL`.
2. Confirm the trigger accepts the message envelope (schema above, or the Teams webhook trigger).
3. Save.
4. Re-run `post_progress_to_teams.py`.

## What the script sends

The POST body is a **Teams webhook message** (not a raw Adaptive Card). Workflows that
expect `triggerBody().attachments` return **HTTP 400** if the root `type` is `AdaptiveCard`.

```json
{
  "type": "message",
  "attachments": [
    {
      "contentType": "application/vnd.microsoft.card.adaptive",
      "contentUrl": null,
      "content": {
        "type": "AdaptiveCard",
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2",
        "body": []
      }
    }
  ]
}
```

If that envelope still returns HTTP 400, the script retries with the Adaptive Card as the
JSON root (for custom **When an HTTP request is received** → **Post adaptive card** flows
that use `string(triggerBody())`).

Teams Adaptive Cards cannot attach a `.md` or HTML file. The script **inlines** the full progress report as TextBlocks under **Full report** (HTML lists/tables flattened to text). If the card would exceed ~22 KB, the report text is truncated.

For the built-in **When a Teams webhook request is received** template, keep **Send each adaptive card** bound to `triggerBody()['attachments']`. Do **not** pass `string(triggerBody())` into Post adaptive card when the body is this envelope (root `type` is `message`).

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
