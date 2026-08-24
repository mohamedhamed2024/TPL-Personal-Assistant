# Pattern Data — delivery progress

**Feature:** [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) · **As of:** 2026-08-23  
**Targets:** UAT sandbox **2026-08-31** · Production **2026-09-30**

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **PD Sandbox finalize** | Team | In progress | <ul><li>Islam closed **RequestShare** testing Thursday</li><li>Michael replied to Austin on file / request-ID handling — first approach rejected</li></ul> | <ul><li>Match file attach to **BAU** (request ID only after paid)</li><li>Re-trigger when a file is uploaded **after Complete**</li></ul> | Rolling | — | Standup **2026-08-23** — Austin wants same business behavior as ChartSwap BAU; automation still off |
| **UAT Sandbox deploy** | Team | In progress | <ul><li>Payment Management deploy packages built; UAT upload in progress</li></ul> | <ul><li>Remaining features queued **one at a time**</li></ul> | **2026-08-31** | **2026-08-31** | Features promote per **Austin's** current plan |
| **Production** | Team | Not started | — | <ul><li>UAT sign-off; production deploy packages per feature</li></ul> | **2026-09-30** | **2026-09-30** | Live release after UAT sign-off per Austin |

---

## Deployment plan (Austin)

*Engineering manager **Austin** sets deployment order and scope — this may change after each Austin meeting or PD Review.*

| Priority | Feature / story | Environment | Status |
| --- | --- | --- | --- |
| 1 | Wrap current PD details — [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) Payment Management | UAT sandbox | Upload in progress — PR #220 in review; applied payment should use the **new approved fee** |
| 2 | **Approved Fee overhaul** | pddev | Next after wrap-up (Austin, 2026-08-20) |
| 3 | **PCI cart** (not MPI) | pddev | Look **Monday** (week of 2026-08-24) — functionally works; page redesign possible |
| — | Remaining 8 stories | pddev → UAT | Queue per Austin — status sync / invoice line items for CSI come later |

*Last plan input:* [PD Review with Austin — 2026-08-20](../Transcript/PDReviewWithAustin/PDReviewWithAustin-2026-08-20). Day-to-day from [ChartSwap Daily Stand-up — 2026-08-23](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-08-21.docx) (file dated 08-21; recording is **2026-08-23**). Sarah on PTO; Michael covers.

---

## Feature delivery tracker

*Synced from [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) on 2026-08-23 (live).*

*Deploy packages = Salesforce changesets: **Forward** (ship feature) + **Rollback** (undo if needed) + **Settings** (optional config flags).*

### [LNI-2309 — Payment Management](https://datavant.atlassian.net/browse/LNI-2309)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) | Michael | In Progress | In review (#220) | Forward ✓ · Rollback ✓ · Settings ✓ | Pending approval | Tested | Upload in progress | **Update 2026-08-23:** Wire applied payment to the **new approved fee**; merge PR #220; finish UAT package upload |

### [LNI-2310 — AutoPay Submission Flow](https://datavant.atlassian.net/browse/LNI-2310)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | Michael | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · — | Pending approval | In progress | Not deployed | **Update 2026-08-23:** New requestor Autopay Threshold stays **blank** (not zero); GetThreshold falls back to partner master |

### [LNI-2311 — Authenticate & Provision Users via SAML SSO](https://datavant.atlassian.net/browse/LNI-2311)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) | Sarah | In Progress | In review (#193) | Pending · Pending · Pending | Pending approval | In progress | Not deployed | **Update 2026-08-23:** No new Account Active Flag this release — emergency firm SSO suspend is suffix the firm external ID (`-cancelled` / `-suspended`) |

### [LNI-2312 — Status Sync — Request State Management & Webhook Notifications](https://datavant.atlassian.net/browse/LNI-2312)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) | Michael | In Progress | In review (#222) | Pending · Pending · — | Pending approval | In progress | Not deployed | **Update 2026-08-23:** Austin wants files to attach like BAU — request ID only after paid; re-trigger when a file is uploaded after Complete (first fix rejected) |

