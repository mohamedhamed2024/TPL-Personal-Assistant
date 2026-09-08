# Pattern Data — delivery progress

**Feature:** [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) · **As of:** 2026-09-08  
**Targets:** UAT sandbox **2026-09-01** · Production **2026-09-08**

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **PD Sandbox finalize** | Team | In progress | <ul><li><strong>Standup 2026-09-08:</strong> Hamed / Nabawy / Sarah / Michael worked ~11 hours yesterday with Austin on the payment showstopper</li><li><strong>Two criticals (C1 / C2) done</strong> — remaining Copilot highs are review-only, not blockers</li><li>Austin agreed to keep timeout simple: do <strong>not</strong> re-run job logic in the UI; the recovery job already handles a lost Payflow response</li></ul> | <ul><li>Michael: one remaining failure case on the current PR — spinner <strong>timeout</strong> must show a <strong>Custom Label</strong> message (job may have already run)</li><li>Then Michael builds / validates <strong>deploy packages</strong>; Hamed + Sarah split scenario retest of Austin-agreed items</li><li>Client approval on <strong>4 BLOCKING</strong> consent wordings</li></ul> | Rolling | — | Austin: <strong>short UAT window today</strong>. Standup: need <strong>production next Monday (2026-09-14)</strong>. Deployment docs exist per feature; consolidate only after UAT (Austin does not need a combined pack for UAT) |
| **UAT Sandbox deploy** | Team | In progress | <ul><li>Epic [LNI-2309](https://datavant.atlassian.net/browse/LNI-2309) **UAT** in Jira; old Payment Management build in UAT</li><li>Standup: one consolidated PR is the source for UAT packages once the timeout message lands</li></ul> | <ul><li>Finish timeout/failure message, then upload Forward + Rollback packages and test on pddev → UAT <strong>today</strong></li><li><strong>0/9</strong> features UAT-ready at morning Jira sync</li></ul> | **2026-09-01** | **Slipped** | Official UAT date missed; standup says the remaining UAT window is <strong>today</strong> |
| **Production** | Team | Not started | — | <ul><li>UAT sign-off; production deploy packages per feature</li></ul> | **2026-09-08** | **2026-09-14** | Official Production date is <strong>today</strong> and is missed. Austin (standup + Jira sync) is aiming for <strong>next Monday 2026-09-14</strong> |

---

## Daily update from Austin

*What Austin directed — deployment priority, scope, and what's next. Updated from PD Review or Austin meetings; may change day to day.*

| Priority | Feature / story | Environment | Status |
| --- | --- | --- | --- |
| 1 | **Lost Payflow response / double-charge prevention** — [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) / [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | pddev | **PD Review 2026-09-06** showstopper still in force. **Standup 2026-09-08:** two criticals closed; Austin agreed timeout must **not** duplicate job logic in the UI — show a Custom Label message and let the recovery job handle a lost response. Remaining: spinner timeout / failure message on the current PR. **Jira Austin sync 2026-09-08:** blocking spinner on Accept / Retry / Change Card; timeout + strings in Custom Labels; Pending with no PFINVNUM = Failed. On-page-load auto-recovery **deferred** |
| 2 | **Deploy packages → UAT today** | pddev → UAT | Austin: **short UAT window today**. Michael owns package build/validation after the timeout message; Hamed + Sarah retest Austin-agreed scenarios. Consolidated docs only after UAT |
| 3 | **Production** | Production | Standup: Austin said the team must be in **production next Monday (2026-09-14)**. Official target **2026-09-08** missed |
| — | Consolidated deploy packages (all features) | pddev → UAT | Still deferred for UAT; Michael: prepare UAT packages first, gather a combined pack later if Austin wants it for production |
| — | **PCI cart** | pddev | Independent deploy when packaging resumes |
| — | **Client wordings** | All features | **21** pending (**4 BLOCKING** consent) — still blocks package attach |

*Last Austin input:* [PD Review with Austin — 2026-09-06](../Transcript/PDReviewWithAustin/PDReviewWithAustin-2026-09-06) — transcript has a **timestamp jump** (~0:57 → ~1:19:22); middle not captured. Day-to-day from [ChartSwap Daily Stand-up — 2026-09-08](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-09-08.docx). Jira backfill: [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) *Austin requirement sync — 2026-09-08* (`Call / source:` Call with Austin Moss (2).vtt). No PD Review `.docx` for **2026-09-08**.

---

## Feature delivery tracker

*Synced from [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) on 2026-09-08 (live).*

*Deploy packages = Salesforce changesets: **Forward** (ship feature) + **Rollback** (undo if needed) + **Settings** (optional config flags).*

### [LNI-2309 — Payment Management](https://datavant.atlassian.net/browse/LNI-2309)

*Epic Jira status: **UAT** (as of 2026-09-08).*

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#220)</li><li><strong>Packages:</strong> Forward ✓ · Rollback ✓ · Settings ✓</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> Tested</li><li><strong>UAT sandbox:</strong> Old PM build — refresh after timeout message + new packages</li></ul> | **Update 2026-09-08:** Two criticals done. Land spinner timeout / failure Custom Label on the current PR, then Michael builds UAT packages today |

### [LNI-2310 — AutoPay Submission Flow](https://datavant.atlassian.net/browse/LNI-2310)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#223)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-09-08:** Finish timeout/failure message (Custom Label); confirm Stuck-Pending-no-PFINVNUM → Failed in the recovery job. Austin: do not re-implement job logic in the UI on spinner timeout. Then package for today’s UAT window |

### [LNI-2311 — Authenticate & Provision Users via SAML SSO](https://datavant.atlassian.net/browse/LNI-2311)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) | Sarah | In Progress | <ul><li><strong>PR:</strong> In review (#193)</li><li><strong>Packages:</strong> Pending · Pending · Pending</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | No new Account Active Flag — emergency firm SSO suspend is suffix the firm external ID (`-cancelled` / `-suspended`) |

### [LNI-2312 — Status Sync — Request State Management & Webhook Notifications](https://datavant.atlassian.net/browse/LNI-2312)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#221, #222)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-09-08:** Standup — sync “duplication” gap was the long Austin thread yesterday; Austin signed the scoped approach. Secondary to today’s payment timeout + packages |

*Open subtasks*

| Sub-task | Assignee | Status | Notes |
| --- | --- | --- | --- |
| [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708) | Michael | To Do | Track: PD ingestion fails on application/octet-stream PDFs from ChartSwap S3 |

### [LNI-2313 — Receive & Store Patient Data via Order Initialization API](https://datavant.atlassian.net/browse/LNI-2313)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3139](https://datavant.atlassian.net/browse/LNI-3139) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#219)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Finalize PR #219; keep partner `externalReferenceId` passthrough — after today’s payment packages |

### [LNI-3141 — Invoice Upload to S3](https://datavant.atlassian.net/browse/LNI-3141)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3142](https://datavant.atlassian.net/browse/LNI-3142) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#216)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Finish code review on PR #216; build deploy packages — after today’s payment packages |

### [LNI-3216 — General](https://datavant.atlassian.net/browse/LNI-3216)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3225](https://datavant.atlassian.net/browse/LNI-3225) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#211–#213)</li><li><strong>Packages:</strong> Pending · Pending · Pending</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Turn off non-applicable features and emails for Pattern Data requests; Record Finder tab stays enabled (Austin **2026-08-31**) |
| [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) | Sarah | In Progress | <ul><li><strong>PR:</strong> In review (#256, #253)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval — 21 items in official review doc</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-09-08:** Sarah’s RequestShare comments were yesterday’s long thread; [LNI-4978](https://datavant.atlassian.net/browse/LNI-4978) **Done**. Hamed + Sarah split scenario retest of Austin-agreed items while Michael packages |
| [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#231)</li><li><strong>Packages:</strong> Pending · Pending · Pending</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Add ability to disable Mail Order / SFTP for Pattern Data accounts |

---

## Team focus

| Member | Focus |
| --- | --- |
| **Michael** | Land spinner timeout / failure Custom Label on [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) / [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223), then **build and validate UAT deploy packages today**. Also open: [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226), [LNI-3139](https://datavant.atlassian.net/browse/LNI-3139), [LNI-3142](https://datavant.atlassian.net/browse/LNI-3142), [LNI-3225](https://datavant.atlassian.net/browse/LNI-3225), [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769), subtask [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708) |
| **Sarah** | Split scenario retest with Hamed of Austin-agreed payment / RequestShare items. [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare (PR #256 / #253). [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) SAML SSO PR #193 |
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
| 1 | **Islam cannot log defects or update Jira.** Islam has no Jira account — QA progress is invisible in the tracker and defects may be tracked only in standup or chat. Datavant IT said **HR approval** is required; Austin's follow-up with Datavant HR/IT is inconsistent. | <ul><li>Standup **2026-09-07:** Michael raised Datavant / Islam access; Mohamed Ahmed said he will request IT add to the security group — Islam not mentioned in today’s standup; still not confirmed in Jira</li><li>**Hamed / Nabawy** keep following Austin and this IT request (still open **2026-09-08**)</li></ul> | Medium |
| 2 | **Client wordings (PATTERNDATA) are not approved for any feature.** Official review doc lists **21** pending wordings — **4 BLOCKING** consent/legal items. Deploy packages cannot be finalized with approved copy until Legal/Business sign-off. | <ul><li>Islam implementing wordings as **custom labels** on open PRs</li><li>Escalate **4 BLOCKING** consent wordings to Mariah Ritter / Legal</li><li>Do not attach PATTERNDATA text to packages until approved</li></ul> | Medium |
| 3 | **Lost Payflow response can double-charge** — Austin showstopper. Official Production **2026-09-08** is missed; remaining UAT window is **today**. | <ul><li>Two criticals closed; remaining gap is spinner timeout / failure Custom Label (Austin: do not duplicate job logic in the UI)</li><li>Michael packages today after that PR change; Hamed + Sarah retest Austin-agreed scenarios</li><li>**Hamed / Nabawy** stay on Austin so scope does not reopen; standup working Production date is **Monday 2026-09-14**</li></ul> | **High** |
