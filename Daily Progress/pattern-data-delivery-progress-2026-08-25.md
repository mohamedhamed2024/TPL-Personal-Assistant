# Pattern Data — delivery progress

**Feature:** [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) · **As of:** 2026-08-25  
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

---

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **PD Sandbox finalize** | Team | In progress | <ul><li>Michael shipped **RF-035 threshold heal** on [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) PR #220 and [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) PR #223 — SMK-02 PASS on pddev</li><li>Michael compared provider portal vs ChartSwap — only gap so far is the **upload file** page</li><li>Islam finished an Excel inventory of Pattern Data UI text from pull requests</li></ul> | <ul><li>Compare Islam's Excel to **Youssef's wording document**, then move differences to **custom labels**</li><li>Align Austin / Van on which **record types** go in status sync</li><li>**PCI cart** look</li></ul> | Rolling | — | Standup **2026-08-25** — Thursday **2026-08-27** is a holiday (short week). Sarah on PTO |
| **UAT Sandbox deploy** | Team | In progress | <ul><li>Payment Management deploy packages built; UAT upload in progress</li><li>Jira epic [LNI-2309](https://datavant.atlassian.net/browse/LNI-2309) moved to **UAT** (story [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) still In Progress)</li></ul> | <ul><li>Austin has **not started** promoting features — still busy with other work</li><li>Remaining features **one at a time**</li></ul> | **2026-08-31** | **2026-08-31** | Austin is shipping other work first, then Pattern Data |
| **Production** | Team | Not started | — | <ul><li>UAT sign-off; production deploy packages per feature</li></ul> | **2026-09-30** | **2026-09-30** | Live release after UAT sign-off per Austin |

---

## Deployment plan (Austin)

*Engineering manager **Austin** sets deployment order and scope — this may change after each Austin meeting or PD Review.*

| Priority | Feature / story | Environment | Status |
| --- | --- | --- | --- |
| 1 | Wrap current PD details — [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) Payment Management + file attach | UAT sandbox | Attach retest with Austin; Austin **may start UAT this week or next** — standup **2026-08-25**: promotion **not started** (Austin busy elsewhere) |
| 2 | **Approved Fee overhaul** | pddev | Next after wrap-up (Austin, 2026-08-20) |
| 3 | **PCI cart** (not MPI) | pddev | Look this week — functionally works; page redesign possible |
| — | Remaining 8 stories | pddev → UAT | Queue per Austin — record types for status sync TBD with Van |

*Last plan input:* [PD Review with Austin — 2026-08-20](../Transcript/PDReviewWithAustin/PDReviewWithAustin-2026-08-20). Day-to-day from [ChartSwap Daily Stand-up — 2026-08-25](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-08-25.docx). No Austin-class transcript on **2026-08-25**. Remind Austin **Thursday is a holiday**. Sarah on PTO.

---

## Feature delivery tracker

*Synced from [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) on 2026-08-25 (live).*

*Deploy packages = Salesforce changesets: **Forward** (ship feature) + **Rollback** (undo if needed) + **Settings** (optional config flags).*

### [LNI-2309 — Payment Management](https://datavant.atlassian.net/browse/LNI-2309)

*Epic Jira status: **UAT** (as of 2026-08-25).*

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) | Michael | In Progress | In review (#220) | Forward ✓ · Rollback ✓ · Settings ✓ | Pending approval | Tested | Upload in progress | **Update 2026-08-25:** RF-035 threshold heal on PR #220 (SMK-02 PASS). Epic **UAT** in Jira; Austin has not started promotion. Merge PR #220; finish UAT package upload |

### [LNI-2310 — AutoPay Submission Flow](https://datavant.atlassian.net/browse/LNI-2310)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | Michael | In Progress | In review (#223) | Pending · Pending · — | Pending approval | In progress | Not deployed | **Update 2026-08-25:** RF-035 heal on PR #223 (SMK-02 PASS). New requestor Autopay Threshold stays **blank** (not zero); GetThreshold falls back to partner master |

### [LNI-2311 — Authenticate & Provision Users via SAML SSO](https://datavant.atlassian.net/browse/LNI-2311)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) | Sarah | In Progress | In review (#193) | Pending · Pending · Pending | Pending approval | In progress | Not deployed | No new Account Active Flag this release — emergency firm SSO suspend is suffix the firm external ID (`-cancelled` / `-suspended`) |

### [LNI-2312 — Status Sync — Request State Management & Webhook Notifications](https://datavant.atlassian.net/browse/LNI-2312)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) | Michael | In Progress | In review (#222) | Pending · Pending · — | Pending approval | In progress | Not deployed | Align Austin / Van on which record types go in the API; send Nabawy the record-type table |

*Open subtasks*

| Sub-task | Assignee | Status | Notes |
| --- | --- | --- | --- |
| [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708) | Michael | To Do | Track: PD ingestion fails on application/octet-stream PDFs from ChartSwap S3 |

### [LNI-2313 — Receive & Store Patient Data via Order Initialization API](https://datavant.atlassian.net/browse/LNI-2313)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3139](https://datavant.atlassian.net/browse/LNI-3139) | Michael | In Progress | In review (#219) | Pending · Pending · — | Pending approval | In progress | Not deployed | **Update 2026-08-25:** Prefill in-app nav skip QA PASS. Finalize PR #219; keep partner `externalReferenceId` passthrough |

### [LNI-3141 — Invoice Upload to S3](https://datavant.atlassian.net/browse/LNI-3141)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3142](https://datavant.atlassian.net/browse/LNI-3142) | Michael | In Progress | In review (#216) | Pending · Pending · — | Pending approval | In progress | Not deployed | Finish Invoice S3 code review on PR #216; build deploy packages |

### [LNI-3216 — General](https://datavant.atlassian.net/browse/LNI-3216)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3225](https://datavant.atlassian.net/browse/LNI-3225) | Michael | In Progress | In review (#211–#213) | Pending · Pending · Pending | Pending approval | In progress | Not deployed | Turn off non-applicable features and emails for Pattern Data requests |
| [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) | Sarah | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · — | Pending approval | In progress | Not deployed | **Update 2026-08-25:** Islam inventoried UI text from PRs — **compare to Youssef's wording document** (Hamed to send), then move ChartSwap vs Pattern Data differences to **custom labels** |
| [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769) | Michael | In Progress | In review (#231) | Pending · Pending · Pending | Pending approval | In progress | Not deployed | Add ability to disable Mail Order / SFTP for Pattern Data accounts |

---

## Team focus

| Member | Focus |
| --- | --- |
| **Michael** | RF-035 threshold heal on [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) PR #220 and [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) PR #223; document provider-portal **upload file** page gap; [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) record types + [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708) octet-stream PDFs |
| **Sarah** | PTO — Michael covers if her work needs a change ([LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) SSO PR #193, [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare) |
| **Islam** | Compare the Excel of Pattern Data UI text to **Youssef's wording document**; only custom-label items that differ ChartSwap vs Pattern Data |

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
| 1 | **Islam cannot log defects or update Jira.** Islam has no Jira account — QA progress is invisible in the tracker and defects may be tracked only in standup or chat. Datavant IT said **HR approval** is required; Austin's follow-up with Datavant HR/IT is inconsistent. | <ul><li>**Austin** owns the Datavant HR/IT ticket until Islam can log in</li><li>**Hamed / Nabawy** keep following Austin (week of **2026-08-24** target slipped — still open **2026-08-25**)</li></ul> | Medium |
| 2 | **Client wordings (PATTERNDATA) are not approved for any feature.** All nine stories show wordings **Pending approval** — deploy packages cannot be finalized or attached with approved copy, blocking UAT promotion even when code is ready. | <ul><li>Islam inventoried UI text from PRs — **compare to Youssef's wording email/doc** (Hamed to send), then move ChartSwap vs Pattern Data differences to custom labels</li><li>Do not attach PATTERNDATA text to packages until approved</li></ul> | Low |

---

## Standup action items (2026-08-25)

*From [ChartSwap Daily Stand-up — 2026-08-25](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-08-25.docx) and live Jira comments the same day.*

| Owner | Action |
| --- | --- |
| **Austin** | Get **HR approval** for Islam's Datavant account (IT gate); confirm when UAT promotion actually starts |
| **Hamed** | Send Islam **Youssef's wording document/email**; keep following Austin on Islam's Datavant / Jira access until the account is live |
| **Islam** | Compare the Excel of Pattern Data UI text to Youssef's wording document; custom-label only ChartSwap vs Pattern Data differences |
| **Michael** | Document the provider-portal **upload file** page gap vs ChartSwap; land **RF-035** on PR **#220** / **#223** |
| **Nabawy** | Keep following Austin with Hamed on Islam's Datavant HR/IT approval |
