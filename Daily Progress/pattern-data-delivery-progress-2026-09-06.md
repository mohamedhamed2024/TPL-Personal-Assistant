# Pattern Data — delivery progress

**Feature:** [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) · **As of:** 2026-09-06  
**Targets:** UAT sandbox **2026-09-01** · Production **2026-09-08**

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **PD Sandbox finalize** | Team | In progress | <ul><li><strong>Standup 2026-09-06:</strong> Michael — homepage no longer updates AutoPay after pay; pay-button hide/disable in progress; duplicate-key check exists, PFINV send still to confirm</li><li>Sarah — RequestShare reviewer comments 6–7 addressed; comment 8 is new</li><li><strong>PD Review:</strong> Austin refined pending-unresolved job + disable pay buttons on click and when a transaction already exists</li></ul> | <ul><li>Wrap payment showstopper <strong>Sunday–Monday</strong> so deploy packages can be ready <strong>Tuesday</strong></li><li>Confirm PFINV / pay-key set and cleared on the request the same way as production; job must pick up only <strong>pending unresolved</strong> (not currently processing)</li><li>Nabawy re-run Copilot code scan after Michael commits</li><li>Client approval on <strong>4 BLOCKING</strong> consent wordings</li></ul> | Rolling | — | Austin available Sunday/Monday for questions (no meetings). Hamed / Nabawy to keep Austin from drip-feeding one change at a time |
| **UAT Sandbox deploy** | Team | Blocked | <ul><li>Epic [LNI-2309](https://datavant.atlassian.net/browse/LNI-2309) **UAT** in Jira; old Payment Management build in UAT</li><li>UAT promotion still paused until the double-charge fix is wrapped</li></ul> | <ul><li>Finish showstopper on pddev, then resume packaging — Austin wants changesets <strong>ready Tuesday</strong></li><li><strong>0/9</strong> features UAT-ready</li></ul> | **2026-09-01** | **Slipped** | UAT target **2026-09-01** missed; Tuesday package-ready is the new near-term gate |
| **Production** | Team | Not started | — | <ul><li>UAT sign-off; production deploy packages per feature</li></ul> | **2026-09-08** | **At risk** | Production target is **Tuesday** — same day Austin asked for changesets ready; **2 days** left |

---

## Daily update from Austin

*What Austin directed — deployment priority, scope, and what's next. Updated from PD Review or Austin meetings; may change day to day.*

| Priority | Feature / story | Environment | Status |
| --- | --- | --- | --- |
| 1 | **Lost Payflow response / double-charge prevention** — [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) / [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | pddev | **Wrap Sunday–Monday; packages ready Tuesday.** Job must process only **pending unresolved** (not currently processing). Disable pay buttons if a transaction already exists **and** immediately on click. Set/clear PFINV / pay key / PFIND on the **request** the same way as production (never clear from the transaction). Clean confusing AutoPay labels — AutoPay is only a trigger for a transaction |
| 2 | **Deploy packages ready** | pddev → UAT | UAT promotion still paused until showstopper wraps; Austin: have changesets ready **Tuesday 2026-09-08** |
| 3 | Consolidated deploy packages (all features) | pddev → UAT | **Deferred** — prior plan from PD Review **2026-08-26** resumes after showstopper |
| — | **PCI cart** | pddev | Independent deploy when packaging resumes |
| — | **Client wordings** | All features | **21** pending (**4 BLOCKING** consent) — still blocks package attach |

*Last Austin input:* [PD Review with Austin — 2026-09-06](../Transcript/PDReviewWithAustin/PDReviewWithAustin-2026-09-06) — transcript has a **timestamp jump** (~0:57 → ~1:19:22); middle not captured. Jira **Austin requirement sync** comments for this date could not be fetched (Datavant Jira unavailable this session). Captured start + close used above. Day-to-day from [ChartSwap Daily Stand-up — 2026-09-06](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-09-06.docx). Islam Jira access — still no update.

---

## Feature delivery tracker

*Synced from [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) on 2026-09-03 (last live). 2026-09-06 Datavant Jira unavailable this session — story statuses carried forward; standup and PD Review applied.*

*Deploy packages = Salesforce changesets: **Forward** (ship feature) + **Rollback** (undo if needed) + **Settings** (optional config flags).*

### [LNI-2309 — Payment Management](https://datavant.atlassian.net/browse/LNI-2309)

*Epic Jira status: **UAT** (as of 2026-09-03).*

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#220)</li><li><strong>Packages:</strong> Forward ✓ · Rollback ✓ · Settings ✓</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> Tested</li><li><strong>UAT sandbox:</strong> Old PM build — UAT promotion paused until showstopper wraps</li></ul> | **Update 2026-09-06:** Confirm hide/disable pay buttons (on click and if a transaction exists); PFINV / PFIND set and cleared on the request like production; pending-unresolved job only. Wrap Sunday–Monday |

### [LNI-2310 — AutoPay Submission Flow](https://datavant.atlassian.net/browse/LNI-2310)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#223)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-09-06:** Same showstopper — homepage no longer runs AutoPay post-pay updates; confirm duplicate-key / PFINV so concurrent Payflow calls cannot double-charge. Clean AutoPay-only naming if it confuses transaction types |

### [LNI-2311 — Authenticate & Provision Users via SAML SSO](https://datavant.atlassian.net/browse/LNI-2311)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) | Sarah | In Progress | <ul><li><strong>PR:</strong> In review (#193)</li><li><strong>Packages:</strong> Pending · Pending · Pending</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | No new Account Active Flag — emergency firm SSO suspend is suffix the firm external ID (`-cancelled` / `-suspended`) |

### [LNI-2312 — Status Sync — Request State Management & Webhook Notifications](https://datavant.atlassian.net/browse/LNI-2312)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#221, #222)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-08-26:** Request sync naming; Van alignment on upload / request ID — secondary to payment showstopper |

*Open subtasks*

| Sub-task | Assignee | Status | Notes |
| --- | --- | --- | --- |
| [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708) | Michael | To Do | Track: PD ingestion fails on application/octet-stream PDFs from ChartSwap S3 |

### [LNI-2313 — Receive & Store Patient Data via Order Initialization API](https://datavant.atlassian.net/browse/LNI-2313)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3139](https://datavant.atlassian.net/browse/LNI-3139) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#219)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Finalize PR #219; keep partner `externalReferenceId` passthrough — after payment showstopper |

### [LNI-3141 — Invoice Upload to S3](https://datavant.atlassian.net/browse/LNI-3141)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3142](https://datavant.atlassian.net/browse/LNI-3142) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#216)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Finish code review on PR #216; build deploy packages — after payment showstopper |

### [LNI-3216 — General](https://datavant.atlassian.net/browse/LNI-3216)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3225](https://datavant.atlassian.net/browse/LNI-3225) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#211–#213)</li><li><strong>Packages:</strong> Pending · Pending · Pending</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Turn off non-applicable features and emails for Pattern Data requests |
| [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) | Sarah | In Progress | <ul><li><strong>PR:</strong> In review (#256, #253)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval — 21 items in official review doc</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-09-06:** Reviewer comments 6–7 addressed; comment 8 is new. Sarah to pick remaining scan comments so work is not all on Michael |
| [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#231)</li><li><strong>Packages:</strong> Pending · Pending · Pending</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Add ability to disable Mail Order / SFTP for Pattern Data accounts |

*Open subtasks*

| Sub-task | Assignee | Status | Notes |
| --- | --- | --- | --- |
| [LNI-4978](https://datavant.atlassian.net/browse/LNI-4978) | Sarah | In Progress | Resolve remaining reviewer comments (comment 8 new; 6–7 addressed) on PR #256, #253 (RequestShare) |

---

## Team focus

| Member | Focus |
| --- | --- |
| **Michael** | Wrap payment showstopper Sunday–Monday: hide/disable pay buttons, PFINV / PFIND request clearing, pending-unresolved job only; commit so Nabawy can re-run Copilot scan. Loop Nabawy into Austin chats |
| **Sarah** | [LNI-4978](https://datavant.atlassian.net/browse/LNI-4978) / [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare — remaining reviewer comments; take scan comments off Michael where possible; [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) SSO |
| **Islam** | PD sandbox testing of [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare (Sarah's implementation) |

---

## Path to UAT & Production

**UAT-ready progress:** **0/9** features UAT-ready (see Feature delivery tracker)

### To reach UAT sandbox (target 2026-09-01)

- [ ] All in-scope stories finalized/refactored on **pddev**
- [ ] Each feature: **Forward + Rollback** deploy packages built (Settings package if needed)
- [ ] Each package uploaded and **tested on pddev**, then promoted to **UAT sandbox** (one feature at a time)
- [ ] **Client wordings (PATTERNDATA)** approved and attached to each package
- [ ] Code review complete — pull request merged for each feature

### To reach Production (target 2026-09-08)

- [ ] UAT validation complete for every feature
- [ ] Austin / client sign-off on UAT completion (per current deployment plan)
- [ ] Production deploy packages built per feature (same 3-pack pattern)
- [ ] Production release + smoke test

---

## Risks & challenges

Each item below is stated as a **condition → consequence**, with a mitigation that addresses that specific consequence.

| # | Risk / challenge | Mitigation | Severity |
| --- | --- | --- | --- |
| 1 | **Islam cannot log defects or update Jira.** Islam has no Jira account — QA progress is invisible in the tracker and defects may be tracked only in standup or chat. Datavant IT said **HR approval** is required; Austin's follow-up with Datavant HR/IT is inconsistent. | <ul><li>**Austin** owns the Datavant HR/IT ticket — still no update</li><li>**Hamed / Nabawy** keep following Austin (still open **2026-09-06**)</li></ul> | Medium |
| 2 | **Client wordings (PATTERNDATA) are not approved for any feature.** Official review doc lists **21** pending wordings — **4 BLOCKING** consent/legal items. Deploy packages cannot be finalized with approved copy until Legal/Business sign-off. | <ul><li>Islam implementing wordings as **custom labels** on open PRs</li><li>Escalate **4 BLOCKING** consent wordings to Mariah Ritter / Legal</li><li>Do not attach PATTERNDATA text to packages until approved</li></ul> | Medium |
| 3 | **Lost Payflow response can double-charge** — Austin showstopper; blocks UAT and threatens Production **2026-09-08**. | <ul><li>Michael: wrap Sunday–Monday — pending-unresolved job, hide/disable pay buttons, PFINV/PFIND request clearing like production</li><li>Nabawy re-run Copilot scan after Michael commits; Sarah take remaining comments where possible</li><li>**Hamed / Nabawy** stay on Austin calls so new payment rules are not drip-fed one at a time</li><li>Austin wants changesets ready **Tuesday**; he is reachable Sunday/Monday for questions</li></ul> | **High** |
