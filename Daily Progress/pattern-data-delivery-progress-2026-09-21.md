# Pattern Data — delivery progress

**Feature:** [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) · **As of:** 2026-09-21  
**Targets:** UAT sandbox **2026-09-01** · Production **2026-09-08**

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **PD Sandbox finalize** | Team | In progress | <ul><li><strong>Jira sync 2026-09-21 (morning):</strong> no story, subtask, or comment change since Sunday. 7 stories remain In Progress; SSO [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) and RequestShare [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) stay <strong>UAT</strong></li><li>Sunday close of SSO deployment subtask [LNI-5342](https://datavant.atlassian.net/browse/LNI-5342) (<strong>Done</strong>, ~13h) still the latest Jira event</li></ul> | <ul><li>Apply Code V13 + Rollback V2 test classes; land the dedicated Payment Transaction visibility flag</li><li>Finish UAT org config / Pattern Data accounts if still incomplete (Michael)</li><li>UAT smoke of SSO and RequestShare after Sunday’s status move — Sarah</li><li>Client approval on <strong>4 BLOCKING</strong> consent wordings</li></ul> | Rolling | — | Monday Jira-only run. No standup or Austin-class transcript for <strong>2026-09-21</strong>. Last captured standup in this report series was <strong>2026-09-10</strong> |
| **UAT Sandbox deploy** | Team | In progress | <ul><li>Epic [LNI-2309](https://datavant.atlassian.net/browse/LNI-2309) **UAT** in Jira</li><li>Stories [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) and [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) still **UAT** (moved 2026-09-20 by Sarah)</li><li>Payment packages uploaded 2026-09-08 (flow-dependency split) — last standup (2026-09-10) confirmed they are on UAT; Jira still does not mark UAT validated</li></ul> | <ul><li>Org config + smoke, then UAT test of business and SSO / RequestShare paths — not signed off</li><li><strong>0/9</strong> features UAT-ready (wordings still pending; UAT not validated)</li></ul> | **2026-09-01** | **Slipped** | Official UAT date missed. Jira UAT on SSO / RequestShare is not the same as UAT-ready — smoke, wordings, and client sign-off still required |
| **Production** | Team | Not started | — | <ul><li>UAT sign-off; production deploy packages per feature (same split journey Michael documented, plus Code V13 and Rollback V2 tests listed on [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137))</li></ul> | **2026-09-08** | **Slipped** | Official Production date missed. Last Austin / standup working date was <strong>Monday 2026-09-14</strong> — also missed (7 days ago). UAT still unsigned; no new Austin date this morning |

---

## Daily update from Austin

*What Austin directed — deployment priority, scope, and what's next. Updated from PD Review or Austin meetings; may change day to day.*

| Priority | Feature / story | Environment | Status |
| --- | --- | --- | --- |
| 1 | **Lost Payflow response / double-charge prevention** — [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) / [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | UAT | **PD Review 2026-09-06** showstopper still in force. Packages on UAT (flow-dependency split). Last standup (2026-09-10): start UAT testing (business with Sarah; SSO separately). **Jira Austin 2026-09-13:** test class list for **LNI-3137 Rollback V2**. **Jira 2026-09-14 (Luis):** test class list for forward package **LNI-3137 Pattern Data — Code V13**. **Jira Austin sync 2026-09-10:** Payment Transaction view needs a **standalone account flag** (supersedes “no extra flag”). ChartSwap refresh-hold for BAU remains **after Pattern Data** |
| 2 | **UAT config + smoke + test** | UAT | Austin short huddle (2026-09-09): **ready, have a plan, will deploy**. Last standup asked Hamed + Islam to start testing. **Jira 2026-09-20:** Sarah closed [LNI-5342](https://datavant.atlassian.net/browse/LNI-5342) and moved SSO [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) + RequestShare [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) to UAT — still UAT this morning, no new comments |
| 3 | **Production** | Production | Last confirmed working date **Monday 2026-09-14** is missed. Official target **2026-09-08** missed. No new Austin date. Use the same package-split journey as UAT; include Code V13 and Rollback V2 tests listed on [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) |
| — | Consolidated deploy packages (all features) | pddev → UAT | Still deferred for UAT; Michael documented the split so production can follow the same order |
| — | **PCI cart** | pddev | Independent; ChartSwap refresh-hold comment is after Pattern Data |
| — | **Client wordings** | All features | **21** pending (**4 BLOCKING** consent) — still blocks package attach |

*Last Austin input:* [PD Review with Austin — 2026-09-06](../Transcript/PDReviewWithAustin/PDReviewWithAustin-2026-09-06) — transcript has a **timestamp jump** (~0:57 → ~1:19:22); middle not captured. No PD Review, Austin meeting, or ChartSwap standup `.docx` for **2026-09-21**. Day-to-day last captured from [ChartSwap Daily Stand-up — 2026-09-10](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-09-10.docx). Jira backfill: no new comments or status moves since [LNI-5342](https://datavant.atlassian.net/browse/LNI-5342) **Done** **2026-09-20** (Sarah; ~13h) and parents [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) / [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) to **UAT**; prior [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) Luis comment **2026-09-14** (Code V13 deployment test classes), Austin comment **2026-09-13** (Rollback V2 test classes), plus [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) *Austin requirement sync — 2026-09-10* (`Call / source:` Call with Austin Moss (4)) and the earlier *Austin requirement sync — 2026-09-08*. **Baseline from Jira sync 2026-09-21.**

---

## Feature delivery tracker

*Synced from [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) on 2026-09-21 (live).*

*Deploy packages = Salesforce changesets: **Forward** (ship feature) + **Rollback** (undo if needed) + **Settings** (optional config flags).*

### [LNI-2309 — Payment Management](https://datavant.atlassian.net/browse/LNI-2309)

*Epic Jira status: **UAT** (as of 2026-09-21).*

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#220)</li><li><strong>Packages:</strong> Forward ✓ · Rollback ✓ · Settings ✓</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> Tested</li><li><strong>UAT sandbox:</strong> Uploaded 2026-09-08 — config + smoke remaining</li></ul> | **Update 2026-09-21:** Jira comments unchanged since Luis’s 2026-09-14 Code V13 list. Pair with Austin’s Rollback V2 list (2026-09-13). Complete UAT config/smoke and include both test lists before any production push |

### [LNI-2310 — AutoPay Submission Flow](https://datavant.atlassian.net/browse/LNI-2310)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#223)</li><li><strong>Packages:</strong> Forward ✓ · Rollback Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Uploaded with payment batch — not validated</li></ul> | **Update 2026-09-21:** Jira unchanged since 2026-09-10. Dedicated account-level flag for Payment Transaction visibility still required before ship. Include lost-Payflow / AutoPay path in UAT test |

### [LNI-2311 — Authenticate & Provision Users via SAML SSO](https://datavant.atlassian.net/browse/LNI-2311)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) | Sarah | UAT | <ul><li><strong>PR:</strong> In review (#193)</li><li><strong>Packages:</strong> Deployment activities closed on [LNI-5342](https://datavant.atlassian.net/browse/LNI-5342) — Forward / Rollback / Settings not yet marked validated in comments</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Jira UAT as of 2026-09-20 — not validated</li></ul> | **Update 2026-09-21:** Still UAT; no new comments since Sunday’s [LNI-5342](https://datavant.atlassian.net/browse/LNI-5342) close. Confirm SSO package set on UAT and run the SSO smoke path. No new Account Active Flag — emergency firm SSO suspend is suffix the firm external ID (`-cancelled` / `-suspended`) |

### [LNI-2312 — Status Sync — Request State Management & Webhook Notifications](https://datavant.atlassian.net/browse/LNI-2312)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#221, #222)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-09-21:** Jira unchanged. Secondary to UAT test — confirm whether status-sync components were in the 2026-09-08 UAT batch |

*Open subtasks*

| Sub-task | Assignee | Status | Notes |
| --- | --- | --- | --- |
| [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708) | Michael | To Do | Track: PD ingestion fails on application/octet-stream PDFs from ChartSwap S3 |

### [LNI-2313 — Receive & Store Patient Data via Order Initialization API](https://datavant.atlassian.net/browse/LNI-2313)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3139](https://datavant.atlassian.net/browse/LNI-3139) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#219)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Finalize PR #219; keep partner `externalReferenceId` passthrough — after UAT test |

### [LNI-3141 — Invoice Upload to S3](https://datavant.atlassian.net/browse/LNI-3141)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3142](https://datavant.atlassian.net/browse/LNI-3142) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#216)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Finish code review on PR #216; build deploy packages — after UAT test |

### [LNI-3216 — General](https://datavant.atlassian.net/browse/LNI-3216)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3225](https://datavant.atlassian.net/browse/LNI-3225) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#211–#213)</li><li><strong>Packages:</strong> Pending · Pending · Pending</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Turn off non-applicable features and emails for Pattern Data requests; Record Finder tab stays enabled (Austin **2026-08-31**) |
| [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) | Sarah | UAT | <ul><li><strong>PR:</strong> In review (#256, #253)</li><li><strong>Packages:</strong> Covered by SSO/RequestShare changeset guide on [LNI-5342](https://datavant.atlassian.net/browse/LNI-5342) — Forward / Rollback not yet marked validated in comments</li><li><strong>Wordings:</strong> Pending approval — 21 items in official review doc</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Jira UAT as of 2026-09-20 — not validated</li></ul> | **Update 2026-09-21:** Story comments still empty; Jira status still **UAT** (moved 2026-09-20). RequestShare remains Sarah’s implementation and Islam’s standing QA default. Confirm packages on UAT and smoke the share path |
| [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#231)</li><li><strong>Packages:</strong> Pending · Pending · Pending</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Add ability to disable Mail Order / SFTP for Pattern Data accounts |

---

## Team focus

| Member | Focus |
| --- | --- |
| **Michael** | [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) / [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) UAT config + smoke; **Code V13** forward tests (Luis **2026-09-14**) and **Rollback V2** tests (Austin **2026-09-13**); dedicated Payment Transaction visibility flag (Austin **2026-09-10**); also [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226), [LNI-3139](https://datavant.atlassian.net/browse/LNI-3139), [LNI-3142](https://datavant.atlassian.net/browse/LNI-3142), [LNI-3225](https://datavant.atlassian.net/browse/LNI-3225), [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769), subtask [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708) |
| **Sarah** | [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) SAML SSO and [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare still **UAT** in Jira; [LNI-5342](https://datavant.atlassian.net/browse/LNI-5342) Deployment Activities **Done**; confirm UAT package set + SSO/RequestShare smoke |
| **Islam** | PD sandbox testing of [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare (Sarah's implementation) — default; no standup today |

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
| 1 | **Islam cannot log defects or update Jira.** Islam has no Jira account — QA progress is invisible in the tracker and defects may be tracked only in standup or chat. Datavant IT said **HR approval** is required; Austin's follow-up with Datavant HR/IT is inconsistent. | <ul><li>No standup dated 2026-09-21 to confirm whether UAT testing continued over the weekend</li><li>**Hamed / Nabawy** keep following Austin and the IT security-group request (still open **2026-09-21**)</li></ul> | Medium |
| 2 | **Client wordings (PATTERNDATA) are not approved for any feature.** Official review doc lists **21** pending wordings — **4 BLOCKING** consent/legal items. Deploy packages cannot be finalized with approved copy until Legal/Business sign-off. | <ul><li>Islam implementing wordings as **custom labels** on open PRs</li><li>Escalate **4 BLOCKING** consent wordings to Mariah Ritter / Legal</li><li>Do not attach PATTERNDATA text to packages until approved</li></ul> | Medium |
| 3 | **Lost Payflow response can double-charge** — Austin showstopper. Official Production **2026-09-08** and working date **Monday 2026-09-14** are both missed, with UAT unsigned. Austin added a dedicated Payment Transaction visibility flag (2026-09-10) and a Rollback V2 test list (2026-09-13); Luis added a Code V13 forward test list (2026-09-14) that must land before ship. | <ul><li>Confirm UAT smoke, Code V13 + Rollback V2 tests, and the new PT visibility flag before any production push</li><li>Reuse the flow-dependency package split for production</li><li>**Hamed / Nabawy** stay on Austin so scope does not reopen; ask for a new Production working date now that **2026-09-14** has passed</li></ul> | **High** |
