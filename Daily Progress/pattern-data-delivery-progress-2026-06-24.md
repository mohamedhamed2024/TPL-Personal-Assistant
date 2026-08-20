# Pattern Data — delivery progress

**Go-live goal:** End of June 2026 · **Epic:** [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) · **As of:** 2026-06-24

---

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Pre-UAT** | Youssef | In progress | <li>4/7 providers tested [STD, PFP, RR, Waystar]</li><li>RR payment bugs cleared and retested (OC-9529, OC-9531 closed; full flow retest 2026-06-08)</li><li>Van demo held **2026-06-22**; Youssef delivered **12 Wave 1 UAT scenarios** + testing guide (2026-06-23)</li><li>Michael fixed card-management bugs and deployed to QA (2026-06-24) — OC-9649 (last-card removal gate), OC-9653 (Add Account Card Insufficient Privileges); Islam unblocked on firm-card add</li><li>Michael completed Payment Management Wave 1 chain set — card path ready for UAT deploy (2026-06-24)</li><li>Youssef CNR retest OK — request creation and CNR visibility working (2026-06-24)</li><li>Wave 1 UAT scenario testing **started** (2026-06-24) — Islam on assigned scenarios; Sarah finished last UAT scenario, moving to provider flows</li> | <ul><li>ShareCare **provider visibility** — workflow runs but provider not shown on ChartSwap provider page; reassigned to **Sarah** (was Hamed Blocked)</li><li>OC-9630 CNR — core flow retested OK; **empty file also uploads** — Michael reviewing before close</li><li>Michael: 5 open bugs — 3 Van-demo items + CNR empty-file + 2 Youssef handover items (OC-9652, OC-9659, OC-9656, etc. in QA)</li><li>Salah create **5 Jira issues** from UAT handover chat (Youssef md items not yet on board)</li><li>Islam continue Wave 1 UAT scenarios (Course Health rejection, AutoPay paths) after card fix verified live</li><li>Sarah: confirm consent/card-expiry logic with Michael; then start assigned provider-type flows</li></ul> | 2026-05-21 | **2026-06-17** *(at risk — dates TBD pending Austin)* | <li>Sandbox goal: **pre-fulfillment parity with UAT** — not chasing fulfillment simulation on sandbox. CIOX fulfillment gap accepted per 06-05 agreement.</li><li>External-provider fulfillment simulation deferred to UAT (Eric).</li><li>Automation paused — manual retest for now.</li><li>**06/14 Pre-UAT forecast missed** — Wave 1 UAT did not start 6/15.</li><li>**Updox deprioritized** per Austin.</li><li>Team adopting feature-branch + PR workflow; Salah + Michael investigating PR adoption.</li><li>**06/24 standup:** Hussein — log UAT effort under epic story with **QA** prefix in title; subtasks per tester.</li><li>Jira access partial progress — Sarah/Hamed on BO board; Youssef new account lacks project space.</li> |
| **PD Sandbox (BAU)** | Van | In progress | — | BAU flows — can start now on STD, PFP, RR, Way-Star in parallel | 2026-05-21 | **2026-06-02** | agreed to conduct regular demos for Van as he's not testing PD sandbox and relying more on testing on UAT once code is promoted. |
| **UAT** | Van | In progress | <li>Wave 1 Payment Management UI chain set complete — card path deployed QA/UAT (2026-06-24)</li><li>12 Wave 1 scenarios documented; Islam + Sarah started execution (2026-06-24)</li> | <ul><li>Wave 1 (6/22): Prefill API, CC Management, Invoice Upload — retest payment bugs in QA</li><li>Wave 2 (TBD): Status Retrieval API, Status Sync Job</li><li>Wave 3 (TBD): Auto-Pay via CC (TPR)</li><li>Austin deploy decision on Payment Management page</li></ul> | 2026-06-15 – 2026-06-25 | **At risk** — Wave 1 UAT missed 6/15; scenario testing started 6/24; Salah confirming slip with Austin | Wave 2 dates may slip — PD webhook details not provided yet (see Risks). Austin also waiting on ShareCare partnership item before Wave 1 push. |
| **Production** | — | Not started | — | UAT sign-off | 2026-06-30 | Unverified | — |

