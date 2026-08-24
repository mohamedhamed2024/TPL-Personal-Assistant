# Pattern Data — delivery progress

**Feature:** [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) · **As of:** 2026-08-24  
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
| **PD Sandbox finalize** | Team | In progress | <li>Sarah closed RequestShare / SSO subtasks [LNI-4108](https://datavant.atlassian.net/browse/LNI-4108), [LNI-4438](https://datavant.atlassian.net/browse/LNI-4438), [LNI-4619](https://datavant.atlassian.net/browse/LNI-4619), [LNI-4636](https://datavant.atlassian.net/browse/LNI-4636) (Done 2026-08-20; first visible on this Jira sync)</li><li>Michael validated late-file Status Sync on pddev and opened tracker [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708) (octet-stream PDF ingest — Pattern Data owns the fix)</li> | <ul><li>**9** open stories still In Progress on pddev</li><li>Islam testing **RequestShare** ([LNI-3763](https://datavant.atlassian.net/browse/LNI-3763))</li><li>Open code reviews: Payment Management #220, AutoPay #238, SSO #193, Status Sync #221/#222, Prefill #219, Invoice S3 #216, Mail/SFTP #231</li></ul> | Rolling | — | No ChartSwap standup or Austin meeting transcript on **2026-08-24**. Dev finishing Pattern Data features on the **development sandbox** before any UAT move |
| **UAT Sandbox deploy** | Team | In progress | <li>[LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) Payment Management — Forward + Rollback + Settings packages uploaded to UAT **2026-08-07** (historical); epic [LNI-2309](https://datavant.atlassian.net/browse/LNI-2309) remains **UAT**</li> | <ul><li>Finish Payment Management UAT validation; **PATTERNDATA wordings** still pending</li><li>Remaining **8** features queued **one at a time** per Austin</li></ul> | **2026-08-31** | **2026-08-31** | Features promote **one at a time** per **Austin's** current deployment plan. No forecast slip confirmed |
| **Production** | Team | Not started | — | <ul><li>UAT sign-off per feature</li><li>Production deploy packages per feature</li></ul> | **2026-09-30** | **2026-09-30** | Live release after UAT sign-off per Austin's deployment plan |

---

## Deployment plan (Austin)

*Engineering manager **Austin** sets deployment order and scope — this may change after each Austin meeting. Update this block from the latest Austin meeting transcript when provided.*

| Priority | Feature / story | Environment | Status |
| --- | --- | --- | --- |
| 1 | [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) Payment Management | UAT sandbox | Upload in progress — PR #220 in review; epic [LNI-2309](https://datavant.atlassian.net/browse/LNI-2309) in **UAT** |
| — | Remaining 8 stories | pddev → UAT | Queue per Austin — see Feature delivery tracker |

*Last plan input:* [ChartSwap Daily Stand-up — 2026-08-20](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-08-20.docx) — **no ChartSwap standup or Austin meeting transcript on 2026-08-24**; Austin's 2026-08-20 plan carried forward. **RequestShare** still on pddev; Payment Management still next for UAT pending PR #220 + wordings.

---

## Feature delivery tracker

*Synced from [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) on 2026-08-24 (live).*

*Deploy packages = Salesforce changesets: **Forward** (ship feature) + **Rollback** (undo if needed) + **Settings** (optional config flags).*

### [LNI-2309 — Payment Management](https://datavant.atlassian.net/browse/LNI-2309)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) | Michael | In Progress | In review (#220) | Forward ✓ · Rollback ✓ · Settings ✓ | Pending approval | Tested | Upload in progress | Complete UAT package validation; merge PR #220; get client wordings approved |

### [LNI-2310 — AutoPay Submission Flow](https://datavant.atlassian.net/browse/LNI-2310)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | Michael | In Progress | In progress (#238) | Pending · Pending · — | Pending approval | In progress | Not deployed | Finish AutoPay / threshold work on pddev; complete PR #238; build Forward + Rollback packages |

### [LNI-2311 — Authenticate & Provision Users via SAML SSO](https://datavant.atlassian.net/browse/LNI-2311)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) | Sarah | In Progress | In review (#193) | Pending · Pending · Pending | Pending approval | In progress | Not deployed | Complete second PR approval on #193; build Forward + Rollback + Settings packages; ops SSO kill-switch is documented (no new Account flag) |

### [LNI-2312 — Status Sync — Request State Management & Webhook Notifications](https://datavant.atlassian.net/browse/LNI-2312)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) | Michael | In Progress | In progress (#221 / #222) | Pending · Pending · — | Pending approval | In progress | Not deployed | Finish Status Sync PRs; track Pattern Data octet-stream ingest via [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708); build Forward + Rollback packages |

*Open subtasks*

| Sub-task | Assignee | Status | Notes |
| --- | --- | --- | --- |
| [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708) | Michael | To Do | Track: PD ingestion fails on `application/octet-stream` PDFs from ChartSwap S3 — Pattern Data owns the fix; ChartSwap re-tests after it lands |

### [LNI-2313 — Receive & Store Patient Data via Order Initialization API](https://datavant.atlassian.net/browse/LNI-2313)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3139](https://datavant.atlassian.net/browse/LNI-3139) | Michael | In Progress | In progress (#219) | Pending · Pending · — | Pending approval | Tested | Not deployed | Finalize Prefill PR #219; build Forward + Rollback packages |

### [LNI-3141 — Invoice Upload to S3](https://datavant.atlassian.net/browse/LNI-3141)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3142](https://datavant.atlassian.net/browse/LNI-3142) | Michael | In Progress | In progress (#216) | Pending · Pending · — | Pending approval | Tested | Not deployed | Finalize Invoice S3 PR; build Forward + Rollback packages |

### [LNI-3216 — General](https://datavant.atlassian.net/browse/LNI-3216)

| Story | Assignee | Jira status | Code review (PR) | Deploy packages | Client wordings | PD sandbox | UAT sandbox | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [LNI-3225](https://datavant.atlassian.net/browse/LNI-3225) | Michael | In Progress | In progress (#211 / #212 / #213) | Pending · Pending · Pending | Pending approval | Tested | Not deployed | Finalize disable-features / email PRs; build deploy packages |
| [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) | Sarah | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · — | Pending approval | In progress | Not deployed | Change-owner scenario and test scenarios **Done**; open pull request and build Forward + Rollback packages; Islam testing on pddev |
| [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769) | Michael | In Progress | In progress (#231) | Pending · Pending · Pending | Pending approval | Tested | Not deployed | Finalize Mail Order / SFTP disable PR #231; build deploy packages |

---

## Team focus

| Member | Focus |
| --- | --- |
| **Michael** | Payment Management UAT ([LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) PR #220); AutoPay ([LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) #238); Status Sync ([LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) #221/#222) including octet-stream tracker [LNI-4708](https://datavant.atlassian.net/browse/LNI-4708); Prefill ([LNI-3139](https://datavant.atlassian.net/browse/LNI-3139)); Invoice S3 ([LNI-3142](https://datavant.atlassian.net/browse/LNI-3142)); General ([LNI-3225](https://datavant.atlassian.net/browse/LNI-3225), [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769)) |
| **Sarah** | SAML SSO ([LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) PR #193); **RequestShare** ([LNI-3763](https://datavant.atlassian.net/browse/LNI-3763)) — implementation subtasks Done; remaining story-level code review and deploy packages |
| **Islam** | PD sandbox testing of [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) RequestShare (Sarah's implementation) — default (no standup transcript today) |

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
| 1 | **Islam cannot log defects or update Jira.** Islam is testing RequestShare on pddev but has no Jira account — QA progress is invisible in the tracker and defects may be tracked only in standup or chat. | <ul><li>**Hamed** or **Nabawy** follow up with **Austin** on Islam's Jira access</li><li>Continue capturing Islam's status in Team focus until access is granted</li></ul> | Medium |
| 2 | **Client wordings (PATTERNDATA) are not approved for any feature.** All nine stories show wordings **Pending approval** — deploy packages cannot be finalized or attached with approved copy, blocking UAT promotion even when code is ready. | <ul><li>Escalate wordings review to Austin / client contacts via **Hamed** or **Nabawy**</li><li>Prioritize wordings for Payment Management ([LNI-3137](https://datavant.atlassian.net/browse/LNI-3137)) as the next feature Austin directed for UAT</li><li>Do not mark UAT complete until wordings are signed off per feature</li></ul> | Low |

---

## Standup action items (2026-08-24)

*No ChartSwap standup transcript on 2026-08-24. Open Jira-driven next steps only (carried from the 2026-08-24 DVI-1086 sync). No new meeting assignments.*

| Owner | Action |
| --- | --- |
| **Hamed** | Follow up with **Austin** on **Islam's Jira access** |
| **Islam** | PD sandbox testing of **RequestShare** ([LNI-3763](https://datavant.atlassian.net/browse/LNI-3763)) — Sarah's implementation |
| **Michael** | Finish **PR #220** and UAT package validation for Payment Management ([LNI-3137](https://datavant.atlassian.net/browse/LNI-3137)); continue AutoPay **#238**, Status Sync **#221/#222**, Prefill **#219**; track octet-stream ingest ([LNI-4708](https://datavant.atlassian.net/browse/LNI-4708)) |
| **Nabawy** | Escalate **PATTERNDATA wordings** — all nine features still **Pending approval**, blocking UAT-ready |
| **Sarah** | Continue **SAML SSO** ([LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) PR #193) and open code review / deploy packages for **RequestShare** ([LNI-3763](https://datavant.atlassian.net/browse/LNI-3763)) |
