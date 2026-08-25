# Teams post — Lokka (Microsoft Graph)

After today's progress markdown is on **main**, post **the `.md` file** to the Teams channel using the **Lokka** MCP server **`Lokka-Microsoft-365`**. Do not use Power Automate / `TEAMS_WEBHOOK_URL` unless Lokka is disconnected.

Lokka is a Graph proxy: tool **`Lokka-Microsoft`** (`apiType: graph`, `path`, `method`, `body`).

## One-time setup

Project MCP is [`.cursor/mcp.json`](../../../mcp.json). Use the **default Lokka app** (no tenant/client IDs in `mcp.json`):

```json
{
  "mcpServers": {
    "Lokka-Microsoft-365": {
      "command": "npx",
      "args": ["-y", "@merill/lokka"]
    }
  }
}
```

1. Reload the **Lokka-Microsoft-365** MCP server in Cursor Settings (MCP).
2. Sign in with **Lokka connections** (say `lokka sign in`, or the agent opens the dialog). Do not expect Graph to work until a tenant connection appears.
3. Grant delegated Graph scopes: `ChannelMessage.Send`, `Team.ReadBasic.All`, `Channel.ReadBasic.All`, `Files.ReadWrite.All` (or `Sites.ReadWrite.All`).
4. Set `TEAMS_CHANNEL_ID` in gitignored `.env.local` (skill only — not passed to Lokka). Never commit or print it.

Optional custom Entra app (only if the default Lokka app cannot consent): set `TENANT_ID` / `CLIENT_ID` from `MICROSOFT_TENANT_ID` / `MICROSOFT_CLIENT_ID`, `USE_INTERACTIVE=true`, and `REDIRECT_URI=http://localhost:3000` (must match the app registration — do **not** use `http://localhost` with no port).

Cloud Automations: `TEAMS_CHANNEL_ID` as an environment secret, plus Lokka signed in for Cloud Agents. Custom-app secrets (`MICROSOFT_TENANT_ID` / `MICROSOFT_CLIENT_ID`) only if you use that path.

## Each run (after the report exists)

Read `Daily Progress/pattern-data-delivery-progress-YYYY-MM-DD.md`. Read `TEAMS_CHANNEL_ID` from the environment or `.env.local` **without printing it**.

### 1. Resolve the team from the channel

`TEAMS_CHANNEL_ID` is required. Team id is **not** required.

- `GET /me/joinedTeams` (`$select=id,displayName`)
- For each team, `GET /teams/{team-id}/channels` (`$select=id,displayName`) until `id` matches `TEAMS_CHANNEL_ID`
- Use that `team-id` for upload + message calls

If the channel is not in joined teams, stop and say Lokka/Graph cannot see that channel (membership or permission).

### 2. Upload the `.md` to the channel Files tab

```
GET /teams/{team-id}/channels/{channel-id}/filesFolder
```

Use `parentReference.driveId` and `id` (folder item), then:

```
PUT /drives/{drive-id}/items/{folder-id}:/pattern-data-delivery-progress-YYYY-MM-DD.md:/content
```

UTF-8 body = the markdown file. If PUT content fails through Lokka, fall back to:

```
PUT /groups/{team-id}/drive/root:/General/pattern-data-delivery-progress-YYYY-MM-DD.md:/content
```

(Use the channel folder name from `filesFolder` when it is not `General`.)

### 3. Post a channel message that points at the file

```
POST /teams/{team-id}/channels/{channel-id}/messages
```

Body (HTML — Teams does not render raw `.md` in the message pane):

```json
{
  "body": {
    "contentType": "html",
    "content": "<p><b>Pattern Data — delivery progress</b> (YYYY-MM-DD)</p><p>Full report in channel Files: pattern-data-delivery-progress-YYYY-MM-DD.md</p><p>Short HTML of glance / team focus / actions…</p>"
  }
}
```

If the upload returned a `webUrl`, include it as a link. If Graph returns an attachment handle:

```json
{
  "attachments": [
    {
      "id": "1",
      "contentType": "reference",
      "contentUrl": "<item webUrl>",
      "name": "pattern-data-delivery-progress-YYYY-MM-DD.md"
    }
  ]
}
```

and `<attachment id=\"1\"></attachment>` in the HTML.

Keep the HTML summary short. The **file** is what Amr asked for.

## Fallback (Lokka unavailable)

Remind the user to post the `.md` in Teams manually. Optional last resort: [scripts/post_progress_to_teams.py](../scripts/post_progress_to_teams.py) + `TEAMS_WEBHOOK_URL` (Adaptive Card only — no real file attach).
