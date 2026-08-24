# Pattern Data — delivery progress

**Feature:** [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) · **As of:** 2026-08-24  
**Targets:** UAT sandbox **2026-08-31** · Production **2026-09-30**

## How to read this report

*Audience: delivery managers and stakeholders.*

| If you see… | It means… |
| --- | --- |
| **PD Sandbox finalize** | Dev team finishing and testing features on the Pattern Data development sandbox (pddev) |
| **UAT Sandbox deploy** | Approved features being moved **one at a time** to the pre-production UAT environment |
| **Deploy packages** | Salesforce outbound **changesets** — bundled code/config uploaded between environments (Forward + Rollback + optional Settings per feature) |
| **UAT-ready (N/M)** | **N** of **M** features have passed all gates to promote to UAT (code merged, packages validated, client wordings approved) |
| **Pending approval** (wordings) | Client copy/labels not yet signed off — blocks attaching text to the deploy package |
| **Deployment plan (Austin)** | Current feature promotion order and scope — set by engineering manager Austin; may change after each Austin meeting |

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **PD Sandbox finalize** | Team | In progress | <ul><li>Sarah closed RequestShare test-scenario + change-owner work ([LNI-4108](https://datavant.atlassian.net/browse/LNI-4108), [LNI-4438](https://datavant.atlassian.net/browse/LNI-4438))</li><li>Sarah closed SSO ops onboarding doc ([LNI-4619](https://datavant.atlassian.net/browse/LNI-4619)) and Account Active Flag investigation ([LNI-4636](https://datavant.atlassian.net/browse/LNI-4636))</li></ul> | <ul><li>All **9** stories still In Progress on pddev</li><li>New Status Sync tracker: octet-stream PDF ingest ([LNI-4708](https://datavant.atlassian.net/browse/LNI-4708))</li></ul> | Rolling | — | Jira-only sync **2026-08-24** — no standup or Austin meeting transcript on file today; last Austin plan remains **2026-08-20** |
| **UAT Sandbox deploy** | Team | In progress | <ul><li>Payment Management Forward + Rollback + Settings packages uploaded to UAT (2026-08-07)</li></ul> | <ul><li>UAT validation still open for [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137)</li><li>Remaining 8 features queued **one at a time** after Austin’s next call</li><li>Client wordings pending on all 9 features</li></ul> | **2026-08-31** | **2026-08-31** | Features promote **one at a time** per **Austin's** current deployment plan |
| **Production** | Team | Not started | — | <ul><li>UAT sign-off per feature</li><li>Production deploy packages after Austin / client approval</li></ul> | **2026-09-30** | **2026-09-30** | Production follows UAT sign-off per feature — plan set by Austin |

## Deployment plan (Austin)

*Engineering manager **Austin** sets deployment order and scope — this may change after each Austin meeting. Update this block from the latest Austin meeting transcript when provided.*

| Priority | Feature / story | Environment | Status |
| --- | --- | --- | --- |
| 1 | [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) Payment Management | UAT sandbox | Upload in progress — PR #220 in review; epic [LNI-2309](https://datavant.atlassian.net/browse/LNI-2309) in **UAT** |
| — | Remaining 8 stories | pddev → UAT | Queue per Austin — see Feature delivery tracker |

*Last plan input:* [ChartSwap Daily Stand-up — 2026-08-20](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-08-20.docx) — no ChartSwap standup or Austin meeting transcript on file for **2026-08-24**; carrying forward Austin’s last plan (Payment Management next for UAT). **RequestShare** remains the default Islam pddev focus.

## Feature delivery tracker

*Synced from [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) on 2026-08-24 (live).*

*Deploy packages = Salesforce changesets: **Forward** (ship feature) + **Rollback** (undo if needed) + **Settings** (optional config flags).*

### [LNI-2309 — Payment Management](https://datavant.atlassian.net/browse/LNI-2309)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) | Michael | In Progress | In progress (#220) | Forward ✓ · Rollback ✓ · Settings ✓ | Pending approval | Tested | Upload in progress | Merge PR #220; complete UAT package validation; get client wordings approved |

### [LNI-2310 — AutoPay Submission Flow](https://datavant.atlassian.net/browse/LNI-2310)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | Michael | In Progress | In progress (#238) | Pending · Pending · — | Pending approval | In progress | Not deployed | Finish AutoPay / GetThreshold work on pddev; finalize PR #238; build Forward + Rollback packages |

### [LNI-2311 — Authenticate & Provision Users via SAML SSO](https://datavant.atlassian.net/browse/LNI-2311)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) | Sarah | In Progress | In progress (#193) | Pending · Pending · Pending | Pending approval | In progress | Not deployed | Complete second PR #193 approval; document emergency SSO suspend runbook; build Forward + Rollback + Settings packages |

### [LNI-2312 — Status Sync — Request State Management & Webhook Notifications](https://datavant.atlassian.net/browse/LNI-2312)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) | Michael | In Progress | In progress (#221 · #222) | Pending · Pending · — | Pending approval | In progress | Not deployed | Finalize PRs #221 / #222; track octet-stream ingest ([LNI-4708](https://datavant.atlassian.net/browse/LNI-4708)); confirm Buy Now filter with ops |

*Open subtasks*

| Sub-task | Assignee | Status | Notes |
| --- | --- | --- | --- |
| [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708) | Michael | To Do | PD ingestion fails on application/octet-stream PDFs from ChartSwap S3 — PD-owned fix; ChartSwap re-tests after deploy |

### [LNI-2313 — Receive & Store Patient Data via Order Initialization API](https://datavant.atlassian.net/browse/LNI-2313)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3139](https://datavant.atlassian.net/browse/LNI-3139) | Michael | In Progress | In progress (#219) | Pending · Pending · — | Pending approval | In progress | Not deployed | Merge PR #219 (externalReferenceId passthrough); build Forward + Rollback packages |

### [LNI-3141 — Invoice Upload to S3](https://datavant.atlassian.net/browse/LNI-3141)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3142](https://datavant.atlassian.net/browse/LNI-3142) | Michael | In Progress | In progress (#216) | Pending · Pending · — | Pending approval | Tested | Not deployed | Finalize PR #216; build Forward + Rollback packages for Austin’s UAT queue |

### [LNI-3216 — General](https://datavant.atlassian.net/browse/LNI-3216)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3225](https://datavant.atlassian.net/browse/LNI-3225) | Michael | In Progress | In progress (#211 · #212 · #213) | Pending · Pending · Pending | Pending approval | In progress | Not deployed | Turn off non-applicable features and emails for Pattern Data requests; finalize PRs and deploy packages |
| [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) | Sarah | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · — | Pending approval | In progress | Not deployed | RequestShare implementation subtasks closed — keep available for Islam pddev testing; finalize code review and deploy packages |
| [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769) | Michael | In Progress | In progress (#231) | Pending · Pending · Pending | Pending approval | Tested | Not deployed | Finalize PR #231 (Mail Order / SFTP disable); build Forward + Rollback + Settings packages |

## Team focus

| Member | Focus |
| --- | --- |
| **Michael** | Payment Management UAT ([LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) PR #220); AutoPay ([LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) PR #238); Status Sync ([LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) PRs #221/#222) plus octet-stream tracker ([LNI-4708](https://datavant.atlassian.net/browse/LNI-4708)); Patient Prefill ([LNI-3139](https://datavant.atlassian.net/browse/LNI-3139)); Invoice S3 ([LNI-3142](https://datavant.atlassian.net/browse/LNI-3142)); General ([LNI-3225](https://datavant.atlassian.net/browse/LNI-3225), [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769)) |
| **Sarah** | SAML SSO ([LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) PR #193); **RequestShare** ([LNI-3763](https://datavant.atlassian.net/browse/LNI-3763)) — test-scenario and change-owner subtasks **Done** |
| **Islam** | PD sandbox testing of [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare (Sarah's implementation) — default (no standup transcript today) |

## Path to UAT & Production

**UAT-ready progress:** **0/9** features UAT-ready (see Feature delivery tracker)

### To reach UAT sandbox (target 2026-08-31)

- [ ] All in-scope stories finalized/refactored on **pddev**
- [ ] Each feature: **Forward + Rollback** deploy packages built (Settings package if needed)
- [ ] Each package uploaded and **tested on pddev**, then promoted to **UAT sandbox** (one feature at a time)
- [ ] **Client wordings (PATTERNDATA)** approved and attached to each package
- [ ] Code review complete — pull request merged for each feature

### To reach Production (target 2026-09-30)

- [ ] UAT validation complete for every feature
- [ ] Austin / client sign-off on UAT completion (per current deployment plan)
- [ ] Production deploy packages built per feature (same 3-pack pattern)
- [ ] Production release + smoke test

## Risks & challenges

Each item below is stated as a **condition → consequence**, with a mitigation that addresses that specific consequence.

| # | Risk / challenge | Mitigation | Severity |
| --- | --- | --- | --- |
| 1 | **Islam cannot log defects or update Jira.** Islam is testing RequestShare on pddev but has no Jira account — QA progress is invisible in the tracker and defects may be tracked only in standup or chat. | <ul><li>**Hamed** or **Nabawy** follow up with **Austin** on Islam's Jira access</li><li>Continue capturing Islam's status in Team focus until access is granted</li></ul> | Medium |
| 2 | **Client wordings (PATTERNDATA) are not approved for any feature.** All nine stories show wordings **Pending approval** — deploy packages cannot be finalized or attached with approved copy, blocking UAT promotion even when code is ready. | <ul><li>Escalate wordings review to Austin / client contacts via **Hamed** or **Nabawy**</li><li>Prioritize wordings for Payment Management ([LNI-3137](https://datavant.atlassian.net/browse/LNI-3137)) as the next feature Austin directed for UAT</li><li>Do not upload UAT packages until wordings are signed off per feature</li></ul> | Low |

---

## Standup action items (2026-08-24)

*No ChartSwap standup transcript on file for 2026-08-24. Open items below are Jira-driven next steps carried from the live tracker — not new meeting assignments.*

| Owner | Action |
| --- | --- |
| **Hamed** | Follow up with **Austin** on **Islam's Jira access** so QA defects can be logged in the tracker |
| **Islam** | Continue PD sandbox testing of **RequestShare** ([LNI-3763](https://datavant.atlassian.net/browse/LNI-3763)) — Sarah's implementation |
| **Michael** | Finalize **PR #220** and complete UAT package validation for Payment Management ([LNI-3137](https://datavant.atlassian.net/browse/LNI-3137)); continue AutoPay ([LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) PR #238) and Status Sync ([LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) PRs #221/#222) including octet-stream tracker ([LNI-4708](https://datavant.atlassian.net/browse/LNI-4708)) |
| **Nabawy** | Escalate **PATTERNDATA wordings** approval — blocks UAT attach for all nine features, starting with [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) |
| **Sarah** | Complete **PR #193** for SAML SSO ([LNI-3224](https://datavant.atlassian.net/browse/LNI-3224)); keep RequestShare ([LNI-3763](https://datavant.atlassian.net/browse/LNI-3763)) ready for Islam testing and finalize code review / deploy packages |
