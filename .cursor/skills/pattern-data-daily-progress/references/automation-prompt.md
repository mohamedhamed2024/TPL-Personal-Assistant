# Cursor Automation — Pattern Data morning progress

Paste this into a new Cursor Automation. Create it at [cursor.com/automations](https://cursor.com/automations) or with `/automate` in the **Agents Window** (that editor is the only place that can save the live job).

The skill has `disable-model-invocation: true` — the automation **must** name this skill file. Do not rely on automatic skill attach.

## Editor settings

| Field | Value |
|-------|--------|
| **Name** | Pattern Data morning progress |
| **Description** | Weekday morning Jira sync of the Pattern Data delivery progress report. Opens a PR and posts a Teams summary card. |
| **Trigger** | On a schedule — weekdays. Pick the Cairo morning hour in the editor (cron is stored as UTC). Example: 07:00 Africa/Cairo = `0 4 * * 1-5`. |
| **Repository** | This repo, default branch |
| **Tools** | Atlassian (Jira); pull request creation |
| **Memories** | Off unless you need cross-run notes |
| **Secret** | `TEAMS_WEBHOOK_URL` — Power Automate HTTP URL (see [teams-post.md](teams-post.md)) |

Authenticate **Atlassian** in Cursor before saving. An unauthenticated Jira connection blocks the automation from saving.

## Instructions (paste into the prompt)

```
Follow the Pattern Data daily progress skill at .cursor/skills/pattern-data-daily-progress/SKILL.md and its references (document-template.md, jira-sync.md, salesforce-deploy.md, domain-decisions.md). Do not skip that skill.

Target today's calendar date. This is a weekday-morning Jira-only run:

1. Bootstrap Daily Progress/pattern-data-delivery-progress-YYYY-MM-DD.md from the most recent file in Daily Progress/ if today's file does not exist. Update only the As of header, Jira sync date, and standup/Austin input dates. Leave historical event dates unchanged.
2. If today's ChartSwap standup .docx or Austin-class transcript is missing from Transcript/, skip transcript extraction. Keep Austin's last deployment plan. Do not invent standup action items. Default Islam's Team focus to PD sandbox testing of LNI-3763 RequestShare unless a transcript says otherwise.
3. Sync Datavant Jira on DVI-1086 (epics → open stories → open subtasks) before editing the report. Parse story comments for PR and changeset status. Exclude Youssef Yahia. Team focus: Michael and Sarah from Jira assignees.
4. Update all report sections per the skill template. Recompute Path to UAT N/M. Replace the Standup action items section: if there was no standup transcript, keep prior open Jira-driven next steps only — do not fabricate owners or meetings.
5. Optionally align Testing Updates.md. Delete temp extract files.
6. git fetch origin, rebase onto the latest default branch if needed, then open a pull request with today's progress markdown (and Testing Updates.md if changed). Do not push to the default branch. Do not force-push.
7. After the PR exists, run:
   python .cursor/skills/pattern-data-daily-progress/scripts/post_progress_to_teams.py --pr-url "<the PR url>"
   The card inlines the full progress report (Teams cannot attach .md or HTML). TEAMS_WEBHOOK_URL is a Cloud Agent secret. Never print, commit, or echo the webhook URL.
8. Reply with the skill's "When done" summary plus the PR URL and whether the Teams post succeeded.

Do not use wave / Wave 1 / Wave 2 language.
```

## After save

1. Confirm Atlassian (Jira) is connected for Cloud Agents.
2. Confirm `TEAMS_WEBHOOK_URL` is set on the environment this automation uses.
3. Run once manually from the Automations page before relying on the weekday cron.
4. Confirm a PR opened and a Teams card arrived in the channel bound to the Power Automate flow.
