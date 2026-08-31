# Pattern Data — delivery progress

**Feature:** [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) · **As of:** 2026-08-31  
**Targets:** UAT sandbox **2026-08-31** · Production **2026-09-30**

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **PD Sandbox finalize** | Team | In progress | <ul><li><strong>PD Review 2026-08-26:</strong> Austin — ready to <strong>start packaging</strong>; Michael to build deploy packages for <strong>all features</strong> (RequestShare included)</li><li>Provider-portal isolation confirmed; threshold, attachment, and after-completed fixes <strong>done</strong></li><li>PCI cart — <strong>functionally done</strong>; deploy <strong>independently</strong></li><li>Jira sync <strong>2026-08-31:</strong> 9 open stories unchanged; all still In Progress</li></ul> | <ul><li>Michael: consolidated <strong>3 deploy packages</strong> (settings/fields · code · rollback) — <strong>Monday</strong> check-in with Austin per PD Review</li><li>Map feature dependencies; align with Van on request-sync upload ([LNI-3226](https://datavant.atlassian.net/browse/LNI-3226))</li><li>SSO production-credentials test answer for Austin; payment transaction flow doc</li><li>Client approval on <strong>4 BLOCKING</strong> consent wordings</li></ul> | Rolling | — | No standup or Austin-class transcript since <strong>2026-08-26</strong> (Thu <strong>2026-08-27</strong> holiday; Fri–Mon no transcript). Sarah returned from PTO |
| **UAT Sandbox deploy** | Team | In progress | <ul><li>Epic [LNI-2309](https://datavant.atlassian.net/browse/LNI-2309) **UAT** in Jira; old Payment Management build in UAT — pddev is latest</li><li><strong>PD Review 2026-08-26:</strong> Michael <strong>cleared to start packaging</strong>; Luis can refresh UAT from master when Austin gives go-ahead</li></ul> | <ul><li>Finish package build on pddev; promote <strong>one consolidated push</strong> (or mapped smaller sets if dependency review allows)</li><li>Resolve what's in UAT — deploy or rollback before back-merge</li><li>PCI cart as separate deploy if scoped independently</li><li><strong>0/9</strong> features UAT-ready — packaging, PR merges, and wordings all block promotion</li></ul> | **2026-08-31** | **2026-08-31** | UAT target is <strong>today</strong> — milestone at risk unless packaging completes and Austin confirms promotion; no Jira movement since <strong>2026-08-30</strong> |
| **Production** | Team | Not started | — | <ul><li>UAT sign-off; production deploy packages per feature</li></ul> | **2026-09-30** | **2026-09-30** | Live release after UAT sign-off per Austin |

---

## Daily update from Austin

*What Austin directed — deployment priority, scope, and what's next. Updated from PD Review or Austin meetings; may change day to day.*

| Priority | Feature / story | Environment | Status |
| --- | --- | --- | --- |
| 1 | **All PD features** — consolidated deploy packages (RequestShare included) | pddev → UAT | **PD Review 2026-08-26:** Michael build **3 changesets** (settings/fields/connected apps · code · rollback); map dependencies to see if smaller sets possible — **Sunday** main focus, **Monday** check-in |
| 2 | **PCI cart** | pddev → UAT | Functionally **done** — deploy **independently**; optional iframe design tweak (smallest impact only) |
| 3 | [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) request sync | pddev | Clarify request-sync semantics with Van; post-completed upload / request ID behavior — Austin messaging Van |
| — | SSO production-credentials test | Client question | Cannot test prod SSO creds until production push — Michael to confirm classes and give Austin a solid answer |
| — | Payment transaction flow | Documentation | Austin still wants clear doc on transaction permutations and request/fulfillment field updates |
| — | **Client wordings** | All features | **21** pending items (**4 BLOCKING** consent) — blocks attach to deploy packages until approved |

*Last Austin input:* [PD Review with Austin — 2026-08-26](../Transcript/PDReviewWithAustin/PDReviewWithAustin-2026-08-26.docx) (30 min meeting). Day-to-day from [ChartSwap Daily Stand-up — 2026-08-26](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-08-26.docx). **Baseline from Jira sync 2026-08-31** — no standup or Austin-class transcript on file for 2026-08-28 through 2026-08-31. Islam Jira access — Austin no update yet (**2026-08-26**).

---

## Feature delivery tracker

*Synced from [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) on 2026-08-31 (live).*

*Deploy packages = Salesforce changesets: **Forward** (ship feature) + **Rollback** (undo if needed) + **Settings** (optional config flags).*

### [LNI-2309 — Payment Management](https://datavant.atlassian.net/browse/LNI-2309)

*Epic Jira status: **UAT** (as of 2026-08-31).*

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#220)</li><li><strong>Packages:</strong> Forward ✓ · Rollback ✓ · Settings ✓</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> Tested</li><li><strong>UAT sandbox:</strong> Old PM build in UAT — pddev is latest; repackage per Austin **2026-08-26</strong></li></ul> | **Update 2026-08-26:** Austin — same package for UAT and prod; start consolidated packaging. Merge PR #220; include in 3-pack build |

### [LNI-2310 — AutoPay Submission Flow](https://datavant.atlassian.net/browse/LNI-2310)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#223)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-08-25:** RF-035 heal on PR #223 (SMK-02 PASS). Austin Change Set hold — open pddev sets not uploaded. New requestor Autopay Threshold stays **blank** (not zero) |

### [LNI-2311 — Authenticate & Provision Users via SAML SSO](https://datavant.atlassian.net/browse/LNI-2311)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) | Sarah | In Progress | <ul><li><strong>PR:</strong> In review (#193)</li><li><strong>Packages:</strong> Pending · Pending · Pending</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | No new Account Active Flag this release — emergency firm SSO suspend is suffix the firm external ID (`-cancelled` / `-suspended`) |

### [LNI-2312 — Status Sync — Request State Management & Webhook Notifications](https://datavant.atlassian.net/browse/LNI-2312)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#221, #222)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-08-26:** Austin — call it **request sync** (not status sync); upload trigger OK. Van alignment on post-completed upload / request ID on upload object — Austin messaging Van |

*Open subtasks*

| Sub-task | Assignee | Status | Notes |
| --- | --- | --- | --- |
| [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708) | Michael | To Do | Track: PD ingestion fails on application/octet-stream PDFs from ChartSwap S3 |

### [LNI-2313 — Receive & Store Patient Data via Order Initialization API](https://datavant.atlassian.net/browse/LNI-2313)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3139](https://datavant.atlassian.net/browse/LNI-3139) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#219)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-08-25:** Prefill in-app nav skip QA PASS. Finalize PR #219; keep partner `externalReferenceId` passthrough |

### [LNI-3141 — Invoice Upload to S3](https://datavant.atlassian.net/browse/LNI-3141)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3142](https://datavant.atlassian.net/browse/LNI-3142) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#216)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-08-26:** All PARTIAL QA cases converted to PASS on pddev. Finish code review on PR #216; build deploy packages |

### [LNI-3216 — General](https://datavant.atlassian.net/browse/LNI-3216)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3225](https://datavant.atlassian.net/browse/LNI-3225) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#211–#213)</li><li><strong>Packages:</strong> Pending · Pending · Pending</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Turn off non-applicable features and emails for Pattern Data requests |
| [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) | Sarah | In Progress | <ul><li><strong>PR:</strong> Ready — finalize code review & deploy packages</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval — 21 items in official review doc</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-08-27:** Official wordings doc lists **21** pending items (**4 BLOCKING** consent). Islam implementing as custom labels on open PRs |
| [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#231)</li><li><strong>Packages:</strong> Pending · Pending · Pending</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Add ability to disable Mail Order / SFTP for Pattern Data accounts |

---

## Team focus

| Member | Focus |
| --- | --- |
| **Michael** | Consolidated **3 deploy packages** for all features — **Monday check-in** with Austin per PD Review **2026-08-26**; open PRs #219–#223, #231; [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) request sync; PCI cart independent deploy; SSO prod-creds answer; payment transaction flow doc — from Jira |
| **Sarah** | [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) SSO PR #193; [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare — included in consolidated package — from Jira |
| **Islam** | PD sandbox testing — [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare (Sarah's implementation) |

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
| 1 | **Islam cannot log defects or update Jira.** Islam has no Jira account — QA progress is invisible in the tracker and defects may be tracked only in standup or chat. Datavant IT said **HR approval** is required; Austin's follow-up with Datavant HR/IT is inconsistent. | <ul><li>**Austin** owns the Datavant HR/IT ticket — <strong>no update</strong> on PD Review **2026-08-26</strong> (message out, waiting on reply)</li><li>**Hamed / Nabawy** keep following Austin (still open **2026-08-31**)</li></ul> | Medium |
| 2 | **Client wordings (PATTERNDATA) are not approved for any feature.** Official review doc (**2026-08-26**) lists **21** pending wordings — **4 BLOCKING** consent/legal items (W-001 AutoPay, W-002 T&C SSO, W-003 over-threshold, W-004 card re-consent). Deploy packages cannot be finalized with approved copy until Legal/Business sign-off. | <ul><li>Islam implementing wordings as **custom labels** on open PRs; Hamed shared doc — track which of **21** items are approved vs pending</li><li>Escalate **4 BLOCKING** consent wordings to Mariah Ritter / Legal — highest priority per doc</li><li>Do not attach PATTERNDATA text to packages until approved</li></ul> | Medium |