*Open subtasks*

| Sub-task | Assignee | Status | Notes |
| --- | --- | --- | --- |
| [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708) | Michael | To Do | Track: PD ingestion fails on application/octet-stream PDFs from ChartSwap S3 |

### [LNI-2313 — Receive & Store Patient Data via Order Initialization API](https://datavant.atlassian.net/browse/LNI-2313)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3139](https://datavant.atlassian.net/browse/LNI-3139) | Michael | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · — | Pending approval | In progress | Not deployed | Refactor Patient Prefill API on pddev; finalize code review |

### [LNI-3141 — Invoice Upload to S3](https://datavant.atlassian.net/browse/LNI-3141)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3142](https://datavant.atlassian.net/browse/LNI-3142) | Michael | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · — | Pending approval | Not deployed | Not deployed | Finish Invoice S3 code on pddev; build deploy packages |

### [LNI-3216 — General](https://datavant.atlassian.net/browse/LNI-3216)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3225](https://datavant.atlassian.net/browse/LNI-3225) | Michael | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · Pending | Pending approval | In progress | Not deployed | Turn off non-applicable features and emails for Pattern Data requests |
| [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) | Sarah | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · — | Pending approval | In progress | Not deployed | **Update 2026-08-23:** Islam closed RequestShare testing Thursday; sit with Michael today on **PATTERNDATA wordings** |
| [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769) | Michael | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · Pending | Pending approval | Not deployed | Not deployed | Add ability to disable Mail Order / SFTP for Pattern Data accounts |

---

## Team focus

| Member | Focus |
| --- | --- |
| **Michael** | Austin file / request-ID handling on [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) — match BAU (attach after paid) + re-trigger after Complete; wordings call with Islam today |
| **Sarah** | PTO — Michael covers if her work needs a change |
| **Islam** | Sit with Michael today on **PATTERNDATA wordings**; RequestShare ([LNI-3763](https://datavant.atlassian.net/browse/LNI-3763)) testing closed Thursday |

---

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

---

## Risks & challenges

Each item below is stated as a **condition → consequence**, with a mitigation that addresses that specific consequence.

| # | Risk / challenge | Mitigation | Severity |
| --- | --- | --- | --- |
| 1 | **Islam cannot log defects or update Jira.** Islam is testing RequestShare on pddev but has no Jira account — QA progress is invisible in the tracker and defects may be tracked only in standup or chat. | <ul><li>**Austin** is working a Datavant account question from PD Review **2026-08-20** — hoped week of **2026-08-24**</li><li>**Hamed / Nabawy** follow Austin until Islam can log in</li></ul> | Medium |
| 2 | **Client wordings (PATTERNDATA) are not approved for any feature.** All nine stories show wordings **Pending approval** — deploy packages cannot be finalized or attached with approved copy, blocking UAT promotion even when code is ready. | <ul><li>**Islam + Michael** sit today (standup **2026-08-23**) on wordings</li><li>Do not attach PATTERNDATA text to packages until approved</li></ul> | Low |

---

## Standup action items (2026-08-23)

*From [ChartSwap Daily Stand-up — 2026-08-23](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-08-21.docx) (recording date) and [PD Review with Austin — 2026-08-20](../Transcript/PDReviewWithAustin/PDReviewWithAustin-2026-08-20).*

| Owner | Action |
| --- | --- |
| **Austin** | Finish the Datavant-account question so **Islam** can get access (hoped week of 2026-08-24) |
| **Hamed** | Join the Austin chat on file / request-ID handling; post today's progress report to the group; follow Islam's Datavant / Jira access |
| **Islam** | Sit with **Michael** today on **PATTERNDATA wordings** |
| **Michael** | Match file attach to BAU (request ID only after paid) on [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226); add re-trigger when a file is uploaded after Complete; wordings call with Islam today |
| **Nabawy** | Align with Michael / Hamed on the file-after-Complete problem before Austin sets the approach |