---

## Client release plan (received 2026-06-01)

*Source: client release plan (Austin). Account-flagged items ship when enabled per account.*

*Environment promotion targets by wave.*

*Update 2026-06-15:* Scheduled demo for Van postponed to **Monday 2026-06-22**. Wave 1 UAT dates most likely to be pushed — dates to be confirmed with Austin.

*Update 2026-06-16:* Wave 1 UAT did not start 6/15 — Austin sent no deployment/follow-up. Salah confirming revised Wave 1 dates with Austin today; Austin indicated ShareCare partnership item must land first — full slip duration **TBD**.

*Update 2026-06-22:* Van demo held **2026-06-22** as scheduled.

*Update 2026-06-23:* Wave 1 UAT set to **2026-06-22**; Wave 2–3 and all Prod dates **TBD**.

*Update 2026-06-24:* Michael Payment Management **Wave 1 page** (card path) ready for UAT promotion — **Credit Card Management** only retains a UAT date on the plan; Prefill API and Invoice Upload UAT **TBD**; Wave 2–3 Prod still **TBD**.

| Wave | Feature | Scope | Account flag | UAT | Prod | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Wave 1 | Credit Card Management | Shows existing User SavedPayments; cart must include User **and** Account SavedPayments (valid / non-expired only). Assumes Payflow issues resolved. | Yes | 2026-06-22 | TBD | OC-9649/OC-9653 fixes in QA (2026-06-24); Islam unblocked on Add Account Card. |
| Wave 1 | Prefill Order form API | API to prefill order form | Yes | TBD | TBD | Scenario testing started 2026-06-24. |
| Wave 1 | Invoice Upload to S3 | On successful Request payment: upload with Type **Invoice**. Prod path: `Chartswap/Invoices`. | Yes | TBD | TBD | Validate VF bucket filtering — invoice filter may hide provider cost on portal; ShareCare provider visibility still open (Sarah). |
| Wave 2 | Status Retrieval API | Method to build response body; also used for Status Sync Job payload. | — | TBD | TBD | Webhook integration has not been communicated to us yet from their side. |
| Wave 2 | Status Sync Job | Scheduled / account-scoped status sync. | Yes | TBD | TBD | Webhook integration has not been communicated to us yet from their side. |
| Wave 3 | Auto-Pay via Credit Card | New payment flow (Transaction Reconciliation Project / TPR). If Request is in any cart and user pays via Auto-Pay, remove Request from **all** carts before Auto-Pay runs. | — | TBD | TBD | — |
| TBD | SSO | Single sign-on integration — requires PD metadata and config. | Yes | TBD | TBD | Release wave unknown; PD metadata, and config still missing — see Risks |
| TBD | Cart hiding | Hide cart UI when enabled. | Yes | TBD | TBD | — |
| TBD | Prevent Record Finder | Block Record Finder when enabled. | Yes | TBD | TBD | — |
| TBD | Suppress email notifications | Disable email notifications when enabled. | Yes | TBD | TBD | Account-flag behavior confirm with client (Salah) |

---

## Open delivery blockers — payment bugs (1 To-Do + 1 in QA)

*Process (2026-06-22 standup):* When handing a bug to QA, dev should demo the fix with the tester first to reduce ping-pong. Use **Blocked** (not Re-open) when fix is merged but retest cannot proceed — preserves reopen analytics.

*Synced from Jira epic [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) on 2026-06-24 (live refresh).*

**Nine open bugs** on the epic. **Two Major bugs** below block provider sign-off or RR no-records flow. **Seven others** in QA (all Michael Girgis) — excluded per severity/scope: OC-9575, OC-9654 (Minor); OC-9656 (Medium); OC-9649, OC-9652, OC-9653, OC-9659 (Wave 1 payment — in QA, slow UAT retest but not hard Pre-UAT provider blockers). OC-9564, OC-9618, OC-9620 **closed** since last sync.

