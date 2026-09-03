# Pattern Data — delivery progress

**Feature:** [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) · **As of:** 2026-09-03  
**Targets:** UAT sandbox **2026-09-01** · Production **2026-09-08**

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **PD Sandbox finalize** | Team | In progress | <ul><li><strong>Standup 2026-09-03:</strong> Nabawy shared Copilot <strong>code scan</strong> vs Austin PD Review gaps — critical / medium items categorized; Michael validating; most yesterday PR comments addressed</li><li>Sarah on [LNI-4978](https://datavant.atlassian.net/browse/LNI-4978) — RequestShare PR #256 / #253 reviewer comments</li><li>Michael removed invalid PayPal <strong>cost ID</strong> from body; <strong>idempotency</strong> belongs in header (per Nabawy / Austin thread)</li></ul> | <ul><li><strong>PD Review 2026-09-02 showstopper:</strong> prevent <strong>double charge</strong> on lost Payflow response — pending-transaction job, homepage recovery, block new transactions + hide pay buttons</li><li>Michael: validate Copilot scan — fix <strong>critical</strong> gaps first; pair with Sarah on components if needed</li><li>Client approval on <strong>4 BLOCKING</strong> consent wordings</li></ul> | Rolling | — | Austin **2026-09-02:** <strong>all hands on deck</strong> on payment resilience — <strong>pause UAT packaging</strong> until fixed. Team Claude subscription on hold (Austin review next week) |
| **UAT Sandbox deploy** | Team | Blocked | <ul><li>Epic [LNI-2309](https://datavant.atlassian.net/browse/LNI-2309) **UAT** in Jira; old Payment Management build in UAT</li><li><strong>PD Review 2026-09-02:</strong> Austin — <strong>don't push to UAT now</strong>; he will handle stakeholders and may <strong>push deployment date</strong></li></ul> | <ul><li>Resolve payment <strong>showstopper</strong> on pddev first</li><li>Then resume consolidated packaging (per **2026-08-26** plan)</li><li><strong>0/9</strong> features UAT-ready</li></ul> | **2026-09-01** | **Slipped** | UAT target **2026-09-01** missed; Austin may slip deployment further for double-charge fix |
| **Production** | Team | Not started | — | <ul><li>UAT sign-off; production deploy packages per feature</li></ul> | **2026-09-08** | **At risk** | **5 days** to Production target with UAT blocked on showstopper |

---

## Daily update from Austin

*What Austin directed — deployment priority, scope, and what's next. Updated from PD Review or Austin meetings; may change day to day.*

| Priority | Feature / story | Environment | Status |
| --- | --- | --- | --- |
| 1 | **Lost Payflow response / double-charge prevention** — [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) / [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) payment flows | pddev | **PD Review 2026-09-02 showstopper** — (1) pending-transaction deem job, (2) homepage recovery must not conflict with pending transactions, (3) before any new transaction: block if request already on pending transaction; <strong>hide/disable pay buttons</strong>. Trial logic can double-charge on lost response |
| 2 | **UAT promotion** | UAT sandbox | <strong>Paused</strong> — Austin: focus on showstopper; he owns UAT stakeholder comms; may push deployment date |
| 3 | Consolidated deploy packages (all features) | pddev → UAT | **Deferred** — prior plan from PD Review **2026-08-26** resumes after showstopper |
| — | **PCI cart** | pddev | Independent deploy when packaging resumes |
| — | **Client wordings** | All features | **21** pending (**4 BLOCKING** consent) — still blocks package attach |

*Last Austin input:* [PD Review with Austin — 2026-09-02](../Transcript/PDReviewWithAustin/PDReviewWithAustin-2026-09-02) — transcript has a <strong>timestamp jump</strong> (~0:28 → ~1:01:35); payment / pending-transaction section captured above. Day-to-day from [ChartSwap Daily Stand-up — 2026-09-03](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-09-03.docx). Islam Jira access — still no update. Jira synced **2026-09-03** (morning).

---

## Feature delivery tracker

*Synced from [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) on 2026-09-03 (live).*

*Deploy packages = Salesforce changesets: **Forward** (ship feature) + **Rollback** (undo if needed) + **Settings** (optional config flags).*

### [LNI-2309 — Payment Management](https://datavant.atlassian.net/browse/LNI-2309)

*Epic Jira status: **UAT** (as of 2026-09-03).*

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#220)</li><li><strong>Packages:</strong> Forward ✓ · Rollback ✓ · Settings ✓</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> Tested</li><li><strong>UAT sandbox:</strong> Old PM build — UAT promotion paused (**2026-09-02**)</li></ul> | **Update 2026-09-02:** Austin showstopper — pending-transaction job, recovery process, block duplicate charges on lost Payflow response. **Update 2026-09-03:** Validate Copilot critical scan gaps |

### [LNI-2310 — AutoPay Submission Flow](https://datavant.atlassian.net/browse/LNI-2310)

| Story | Assignee | Jira status | Delivery gates | Next step |
| --- | --- | --- | --- | --- |
| [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#223)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-09-02:** Same double-charge / pending-transaction showstopper as Payment Management. Idempotency via header, not BFM in body (**2026-09-03** standup) |

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
| [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) | Sarah | In Progress | <ul><li><strong>PR:</strong> In review (#256, #253)</li><li><strong>Packages:</strong> Pending · Pending · —</li><li><strong>Wordings:</strong> Pending approval — 21 items in official review doc</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | **Update 2026-09-03:** [LNI-4978](https://datavant.atlassian.net/browse/LNI-4978) — resolve reviewer comments on PR #256, #253; SAML duplication GROUP BY note — low priority (owner vs manual share only) |
| [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769) | Michael | In Progress | <ul><li><strong>PR:</strong> In review (#231)</li><li><strong>Packages:</strong> Pending · Pending · Pending</li><li><strong>Wordings:</strong> Pending approval</li><li><strong>PD sandbox:</strong> In progress</li><li><strong>UAT sandbox:</strong> Not deployed</li></ul> | Add ability to disable Mail Order / SFTP for Pattern Data accounts |

*Open subtasks*

| Sub-task | Assignee | Status | Notes |
| --- | --- | --- | --- |
| [LNI-4978](https://datavant.atlassian.net/browse/LNI-4978) | Sarah | In Progress | Resolve reviewer comments on PR #256, #253 (RequestShare) |

---

## Team focus

| Member | Focus |
| --- | --- |
| **Michael** | **PD Review 2026-09-02 showstopper** — pending-transaction job, lost Payflow / double-charge prevention, hide pay buttons; validate Nabawy's Copilot <strong>critical</strong> scan gaps; PayPal idempotency header; available to pair with Sarah after Austin items |
| **Sarah** | [LNI-4978](https://datavant.atlassian.net/browse/LNI-4978) — RequestShare PR #256 / #253 reviewer comments; [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) SSO PR #193; pair with Michael on components / branch definition when needed |
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
| 1 | **Islam cannot log defects or update Jira.** Islam has no Jira account — QA progress is invisible in the tracker and defects may be tracked only in standup or chat. Datavant IT said **HR approval** is required; Austin's follow-up with Datavant HR/IT is inconsistent. | <ul><li>**Austin** owns the Datavant HR/IT ticket — still no update</li><li>**Hamed / Nabawy** keep following Austin (still open **2026-09-03**)</li></ul> | Medium |
| 2 | **Client wordings (PATTERNDATA) are not approved for any feature.** Official review doc lists **21** pending wordings — **4 BLOCKING** consent/legal items. Deploy packages cannot be finalized with approved copy until Legal/Business sign-off. | <ul><li>Islam implementing wordings as **custom labels** on open PRs</li><li>Escalate **4 BLOCKING** consent wordings to Mariah Ritter / Legal</li><li>Do not attach PATTERNDATA text to packages until approved</li></ul> | Medium |
| 3 | **Lost Payflow response can double-charge** — Austin **2026-09-02** showstopper; blocks UAT and threatens Production **2026-09-08**. | <ul><li>Michael: pending-transaction job + homepage recovery fix + block new transactions when pending; hide pay buttons in UI</li><li>Nabawy Copilot scan — fix <strong>critical</strong> gaps first; cloud code review as needed</li><li>Austin paused UAT promotion and may slip deployment date</li></ul> | **High** |
