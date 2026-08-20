# Pattern Data — delivery progress

**Go-live goal:** End of June 2026 · **Epic:** [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) · **As of:** 2026-06-23

---

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Pre-UAT** | Youssef | In progress | <li>4/7 providers tested [STD, PFP, RR, Waystar]</li><li>RR payment bugs cleared and retested (OC-9529, OC-9531 closed; full flow retest 2026-06-08)</li><li>Hamed completed ShareCare and Updox sandbox passes (2026-06-10); Updox deprioritized per Austin</li><li>Islam pushed Wave 1 unit tests to feature branch (2026-06-15) — coverage ≥75% on under-covered classes; deployed to sandbox</li><li>Michael completed most Austin transaction + Invoice/S3 comments (2026-06-15); CNR fix deployed to QA/UAT build (2026-06-22)</li><li>Youssef closed most open bugs (2026-06-21) — OC-9566, OC-9576, OC-9567, OC-9574, OC-9389 closed; ~2 items remaining</li><li>Youssef retested open bugs (2026-06-16) — stable on current fix batch through 6/21 close-out</li><li>Islam back from leave (2026-06-16/17) — provider-testing session with Michael + Youssef scheduled 2026-06-22</li><li>Hussein confirmed process: dev demos fix with tester before QA handoff; testers self-test once they understand the change (2026-06-22)</li> | <ul><li>ShareCare **Blocked** on Hamed — fix merged but provider cost not visible in ChartSwap UI (Michael investigating master/data visibility)</li><li>OC-9630 CNR requester visibility in QA — Michael confirming UAT vs Pattern Data portal UI behavior with Youssef</li><li>~2 open bugs Youssef finishing before demo wrap-up (2026-06-22)</li><li>Written **testing scenarios doc** from Youssef — required before provider split and business Q&amp;A (due 2026-06-22)</li><li>Michael: ShareCare provider-cost visibility; CNR UI if not shown in UAT; remaining field-removal items; merge/VoicePlus deploy gaps on master</li><li>Islam + Michael code review — 3 classes still below 75% coverage</li><li>Sarah CIOX data classes not started — waiting for bug churn to clear</li><li>Wave 1 unit-test sign-off before UAT — Islam + Michael</li><li>Salah confirm Wave 1 / Pre-UAT dates with Austin — slip duration still TBD</li></ul> | 2026-05-21 | **2026-06-17** *(at risk — dates TBD pending Austin)* | <li>Sandbox goal: **pre-fulfillment parity with UAT** — not chasing fulfillment simulation on sandbox. CIOX fulfillment gap accepted per 06-05 agreement.</li><li>External-provider fulfillment simulation deferred to UAT (Eric).</li><li>Automation paused — manual retest for now.</li><li>**06/14 Pre-UAT forecast missed** — Wave 1 UAT did not start 6/15.</li><li>**Updox deprioritized** per Austin.</li><li>Team adopting feature-branch + PR workflow; Salah + Michael investigating PR adoption.</li><li>**06/22 standup:** Van demo day — light retesting during demo; use **Blocked** (not Re-open) when fix is done but retest cannot proceed (ShareCare).</li><li>Jira access partial progress — Sarah/Hamed on BO board; Youssef new account lacks project space.</li> |
| **PD Sandbox (BAU)** | Van | In progress | — | BAU flows — can start now on STD, PFP, RR, Way-Star in parallel | 2026-05-21 | **2026-06-02** | agreed to conduct regular demos for Van as he's not testing PD sandbox and relying more on testing on UAT once code is promoted. |
| **UAT** | Van | Not started | — | <ul><li>Wave 1 (6/15): Prefill API, CC Management, Invoice Upload</li><li>Wave 2 (6/17): Status Retrieval API, Status Sync Job</li><li>Wave 3 (6/22): Auto-Pay via CC (TPR)</li></ul> | 2026-06-15 – 2026-06-25 | **At risk** — Wave 1 UAT missed 6/15; Van demo held **2026-06-22**; Salah confirming slip with Austin | Wave 2 dates may slip — PD webhook details not provided yet (see Risks). Austin also waiting on ShareCare partnership item before Wave 1 push. |
| **Production** | — | Not started | — | UAT sign-off | 2026-06-30 | Unverified | — |

---

## Client release plan (received 2026-06-01)

*Source: client release plan (Austin). Account-flagged items ship when enabled per account.*

*Environment promotion targets by wave.*

*Update 2026-06-15:* Scheduled demo for Van postponed to **Monday 2026-06-22**. Wave 1 UAT dates most likely to be pushed — dates to be confirmed with Austin.

*Update 2026-06-16:* Wave 1 UAT did not start 6/15 — Austin sent no deployment/follow-up. Salah confirming revised Wave 1 dates with Austin today; Austin indicated ShareCare partnership item must land first — full slip duration **TBD**.

*Update 2026-06-22:* Van demo held **2026-06-22** as scheduled.

