---

name: pattern-data-daily-progress

description: >-

  Build or update the Pattern Data daily delivery progress report from ChartSwap

  standup transcripts, Austin engineering-manager meetings, PD Review with Austin

  transcripts, and live Datavant Jira on feature DVI-1086. Use when the user asks

  for a daily progress report, standup sync, Austin meeting sync, PD Review sync,

  pattern-data-daily-progress update, PD delivery plan update, or to copy/create

  today's progress markdown from a transcript.

disable-model-invocation: true

---



# Pattern Data — Daily Progress Report



Build or update the dated delivery progress markdown from standup transcripts, **Austin-class transcripts** (Austin meeting **or** PD Review with Austin), and live Jira on feature [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086).



## Project paths



- `Daily Progress/pattern-data-delivery-progress-YYYY-MM-DD.md` — primary deliverable

- `Transcript/ChartSwap Daily Stand up/ChartSwap-Daily-Stand-up-YYYY-MM-DD.docx` — daily standup transcript

- `Transcript/PDReviewWithAustin/PDReviewWithAustin-YYYY-MM-DD.docx` — **PD Review with Austin** (Microsoft Word `.docx`; primary Austin-class source). Legacy plain-text copies without extension are still supported.

- `Transcript/Austin Meeting/Pattern-Data-Austin-YYYY-MM-DD.docx` — shorter Austin engineering-manager meeting (same class as PD Review)

- `Daily Actions/daily-actions-YYYY-MM-DD.md` — optional separate action tracker (not used as source for the progress report)

- `Testing Updates.md` — optional sync after progress update



## Engineering manager — Austin



**Austin** is the engineering manager and **owns deployment order and scope**. He may change the plan or next deployment frequently.



**Austin-class transcripts** (treat the same; use the **latest dated** file):



| Source | Typical file | Use for |

| --- | --- | --- |

| **PD Review with Austin** | `Transcript/PDReviewWithAustin/PDReviewWithAustin-YYYY-MM-DD.docx` | Long review — deployment order, scope, implementation direction, next-up work after wrap-up |

| **Austin meeting** | `Transcript/Austin Meeting/Pattern-Data-Austin-YYYY-MM-DD.docx` | Shorter EM meeting — same fields |



When either is provided:



1. Extract **deployment priority**, **scope in/out**, **date changes**, and **implementation direction**

2. Update **Daily update from Austin**, **Status at a glance** (Forecast / Notes), **Feature delivery tracker** Next step, and **Path to UAT** targets if Austin changed them

3. Record Austin-driven follow-ups in **Risks & challenges** mitigations, **Daily update from Austin** notes, or tracker **Next step** — not in a separate action-items section

4. If the transcript **jumps timestamps** (e.g. 1 min → 1h23) or is otherwise incomplete, do **not** invent the missing middle. Note the gap in *Last Austin input* and backfill only from Jira comments titled **Austin requirement sync** on that date whose `Call / source` is **PD Review**



**Do not use wave / Wave 1 / Wave 2 language** — retired delivery model. Use **feature-by-feature** promotion per Austin's current plan.



## Workflow



Copy this checklist and track progress:



```

- [ ] 1. Determine today's date (YYYY-MM-DD)

- [ ] 2. Bootstrap file (copy prior day OR open today's file)

- [ ] 3. Extract standup transcript (if provided)

- [ ] 3b. Extract Austin-class transcript (PD Review with Austin and/or Austin meeting) — update deployment plan first

- [ ] 4. Sync Datavant Jira: DVI-1086 → epics → open stories → open subtasks (exclude Youssef Yahia)

- [ ] 5. Parse story comments for PR + changeset status

- [ ] 6. Extract Islam focus from standup (default: LNI-3763 RequestShare testing); exclude Youssef subtasks

- [ ] 7. Update all report sections per template (Austin plan overrides static assumptions)

- [ ] 8. Compute Path to UAT/Prod checklist counts (N/M features UAT-ready)

- [ ] 9. Optionally sync Testing Updates.md

- [ ] 10. Delete temp extract files

- [ ] 11. git fetch + pull --ff-only, commit today's progress on **main**, push to origin (no PR)

- [ ] 12. Post Adaptive Card to Teams via TEAMS_WEBHOOK_URL (scripts/post_progress_to_teams.py)

```



