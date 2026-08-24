# Domain decisions — Pattern Data daily progress

Standing decisions from prior sessions. Apply unless standup or user explicitly overrides.

## Delivery phases

Active work is **PD sandbox finalize → UAT sandbox (feature-by-feature) → Production**. Pre-UAT provider testing, OC-9223 bug tracking, and **wave-based release planning** are **retired** from the daily progress report.

| Phase | Target |
| --- | --- |
| UAT sandbox | **2026-08-31** |
| Production | **2026-09-30** |

Dates are **indicative** — **Austin** (engineering manager) may change deployment order or targets after each meeting. Update from the latest **Austin-class** transcript when provided.

## Austin — engineering manager

| Role | Name | Source for |
| --- | --- | --- |
| Engineering manager | **Austin** | Deployment priority, scope in/out, UAT/Prod dates, next feature to promote |

- Austin may **change the plan frequently** — do not hard-code a fixed release sequence beyond what Austin last confirmed
- **Deployment plan (Austin)** section in each report reflects the latest Austin input
- **Austin-class transcripts** (latest dated file wins):
  - `Transcript/PDReviewWithAustin/PDReviewWithAustin-YYYY-MM-DD` — PD Review with Austin (plain text, `.txt`, or `.docx`)
  - `Transcript/Austin Meeting/Pattern-Data-Austin-YYYY-MM-DD.docx` — shorter Austin meeting
- Prefer **PD Review** when both exist for the same date
- When Austin and Jira disagree on priority, **Austin-class transcript wins** for deployment order; Jira wins for dev status
- Incomplete PD Review (timestamp jump): backfill only from Jira comments titled **Austin requirement sync** on that date with `Call / source: PD Review`

## Standing decisions — PD Review 2026-08-20

Apply until a later Austin-class transcript overrides:

| Topic | Decision |
| --- | --- |
| After current wrap-up | **Approved Fee overhaul first**, then other reuse work |
| Applied payment | Applied-payment process should use the **new approved fee** |
| CSI invoice line items | Later — status sync / retrieval first; line items so CSI can display them come after |
| PCI cart | Functionally works; **look Monday** (week of 2026-08-24) — possible page redesign only |
| Account / new-account flag | Sarah asked which features the flag controls. **No new Account Active Flag this release** — emergency firm SSO suspend is suffix the firm external ID (`-cancelled` / `-suspended`) |
| Autopay threshold (new accounts) | Leave **blank** (not zero); GetThreshold falls back to partner master |
| Status sync reuse | Design for reuse beyond Pattern Data (other integrations) |
| Islam access | Datavant account **in progress** (Austin answering a question); hoped the week of 2026-08-24 |
| Sarah | PTO after 2026-08-20; reconvene **Monday** |

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

Follow up with **Austin on Islam's Datavant / Jira access** until resolved — action owner **Hamed** or **Nabawy** (not Salah). As of PD Review **2026-08-20**, Austin said an account is **in progress** (hoped week of 2026-08-24).

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