*Update 2026-06-23:* Wave 1 UAT set to **2026-06-22**; Wave 2–3 and all Prod dates **TBD**.

| Wave | Feature | Scope | Account flag | UAT | Prod | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Wave 1 | Prefill Order form API | API to prefill order form | Yes | 2026-06-22 | TBD | — |
| Wave 1 | Credit Card Management | Shows existing User SavedPayments; cart must include User **and** Account SavedPayments (valid / non-expired only). Assumes Payflow issues resolved. | Yes | 2026-06-22 | TBD | Added new Contact/User-level flag to enable the saved payments page edit per contact. |
| Wave 1 | Invoice Upload to S3 | On successful Request payment: upload with Type **Invoice**. Prod path: `Chartswap/Invoices`. | Yes | 2026-06-22 | TBD | Validate VF bucket filtering — invoice filter may hide provider cost on portal; Michael fixing provider visibility 2026-06-22. |
| Wave 2 | Status Retrieval API | Method to build response body; also used for Status Sync Job payload. | — | TBD | TBD | Webhook integration has not been communicated to us yet from their side. |
| Wave 2 | Status Sync Job | Scheduled / account-scoped status sync. | Yes | TBD | TBD | Webhook integration has not been communicated to us yet from their side. |
| Wave 3 | Auto-Pay via Credit Card | New payment flow (Transaction Reconciliation Project / TPR). If Request is in any cart and user pays via Auto-Pay, remove Request from **all** carts before Auto-Pay runs. | — | TBD | TBD | — |
| TBD | SSO | Single sign-on integration — requires PD metadata and config. | Yes | TBD | TBD | Release wave unknown; PD metadata, and config still missing — see Risks |
| TBD | Cart hiding | Hide cart UI when enabled. | Yes | TBD | TBD | — |
| TBD | Prevent Record Finder | Block Record Finder when enabled. | Yes | TBD | TBD | — |
| TBD | Suppress email notifications | Disable email notifications when enabled. | Yes | TBD | TBD | Account-flag behavior confirm with client (Salah) |

---

## Open delivery blockers — payment bugs (1 blocked + 1 in QA)

*Process (2026-06-22 standup):* When handing a bug to QA, dev should demo the fix with the tester first to reduce ping-pong. Use **Blocked** (not Re-open) when fix is merged but retest cannot proceed — preserves reopen analytics.

*Synced from Jira epic [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) on 2026-06-23 (live).*

**Two open Major payment bugs** block provider sign-off or RR no-records flow. Four additional **Minor** bugs remain in QA (OC-9564, OC-9575, OC-9618, OC-9620) — excluded below per severity filter; they slow Pre-UAT but do not hard-block provider paths.