### ShareCare

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9562](https://ontellus.atlassian.net/browse/OC-9562) | Sharecare authorization submit fails with Too many SOQL queries (101) on `enterrequestdatasc` — blocks ShareCare workflow completion | **To-Do** | Sara Hassan | **New 2026-06-09** — Major — no workaround. **Update 2026-06-10:** Michael fixing sandbox company routing — ShareCare S3 uploads were hitting production bucket. **Update 2026-06-15:** Michael fixing cost/full-film scenario in sandbox. **Update 2026-06-16:** Hamed retested report scenario — OK; provider cost not visible in VF. **Update 2026-06-22:** Conversation fix **merged** — retest blocked on provider-cost / provider-dot visibility in ChartSwap. **Update 2026-06-24:** Workflow runs; provider not shown on ChartSwap provider page — reassigned from Hamed to **Sarah** *(Jira updated 2026-06-24)* |

### Record Retrieval

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9630](https://ontellus.atlassian.net/browse/OC-9630) | CNR document not visible to requester after No-Records **Rejected** — requester cannot download no-records evidence | **QA** | Michael Girgis | **New 2026-06-21** — Major — no workaround. **Update 2026-06-22:** Michael deployed CNR fix to QA/UAT build. **Update 2026-06-24:** Youssef retested — CNR visible and request creation OK; **empty file also uploads** — not closing until Michael reviews *(Jira unchanged — still QA)* |

### Wave 1 Payment Management (in QA — excluded from blockers)

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9649](https://ontellus.atlassian.net/browse/OC-9649) | Removal of the firm's last valid card is not blocked | **QA** | Michael Girgis | **New 2026-06-24** — fix deployed QA |
| [OC-9653](https://ontellus.atlassian.net/browse/OC-9653) | "Add Account Card" shows Insufficient Privileges instead of secure card form | **QA** | Michael Girgis | **New 2026-06-24** — fix deployed QA; unblocked Islam on firm-card add |
| [OC-9652](https://ontellus.atlassian.net/browse/OC-9652) | Patient prefill PHI not deleted when PatternData session ends (tab/window closed) | **QA** | Michael Girgis | **New 2026-06-24** — Van-demo / DEF-017 re-scope |
| [OC-9659](https://ontellus.atlassian.net/browse/OC-9659) | Request submission stays enabled when firm has no valid card (submission gate not enforced) | **QA** | Michael Girgis | **New 2026-06-24** |
| [OC-9656](https://ontellus.atlassian.net/browse/OC-9656) | Payment Transactions page: Transaction ID exposes internal admin link; remove misleading Threshold Approved and Invoice # details | **QA** | Michael Girgis | **New 2026-06-24** — Medium (workaround: ignore link/details) |
| [OC-9654](https://ontellus.atlassian.net/browse/OC-9654) | Replace card reports "No active AutoPay requests are linked" when card has New/Ordered requests | **QA** | Michael Girgis | **New 2026-06-24** — Minor |
| [OC-9575](https://ontellus.atlassian.net/browse/OC-9575) | Submit with AutoPay stays disabled on saved Draft even when authorization form is uploaded | **QA** | Michael Girgis | Minor — updated 2026-06-24 |

---

## Current Focus

| Member | Focus |
| --- | --- |
| Michael | Five open bugs (Van-demo batch + CNR empty-file + Youssef handover); Payment Management Wave 1 deploy follow-up; consent/card-expiry logic with Sarah; demo fixes with testers before QA handoff |
| Islam | Wave 1 UAT scenarios — Course Health rejection, AutoPay paths; verify firm-card add after OC-9653 fix; 3 classes still below 75% coverage |
| Sarah | PFP providers e2e testing |
| Youssef | CNR retest done — hold close until empty-file resolved; support Islam/Sarah on scenario splits (STD, PFP, RR) |

---

## Risks & challenges

Each item below is stated as a **condition → consequence**, with a mitigation that addresses that specific consequence.


| #   | Risk / challenge                                                                                                                                                                                                                                                                                                               | Mitigation                                                                                                                                                                                                                                                                 | Severity |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| 1   | **Pre-UAT missed 06/14 forecast; Wave 1 UAT missed 6/15; scenario testing started 6/24 but Austin has not confirmed revised dates.** ShareCare provider visibility and CNR empty-file upload are the remaining Pre-UAT gaps — June go-live still at risk until Wave 1 dates are re-baselined.                                                                                          | <ul><li>Salah confirm slip duration with Austin</li><li>Re-baseline Pre-UAT forecast once Austin responds</li><li>Michael demo fixes with testers before QA handoff</li><li>Escalate if go-live is threatened</li></ul> | High     |
| 2   | **End-to-end testing against the PD lower env cannot start.** PD has not responded on lower-environment access, so BAU/E2E validation hasn't begun — only provider-level sandbox testing is underway. The integration risks being validated late, or not before go-live. **Escalation deadline was 2026-06-08** — no response confirmed (Maria engaged 06-08; still awaiting internal PD reply).                                                         | <ul><li>Follow up with Katherine; keep mocking the integration in the meantime</li><li>Escalate to Austin / Van that go-live is at risk if the needed access is not received</li></ul>                                                                                | High     |
| 3   | **SSO cannot be configured or release-planned.** PD has not provided the SSO metadata and configuration required for sandbox/UAT access, leaving the SSO release wave undefined and blocking UAT sign-off.                                                                                                                     | <ul><li>Track as a PD dependency</li><li>Escalated to Austin / PD contacts</li><li>Hold UAT sign-off until SSO config is in place</li></ul>                                                                                                                                                     | High     |
| 4   | **Wave 2 dates may slip (Status Retrieval API & Status Sync Job).** PD has not yet communicated the webhook integration details these features depend on, so the 06/17 UAT / 06/22 prod targets may move. **Escalation deadline was 2026-06-10** — no PD response confirmed in standup.                                                                                                                      | <ul><li>Request webhook details from PD; track alongside the SSO dependency</li><li>Re-baseline Wave 2 dates once received</li><li>Escalate to Austin if still not received after 06/10</li></ul>                                                                                                 | Medium   |
| 5   | **Provider scope uncertainty.** Pharmacy and other provider paths discovered in code; unclear if in scope vs legacy. Expanding scope could delay Pre-UAT on the 7 known providers. **Updox** now deprioritized per Austin (likely not on production).                                                                                                                      | <ul><li>Limit focus to STD, PFP, RR, Waystar, CIOX, ShareCare unless Van/Nabuya confirms otherwise</li><li>Michael posted Pharmacy question to PD group; follow up with LeBon on Walmart/Pharmacy payment approach</li><li>Hamed reviewing provider list Michael sends</li></ul>                                                                                                 | Low   |
| 6   | **Code updates can reopen fixed bugs and break previously passing scenarios.** Ongoing fixes and Austin-driven changes may regress areas already signed off in Pre-UAT, forcing duplicate retest cycles. Van-demo bug batch (OC-9652–9659) filed 2026-06-24 adds UAT retest load on Michael.                                                                                                                      | <ul><li>Include detailed testing steps, expected results, and related areas to retest after updates in each story</li><li>Add screenshots of the resolution as evidence in a Jira comment when closing or handing off a fix</li><li>Adopt feature-branch + PR workflow to preserve change history</li><li>Michael follow up with Austin on master merge gaps</li></ul>                                                                                                 | High     |
| 7   | **Post-Atlassian migration Jira access gaps — partial progress.** Sarah old account works via new-browser workaround; Hamed BO board access restored. Youssef new account active but **no project space** — cannot board items; daily log automation paused until permissions stable.                                                                                                                      | <ul><li>Salah escalate with Austin/IT</li><li>Use BO board and Teams for interim coordination</li><li>Each person document their specific access issue on Austin tracking sheet</li><li>Log interim work outside Jira until access restored</li></ul>                                                                                                 | Medium   |
