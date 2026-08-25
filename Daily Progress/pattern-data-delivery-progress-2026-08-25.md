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

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **PD Sandbox finalize** | Team | In progress | <ul><li>Michael rebased **master** and related PRs ([LNI-4781](https://datavant.atlassian.net/browse/LNI-4781) Done — tip `558e2c41a`; #220 / #238 0 behind master)</li><li>Islam inventoried **PATTERNDATA UI text** from PRs into Excel</li></ul> | <ul><li>Islam: compare Excel with Youssef's wordings document; move scoped **messages** to custom labels</li><li>Michael: document provider-portal **upload-file** page difference vs current</li><li>Nine open stories still in progress on pddev</li></ul> | Rolling | — | Standup **2026-08-25** — no Austin-class transcript today |
| **UAT Sandbox deploy** | Team | In progress | <ul><li>Payment Management deploy packages built; UAT upload in progress</li></ul> | <ul><li>Austin is **busy this week** — UAT start still uncertain</li><li>Remaining features **one at a time**</li></ul> | **2026-08-31** | **2026-08-31** | Hamed: Austin has other work first; target dates may move but no new date was set |
| **Production** | Team | Not started | — | <ul><li>UAT sign-off; production deploy packages per feature</li></ul> | **2026-09-30** | **2026-09-30** | Live release after UAT sign-off per Austin |

---

## Deployment plan (Austin)

*Engineering manager **Austin** sets deployment order and scope — this may change after each Austin meeting or PD Review.*

| Priority | Feature / story | Environment | Status |
| --- | --- | --- | --- |
| 1 | Wrap current PD details — [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) Payment Management | UAT sandbox | PR #220 current with master after last night's rebase; UAT package upload still in progress |
| 2 | **Approved Fee overhaul** | pddev | Next after wrap-up (Austin, 2026-08-20) |
| 3 | **PCI cart** (not MPI) | pddev | Look this week — functionally works; page redesign possible (Austin, 2026-08-20) |
| — | Remaining 8 stories | pddev → UAT | Queue per Austin — CSI invoice line items later |

*Last plan input:* [PD Review with Austin — 2026-08-20](../Transcript/PDReviewWithAustin/PDReviewWithAustin-2026-08-20). Day-to-day from [ChartSwap Daily Stand-up — 2026-08-25](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-08-25.docx). No new Austin-class transcript on **2026-08-25** — keep the 2026-08-20 order. Standup: Austin is busy this week, so UAT promotion is still waiting on him.

---

## Feature delivery tracker

*Synced from [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) on 2026-08-25 (live).*

*Deploy packages = Salesforce changesets: **Forward** (ship feature) + **Rollback** (undo if needed) + **Settings** (optional config flags).*

### [LNI-2309 — Payment Management](https://datavant.atlassian.net/browse/LNI-2309)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) | Michael | In Progress | In review (#220) | Forward ✓ · Rollback ✓ · Settings ✓ | Pending approval | Tested | Upload in progress | **Update 2026-08-25:** PR #220 0 behind master after rebase; finish UAT package upload; wordings still pending |

### [LNI-2310 — AutoPay Submission Flow](https://datavant.atlassian.net/browse/LNI-2310)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | Michael | In Progress | In review (#238) | Pending · Pending · — | Pending approval | In progress | Not deployed | **Update 2026-08-25:** Master re-sync Done ([LNI-4781](https://datavant.atlassian.net/browse/LNI-4781)); new requestor Autopay Threshold stays **blank** (not zero) |

### [LNI-2311 — Authenticate & Provision Users via SAML SSO](https://datavant.atlassian.net/browse/LNI-2311)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) | Sarah | In Progress | In review (#193) | Pending · Pending · Pending | Pending approval | In progress | Not deployed | No new Account Active Flag this release — emergency firm SSO suspend is suffix the firm external ID (`-cancelled` / `-suspended`) |

### [LNI-2312 — Status Sync — Request State Management & Webhook Notifications](https://datavant.atlassian.net/browse/LNI-2312)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) | Michael | In Progress | In review (#222) | Pending · Pending · — | Pending approval | In progress | Not deployed | Finalize code review on #222; track octet-stream PDF ingest ([LNI-4708](https://datavant.atlassian.net/browse/LNI-4708)) |

*Open subtasks*

| Sub-task | Assignee | Status | Notes |
| --- | --- | --- | --- |
| [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708) | Michael | To Do | Track: PD ingestion fails on application/octet-stream PDFs from ChartSwap S3 |

### [LNI-2313 — Receive & Store Patient Data via Order Initialization API](https://datavant.atlassian.net/browse/LNI-2313)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3139](https://datavant.atlassian.net/browse/LNI-3139) | Michael | In Progress | In review (#219) | Pending · Pending · — | Pending approval | In progress | Not deployed | Prefill REST validated on pddev; merge PR #219 (externalReferenceId passthrough) |

### [LNI-3141 — Invoice Upload to S3](https://datavant.atlassian.net/browse/LNI-3141)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3142](https://datavant.atlassian.net/browse/LNI-3142) | Michael | In Progress | In review (#216) | Pending · Pending · — | Pending approval | In progress | Not deployed | Invoice S3 uses requestor-account flag only; build Forward + Rollback packages |

### [LNI-3216 — General](https://datavant.atlassian.net/browse/LNI-3216)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3225](https://datavant.atlassian.net/browse/LNI-3225) | Michael | In Progress | In review (#211) | Pending · Pending · Pending | Pending approval | In progress | Not deployed | Turn off non-applicable features and emails for Pattern Data requests |
| [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) | Sarah | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · — | Pending approval | In progress | Not deployed | **Update 2026-08-25:** Islam inventoried PR UI text — compare with Youssef's document, then custom labels for scoped messages |
| [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769) | Michael | In Progress | In review (#231) | Pending · Pending · Pending | Pending approval | In progress | Not deployed | Disable Mail Order / SFTP for Pattern Data accounts; finalize PR #231 |

---

## Team focus

| Member | Focus |
| --- | --- |
| **Michael** | Provider-portal **upload-file** page vs current (document findings); [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) PR #220 UAT upload; [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) / #238; [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) + [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708) |
| **Sarah** | [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) SAML SSO (#193); [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare |
| **Islam** | Compare PR UI-text Excel with Youssef's wordings document (Hamed to send); then move scoped **messages** to custom labels — not the full UI inventory |

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
| 1 | **Islam cannot log defects or update Jira.** Islam has no Jira account — QA progress is invisible in the tracker and defects may be tracked only in standup or chat. | <ul><li>Standup **2026-08-25:** Datavant IT is waiting on **HR** green light; Austin follows HR; Islam's IT ticket got no reply</li><li>**Hamed / Nabawy** keep following Austin until Islam can log in</li></ul> | Medium |
| 2 | **Client wordings (PATTERNDATA) are not approved for any feature.** All nine stories show wordings **Pending approval** — deploy packages cannot be finalized or attached with approved copy, blocking UAT promotion even when code is ready. | <ul><li>Islam inventoried UI text from PRs — compare with Youssef's document (Hamed to send), then custom labels for scoped **messages** only</li><li>Do not attach PATTERNDATA text to packages until approved</li></ul> | Low |

---

## Standup action items (2026-08-25)

*From [ChartSwap Daily Stand-up — 2026-08-25](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-08-25.docx).*

| Owner | Action |
| --- | --- |
| **Hamed** | Send Islam **Youssef's wordings document** so he can compare it with the Excel inventory |
| **Hamed** | Follow Austin on **Islam's Datavant / Jira access** — IT is waiting on Datavant HR; still not live |
| **Islam** | Compare the PR UI-text Excel with Youssef's document; move only scoped **messages** to **custom labels** |
| **Michael** | Document the provider-portal **upload-file** page difference vs current (config vs code) |
| **Nabawy** | Adjust the progress-report **Teams** format (plain chat message vs Adaptive Card) and send |
