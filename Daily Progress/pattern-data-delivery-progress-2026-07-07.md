# Pattern Data — delivery progress

**Go-live goal:** End of June 2026 · **Epic:** [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) · **As of:** 2026-07-07

---

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Pre-UAT** | Youssef | In progress | <li>[OC-9630](https://ontellus.atlassian.net/browse/OC-9630) CNR **closed in Jira** (2026-07-07 sync)</li><li>ShareCare [OC-9676](https://ontellus.atlassian.net/browse/OC-9676) **live demo passed** — transaction OK (Sarah + Hamed test 62)</li><li>Michael: **Wave 1 deploy package** updated — apt-card component removed per Austin; sandbox-first path</li> | <ul><li>**2 Major blockers in QA:** [OC-9676](https://ontellus.atlassian.net/browse/OC-9676) ShareCare status transition; **[OC-9715](https://ontellus.atlassian.net/browse/OC-9715) Submit-with-AutoPay on all statuses** (new 2026-07-06)</li><li>**1 Major To-Do:** [OC-9659](https://ontellus.atlassian.net/browse/OC-9659) submission gate → **Islam**</li><li>Michael: **[OC-9575](https://ontellus.atlassian.net/browse/OC-9575)** in Progress + **[OC-9686](https://ontellus.atlassian.net/browse/OC-9686)** declined-card UI</li><li>Youssef: retest **STD 6-substatus blocker** (rollback on Michael's Thu code)</li><li>Salah: confirm **revised dates** with Austin; fix **daily stats + action items** delivery (Amr)</li></ul> | 2026-05-21 | **2026-06-17** *(at risk — dates TBD pending Austin)* | <li>**Demo-before-QA** reinforced — fixer + reporter test together before handoff</li><li>Michael scheduling **branches/sandbox session** (~30 min) with Islam, Sarah, Salah today</li><li>Austin: **Payment Management only** to UAT first; cart deferred</li> |
| **PD Sandbox (BAU)** | Van | In progress | — | BAU flows on STD, PFP, RR, Way-Star — parallel track | 2026-05-21 | **2026-06-02** | Van relying on UAT once code is promoted. |
| **UAT** | Van | In progress | <li>Islam progressing **business UAT scenarios** on PatternData sandbox</li><li>Michael **Wave 1 package** ready for Hussein review after Austin doc sign-off</li> | <ul><li>**Business scenarios** + declined-card bugs still open</li><li>Salah confirming **revised Wave 1 / go-live dates** with Austin</li><li>Amr wants **automated daily stats** with action items included</li></ul> | 2026-06-15 – 2026-06-25 | **At risk** — Wave 1 missed 6/15; go-live unverified | Wave 2 blocked on PD webhook (see Risks). |
| **Production** | — | Not started | — | UAT sign-off | 2026-06-30 | **Missed** | Awaiting Austin-confirmed revised dates. |

---

## Client release plan (received 2026-06-01)

*Source: client release plan (Austin). Account-flagged items ship when enabled per account.*

*Environment promotion targets by wave.*

*Update 2026-06-15:* Scheduled demo for Van postponed to **Monday 2026-06-22**. Wave 1 UAT dates most likely to be pushed — dates to be confirmed with Austin.

*Update 2026-06-16:* Wave 1 UAT did not start 6/15 — Austin sent no deployment/follow-up. Salah confirming revised Wave 1 dates with Austin today; Austin indicated ShareCare partnership item must land first — full slip duration **TBD**.

*Update 2026-06-22:* Van demo held **2026-06-22** as scheduled.

*Update 2026-06-23:* Wave 1 UAT set to **2026-06-22**; Wave 2–3 and all Prod dates **TBD**.

*Update 2026-06-24:* Michael Payment Management **Wave 1 page** (card path) ready for UAT promotion — **Credit Card Management** only retains a UAT date on the plan; Prefill API and Invoice Upload UAT **TBD**; Wave 2–3 Prod still **TBD**.

*Update 2026-06-28:* Van requested **firm provider** flow — Youssef building proactively; deploy approach TBD. PD PatternData endpoint migration (point 0) may affect integration testing — no client-side change expected but dual-version validation needed.

*Update 2026-06-29:* Austin confirmed **Payment Management** ships to UAT **without shopping cart** — cart promotion deferred to a later wave. Michael preparing phased UAT deploy bundle.

*Update 2026-06-30:* Go-live target **2026-06-30** reached — Salah confirming revised dates with Austin. Michael sending **component-separated deploy packages** to Hussein tonight for Payment Management Wave 1 review.

*Update 2026-07-07:* Michael removing **apt-card component** from Wave 1 deploy per Austin — hidden except on Payment Management page. **Sandbox-first** promotion (UAT sandbox → UAT); package tested standalone before Hussein/Austin review. Austin exploring future **ChartSwap API exposure** model (Insights-style interface with provider/adaptor filters) — not immediate scope.

| Wave | Feature | Scope | Account flag | UAT | Prod | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Wave 1 | Credit Card Management | Shows existing User SavedPayments; cart must include User **and** Account SavedPayments (valid / non-expired only). Assumes Payflow issues resolved. | Yes | 2026-06-22 | TBD | Deploy **without cart** per Austin (2026-06-29). Apt-card component excluded from bundle (2026-07-07). Michael packages for Hussein review. |
| Wave 1 | Prefill Order form API | API to prefill order form | Yes | TBD | TBD | Scenario testing in progress. |
| Wave 1 | Invoice Upload to S3 | On successful Request payment: upload with Type **Invoice**. Prod path: `Chartswap/Invoices`. | Yes | TBD | TBD | Validate VF bucket filtering — invoice filter may hide provider cost on portal. |
| Wave 2 | Status Retrieval API | Method to build response body; also used for Status Sync Job payload. | — | TBD | TBD | Webhook integration has not been communicated to us yet from their side. |
| Wave 2 | Status Sync Job | Scheduled / account-scoped status sync. | Yes | TBD | TBD | Webhook integration has not been communicated to us yet from their side. |
| Wave 3 | Auto-Pay via Credit Card | New payment flow (Transaction Reconciliation Project / TPR). If Request is in any cart and user pays via Auto-Pay, remove Request from **all** carts before Auto-Pay runs. | — | TBD | TBD | — |
| TBD | SSO | Single sign-on integration — requires PD metadata and config. | Yes | TBD | TBD | Release wave unknown; PD metadata, and config still missing — see Risks |
| TBD | Cart hiding | Hide cart UI when enabled. | Yes | TBD | TBD | Deferred from Wave 1 UAT deploy (2026-06-29). |
| TBD | Prevent Record Finder | Block Record Finder when enabled. | Yes | TBD | TBD | — |
| TBD | Suppress email notifications | Disable email notifications when enabled. | Yes | TBD | TBD | Account-flag behavior confirm with client (Salah) |
| TBD | Firm provider flow | Van-requested firm provider onboarding | Yes | TBD | TBD | Youssef testing on dedicated sandbox account; Michael + Sarah building unified deploy doc. |

---

## Open delivery blockers — payment bugs (2 in QA + 1 Major To-Do)

*Process (2026-07-07 standup):* When handing a bug to QA, dev should demo the fix with the tester first to reduce ping-pong. Use **Blocked** (not Re-open) when fix is merged but retest cannot proceed — preserves reopen analytics. **Multi-QA rule:** consult bug opener before assign/reopen; close original bug when scope is fixed and **open new bug** for distinct issues.

*Synced from Jira epic [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) on 2026-07-07 (live).*

**Six open bugs** on the epic (down from thirteen on 2026-06-30). **Three Major/High bugs** below block provider sign-off or payment flows. **Three others** in QA/Progress — excluded per severity/scope: [OC-9575](https://ontellus.atlassian.net/browse/OC-9575) (Draft submit — Progress), [OC-9654](https://ontellus.atlassian.net/browse/OC-9654) (Minor), [OC-9686](https://ontellus.atlassian.net/browse/OC-9686) (declined-card UI — To-Do, reassigned to Michael).

### ShareCare

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9676](https://ontellus.atlassian.net/browse/OC-9676) | Sharecare Subpoena: PD user autopay fails — request stuck Pending Payment, no transaction | **QA** | Mohamed Hamed | **Update 2026-07-07:** Sarah + Hamed **live demo** — test 62 transaction passed. Team reviewing status-transition path (second payment → Pending vs Completed). Sarah taking lead from Hamed; Michael must complete provisioning fix before final close |

### Wave 1 / AutoPay (in QA — delivery-blocking)

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9715](https://ontellus.atlassian.net/browse/OC-9715) | "Submit with AutoPay" button appears on requests in **all statuses** (Buy Now, Pending Payment, etc.) — broken re-submit path | **QA** | Mahmoud Salah | **New 2026-07-06** — S2-High / P2-High (DEF-019). Filed from Youssef UAT handover chat |

### Payment Management (Major To-Do)

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9659](https://ontellus.atlassian.net/browse/OC-9659) | Request submission stays enabled when firm has no valid card (submission gate not enforced) | **To-Do** | Islam Fathy | **Update 2026-07-07:** Reassigned from Michael to **Islam** during standup workload swap |

### Wave 1 Payment Management (in QA — excluded from blockers)

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9654](https://ontellus.atlassian.net/browse/OC-9654) | Replace card reports "No active AutoPay requests are linked" when card has New/Ordered requests | **QA** | Mahmoud Salah | Minor |

### Declined-card / Draft submit (excluded from blockers)

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9575](https://ontellus.atlassian.net/browse/OC-9575) | Submit with AutoPay stays disabled on saved Draft even when authorization form is uploaded | **Progress** | Michael Girgis | Michael actively working (575) — 2026-07-07 |
| [OC-9686](https://ontellus.atlassian.net/browse/OC-9686) | After decline + card replace: UI message on request page shows wrong info | **To-Do** | Michael Girgis | **Update 2026-07-07:** Swapped from Islam to **Michael** |

---

## Current Focus

| Member | Focus |
| --- | --- |
| Michael | **[OC-9575](https://ontellus.atlassian.net/browse/OC-9575)** Draft submit (575); take **[OC-9686](https://ontellus.atlassian.net/browse/OC-9686)** declined-card UI from Islam; ShareCare fixes; **Wave 1 deploy** to UAT sandbox (apt-card excluded); book **branches/sandbox session** |
| Sarah | **[OC-9676](https://ontellus.atlassian.net/browse/OC-9676)** ShareCare demo with Hamed; sandbox **code-context** investigation from yesterday; review Austin deploy doc/comments |
| Islam | Pair with **Sarah** on current fix (demo-before-QA); **[OC-9659](https://ontellus.atlassian.net/browse/OC-9659)** submission gate; **business UAT scenarios** on PatternData sandbox |
| Youssef | Retest **STD 6-substatus blocker** (rollback fix); firm provider flow; Jira access still blocked |
| Hamed | **[OC-9676](https://ontellus.atlassian.net/browse/OC-9676)** after Sarah demo — verify transaction + status transition |
| Salah | Send Youssef **queued test numbers**; re-escalate **Jira/OC access**; fix **daily stats + action items** for Amr; confirm **go-live slip** with Austin |

---

## Risks & challenges

Each item below is stated as a **condition → consequence**, with a mitigation that addresses that specific consequence.


| #   | Risk / challenge                                                                                                                                                                                                                                                                                                               | Mitigation                                                                                                                                                                                                                                                                 | Severity |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| 1   | **Pre-UAT missed 06/14 forecast; Wave 1 UAT missed 6/15; go-live target 2026-06-30 reached without Austin-confirmed revised dates.** [OC-9715](https://ontellus.atlassian.net/browse/OC-9715) new High regression and [OC-9676](https://ontellus.atlassian.net/browse/OC-9676) still in QA — June go-live not achievable without re-baseline.                                                                                          | <ul><li>Salah confirm slip duration with Austin immediately</li><li>Re-baseline Pre-UAT and Prod forecast once Austin responds</li><li>Prioritize OC-9676 ShareCare close and OC-9715 Submit-gating fix</li><li>Michael demo fixes with testers before QA handoff</li></ul> | High     |
| 2   | **End-to-end testing against the PD lower env cannot start.** PD has not responded on lower-environment access, so BAU/E2E validation hasn't begun — only provider-level sandbox testing is underway. The integration risks being validated late, or not before go-live. **Escalation deadline was 2026-06-08** — no response confirmed (Maria engaged 06-08; still awaiting internal PD reply).                                                         | <ul><li>Follow up with Katherine; keep mocking the integration in the meantime</li><li>Escalate to Austin / Van that go-live is at risk if the needed access is not received</li></ul>                                                                                | High     |
| 3   | **SSO cannot be configured or release-planned.** PD has not provided the SSO metadata and configuration required for sandbox/UAT access, leaving the SSO release wave undefined and blocking UAT sign-off. **Cross-firm data boundary** raised 2026-06-29 — user authenticated via one firm's form ID may access another firm's requests.                                                                                                                     | <ul><li>Track as a PD dependency</li><li>Youssef escalate cross-firm boundary to Nabuya / PD IdP team</li><li>Escalated to Austin / PD contacts</li><li>Hold UAT sign-off until SSO config is in place</li></ul>                                                                                                                                                     | High     |
| 4   | **Wave 2 dates may slip (Status Retrieval API & Status Sync Job).** PD has not yet communicated the webhook integration details these features depend on, so the 06/17 UAT / 06/22 prod targets may move. **Escalation deadline was 2026-06-10** — no PD response confirmed in standup.                                                                                                                      | <ul><li>Request webhook details from PD; track alongside the SSO dependency</li><li>Re-baseline Wave 2 dates once received</li><li>Escalate to Austin if still not received after 06/10</li></ul>                                                                                                 | Medium   |
| 5   | **Provider scope uncertainty.** Pharmacy and other provider paths discovered in code; unclear if in scope vs legacy. Expanding scope could delay Pre-UAT on the 7 known providers. **Updox** now deprioritized per Austin (likely not on production). **Firm provider** flow now requested by Van — scope addition mid-stream.                                                                                                                      | <ul><li>Limit focus to STD, PFP, RR, Waystar, CIOX, ShareCare unless Van/Nabuya confirms otherwise</li><li>Youssef test firm flow on dedicated account; Michael + Sarah unify deploy doc</li><li>Michael posted Pharmacy question to PD group; follow up with LeBon on Walmart/Pharmacy payment approach</li></ul>                                                                                                 | Low   |
| 6   | **Code updates can reopen fixed bugs and break previously passing scenarios.** Ongoing fixes and Austin-driven changes may regress areas already signed off in Pre-UAT, forcing duplicate retest cycles. **[OC-9715](https://ontellus.atlassian.net/browse/OC-9715)** Submit-button gating regression filed 2026-07-06 exemplifies UI action-button scope drift.                                                                                                                      | <ul><li>Include detailed testing steps, expected results, and related areas to retest after updates in each story</li><li>Add screenshots of the resolution as evidence in a Jira comment when closing or handing off a fix</li><li>Adopt feature-branch + PR workflow (Michael scheduling session 2026-07-07)</li><li>Multi-QA: close original bug, open new for distinct issues; document transition state in comments</li></ul>                                                                                                 | High     |
| 7   | **Post-Atlassian migration Jira access gaps — partial progress.** Austin sent Jira/Bitbucket access (2026-06-29) — Salah verified login. Islam can view board but **cannot create bugs**; **Youssef still lacks OC project access** (2026-07-07). Michael blocked on Salesforce mobile auth (needs Jay approval).                                                                                                                      | <ul><li>Salah re-escalate Youssef/Islam access with Jamie/Austin</li><li>Michael contact Jay on Teams for Salesforce auth</li><li>Use BO board and Teams for interim coordination</li></ul>                                                                                                 | Medium   |
| 8   | **PD PatternData endpoint migration (point 0) may break dual-version testing.** PD changed PatternData to point 0 with UX updates (2026-06-25 meeting) — team must confirm both old and new endpoints work on same account before deploy.                                                                                                                      | <ul><li>Youssef validate both PD accounts independently and together on sandbox</li><li>Michael send admin config doc to Youssef when available</li><li>Do not deploy bundled PD+Payment until each path verified separately</li></ul>                                                                                                 | Medium   |
| 9   | **QA capacity recovering but uneven.** Sarah returned from vacation (2026-07-07); Hamed audio/setup issues at standup start. Workload rebalanced: Sarah on ShareCare, Islam on submission gate, Michael on declined-card + Draft submit.                                                                                                                      | <ul><li>Islam focus on business scenarios + demo-before-QA with Sarah</li><li>Michael prioritize payment bugs blocking Islam's queue</li><li>Salah backfill Youssef Jira logs until OC access restored</li></ul>                                                                                                 | Medium   |

---

## Standup action items (2026-07-07)

*From [ChartSwap Daily Stand-up — 2026-07-07](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-07-07.docx).*

| Owner | Action | Status |
| --- | --- | --- |
| **Islam** | Pair with **Sarah** to demo/retest current fix before QA handoff | Open |
| **Islam** | Retest **[OC-9659](https://ontellus.atlassian.net/browse/OC-9659)** submission gate (reassigned from Michael) | Open |
| **Michael** | Book **~30 min branches/sandbox session** with Islam, Sarah, Salah today | Open |
| **Michael** | Deploy **Wave 1 Payment Management** to UAT sandbox first — **apt-card component excluded** per Austin | Open |
| **Michael** | Finish **[OC-9575](https://ontellus.atlassian.net/browse/OC-9575)** Submit-with-AutoPay on Draft (575) | Open |
| **Michael** | Take **[OC-9686](https://ontellus.atlassian.net/browse/OC-9686)** declined-card UI from Islam | Open |
| **Michael** | Work on **ShareCare** fixes today | Open |
| **Salah** | Re-escalate **Youssef Jira/OC access** with Jamie/Austin | Open |
| **Salah** | Fix **daily stats delivery** — Amr wants automatic post with **action items** included | Open |
| **Sarah** | Investigate **sandbox code issue** from yesterday (context study before retest) | Open |
| **Youssef** | Retest **STD 6-substatus blocker** — rollback applied on Michael's Thu code | Open |
| **Team** | **Demo fix with reporter** before QA handoff — reduce ping-pong | Open |
