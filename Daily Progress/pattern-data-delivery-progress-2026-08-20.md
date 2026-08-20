# Pattern Data — delivery progress

**Feature:** [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) · **As of:** 2026-08-20  
**Targets:** UAT sandbox **2026-08-31** · Production **2026-09-30**

## Status at a glance


| Phase                   | Owner | Status      | What's done | What's left | Target         | Forecast       | Notes                                                                                  |
| ----------------------- | ----- | ----------- | ----------- | ----------- | -------------- | -------------- | -------------------------------------------------------------------------------------- |
| **PD Sandbox finalize** | Team  | In progress |             |             | Rolling        | —              | Austin meeting **2026-08-20** — plan may shift again; team sending daily priority list |
| **UAT Sandbox deploy**  | Team  | In progress |             |             | **2026-08-31** | **2026-08-31** | Features promote **one at a time** per **Austin's** current deployment plan            |
| **Production**          | Team  | Not started | —           |             | **2026-09-30** | **2026-09-30** | Production follows UAT sign-off per feature — plan set by Austin                       |


---



## Deployment plan (Austin)

*Engineering manager **Austin** sets deployment order and scope — this may change after each Austin meeting. Update this block from the latest Austin meeting transcript when provided.*


| Priority | Feature / story                                                               | Environment | Status                                                                                                             |
| -------- | ----------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------ |
| 1        | [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) Payment Management | UAT sandbox | Upload in progress — PR #220 in review; epic [LNI-2309](https://datavant.atlassian.net/browse/LNI-2309) in **UAT** |
| —        | Remaining 8 stories                                                           | pddev → UAT | Queue per Austin — see Feature delivery tracker                                                                    |


*Last plan input:* [ChartSwap Daily Stand up — 2026-08-20](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap%20Daily%20Stand%20up08-20-2026.docx) — Austin meeting scheduled **2026-08-20**; Michael sending daily priority/estimate list per Nabawy. **RequestShare** active on pddev; Payment Management still next for UAT pending PR #220 + wordings.

---



## Feature delivery tracker

