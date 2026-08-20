# Pattern Data — delivery progress

**Go-live goal:** End of June 2026 · **Epic:** [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) · **As of:** 2026-06-10

---

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Pre-UAT** | Youssef | In progress | <li>4/7 providers tested [STD, PFP, RR, Waystar]</li><li>RR payment bugs cleared and retested (OC-9529, OC-9531 closed; full flow retest 2026-06-08)</li><li>CIOX payment bugs closed (OC-9532, OC-9552 closed 2026-06-08)</li><li>Hamed completed ShareCare and Updox sandbox passes (2026-06-10); ShareCare report conflict logged; Updox deprioritized per Austin</li><li>Youssef RR retest (2026-06-10) surfaced [OC-9566](https://ontellus.atlassian.net/browse/OC-9566); RR card-payment scenarios partially verified</li> | <ul><li>Fix remaining 4 bugs — RR & PFP payment blocker issues — Michael</li><li>Finalize transaction object updates — Michael</li><li>Finalize invoice to S3 updates — Michael</li><li>Michael fix ShareCare sandbox company routing — S3 uploads were hitting production bucket instead of sandbox (blocks Hamed continuation)</li><li>Wave 1 unit-test coverage (Payment Management, Invoice, Prefill) before UAT 2026-06-16 — Islam + Michael</li><li>Islam verify CNR file display on UAT after reject flow (Youssef found provider can still fulfill post-reject; CNR not in requester records table)</li></ul> | 2026-05-21 | **2026-06-14** | <li>Sandbox goal: **pre-fulfillment parity with UAT** — not chasing fulfillment simulation on sandbox. CIOX fulfillment gap accepted per 06-05 agreement; escalate only if new non-fulfillment issues surface.</li><li>External-provider fulfillment simulation deferred to UAT (Eric).</li><li>Automation paused — manual retest for now.</li><li>Michael prioritizing open bugs over remaining Austin transaction comments today (2026-06-10 standup).</li><li>**Updox deprioritized** per Austin (likely not active on production; Hamed already tested replacement path).</li><li>Batch Payflow risk: multiple requests/charges on same card in sandbox may hit provider limits — Austin said not to worry (06-09); team wants to revisit batching control before production.</li> |
| **PD Sandbox (BAU)** | Van | In progress | — | BAU flows — can start now on STD, PFP, RR, Way-Star in parallel | 2026-05-21 | **2026-06-02** | agreed to conduct regular demos for Van as he's not testing PD sandbox and relying more on testing on UAT once code is promoted. |
| **UAT** | Van | Not started | — | <ul><li>Wave 1 (6/15): Prefill API, CC Management, Invoice Upload</li><li>Wave 2 (6/17): Status Retrieval API, Status Sync Job</li><li>Wave 3 (6/22): Auto-Pay via CC (TPR)</li></ul> | 2026-06-15 – 2026-06-25 | On track if Pre-UAT closes 06/14 | Wave 2 dates may be delayed as it depends on PD webhook details which is not provided yet (see Risks). |
| **Production** | — | Not started | — | UAT sign-off | 2026-06-30 | Unverified | — |

---

## Client release plan (received 2026-06-01)

*Source: client release plan (Austin). Account-flagged items ship when enabled per account.*

*Environment promotion targets by wave.*

| Wave | Feature | Scope | Account flag | UAT | Prod | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Wave 1 | Prefill Order form API | API to prefill order form | Yes | 2026-06-15 | 2026-06-17 | — |
| Wave 1 | Credit Card Management | Shows existing User SavedPayments; cart must include User **and** Account SavedPayments (valid / non-expired only). Assumes Payflow issues resolved. | Yes | 2026-06-15 | 2026-06-17 | Added new Contact/User-level flag to enable the saved payments page edit per contact. |
| Wave 1 | Invoice Upload to S3 | On successful Request payment: upload with Type **Invoice**. Prod path: `Chartswap/Invoices`. | Yes | 2026-06-15 | 2026-06-17 | Validate VF bucket filtering — invoice may appear alongside request payload; filtering fix in progress. |
| Wave 2 | Status Retrieval API | Method to build response body; also used for Status Sync Job payload. | — | 2026-06-17 | 2026-06-22 | Dates may be pushed: webhook integration has not been communicated to us yet from their side. |
| Wave 2 | Status Sync Job | Scheduled / account-scoped status sync. | Yes | 2026-06-17 | 2026-06-22 | Dates may be pushed: webhook integration has not been communicated to us yet from their side. |
| Wave 3 | Auto-Pay via Credit Card | New payment flow (Transaction Reconciliation Project / TPR). If Request is in any cart and user pays via Auto-Pay, remove Request from **all** carts before Auto-Pay runs. | — | 2026-06-22 | 2026-06-25 | — |
| TBD | SSO | Single sign-on integration — requires PD metadata and config. | Yes | TBD | TBD | Release wave unknown; PD metadata, and config still missing — see Risks |
| TBD | Cart hiding | Hide cart UI when enabled. | Yes | TBD | TBD | — |
| TBD | Prevent Record Finder | Block Record Finder when enabled. | Yes | TBD | TBD | — |
| TBD | Suppress email notifications | Disable email notifications when enabled. | Yes | TBD | TBD | Account-flag behavior confirm with client (Salah) |

---

## Open delivery blockers — payment bugs (0 blocked + 7 in QA + 1 pending code review)

*Process (2026-06-07 standup):* When handing a bug to QA, dev should demo the fix with the tester first to reduce ping-pong.

*Synced from Jira epic [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) on 2026-06-15 (live).*

**Eight open payment bugs** on the epic — three **Major** (ShareCare, RR, PFP) block provider sign-off or PFP testing; five **Minor** (Payment Management + AutoPay draft path) still block or slow Pre-UAT scenario testing.

### ShareCare

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9562](https://ontellus.atlassian.net/browse/OC-9562) | Authorization submit fails with Too many SOQL queries (101) on `enterrequestdatasc` — blocks ShareCare workflow completion | **QA** | Mohamed Hamed | **New 2026-06-09** — Major — no workaround. **Update 2026-06-10:** Michael also fixing sandbox company routing — ShareCare S3 uploads were hitting production bucket |

### Record Retrieval

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9566](https://ontellus.atlassian.net/browse/OC-9566) | Request reaches **Completed** after prepayment with no records uploaded and no recovery path (REQ-23792287) — completion gated on payment instead of fulfillment | **QA** | Youssef Yahia | **New 2026-06-10** — Youssef retest; Hamed's prior RR flow paid-then-fulfilled correctly. Major — no workaround |

### Payment Management

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9567](https://ontellus.atlassian.net/browse/OC-9567) | Firm pre-authorized **Threshold Management** section missing from Payment Management page — admin cannot view or edit threshold | **QA** | Youssef Yahia | **New 2026-06-10** — Minor (Jira); **blocks Youssef firm/scenario testing** until fixed (standup). Backend threshold still applied |
| [OC-9564](https://ontellus.atlassian.net/browse/OC-9564) | Expired/expiring card banners shown when other active firm cards exist — should only show when last active card | **QA** | Youssef Yahia | **New 2026-06-09** — Minor — workaround (ignore banner). Michael reviewing per standup |
| [OC-9574](https://ontellus.atlassian.net/browse/OC-9574) | Replace Card (Mass Replace) lists **Rejected** terminal request among "active" affected requests — incorrect count and consent scope (REQ-23792297) | **QA** | Youssef Yahia | **New 2026-06-11** — Minor — flow not hard-blocked but consent audit trail includes non-active request; user cannot deselect |
| [OC-9389](https://ontellus.atlassian.net/browse/OC-9389) | After Replace/Remove card, payment reinitiation for affected requests not verifiable in UI (DEC-050) | **Pending Code Review** | Sara Hassan | Minor — verifiability gap. Heba retest still pending with Michael; Sarah may assist (standup) |

### AutoPay Submission Flow

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9576](https://ontellus.atlassian.net/browse/OC-9576) | PFP **1st payment never initiated** — request stuck in Pending Payment with no failure note and no Retry / Change Card / Accept actions (REQ-23792610) | **QA** | Youssef Yahia | **New 2026-06-11** — Major — no workaround; blocks PFP payment + fulfillment testing |
| [OC-9575](https://ontellus.atlassian.net/browse/OC-9575) | **Submit with AutoPay** stays disabled on saved Draft even when signed authorization form is already uploaded (REQ-23792608) | **QA** | Youssef Yahia | **New 2026-06-11** — Minor — breaks save-as-draft → submit path; partial workaround (submit without saving as Draft) |

---

### Flow to be retested

*After bug fixes — scheduled retest*

| Flow | Assignee | Date |
| --- | --- | --- |
| Record Retrieval (post OC-9566 fix) | Youssef | TBD |
| Heba Buy Now — two records, one pass / one fail intermittently | Heba + Michael | 2026-06-10 (Michael to retest) |

---

## Current Focus

| Member | Focus |
| --- | --- |
| Michael | **Priority:** Open blockers + ShareCare sandbox company/S3 fix for Hamed; then Austin Invoice/S3 comments. |
| Islam | Unit-test coverage — start uncovered classes now; Wave 1 features (Payment Management, Invoice, Prefill) with Michael once missing test classes committed on branch |
| Sarah | Michael charity/coverage component (conflicts resolved); then CIOX data classes on sandbox |
| Hamed | External-provider testing complete (ShareCare/Updox); blocked on Michael's ShareCare sandbox fix to continue |
| Youssef | RR + Payment Management scenario testing blocked by OC-9566 / OC-9567; verify reject/CNR flow on UAT |

---

## Risks & challenges

Each item below is stated as a **condition → consequence**, with a mitigation that addresses that specific consequence.


| #   | Risk / challenge                                                                                                                                                                                                                                                                                                               | Mitigation                                                                                                                                                                                                                                                                 | Severity |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| 1   | **Late design changes from Austin could force rework.** Further scope or design updates from the client may require re-coding and full-team retest across Pre-UAT and the release waves, threatening the 06/14 date and June go-live. **Michael** carries four open bugs plus partial Austin transaction comments (~55 story comments) and Autopay Tool UI — capacity heavily loaded (2026-06-10 standup).                                                                                          | <ul><li><strong>Michael</strong> focused on bugs first today; Austin comments after</li><li>Track all changes against the [client release plan](#client-release-plan-received-2026-06-01)</li><li>Re-estimate affected waves before committing UAT dates</li><li>Escalate if 06/14 or go-live is threatened</li></ul> | High     |
| 2   | **End-to-end testing against the PD lower env cannot start.** PD has not responded on lower-environment access, so BAU/E2E validation hasn't begun — only provider-level sandbox testing is underway. The integration risks being validated late, or not before go-live. **Escalation deadline was 2026-06-08** — no response confirmed (Maria engaged 06-08; still awaiting internal PD reply).                                                         | <ul><li>Follow up with Katherine; keep mocking the integration in the meantime</li><li>Escalate to Austin / Van that go-live is at risk if the needed access is not received</li></ul>                                                                                | High     |
| 3   | **SSO cannot be configured or release-planned.** PD has not provided the SSO metadata and configuration required for sandbox/UAT access, leaving the SSO release wave undefined and blocking UAT sign-off.                                                                                                                     | <ul><li>Track as a PD dependency</li><li> escalated to Austin / PD contacts</li><li>Hold UAT sign-off until SSO config is in place</li></ul>                                                                                                                                                     | High     |
| 4   | **Wave 2 dates may slip (Status Retrieval API & Status Sync Job).** PD has not yet communicated the webhook integration details these features depend on, so the 06/17 UAT / 06/22 prod targets may move. **Escalation deadline was 2026-06-10** — no PD response confirmed in standup.                                                                                                                      | <ul><li>Request webhook details from PD; track alongside the SSO dependency</li><li>Re-baseline Wave 2 dates once received</li><li>Escalate to Austin if still not received after 06/10</li></ul>                                                                                                 | Medium   |
| 5   | **Provider scope uncertainty.** Pharmacy and other provider paths discovered in code; unclear if in scope vs legacy. Expanding scope could delay Pre-UAT on the 7 known providers. **Updox** now deprioritized per Austin (likely not on production).                                                                                                                      | <ul><li>Limit focus to STD, PFP, RR, Waystar, CIOX, ShareCare unless Van/Nabuya confirms otherwise</li><li>Michael posted Pharmacy question to PD group; follow up with LeBon on Walmart/Pharmacy payment approach</li><li>Hamed reviewing provider list Michael sends</li></ul>                                                                                                 | Low   |
| 6   | **Code updates can reopen fixed bugs and break previously passing scenarios.** Ongoing fixes and Austin-driven changes may regress areas already signed off in Pre-UAT, forcing duplicate retest cycles and eroding confidence in the 06/14 close-out.                                                                                                                      | <ul><li>Include detailed testing steps, expected results, and related areas to retest after updates in each story</li><li>Add screenshots of the resolution as evidence in a Jira comment when closing or handing off a fix</li></ul>                                                                                                 | High   |
