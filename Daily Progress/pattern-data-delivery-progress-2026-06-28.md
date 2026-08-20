# Pattern Data — delivery progress

**Go-live goal:** End of June 2026 · **Epic:** [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) · **As of:** 2026-06-28

---

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Pre-UAT** | Youssef | In progress | <li>4/7 providers tested [STD, PFP, RR, Waystar]</li><li>RR payment bugs cleared and retested (OC-9529, OC-9531 closed; full flow retest 2026-06-08)</li><li>Van demo held **2026-06-22**; Youssef delivered **12 Wave 1 UAT scenarios** + testing guide (2026-06-23)</li><li>Michael fixed card-management bugs and deployed to QA (2026-06-24) — OC-9649, OC-9653; Islam unblocked on firm-card add</li><li>Michael completed Payment Management Wave 1 chain set — card path ready for UAT deploy (2026-06-24)</li><li>Youssef CNR retest OK — request creation and CNR visibility working (2026-06-24)</li><li>Wave 1 UAT scenario testing **started** (2026-06-24)</li><li>**2026-06-28:** Michael confirmed **all his bugs in QA**; Sarah finished UAT Massing scenario + PFP termination-date scenario; Islam finished Wave 1 UAT scenarios except **Winward** (awaiting Michael)</li><li>Label script updated by Youssef; Sarah applied **3 label tags** to open bugs</li> | <ul><li>[OC-9630](https://ontellus.atlassian.net/browse/OC-9630) CNR — still **QA**; empty auth file upload under Michael review</li><li>[OC-9676](https://ontellus.atlassian.net/browse/OC-9676) **new ShareCare autopay** — PD user request stuck Pending Payment; Sarah assigned to test *(filed 2026-06-28)*</li><li>Youssef: verify QA fixes on sandbox with **both PD accounts** before deploy; confirm PD + Payment paths work independently</li><li>Youssef: build **film provider** flow proactively for Van — needs deploy doc / account-flag fields from Sarah</li><li>Salah apply **label categories** on board via Cursor (Youssef lacks Jira access; steps incoming)</li><li>Sarah finish in-progress **PFP provider flow**; then take **2 UAT scenarios** from Michael's queue</li><li>Islam start **VF provider business** scenarios; follow up Michael on **Winward** scenario; take **2 UAT scenarios** from Michael</li><li>Test both **PatternData v0 and v1** after PD endpoint migration (PD meeting 2026-06-25 night)</li></ul> | 2026-05-21 | **2026-06-17** *(at risk — dates TBD pending Austin)* | <li>Sandbox goal: **pre-fulfillment parity with UAT** — not chasing fulfillment simulation on sandbox.</li><li>External-provider fulfillment simulation deferred to UAT (Eric).</li><li>Automation paused — manual retest for now.</li><li>**06/14 Pre-UAT forecast missed** — Wave 1 UAT did not start 6/15.</li><li>**Updox deprioritized** per Austin.</li><li>**06/28 standup:** PD moved PatternData to **point 0** with UX changes — team must validate both versions still work on same account.</li><li>**06/28 standup:** Austin now in **Ireland** (near team timezone) — respond early on client chat.</li><li>Jira access partial — Youssef new account still lacks project space; Salah to apply labels on his behalf.</li> |
| **PD Sandbox (BAU)** | Van | In progress | — | BAU flows — can start now on STD, PFP, RR, Way-Star in parallel | 2026-05-21 | **2026-06-02** | agreed to conduct regular demos for Van as he's not testing PD sandbox and relying more on testing on UAT once code is promoted. |
| **UAT** | Van | In progress | <li>Wave 1 Payment Management UI chain set complete — card path deployed QA/UAT (2026-06-24)</li><li>12 Wave 1 scenarios documented; Islam + Sarah largely complete UI scenario pass (2026-06-28)</li><li>Michael rebalancing — **2 scenarios each** to Sarah and Islam while he focuses on UAT deploy prep</li> | <ul><li>Wave 1 (6/22): Prefill API, CC Management, Invoice Upload — retest payment bugs in QA</li><li>Wave 2 (TBD): Status Retrieval API, Status Sync Job</li><li>Wave 3 (TBD): Auto-Pay via CC (TPR)</li><li>Austin deploy decision on Payment Management page</li><li>Islam: **Winward** scenario blocked on Michael reply</li></ul> | 2026-06-15 – 2026-06-25 | **At risk** — Wave 1 UAT missed 6/15; scenario testing in progress; Salah confirming slip with Austin | Wave 2 dates may slip — PD webhook details not provided yet (see Risks). Youssef building film provider flow proactively per Van request. |
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

*Update 2026-06-28:* Van requested **film provider** flow — Youssef building proactively; deploy approach TBD. PD PatternData endpoint migration (point 0) may affect integration testing — no client-side change expected but dual-version validation needed.

| Wave | Feature | Scope | Account flag | UAT | Prod | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Wave 1 | Credit Card Management | Shows existing User SavedPayments; cart must include User **and** Account SavedPayments (valid / non-expired only). Assumes Payflow issues resolved. | Yes | 2026-06-22 | TBD | OC-9649/OC-9653 fixes in QA (2026-06-24); Islam unblocked on Add Account Card. |
| Wave 1 | Prefill Order form API | API to prefill order form | Yes | TBD | TBD | Scenario testing in progress (2026-06-28). |
| Wave 1 | Invoice Upload to S3 | On successful Request payment: upload with Type **Invoice**. Prod path: `Chartswap/Invoices`. | Yes | TBD | TBD | Validate VF bucket filtering — invoice filter may hide provider cost on portal. |
| Wave 2 | Status Retrieval API | Method to build response body; also used for Status Sync Job payload. | — | TBD | TBD | Webhook integration has not been communicated to us yet from their side. |
| Wave 2 | Status Sync Job | Scheduled / account-scoped status sync. | Yes | TBD | TBD | Webhook integration has not been communicated to us yet from their side. |
| Wave 3 | Auto-Pay via Credit Card | New payment flow (Transaction Reconciliation Project / TPR). If Request is in any cart and user pays via Auto-Pay, remove Request from **all** carts before Auto-Pay runs. | — | TBD | TBD | — |
| TBD | SSO | Single sign-on integration — requires PD metadata and config. | Yes | TBD | TBD | Release wave unknown; PD metadata, and config still missing — see Risks |
| TBD | Cart hiding | Hide cart UI when enabled. | Yes | TBD | TBD | — |
| TBD | Prevent Record Finder | Block Record Finder when enabled. | Yes | TBD | TBD | — |
| TBD | Suppress email notifications | Disable email notifications when enabled. | Yes | TBD | TBD | Account-flag behavior confirm with client (Salah) |
| TBD | Film provider flow | Van-requested film provider onboarding | Yes | TBD | TBD | Youssef building proactively (2026-06-28); Sarah to share AsDocs account-flag field list. |

---

## Open delivery blockers — payment bugs (2 in QA)

*Process (2026-06-22 standup):* When handing a bug to QA, dev should demo the fix with the tester first to reduce ping-pong. Use **Blocked** (not Re-open) when fix is merged but retest cannot proceed — preserves reopen analytics.

*Synced from Jira epic [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) on 2026-06-28 (live refresh).*

**Eleven open bugs** on the epic. **Two Major bugs** below block provider sign-off or ShareCare/RR flows. **Nine others** in QA or Backlog — excluded per severity/scope: OC-9575, OC-9654 (Minor); OC-9656, OC-9674 (Medium/workaround); OC-9649, OC-9652, OC-9653, OC-9659 (Wave 1 payment — in QA); OC-9668 (Backlog/test). OC-9562 **closed** since last sync.

### ShareCare

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9676](https://ontellus.atlassian.net/browse/OC-9676) | Sharecare Subpoena: PD user autopay fails — request stuck Pending Payment, no transaction | **QA** | Sara Hassan | **New 2026-06-28** — Major — found by Hamed during ShareCare creation flow; reassigned to Sarah *(Jira updated 2026-06-28)* |

### Record Retrieval

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9630](https://ontellus.atlassian.net/browse/OC-9630) | CNR document not visible to requester after No-Records **Rejected** — requester cannot download no-records evidence | **QA** | Michael Girgis | **New 2026-06-21** — Major — no workaround. **Update 2026-06-24:** Youssef retested — CNR visible and request creation OK; **empty file also uploads** — not closing until Michael reviews *(still QA 2026-06-28)* |

### Wave 1 Payment Management (in QA — excluded from blockers)

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9649](https://ontellus.atlassian.net/browse/OC-9649) | Removal of the firm's last valid card is not blocked | **QA** | Michael Girgis | Fix deployed QA |
| [OC-9653](https://ontellus.atlassian.net/browse/OC-9653) | "Add Account Card" shows Insufficient Privileges instead of secure card form | **QA** | Michael Girgis | Fix deployed QA; unblocked Islam on firm-card add |
| [OC-9652](https://ontellus.atlassian.net/browse/OC-9652) | Patient prefill PHI not deleted when PatternData session ends (tab/window closed) | **QA** | Michael Girgis | Van-demo / DEF-017 re-scope |
| [OC-9659](https://ontellus.atlassian.net/browse/OC-9659) | Request submission stays enabled when firm has no valid card (submission gate not enforced) | **QA** | Michael Girgis | — |
| [OC-9656](https://ontellus.atlassian.net/browse/OC-9656) | Payment Transactions page: Transaction ID exposes internal admin link; remove misleading Threshold Approved and Invoice # details | **QA** | Michael Girgis | Medium (workaround: ignore link/details) |
| [OC-9654](https://ontellus.atlassian.net/browse/OC-9654) | Replace card reports "No active AutoPay requests are linked" when card has New/Ordered requests | **QA** | Michael Girgis | Minor |
| [OC-9575](https://ontellus.atlassian.net/browse/OC-9575) | Submit with AutoPay stays disabled on saved Draft even when authorization form is uploaded | **QA** | Michael Girgis | Minor |
| [OC-9674](https://ontellus.atlassian.net/browse/OC-9674) | PFP/BAU submit: AutoPay missing-card failure stamped when firm AutoPay disabled | **QA** | Michael Girgis | **New 2026-06-25** — Medium (workaround: ignore stamped fields; pay via cart) |

---

## Current Focus

| Member | Focus |
| --- | --- |
| Michael | UAT deploy prep and post-deploy fixes; all bugs in QA; send sandbox admin config to Youssef when back from doctor; reply Islam on **Winward** scenario |
| Sarah | Finish PFP provider flow scenario; test **OC-9676** ShareCare autopay; take **2 UAT scenarios** from Michael; verify label tags hit new categories |
| Islam | **VF provider business** flow scenarios; follow up Michael on **Winward**; take **2 UAT scenarios** from Michael |
| Youssef | Dual-account sandbox QA retest; build **film provider** flow for Van; send label steps to Salah |
| Hamed | Optional scenario pull from sheet if capacity; ShareCare retest when Sarah clears OC-9676 |

---

## Risks & challenges

Each item below is stated as a **condition → consequence**, with a mitigation that addresses that specific consequence.


| #   | Risk / challenge                                                                                                                                                                                                                                                                                                               | Mitigation                                                                                                                                                                                                                                                                 | Severity |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| 1   | **Pre-UAT missed 06/14 forecast; Wave 1 UAT missed 6/15; scenario testing in progress but Austin has not confirmed revised dates.** ShareCare autopay (OC-9676) and CNR empty-file upload are active Pre-UAT gaps — June go-live still at risk until Wave 1 dates are re-baselined.                                                                                          | <ul><li>Salah confirm slip duration with Austin</li><li>Re-baseline Pre-UAT forecast once Austin responds</li><li>Michael demo fixes with testers before QA handoff</li><li>Escalate if go-live is threatened</li></ul> | High     |
| 2   | **End-to-end testing against the PD lower env cannot start.** PD has not responded on lower-environment access, so BAU/E2E validation hasn't begun — only provider-level sandbox testing is underway. The integration risks being validated late, or not before go-live. **Escalation deadline was 2026-06-08** — no response confirmed (Maria engaged 06-08; still awaiting internal PD reply).                                                         | <ul><li>Follow up with Katherine; keep mocking the integration in the meantime</li><li>Escalate to Austin / Van that go-live is at risk if the needed access is not received</li></ul>                                                                                | High     |
| 3   | **SSO cannot be configured or release-planned.** PD has not provided the SSO metadata and configuration required for sandbox/UAT access, leaving the SSO release wave undefined and blocking UAT sign-off.                                                                                                                     | <ul><li>Track as a PD dependency</li><li>Escalated to Austin / PD contacts</li><li>Hold UAT sign-off until SSO config is in place</li></ul>                                                                                                                                                     | High     |
| 4   | **Wave 2 dates may slip (Status Retrieval API & Status Sync Job).** PD has not yet communicated the webhook integration details these features depend on, so the 06/17 UAT / 06/22 prod targets may move. **Escalation deadline was 2026-06-10** — no PD response confirmed in standup.                                                                                                                      | <ul><li>Request webhook details from PD; track alongside the SSO dependency</li><li>Re-baseline Wave 2 dates once received</li><li>Escalate to Austin if still not received after 06/10</li></ul>                                                                                                 | Medium   |
| 5   | **Provider scope uncertainty.** Pharmacy and other provider paths discovered in code; unclear if in scope vs legacy. Expanding scope could delay Pre-UAT on the 7 known providers. **Updox** now deprioritized per Austin (likely not on production). **Film provider** flow now requested by Van — scope addition mid-stream.                                                                                                                      | <ul><li>Limit focus to STD, PFP, RR, Waystar, CIOX, ShareCare unless Van/Nabuya confirms otherwise</li><li>Youssef build film flow proactively; Sarah share account-flag field requirements</li><li>Michael posted Pharmacy question to PD group; follow up with LeBon on Walmart/Pharmacy payment approach</li></ul>                                                                                                 | Low   |
| 6   | **Code updates can reopen fixed bugs and break previously passing scenarios.** Ongoing fixes and Austin-driven changes may regress areas already signed off in Pre-UAT, forcing duplicate retest cycles.                                                                                                                      | <ul><li>Include detailed testing steps, expected results, and related areas to retest after updates in each story</li><li>Add screenshots of the resolution as evidence in a Jira comment when closing or handing off a fix</li><li>Adopt feature-branch + PR workflow to preserve change history</li></ul>                                                                                                 | High     |
| 7   | **Post-Atlassian migration Jira access gaps — partial progress.** Youssef new account active but **no project space** — cannot board items or apply labels; Salah applying labels via Cursor on his behalf.                                                                                                                      | <ul><li>Salah escalate with Austin/IT</li><li>Use BO board and Teams for interim coordination</li><li>Each person document their specific access issue on Austin tracking sheet</li></ul>                                                                                                 | Medium   |
| 8   | **PD PatternData endpoint migration (point 0) may break dual-version testing.** PD changed PatternData to point 0 with UX updates (2026-06-25 meeting) — team must confirm both old and new endpoints work on same account before deploy.                                                                                                                      | <ul><li>Youssef validate both PD accounts independently and together on sandbox</li><li>Michael send admin config doc to Youssef when available</li><li>Do not deploy bundled PD+Payment until each path verified separately</li></ul>                                                                                                 | Medium   |

---

## Standup action items (2026-06-28)

*From [ChartSwap Daily Stand-up — 2026-06-28](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-06-28.docx).*

| Owner | Action | Status |
| --- | --- | --- |
| **Islam** | Follow up **Michael** on **Winward** UAT scenario (no reply yet) | Open |
| **Islam** | Start **VF provider business** flow scenarios from provider testing sheet | Open |
| **Islam** | Take **2 UAT scenarios** from Michael's queue after current work | Open |
| **Michael** | Send sandbox **admin/config doc** to Youssef for dual-account PD testing (when back from doctor) | Open |
| **Michael** | Reply **Islam** on **Winward** UAT scenario | Open |
| **Salah** | Apply **label categories** to open bugs on board via Cursor (steps from Youssef) | Open |
| **Salah** | Send daily **Pattern Data stats** with standup **action items embedded** (Hussein request) | Open |
| **Sarah** | Finish in-progress **PFP provider flow** scenario; then take **2 UAT scenarios** from Michael | Open |
| **Sarah** | Test **[OC-9676](https://ontellus.atlassian.net/browse/OC-9676)** ShareCare autopay bug (reassigned from Hamed) | Open |
| **Sarah** | Send **AsDocs link** for film account-flag fields to Youssef (field rename pending next week) | Open |
| **Sarah** | Re-verify **3 label tags** hit agreed category list | Open |
| **Team** | Validate **PatternData v0 and v1** both work after PD point-0 migration | Open |
| **Team** | Weekly **office visit Sundays** starting next week — Hussein emailing policy | Open |
| **Youssef** | Send label-application **steps** to Salah on chat | Open |
| **Youssef** | Verify QA fixes on sandbox with **both PD accounts** before deploy | Open |
| **Youssef** | Build **film provider** flow proactively for Van — needs deploy doc from Sarah | Open |
| **Hamed** | Pull scenarios from testing sheet if capacity allows (lower priority) | Open |
| **Islam** | Completed **Wave 1 UAT scenarios** except Winward | Done |
| **Michael** | All assigned bugs moved to **QA** | Done |
| **Sarah** | Finished **UAT Massing scenario** and **PFP termination-date** scenario | Done |
| **Sarah** | Applied **3 label tags** to bugs on board | Done |
| **Youssef** | Updated label **script/scale** for bulk label application | Done |
| **Hamed** | Found ShareCare autopay bug — filed and reassigned to Sarah (**OC-9676**) | Done |