### Step 1 — Bootstrap



**Target date:** use **today** (current calendar day) unless the user invokes `/pattern-data-daily-progress YYYY-MM-DD` or names another date in chat.



**Morning automation (Jira-only):** a weekday Cursor Automation may run before standup transcripts exist. If today's ChartSwap standup `.docx` and Austin-class transcript are missing, skip transcript extraction (checklist 3 / 3b). Keep Austin's last deployment plan. Default Islam to RequestShare / LNI-3763. Still bootstrap today's file and sync Jira. See [references/automation-prompt.md](references/automation-prompt.md).

**Transcript arrives later same day:** if a morning Jira-only file was already written and today's standup `.docx` or Austin-class transcript is added afterward, **re-run the skill** (or update in place): extract the transcript and apply standup/Austin deltas to **Status at a glance**, **Team focus**, **Feature delivery tracker** Next step, **Daily update from Austin** day-to-day notes, and **Risks** — do not leave a "no transcript yet" note once the file exists.



**If today's file does not exist:** copy the most recent `Daily Progress/pattern-data-delivery-progress-*.md` and rename to today's date. Update only:

- `**As of:**` header

- Jira sync date line in Feature delivery tracker

- Standup / Austin plan input dates



Leave historical event dates unchanged (e.g. when a CS was uploaded).



**If today's file exists:** update in place from standup + Austin-class transcript + Jira.



### Step 2 — Extract transcripts



Transcripts are Arabic/English mixed **Microsoft Word** `.docx` files (standup, PD Review, Austin meeting). Legacy PD Review plain-text copies without extension still work. **Always pass the `.docx` path** to the extractor — `extract_standup.py` only parses Word when the filename ends in `.docx`. Run from the skill directory (write UTF-8 temp file; do not print to console on Windows):



```bash

python scripts/extract_standup.py "Transcript/ChartSwap Daily Stand up/ChartSwap-Daily-Stand-up-YYYY-MM-DD.docx" -o _standup_extract.txt

python scripts/extract_standup.py "Transcript/PDReviewWithAustin/PDReviewWithAustin-YYYY-MM-DD.docx" -o _austin_extract.txt

python scripts/extract_standup.py "Transcript/Austin Meeting/Pattern-Data-Austin-YYYY-MM-DD.docx" -o _austin_extract.txt

```



**PD Review `.docx` content:** The Word file may include both the **meeting transcript** (speaker lines, timestamps) and **reference material** (e.g. Pending Wordings review document). Use transcript sections for **Daily update from Austin** (deployment priority, scope, dates). Use wordings tables for **Risks**, wordings delivery gates, and tracker wordings — do not treat a wordings-only extract as an Austin deployment meeting.



Prefer **PD Review with Austin** when both Austin-class files exist for the same date. Delete `_standup_extract.txt` and `_austin_extract.txt` when done.



**Priority when both standup and Austin-class exist:** Austin-class sets **deployment plan and dates**; standup sets **day-to-day dev/QA progress** for tracker and Status at a glance.



### Step 3 — Sync Datavant Jira



Sync **before** editing the report. See [references/jira-sync.md](references/jira-sync.md) for JQL chain, cloud ID, PR/changeset parsing, and assignee mapping.



Also see [references/salesforce-deploy.md](references/salesforce-deploy.md) for changeset validation rules.



### Step 4 — Islam focus



