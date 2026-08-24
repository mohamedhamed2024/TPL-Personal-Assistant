# Pattern Data — delivery progress

**Feature:** [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) · **As of:** 2026-08-24  
**Targets:** UAT sandbox **2026-08-31** · Production **2026-09-30**

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **PD Sandbox finalize** | Team | In progress | <ul><li>Michael retested **file attach** — working so far; sent to Austin</li><li>Islam collected **PATTERNDATA wordings** from pull requests into Excel</li></ul> | <ul><li>Align Austin / Van on which **record types** go in status sync</li><li>Move wordings to **custom labels**</li><li>**PCI cart** look</li></ul> | Rolling | — | Standup **2026-08-24** — Thursday is a holiday (short week) |
| **UAT Sandbox deploy** | Team | In progress | <ul><li>Payment Management deploy packages built; UAT upload in progress</li></ul> | <ul><li>Austin said he **may start promoting this week or next**</li><li>Remaining features **one at a time**</li></ul> | **2026-08-31** | **2026-08-31** | Austin is shipping other work first, then Pattern Data |
| **Production** | Team | Not started | — | <ul><li>UAT sign-off; production deploy packages per feature</li></ul> | **2026-09-30** | **2026-09-30** | Live release after UAT sign-off per Austin |

---

## Deployment plan (Austin)

*Engineering manager **Austin** sets deployment order and scope — this may change after each Austin meeting or PD Review.*

| Priority | Feature / story | Environment | Status |
| --- | --- | --- | --- |
| 1 | Wrap current PD details — [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) Payment Management + file attach | UAT sandbox | Michael's attach retest with Austin; Austin **may start UAT this week or next** |
| 2 | **Approved Fee overhaul** | pddev | Next after wrap-up (Austin, 2026-08-20) |
| 3 | **PCI cart** (not MPI) | pddev | Look this week — functionally works; page redesign possible |
| — | Remaining 8 stories | pddev → UAT | Queue per Austin — record types for status sync TBD with Van |

*Last plan input:* [PD Review with Austin — 2026-08-20](../Transcript/PDReviewWithAustin/PDReviewWithAustin-2026-08-20). Day-to-day from [ChartSwap Daily Stand-up — 2026-08-24](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-08-24.docx). Remind Austin **Thursday is a holiday**. Sarah on PTO.

---

## Feature delivery tracker

*Synced from [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) on 2026-08-24 (live).*

*Deploy packages = Salesforce changesets: **Forward** (ship feature) + **Rollback** (undo if needed) + **Settings** (optional config flags).*

### [LNI-2309 — Payment Management](https://datavant.atlassian.net/browse/LNI-2309)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) | Michael | In Progress | In review (#220) | Forward ✓ · Rollback ✓ · Settings ✓ | Pending approval | Tested | Upload in progress | **Update 2026-08-24:** Austin may start UAT this week or next; merge PR #220; finish UAT package upload |

### [LNI-2310 — AutoPay Submission Flow](https://datavant.atlassian.net/browse/LNI-2310)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | Michael | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · — | Pending approval | In progress | Not deployed | New requestor Autopay Threshold stays **blank** (not zero); GetThreshold falls back to partner master |

### [LNI-2311 — Authenticate & Provision Users via SAML SSO](https://datavant.atlassian.net/browse/LNI-2311)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) | Sarah | In Progress | In review (#193) | Pending · Pending · Pending | Pending approval | In progress | Not deployed | No new Account Active Flag this release — emergency firm SSO suspend is suffix the firm external ID (`-cancelled` / `-suspended`) |

### [LNI-2312 — Status Sync — Request State Management & Webhook Notifications](https://datavant.atlassian.net/browse/LNI-2312)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) | Michael | In Progress | In review (#222) | Pending · Pending · — | Pending approval | In progress | Not deployed | **Update 2026-08-24:** File attach retest sent to Austin; send Nabawy the record-type table; align Austin / Van on which types go in the API |

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
| [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) | Sarah | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · — | Pending approval | In progress | Not deployed | **Update 2026-08-24:** Islam inventoried wordings from PRs — review with Michael, then move to **custom labels** |
| [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769) | Michael | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · Pending | Pending approval | Not deployed | Not deployed | Add ability to disable Mail Order / SFTP for Pattern Data accounts |

---

## Team focus

| Member | Focus |
| --- | --- |
| **Michael** | File / record types on [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226); send Nabawy the type table; wordings review with Islam; **PCI cart** look |
| **Sarah** | PTO — Michael covers if her work needs a change |
| **Islam** | Tell Austin he can move wordings to **custom labels**; finish the Excel review with Michael, then migrate |

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
| 1 | **Islam cannot log defects or update Jira.** Islam has no Jira account — QA progress is invisible in the tracker and defects may be tracked only in standup or chat. | <ul><li>**Austin** said a Datavant account was in progress (hoped week of **2026-08-24**)</li><li>**Hamed / Nabawy** follow Austin until Islam can log in</li></ul> | Medium |
| 2 | **Client wordings (PATTERNDATA) are not approved for any feature.** All nine stories show wordings **Pending approval** — deploy packages cannot be finalized or attached with approved copy, blocking UAT promotion even when code is ready. | <ul><li>Islam inventoried wording from PRs (standup **2026-08-24**) — review with Michael, then move to custom labels</li><li>Islam to tell Austin today he can own the move</li><li>Do not attach PATTERNDATA text to packages until approved</li></ul> | Low |

---

## Standup action items (2026-08-24)

*From [ChartSwap Daily Stand-up — 2026-08-24](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-08-24.docx).*

| Owner | Action |
| --- | --- |
| **Austin** | Confirm whether UAT starts this week; finish **Islam's** Datavant account |
| **Hamed** | Follow Austin on **Islam's Datavant / Jira access** until the account is live |
| **Islam** | Tell Austin today he can move wordings to **custom labels**; finish the Excel review with Michael, then migrate |
| **Michael** | Send Nabawy the **record-type** table; set a group with Nabawy / Van / Austin on file types; look at **PCI cart** |
| **Nabawy** | Remind Austin on the channel that **Thursday is a holiday**; align Austin / Van that portal-visible files should go in the API before any filter |