### ShareCare

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9562](https://ontellus.atlassian.net/browse/OC-9562) | Authorization submit fails with Too many SOQL queries (101) on `enterrequestdatasc` — blocks ShareCare workflow completion | **Blocked** *(board)* / To-Do *(Jira)* | Mohamed Hamed | **New 2026-06-09** — Major — no workaround. **Update 2026-06-10:** Michael fixing sandbox company routing — ShareCare S3 uploads were hitting production bucket. **Update 2026-06-15:** Michael fixing cost/full-film scenario in sandbox. **Update 2026-06-16:** Hamed retested report scenario — OK; provider cost not visible in VF. **Update 2026-06-22:** Conversation fix **merged** — retest blocked on provider-cost / provider-dot visibility in ChartSwap, not fix failure; Salah marked **Blocked** on Hamed (not Re-open); Michael investigating master/data visibility |

### Record Retrieval

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9630](https://ontellus.atlassian.net/browse/OC-9630) | CNR document not visible to requester after No-Records **Rejected** — requester cannot download no-records evidence | **QA** | Michael Girgis | **New 2026-06-21** — Major — no workaround. **Update 2026-06-22:** Michael deployed CNR fix to QA/UAT build; confirming whether CNR must appear in Pattern Data portal when sent via sync (Youssef: if we send CNR in sync it must be visible in portal); Michael verifying UAT vs PD UI behavior |

---

### Flow to be retested

*After bug fixes — scheduled retest*

| Flow | Assignee | Date |
| --- | --- | --- |
| CNR requester visibility (post OC-9630 fix) | Youssef | 2026-06-22 — Michael confirming UAT vs Pattern Data portal UI |
| Record Retrieval (post OC-9566 fix) | Youssef | 2026-06-16 — retest OK; **OC-9566 closed 2026-06-21** |
| Provider testing split (post scenarios doc + Islam/Michael session) | Team | 2026-06-22 — scenarios doc due; Islam + Michael + Youssef session same day |

---

## Current Focus

| Member | Focus |
| --- | --- |
| Michael | ShareCare provider-cost / provider-dot visibility in ChartSwap; CNR UI visibility vs UAT legacy logic; remaining field-removal items after build validation; merge/VoicePlus deploy gaps on master; demo fixes with testers before QA handoff |
| Islam | Provider-testing session with Michael + Youssef; 3 classes still below 75% coverage — reply on coverage report |
| Sarah | CIOX data classes not started (waiting for bug churn); needs written testing scenarios from Youssef; Heba Plus Card fix when Jira access restored |
| Hamed | ShareCare ticket **Blocked** — fix merged, retest blocked on provider-cost visibility; join provider split after scenarios doc |
| Youssef | Send testing scenarios doc (~1 h); finish ~2 remaining bugs; review Pattern Data filter with Salah before SharePoint upload; unavailable until 7:30 PM 2026-06-22 |
| Salah | Mark ShareCare Blocked on board; upload Pattern Data filter to SharePoint; confirm Wave 1 UAT slip with Austin; escalate Youssef Jira access; distribute ~62 h CDP time |

---

## Risks & challenges

Each item below is stated as a **condition → consequence**, with a mitigation that addresses that specific consequence.


| #   | Risk / challenge                                                                                                                                                                                                                                                                                                               | Mitigation                                                                                                                                                                                                                                                                 | Severity |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| 1   | **Pre-UAT missed 06/14 forecast; Wave 1 UAT missed 6/15; Van demo held 6/22 but Austin has not confirmed revised dates.** Youssef closed most bugs 6/21 (~2 remaining) and ShareCare is blocked on UI visibility only — June go-live still at risk until Wave 1 dates are re-baselined.                                                                                          | <ul><li>Salah confirm slip duration with Austin</li><li>Re-baseline Pre-UAT forecast once Austin responds</li><li>Michael demo fixes with testers before QA handoff</li><li>Escalate if go-live is threatened</li></ul> | High     |
| 2   | **End-to-end testing against the PD lower env cannot start.** PD has not responded on lower-environment access, so BAU/E2E validation hasn't begun — only provider-level sandbox testing is underway. The integration risks being validated late, or not before go-live. **Escalation deadline was 2026-06-08** — no response confirmed (Maria engaged 06-08; still awaiting internal PD reply).                                                         | <ul><li>Follow up with Katherine; keep mocking the integration in the meantime</li><li>Escalate to Austin / Van that go-live is at risk if the needed access is not received</li></ul>                                                                                | High     |
| 3   | **SSO cannot be configured or release-planned.** PD has not provided the SSO metadata and configuration required for sandbox/UAT access, leaving the SSO release wave undefined and blocking UAT sign-off.                                                                                                                     | <ul><li>Track as a PD dependency</li><li>Escalated to Austin / PD contacts</li><li>Hold UAT sign-off until SSO config is in place</li></ul>                                                                                                                                                     | High     |
| 4   | **Wave 2 dates may slip (Status Retrieval API & Status Sync Job).** PD has not yet communicated the webhook integration details these features depend on, so the 06/17 UAT / 06/22 prod targets may move. **Escalation deadline was 2026-06-10** — no PD response confirmed in standup.                                                                                                                      | <ul><li>Request webhook details from PD; track alongside the SSO dependency</li><li>Re-baseline Wave 2 dates once received</li><li>Escalate to Austin if still not received after 06/10</li></ul>                                                                                                 | Medium   |
| 5   | **Provider scope uncertainty.** Pharmacy and other provider paths discovered in code; unclear if in scope vs legacy. Expanding scope could delay Pre-UAT on the 7 known providers. **Updox** now deprioritized per Austin (likely not on production).                                                                                                                      | <ul><li>Limit focus to STD, PFP, RR, Waystar, CIOX, ShareCare unless Van/Nabuya confirms otherwise</li><li>Michael posted Pharmacy question to PD group; follow up with LeBon on Walmart/Pharmacy payment approach</li><li>Hamed reviewing provider list Michael sends</li></ul>                                                                                                 | Low   |
| 6   | **Code updates can reopen fixed bugs and break previously passing scenarios.** Ongoing fixes and Austin-driven changes may regress areas already signed off in Pre-UAT, forcing duplicate retest cycles. Merge/rebase class gaps on master flagged 2026-06-16; Michael following up Austin on VoicePlus deploy gaps (2026-06-22).                                                                                                                      | <ul><li>Include detailed testing steps, expected results, and related areas to retest after updates in each story</li><li>Add screenshots of the resolution as evidence in a Jira comment when closing or handing off a fix</li><li>Adopt feature-branch + PR workflow to preserve change history</li><li>Michael follow up with Austin on master merge gaps</li></ul>                                                                                                 | High     |
| 7   | **Post-Atlassian migration Jira access gaps — partial progress.** Sarah old account works via new-browser workaround; Hamed BO board access restored. Youssef new account active but **no project space** — cannot board items; daily log automation paused until permissions stable.                                                                                                                      | <ul><li>Salah escalate with Austin/IT</li><li>Use BO board and Teams for interim coordination</li><li>Each person document their specific access issue on Austin tracking sheet</li><li>Log interim work outside Jira until access restored</li></ul>                                                                                                 | Medium   |
