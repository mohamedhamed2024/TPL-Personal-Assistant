# Pattern Data — delivery progress

**Feature:** [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) · **As of:** 2026-08-27  
**Targets:** UAT sandbox **2026-08-31** · Production **2026-09-30**

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **PD Sandbox finalize** | Team | In progress | <ul><li>Jira sync **2026-08-27:** all **9** open stories still **In Progress** — no overnight status moves</li><li>[PD Review file — 2026-08-26](../Transcript/PDReviewWithAustin/PDReviewWithAustin-2026-08-26.docx): **21 pending wordings** in official review doc — **4 BLOCKING** consent items (W-001–W-004)</li><li>Islam mapping wording sentences to **custom labels** on open PRs (standup **2026-08-26**); Michael confirmed no provider-portal code touches ChartSwap</li></ul> | <ul><li>Client approval on **4 blocking** consent wordings (AutoPay, T&C SSO, over-threshold, card re-consent)</li><li>Islam: implement approved/pending wordings as custom labels; push to each open PR</li><li>Merge open PRs; build deploy packages for remaining features</li><li>Align Austin / Van on record types; PCI cart look</li></ul> | Rolling | — | **Thursday 2026-08-27** holiday — no standup. Sarah on PTO |
| **UAT Sandbox deploy** | Team | In progress | <ul><li>Payment Management deploy packages built; epic [LNI-2309](https://datavant.atlassian.net/browse/LNI-2309) **UAT** in Jira</li><li>Austin Change Set hold on SPM/AutoPay — no new UAT uploads until final approval (Jira comments **2026-08-25**)</li></ul> | <ul><li>Austin has **not started** promoting features — still busy with other work</li><li>Remaining features **one at a time** after Payment Management wrap-up</li></ul> | **2026-08-31** | **2026-08-31** | Austin is shipping other work first, then Pattern Data |
| **Production** | Team | Not started | — | <ul><li>UAT sign-off; production deploy packages per feature</li></ul> | **2026-09-30** | **2026-09-30** | Live release after UAT sign-off per Austin |

---

## Daily update from Austin

*What Austin directed — deployment priority, scope, and what's next. Updated from PD Review or Austin meetings; may change day to day.*

| Priority | Feature / story | Environment | Status |
| --- | --- | --- | --- |
| 1 | Wrap current PD details — [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) Payment Management + file attach | UAT sandbox | Attach retest with Austin; standup **2026-08-26**: UAT promotion still **not started** |
| 2 | **Approved Fee overhaul** | pddev | Next after wrap-up (Austin, 2026-08-20) |
| 3 | **PCI cart** (not MPI) | pddev | Look this week — functionally works; page redesign possible |
| — | Remaining 8 stories | pddev → UAT | Queue per Austin — record types for status sync TBD with Van |
| — | **Client wordings** | All features | **21** items pending in official review doc (**2026-08-26**); **4 BLOCKING** (W-001–W-004 consent/legal) — blocks attach to deploy packages |

*Last Austin input:* Deployment plan from [PD Review with Austin — 2026-08-20](../Transcript/PDReviewWithAustin/PDReviewWithAustin-2026-08-20). [PD Review file — 2026-08-26](../Transcript/PDReviewWithAustin/PDReviewWithAustin-2026-08-26.docx) is the **Pending Wordings Official Review** document (21 items, not a deployment meeting). Day-to-day from [ChartSwap Daily Stand-up — 2026-08-26](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-08-26.docx). **Thursday 2026-08-27** holiday — no standup. Sarah on PTO.

---

## Feature delivery tracker

*Synced from [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) on 2026-08-27 (live).*

*Deploy packages = Salesforce changesets: **Forward** (ship feature) + **Rollback** (undo if needed) + **Settings** (optional config flags).*

### [LNI-2309 — Payment Management](https://datavant.atlassian.net/browse/LNI-2309)

*Epic Jira status: **UAT** (as of 2026-08-27).*

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#220)</li><li><strong>Packages:</strong> Forward ✓ · Rollback ✓ · Settings ✓</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> Tested</li><li><strong>UAT sandbox:</strong> Upload in progress — Austin Change Set hold (open code set on pddev, not uploaded)</li></ul> | **Update 2026-08-27:** Jira unchanged. Merge PR #220; finish UAT package upload after Austin approval |

### [LNI-2310 — AutoPay Submission Flow](https://datavant.atlassian.net/browse/LNI-2310)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#223)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-08-25:** RF-035 heal on PR #223 (SMK-02 PASS). Austin Change Set hold — open pddev sets not uploaded. New requestor Autopay Threshold stays **blank** (not zero) |

### [LNI-2311 — Authenticate & Provision Users via SAML SSO](https://datavant.atlassian.net/browse/LNI-2311)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) | Sarah | In Progress | <ul><li><strong>PR:</strong> In review (#193)</li><li><strong>Packages:</strong> Pending · Pending · Pending</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | No new Account Active Flag this release — emergency firm SSO suspend is suffix the firm external ID (`-cancelled` / `-suspended`). Sarah on PTO |

### [LNI-2312 — Status Sync — Request State Management & Webhook Notifications](https://datavant.atlassian.net/browse/LNI-2312)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#221, #222)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-08-26:** Gap-cluster QA closed — zero FAIL/PARTIAL on qa/index.html. Align Austin / Van on record types; send Nabawy the record-type table |

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
| [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) | Sarah | In Progress | <ul><li><strong>PR:</strong> Ready — finalize code review & deploy packages</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval — 21 items in official review doc</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-08-27:** Official wordings doc lists **21** pending items (**4 BLOCKING** consent). Islam implementing as custom labels on open PRs. Sarah on PTO |
| [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#231)</li><li><strong>Packages:</strong> Pending · Pending · Pending</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Add ability to disable Mail Order / SFTP for Pattern Data accounts |

---

## Team focus

| Member | Focus |
| --- | --- |
| **Michael** | [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) Payment Management PR #220 + UAT CS; [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) AutoPay PR #223; [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) Status Sync PR #221/#222; [LNI-3139](https://datavant.atlassian.net/browse/LNI-3139) Prefill PR #219; [LNI-3142](https://datavant.atlassian.net/browse/LNI-3142) Invoice S3 PR #216; [LNI-3225](https://datavant.atlassian.net/browse/LNI-3225) PR #211–#213; [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769) PR #231 — from Jira |
| **Sarah** | [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) SAML SSO PR #193; [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare — from Jira. PTO — Michael covers if needed |
| **Islam** | Implement **21 pending wordings** as custom labels on open PRs (per Michael); **4 BLOCKING** consent items (W-001–W-004) need client approval before package attach |

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
| 1 | **Islam cannot log defects or update Jira.** Islam has no Jira account — QA progress is invisible in the tracker and defects may be tracked only in standup or chat. Datavant IT said **HR approval** is required; Austin's follow-up with Datavant HR/IT is inconsistent. | <ul><li>**Austin** owns the Datavant HR/IT ticket until Islam can log in</li><li>**Hamed / Nabawy** keep following Austin (week of **2026-08-24** target slipped — still open **2026-08-27**)</li></ul> | Medium |
| 2 | **Client wordings (PATTERNDATA) are not approved for any feature.** Official review doc (**2026-08-26**) lists **21** pending wordings — **4 BLOCKING** consent/legal items (W-001 AutoPay, W-002 T&C SSO, W-003 over-threshold, W-004 card re-consent). Deploy packages cannot be finalized with approved copy until Legal/Business sign-off. | <ul><li>Islam implementing wordings as **custom labels** on open PRs; Hamed shared doc — track which of **21** items are approved vs pending</li><li>Escalate **4 BLOCKING** consent wordings to Mariah Ritter / Legal — highest priority per doc</li><li>Do not attach PATTERNDATA text to packages until approved</li></ul> | Medium |