*Synced from [DVI-1086](https://datavant.atlassian.net/browse/DVI-1086) on 2026-08-20 (live).*

*Deploy packages = Salesforce changesets: **Forward** (ship feature) + **Rollback** (undo if needed) + **Settings** (optional config flags).*

### [LNI-2309 — Payment Management](https://datavant.atlassian.net/browse/LNI-2309)


| Story                                                      | Assignee | Jira status | Code review (PR) | Deploy packages                     | Client wordings  | PD sandbox | UAT sandbox        | Next step                                                                                                                |
| ---------------------------------------------------------- | -------- | ----------- | ---------------- | ----------------------------------- | ---------------- | ---------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| [LNI-3137](https://datavant.atlassian.net/browse/LNI-3137) | Michael  | In Progress | In review (#220) | Forward ✓ · Rollback ✓ · Settings ✓ | Pending approval | Tested     | Upload in progress | **Update 2026-08-20:** Continue Austin-driven Saved Payment + webhook changes; merge PR #220; sit with Islam on wordings |




### [LNI-2310 — AutoPay Submission Flow](https://datavant.atlassian.net/browse/LNI-2310)


| Story                                                      | Assignee | Jira status | Code review (PR)                               | Deploy packages       | Client wordings  | PD sandbox  | UAT sandbox  | Next step                                                                          |
| ---------------------------------------------------------- | -------- | ----------- | ---------------------------------------------- | --------------------- | ---------------- | ----------- | ------------ | ---------------------------------------------------------------------------------- |
| [LNI-3223](https://datavant.atlassian.net/browse/LNI-3223) | Michael  | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · — | Pending approval | In progress | Not deployed | Finish AutoPay code on pddev; open pull request; build Forward + Rollback packages |




### [LNI-2311 — Authenticate & Provision Users via SAML SSO](https://datavant.atlassian.net/browse/LNI-2311)


| Story                                                      | Assignee | Jira status | Code review (PR)                               | Deploy packages             | Client wordings  | PD sandbox  | UAT sandbox  | Next step                                                                                                                                                               |
| ---------------------------------------------------------- | -------- | ----------- | ---------------------------------------------- | --------------------------- | ---------------- | ----------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [LNI-3224](https://datavant.atlassian.net/browse/LNI-3224) | Sarah    | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · Pending | Pending approval | In progress | Not deployed | **Update 2026-08-20:** Hold [LNI-4636](https://datavant.atlassian.net/browse/LNI-4636) Account Active Flag until Austin confirms business impact; resend impact message |


*Open subtasks*


| Sub-task                                                   | Assignee | Status      | Notes                                                        |
| ---------------------------------------------------------- | -------- | ----------- | ------------------------------------------------------------ |
| [LNI-4619](https://datavant.atlassian.net/browse/LNI-4619) | Sarah    | In Progress | Ops firm onboarding document                                 |
| [LNI-4636](https://datavant.atlassian.net/browse/LNI-4636) | Sarah    | In Progress | **Blocked** — awaiting Austin confirmation on cascade impact |




### [LNI-2312 — Status Sync — Request State Management & Webhook Notifications](https://datavant.atlassian.net/browse/LNI-2312)


| Story                                                      | Assignee | Jira status | Code review (PR)                               | Deploy packages       | Client wordings  | PD sandbox  | UAT sandbox  | Next step                                  |
| ---------------------------------------------------------- | -------- | ----------- | ---------------------------------------------- | --------------------- | ---------------- | ----------- | ------------ | ------------------------------------------ |
| [LNI-3226](https://datavant.atlassian.net/browse/LNI-3226) | Michael  | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · — | Pending approval | In progress | Not deployed | Finish status sync / webhook code on pddev |




### [LNI-2313 — Receive & Store Patient Data via Order Initialization API](https://datavant.atlassian.net/browse/LNI-2313)


| Story                                                      | Assignee | Jira status | Code review (PR)                               | Deploy packages       | Client wordings  | PD sandbox  | UAT sandbox  | Next step                                                   |
| ---------------------------------------------------------- | -------- | ----------- | ---------------------------------------------- | --------------------- | ---------------- | ----------- | ------------ | ----------------------------------------------------------- |
| [LNI-3139](https://datavant.atlassian.net/browse/LNI-3139) | Michael  | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · — | Pending approval | In progress | Not deployed | Refactor Patient Prefill API on pddev; finalize code review |




### [LNI-3141 — Invoice Upload to S3](https://datavant.atlassian.net/browse/LNI-3141)


| Story                                                      | Assignee | Jira status | Code review (PR)                               | Deploy packages       | Client wordings  | PD sandbox   | UAT sandbox  | Next step                                              |
| ---------------------------------------------------------- | -------- | ----------- | ---------------------------------------------- | --------------------- | ---------------- | ------------ | ------------ | ------------------------------------------------------ |
| [LNI-3142](https://datavant.atlassian.net/browse/LNI-3142) | Michael  | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · — | Pending approval | Not deployed | Not deployed | Finish Invoice S3 code on pddev; build deploy packages |




### [LNI-3216 — General](https://datavant.atlassian.net/browse/LNI-3216)


| Story                                                      | Assignee | Jira status | Code review (PR)                               | Deploy packages             | Client wordings  | PD sandbox   | UAT sandbox  | Next step                                                                                   |
| ---------------------------------------------------------- | -------- | ----------- | ---------------------------------------------- | --------------------------- | ---------------- | ------------ | ------------ | ------------------------------------------------------------------------------------------- |
| [LNI-3225](https://datavant.atlassian.net/browse/LNI-3225) | Michael  | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · Pending | Pending approval | In progress  | Not deployed | Turn off non-applicable features and emails for Pattern Data requests                       |
| [LNI-3763](https://datavant.atlassian.net/browse/LNI-3763) | Sarah    | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · —       | Pending approval | In progress  | Not deployed | **Update 2026-08-20:** Change-request-owner scenario shipped — Islam testing on pddev today |
| [LNI-3769](https://datavant.atlassian.net/browse/LNI-3769) | Michael  | In Progress | Ready — finalize code review & deploy packages | Pending · Pending · Pending | Pending approval | Not deployed | Not deployed | Add ability to disable Mail Order / SFTP for Pattern Data accounts                          |


*Open subtasks (LNI-3763 — RequestShare)*


| Sub-task                                                   | Assignee | Status      | Notes                               |
| ---------------------------------------------------------- | -------- | ----------- | ----------------------------------- |
| [LNI-4108](https://datavant.atlassian.net/browse/LNI-4108) | Sarah    | In Progress | Drafting test scenarios             |
| [LNI-4438](https://datavant.atlassian.net/browse/LNI-4438) | Sarah    | In Progress | Dev — change request owner scenario |


---



## Team focus


| Member      | Focus                                                                                                                                                                                                                                                                                                                   |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Michael** | Austin-driven **Saved Payment** + webhook / account-level changes on pddev; Payment Management UAT ([LNI-3137](https://datavant.atlassian.net/browse/LNI-3137)); build **daily priority list with estimates** for Austin; sync with Sarah before her vacation                                                           |
| **Sarah**   | SAML SSO ([LNI-3224](https://datavant.atlassian.net/browse/LNI-3224)); **RequestShare** ([LNI-3763](https://datavant.atlassian.net/browse/LNI-3763)) — change-owner scenario delivered; **Account Active Flag** ([LNI-4636](https://datavant.atlassian.net/browse/LNI-4636)) on hold pending Austin; vacation next week |
| **Islam**   | **Finish RequestShare change-owner scenario testing** ([LNI-3763](https://datavant.atlassian.net/browse/LNI-3763)) on pddev today — new scope from Sarah; Michael to align on **PATTERNDATA wordings**                                                                                                                  |


---



## Path to UAT & Production

**UAT-ready progress:** **0/9** features UAT-ready (see Feature delivery tracker)

### To reach UAT sandbox (target 2026-08-31)

- [ ] All features finalized and tested on **pddev**
- [ ] Each feature: **Forward + Rollback** deploy packages built (Settings package if needed)
- [ ] Each package uploaded and **tested on pddev**, then promoted to **UAT** (one feature at a time)
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


| #   | Risk / challenge                                                                                                                                                                                                                              | Mitigation | Severity |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------- |
| 1   | **Islam cannot log defects or update Jira.** Islam is testing RequestShare on pddev but has no Jira account — QA progress is invisible in the tracker and defects may be tracked only in standup or chat.                                     |            | Medium   |
| 2   | **Client wordings (PATTERNDATA) are not approved for any feature.** All nine stories show wordings **Pending approval** — deploy packages cannot be finalized or attached with approved copy, blocking UAT promotion even when code is ready. |            | Low      |


---

