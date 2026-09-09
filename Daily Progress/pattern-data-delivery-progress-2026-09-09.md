# Pattern Data — delivery progress

**Feature:** [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) · **As of:** 2026-09-09  
**Targets:** UAT sandbox **2026-09-01** · Production **2026-09-08**

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **PD Sandbox finalize** | Team | In progress | <ul><li><strong>Standup 2026-09-09:</strong> ChartSwap demo with Austin / Nabawy / Michael went well — partner questions on files; Austin will follow up</li><li>Michael uploaded code, features, and flows to <strong>UAT</strong> yesterday after splitting packages (flows need test classes first)</li><li>Austin 2-minute deploy huddle: team is ready, has a plan, will deploy</li></ul> | <ul><li>Configure UAT like pddev — settings and Pattern Data accounts (not started)</li><li>Smoke test the uploaded packages; Hamed + Sarah start UAT testing once they have accounts</li><li>Client approval on <strong>4 BLOCKING</strong> consent wordings</li></ul> | Rolling | — | Thursday <strong>2026-09-10</strong> is a holiday (standup). Austin still aiming for <strong>production Monday 2026-09-14</strong>. Repeat yesterday’s package split for production |
| **UAT Sandbox deploy** | Team | In progress | <ul><li>Epic [LNI-2309](https://datavant.atlassian.net/browse/LNI-2309) **UAT** in Jira</li><li>Standup: first deploy package went clean; second needed a flow-dependency split — code now on UAT</li></ul> | <ul><li>Org config (settings / Pattern Data accounts) then smoke test — not validated yet</li><li><strong>0/9</strong> features UAT-ready at morning Jira sync (wordings still pending; UAT not signed off)</li></ul> | **2026-09-01** | **Slipped** | Official UAT date missed; packages are on UAT but configuration and testing are today’s work |
| **Production** | Team | Not started | — | <ul><li>UAT sign-off; production deploy packages per feature (same split journey Michael documented)</li></ul> | **2026-09-08** | **2026-09-14** | Official Production date missed. Austin (short huddle + standup) still aiming for <strong>Monday 2026-09-14</strong> |

---

## Daily update from Austin

*What Austin directed — deployment priority, scope, and what's next. Updated from PD Review or Austin meetings; may change day to day.*

| Priority | Feature / story | Environment | Status |
| --- | --- | --- | --- |
| 1 | **Lost Payflow response / double-charge prevention** — [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) / [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | UAT | **PD Review 2026-09-06** showstopper still in force. **Standup 2026-09-09:** packages uploaded to UAT (flow-dependency split). Remaining: UAT settings / Pattern Data accounts + smoke. ChartSwap demo had a **refresh-hold** ask for business-as-usual — Austin: **not now**, after Pattern Data |
| 2 | **UAT config + smoke** | UAT | Austin short huddle: **ready, have a plan, will deploy**. Michael owns org config; Hamed + Sarah start testing. Hamed needs a UAT account |
| 3 | **Production** | Production | Standup: Austin still wants the team in **production next Monday (2026-09-14)**. Official target **2026-09-08** missed. Use the same package-split journey as UAT |
| — | Consolidated deploy packages (all features) | pddev → UAT | Still deferred for UAT; Michael documented the split so production can follow the same order |
| — | **PCI cart** | pddev | Independent; ChartSwap refresh-hold comment is after Pattern Data |
| — | **Client wordings** | All features | **21** pending (**4 BLOCKING** consent) — still blocks package attach |

*Last Austin input:* [PD Review with Austin — 2026-09-06](../Transcript/PDReviewWithAustin/PDReviewWithAustin-2026-09-06) — transcript has a **timestamp jump** (~0:57 → ~1:19:22); middle not captured. Day-to-day from [ChartSwap Daily Stand-up — 2026-09-09](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-09-09.docx) (Austin 2-minute deploy huddle + ChartSwap demo). Jira backfill still [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) *Austin requirement sync — 2026-09-08*. No PD Review `.docx` for **2026-09-09**.

---

## Feature delivery tracker

*Synced from [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) on 2026-09-09 (live).*

*Deploy packages = Salesforce changesets: **Forward** (ship feature) + **Rollback** (undo if needed) + **Settings** (optional config flags).*

### [LNI-2309 — Payment Management](https://datavant.atlassian.net/browse/LNI-2309)

*Epic Jira status: **UAT** (as of 2026-09-09).*

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#220)</li><li><strong>Packages:</strong> Forward ✓ · Rollback ✓ · Settings ✓</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> Tested</li><li><strong>UAT sandbox:</strong> Uploaded 2026-09-08 — config + smoke remaining</li></ul> | **Update 2026-09-09:** Packages on UAT (first set clean; second split for flow dependencies). Configure Pattern Data accounts / settings, then smoke |

### [LNI-2310 — AutoPay Submission Flow](https://datavant.atlassian.net/browse/LNI-2310)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#223)</li><li><strong>Packages:</strong> Forward ✓ · Rollback Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Uploaded with payment batch — not validated</li></ul> | **Update 2026-09-09:** Confirm AutoPay / lost-Payflow path on UAT after org config. Austin: refresh-hold for BAU is after Pattern Data |

### [LNI-2311 — Authenticate & Provision Users via SAML SSO](https://datavant.atlassian.net/browse/LNI-2311)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) | Sarah | In Progress | <ul><li><strong>PR:</strong> In review (#193)</li><li><strong>Packages:</strong> Pending · Pending · Pending</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | No new Account Active Flag — emergency firm SSO suspend is suffix the firm external ID (`-cancelled` / `-suspended`) |

### [LNI-2312 — Status Sync — Request State Management & Webhook Notifications](https://datavant.atlassian.net/browse/LNI-2312)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#221, #222)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-09-09:** Secondary to UAT config + smoke. Confirm whether status-sync components were in yesterday’s UAT batch |

*Open subtasks*

| Sub-task | Assignee | Status | Notes |
| --- | --- | --- | --- |
| [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708) | Michael | To Do | Track: PD ingestion fails on application/octet-stream PDFs from ChartSwap S3 |

### [LNI-2313 — Receive & Store Patient Data via Order Initialization API](https://datavant.atlassian.net/browse/LNI-2313)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3139](https://datavant.atlassian.net/browse/LNI-3139) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#219)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Finalize PR #219; keep partner `externalReferenceId` passthrough — after UAT config + smoke |

### [LNI-3141 — Invoice Upload to S3](https://datavant.atlassian.net/browse/LNI-3141)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3142](https://datavant.atlassian.net/browse/LNI-3142) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#216)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Finish code review on PR #216; build deploy packages — after UAT config + smoke |

### [LNI-3216 — General](https://datavant.atlassian.net/browse/LNI-3216)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3225](https://datavant.atlassian.net/browse/LNI-3225) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#211–#213)</li><li><strong>Packages:</strong> Pending · Pending · Pending</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Turn off non-applicable features and emails for Pattern Data requests; Record Finder tab stays enabled (Austin **2026-08-31**) |
| [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) | Sarah | In Progress | <ul><li><strong>PR:</strong> In review (#256, #253)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval — 21 items in official review doc</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-09-09:** Hamed + Sarah start UAT testing (Hamed needs a UAT login). RequestShare is the default pddev QA focus |
| [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#231)</li><li><strong>Packages:</strong> Pending · Pending · Pending</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Add ability to disable Mail Order / SFTP for Pattern Data accounts |

---

## Team focus

| Member | Focus |
| --- | --- |
| **Michael** | Configure UAT (settings + Pattern Data accounts) and smoke-test yesterday’s upload for [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) / [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223). Also open: [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226), [LNI-3139](https://datavant.atlassian.net/browse/LNI-3139), [LNI-3142](https://datavant.atlassian.net/browse/LNI-3142), [LNI-3225](https://datavant.atlassian.net/browse/LNI-3225), [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769), subtask [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708) |
| **Sarah** | Start UAT testing with Hamed once logins work. [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare (PR #256 / #253). [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) SAML SSO PR #193 |
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
| 1 | **Islam cannot log defects or update Jira.** Islam has no Jira account — QA progress is invisible in the tracker and defects may be tracked only in standup or chat. Datavant IT said **HR approval** is required; Austin's follow-up with Datavant HR/IT is inconsistent. | <ul><li>Standup **2026-09-07:** Michael raised Datavant / Islam access; Mohamed Ahmed said he will request IT add to the security group — Islam not mentioned in today’s standup; still not confirmed in Jira</li><li>**Hamed / Nabawy** keep following Austin and this IT request (still open **2026-09-09**)</li></ul> | Medium |
| 2 | **Client wordings (PATTERNDATA) are not approved for any feature.** Official review doc lists **21** pending wordings — **4 BLOCKING** consent/legal items. Deploy packages cannot be finalized with approved copy until Legal/Business sign-off. | <ul><li>Islam implementing wordings as **custom labels** on open PRs</li><li>Escalate **4 BLOCKING** consent wordings to Mariah Ritter / Legal</li><li>Do not attach PATTERNDATA text to packages until approved</li></ul> | Medium |
| 3 | **Lost Payflow response can double-charge** — Austin showstopper. Official Production **2026-09-08** is missed; UAT packages are uploaded but not configured or smoked. Thursday **2026-09-10** is a holiday. | <ul><li>Michael configures UAT accounts/settings today and smokes the upload; Hamed + Sarah start testing (Hamed needs a UAT login)</li><li>Reuse the flow-dependency package split for production</li><li>**Hamed / Nabawy** stay on Austin so scope does not reopen; working Production date is **Monday 2026-09-14**</li></ul> | **High** |
