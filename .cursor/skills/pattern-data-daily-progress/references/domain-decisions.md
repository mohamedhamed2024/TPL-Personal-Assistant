# Domain decisions — Pattern Data daily progress

Standing decisions from prior sessions. Apply unless standup or user explicitly overrides.

## Delivery phases

Active work is **PD sandbox finalize → UAT sandbox (feature-by-feature) → Production**. Pre-UAT provider testing, OC-9223 bug tracking, and **wave-based release planning** are **retired** from the daily progress report.

| Phase | Target |
| --- | --- |
| UAT sandbox | **2026-08-31** |
| Production | **2026-09-30** |

Dates are **indicative** — **Austin** (engineering manager) may change deployment order or targets after each meeting. Update from Austin meeting transcript when provided.

## Austin — engineering manager

| Role | Name | Source for |
| --- | --- | --- |
| Engineering manager | **Austin** | Deployment priority, scope in/out, UAT/Prod dates, next feature to promote |

- Austin may **change the plan frequently** — do not hard-code a fixed release sequence beyond what Austin last confirmed
- **Deployment plan (Austin)** section in each report reflects the latest Austin input
- Transcript path: `Transcript/Austin Meeting/Pattern-Data-Austin-YYYY-MM-DD.docx`
- When Austin and Jira disagree on priority, **Austin meeting transcript wins** for deployment order; Jira wins for dev status

## Jira source

- **Primary:** Datavant [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) → LNI epics → stories → subtasks
- **Not synced:** Ontellus OC-9223 bugs (historical reports only)

## Changeset rules

Per feature: **Forward + Rollback deploy packages** (+ optional **Settings** package), each ~2–8 hrs. Every package uploaded and tested on target sandbox before promotion. See [salesforce-deploy.md](salesforce-deploy.md).

## PATTERNDATA wordings

**PATTERNDATA — PENDING WORDINGS** must be approved before attaching to changesets. Blocks UAT-ready until approved.

## UAT promotion

**Feature-by-feature** — one feature per deploy package set, order set by **Austin**. Do not bundle all features in one changeset unless Austin explicitly agrees in a meeting.

## Team focus

| Member | Source |
| --- | --- |
| Michael | Jira assignee |
| Sarah | Jira assignee |
| Islam | **Standup transcript** when available; otherwise default: **PD sandbox testing of [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare** (Sarah's implementation) |

Follow up with **Austin on Islam's Jira access** until resolved — action owner **Hamed** or **Nabawy** (not Salah).

## PM / escalation owners

| Owner | Typical actions |
| --- | --- |
| **Hamed** | Client/technical escalations (Austin), Jira access, unblock dev |
| **Nabawy** | Delivery timeline, stakeholder updates, risk visibility |

## Youssef Yahia — excluded

**Youssef is off the project.** Do not list his Jira subtasks, stories, or assignee rows in the progress report — they are stale legacy items. Filter them out on every sync.

## PR readiness

If a story has **no open or in-progress pull request** in Jira comments, mark **Ready — finalize code review & deploy packages** in tracker.

## QA process

Dev should demo fix with tester before handing to QA (reduce ping-pong). Islam validates on pddev — primary focus **RequestShare** ([LNI-3763](https://datavant.atlassian.net/browse/LNI-3763)); standup may add other scenarios.

## Automation

Paused — manual retest unless standup says otherwise.

## Ambiguous scope

Ask user before changing how a story's deploy status affects Path to UAT counts.