**Islam** has no Jira account yet. Populate his Team focus row from the **standup transcript** when Islam is mentioned. If no standup or Islam not mentioned, use the standing default: **PD sandbox testing of [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare** (implemented by Sarah).



Standing item: **Hamed** or **Nabawy** follows up with **Austin on Islam's Jira access** (Risks mitigations when still open).



### Step 4b — Exclude Youssef



**Youssef Yahia is off the project.** Do not list subtasks, stories, or Team focus rows for his Jira assignments — they are legacy. Filter out on every sync (see [references/jira-sync.md](references/jira-sync.md)).



### Step 5 — Update sections



Apply standup + Austin-class deltas to the progress report. See [references/document-template.md](references/document-template.md) for section structure, transcript mapping, and worked examples.

### Standup content vs Standup action items section

**Removing the Standup action items section is not removing standup from the report.** The retired block was only the bottom `## Standup action items` table. Standup transcripts must still drive:

- **Status at a glance** — today's What's done / What's left / Notes
- **Team focus** — especially Islam; Michael/Sarah day-to-day when standup mentions them
- **Feature delivery tracker** — `**Update YYYY-MM-DD:**` in Next step
- **Daily update from Austin** — day-to-day standup notes (Austin-class transcripts still own deployment priority)
- **Risks & challenges** — mitigations when standup surfaces blockers

Assigned follow-ups go in those sections — **not** in a separate action-items table. Use `Daily Actions/daily-actions-YYYY-MM-DD.md` if a standalone action tracker is needed.

Put assigned next steps in **tracker Next step**, **Status at a glance**, or **Risks** mitigations — not a separate action-items section.



### Step 6 — Domain decisions



Apply standing business rules. See [references/domain-decisions.md](references/domain-decisions.md).



### Step 7 — Testing Updates.md (optional)



Align phase summary with today's progress. Set `Last updated` and `Updated by: Standup sync (pattern-data-delivery-progress-YYYY-MM-DD)`.



### Step 8 — Commit to main



After the progress markdown is written (and `Testing Updates.md` if changed):



1. `git fetch origin`

2. Check out **main** (or `master` if that is the default) and `git pull --ff-only`

3. Stage only the progress deliverable(s): `Daily Progress/pattern-data-delivery-progress-YYYY-MM-DD.md` and `Testing Updates.md` if you updated it

4. Commit with a short message (why: standup/Jira sync for that date)

5. `git push origin HEAD` to **main**



Do **not** open a pull request. Do **not** force-push. Do **not** commit `.env.local`, webhook URLs, or other secrets. Skip the commit if there are no file changes.



### Step 9 — Post to Teams (webhook)



Post the progress report as a **full-width Adaptive Card** via **`TEAMS_WEBHOOK_URL`** (Power Automate incoming webhook). Follow [references/teams-post.md](references/teams-post.md):



```bash

py -3 .cursor/skills/pattern-data-daily-progress/scripts/post_progress_to_teams.py --date YYYY-MM-DD

```



The script includes all report sections (Status at a glance, Daily update from Austin, Feature tracker, Team focus, Path to UAT & Production, Risks) and **skips** legacy **How to read** and **Standup action items** blocks if present. It splits into multiple messages when needed.



Never print `TEAMS_WEBHOOK_URL` or other secrets from `.env.local`.



## When done



Reply with:



1. The file path created or updated

2. **Status at a glance** — phase row summary (what changed today)

3. **Daily update from Austin** — current priority if an Austin-class transcript was applied

4. Feature tracker counts — stories in progress, ready-for-PR, UAT-ready (`N/M`)

5. Michael / Sarah / Islam focus one-liners

6. Path-to-UAT gate progress

7. Git: committed and pushed to **main** (or skipped if no changes). Teams: whether the Adaptive Card was posted via webhook (part count + HTTP status)

8. **Hamed / Nabawy:** Austin or Islam Jira access follow-up if still open



## Additional resources



- [references/document-template.md](references/document-template.md) — section templates, transcript mapping, worked examples

- [references/jira-sync.md](references/jira-sync.md) — Datavant JQL, DVI-1086 hierarchy, PR/CS parsing

- [references/salesforce-deploy.md](references/salesforce-deploy.md) — changeset 3-pack, sandbox gates, wordings

- [references/domain-decisions.md](references/domain-decisions.md) — delivery targets, Austin plan, team sources

- [references/teams-post.md](references/teams-post.md) — Teams webhook Adaptive Card post

- [references/automation-prompt.md](references/automation-prompt.md) — weekday-morning Cursor Automation prompt

- [scripts/post_progress_to_teams.py](scripts/post_progress_to_teams.py) — markdown → Adaptive Card 1.5, webhook POST


