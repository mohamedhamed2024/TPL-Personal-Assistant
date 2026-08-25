# Cursor Automation — Pattern Data morning progress

Paste this into a new Cursor Automation. Create it at [cursor.com/automations](https://cursor.com/automations) or with `/automate` in the **Agents Window** (that editor is the only place that can save the live job).

The skill has `disable-model-invocation: true` — the automation **must** name this skill file. Do not rely on automatic skill attach.

## Editor settings

| Field | Value |
|-------|--------|
| **Name** | Pattern Data morning progress |
| **Description** | Weekday morning Jira sync of the Pattern Data delivery progress report. Commits to main and posts the .md to Teams via Lokka. |
| **Trigger** | On a schedule — weekdays. Pick the Cairo morning hour in the editor (cron is stored as UTC). Example: 07:00 Africa/Cairo = `0 4 * * 1-5`. |
| **Repository** | This repo, **main** |
| **Tools** | Atlassian (Jira); **Lokka-Microsoft-365** (Graph / Teams); git push to main |
| **Memories** | Off unless you need cross-run notes |
| **Secrets** | `MICROSOFT_TENANT_ID`, `MICROSOFT_CLIENT_ID` (Lokka auth); `TEAMS_CHANNEL_ID` (destination). Do not use `TEAMS_WEBHOOK_URL` unless Lokka is down. |

Authenticate **Atlassian** and **Lokka** in Cursor before saving. Unauthenticated MCP blocks save.

## Instructions (paste into the prompt)

```
Follow the Pattern Data daily progress skill at .cursor/skills/pattern-data-daily-progress/SKILL.md and its references (document-template.md, jira-sync.md, salesforce-deploy.md, domain-decisions.md, teams-post.md). Do not skip that skill.

Target today's calendar date. This is a weekday-morning Jira-only run:

1. Bootstrap Daily Progress/pattern-data-delivery-progress-YYYY-MM-DD.md from the most recent file in Daily Progress/ if today's file does not exist. Update only the As of header, Jira sync date, and standup/Austin input dates. Leave historical event dates unchanged.
2. If today's ChartSwap standup .docx or Austin-class transcript is missing from Transcript/, skip transcript extraction. Keep Austin's last deployment plan. Do not invent standup action items. Default Islam's Team focus to PD sandbox testing of LNI-3763 RequestShare unless a transcript says otherwise.
3. Sync Datavant Jira on DVI-1086 (epics → open stories → open subtasks) before editing the report. Parse story comments for PR and changeset status. Exclude Youssef Yahia. Team focus: Michael and Sarah from Jira assignees.
4. Update all report sections per the skill template. Recompute Path to UAT N/M. Replace the Standup action items section: if there was no standup transcript, keep prior open Jira-driven next steps only — do not fabricate owners or meetings.
5. Optionally align Testing Updates.md. Delete temp extract files.
6. git fetch origin, checkout main, git pull --ff-only. Commit today's progress markdown (and Testing Updates.md if changed) on main. git push origin HEAD. Do not open a pull request. Do not force-push. Do not commit .env.local or secrets.
7. Post the .md to the Teams channel with Lokka (MCP server Lokka-Microsoft-365), per .cursor/skills/pattern-data-daily-progress/references/teams-post.md: read TEAMS_CHANNEL_ID from the environment (do not print it), resolve the team from joined teams, upload the file to the channel Files folder, then POST a channel message with an HTML summary and a link/attachment to the file. Lokka auth uses MICROSOFT_TENANT_ID and MICROSOFT_CLIENT_ID. Never print tokens or secrets. Do not call post_progress_to_teams.py unless Lokka is unavailable.
8. Reply with the skill's "When done" summary plus whether main was pushed and whether the Teams post succeeded.

Do not use wave / Wave 1 / Wave 2 language.
```

## After save

1. Confirm Atlassian (Jira) and **Lokka-Microsoft-365** are connected for Cloud Agents.
2. Confirm `MICROSOFT_TENANT_ID`, `MICROSOFT_CLIENT_ID`, and `TEAMS_CHANNEL_ID` on that environment.
3. Run once manually from the Automations page before relying on the weekday cron.
4. Confirm a commit landed on **main** and the `.md` appeared in the Teams channel Files tab.
