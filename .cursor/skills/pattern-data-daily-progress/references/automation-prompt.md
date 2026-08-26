# Cursor Automation — Pattern Data morning progress

Paste this into a new Cursor Automation. Create it at [cursor.com/automations](https://cursor.com/automations) or with `/automate` in the **Agents Window** (that editor is the only place that can save the live job).

The skill has `disable-model-invocation: true` — the automation **must** name this skill file. Do not rely on automatic skill attach.

## Editor settings

| Field | Value |
|-------|--------|
| **Name** | Pattern Data morning progress |
| **Description** | Weekday morning Jira sync of the Pattern Data delivery progress report. Commits to main and posts Adaptive Card to Teams via webhook. |
| **Trigger** | On a schedule — weekdays. Pick the Cairo morning hour in the editor (cron is stored as UTC). Example: 07:00 Africa/Cairo = `0 4 * * 1-5`. |
| **Repository** | This repo, **main** |
| **Tools** | Atlassian (Jira); git push to main |
| **Memories** | Off unless you need cross-run notes |
| **Secrets** | `TEAMS_WEBHOOK_URL` |

Authenticate **Atlassian** in Cursor before saving. Unauthenticated MCP blocks save.

## Instructions (paste into the prompt)

```
Follow the Pattern Data daily progress skill at .cursor/skills/pattern-data-daily-progress/SKILL.md and its references (document-template.md, jira-sync.md, salesforce-deploy.md, domain-decisions.md, teams-post.md). Do not skip that skill.

Target today's calendar date. This is a weekday-morning Jira-only run:

1. Bootstrap Daily Progress/pattern-data-delivery-progress-YYYY-MM-DD.md from the most recent file in Daily Progress/ if today's file does not exist. Update only the As of header, Jira sync date, and standup/Austin input dates. Leave historical event dates unchanged.
2. If today's ChartSwap standup .docx or Austin-class transcript is missing from Transcript/, skip transcript extraction. Keep Austin's last deployment plan. Default Islam's Team focus to PD sandbox testing of LNI-3763 RequestShare unless a transcript says otherwise.
3. Sync Datavant Jira on DVI-1086 (epics → open stories → open subtasks) before editing the report. Parse story comments for PR and changeset status. Exclude Youssef Yahia. Team focus: Michael and Sarah from Jira assignees.
4. Update all report sections per the skill template. Do not add a Standup action items section — but still apply standup content to Status at a glance, Team focus, tracker Next step, and Risks when a transcript exists. Recompute Path to UAT N/M. Put follow-ups in tracker Next step, Status at a glance, or Risks mitigations (not a separate action-items table).
5. Optionally align Testing Updates.md. Delete temp extract files.
6. git fetch origin, checkout main, git pull --ff-only. Commit today's progress markdown (and Testing Updates.md if changed) on main. git push origin HEAD. Do not open a pull request. Do not force-push. Do not commit .env.local or secrets.
7. Post to Teams with scripts/post_progress_to_teams.py --date YYYY-MM-DD per teams-post.md. TEAMS_WEBHOOK_URL from the environment (do not print it). Never print tokens or secrets.
8. Reply with the skill's "When done" summary plus whether main was pushed and whether the Teams webhook post succeeded.

Do not use wave / Wave 1 / Wave 2 language.
```

## After save

1. Confirm Atlassian (Jira) is connected for Cloud Agents.
2. Confirm `TEAMS_WEBHOOK_URL` on that environment.
3. Run once manually from the Automations page before relying on the weekday cron.
4. Confirm a commit landed on **main** and the Adaptive Card appeared in the Teams channel.
