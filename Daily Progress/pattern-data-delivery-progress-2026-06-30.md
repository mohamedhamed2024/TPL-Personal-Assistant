# Pattern Data — delivery progress

**Go-live goal:** End of June 2026 · **Epic:** [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) · **As of:** 2026-06-30

---

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Pre-UAT** | Youssef | In progress | <li>4/7 providers tested [STD, PFP, RR, Waystar]</li><li>[OC-9687](https://ontellus.atlassian.net/browse/OC-9687) PFP AutoPay race **closed** (2026-06-30)</li><li>Islam **closed UI UAT scenario queue** — on business scenarios</li><li>Michael: **Payment Management deploy packages** ready for Hussein review</li> | <ul><li>**2 Major blockers in QA:** [OC-9630](https://ontellus.atlassian.net/browse/OC-9630) CNR, [OC-9676](https://ontellus.atlassian.net/browse/OC-9676) ShareCare (sent back to Hamed)</li><li>Michael: **Payment Management-only UAT deploy** + declined-card fixes blocking Islam</li><li>Salah: confirm **revised dates** with Austin — go-live day reached</li></ul> | 2026-05-21 | **2026-06-17** *(at risk — dates TBD pending Austin)* | <li>**Reduced QA capacity** — Sarah on vacation from 2026-06-30; Hamed/Youssef/Hussein absent</li><li>Austin: **Payment Management only** to UAT first; cart deferred</li><li>Austin: **one card at a time** replace — bundled approach rejected</li> |
| **PD Sandbox (BAU)** | Van | In progress | — | BAU flows on STD, PFP, RR, Way-Star — parallel track | 2026-05-21 | **2026-06-02** | Van relying on UAT once code is promoted. |
| **UAT** | Van | In progress | <li>Islam **closed UI scenario queue** (2026-06-30)</li><li>Michael sending **deploy packages** to Hussein tonight — Wave 1 promotion path</li> | <ul><li>**Business scenarios** + declined-card bugs still open</li><li>**Sarah on vacation** — PFP analysis paused</li><li>Salah confirming **revised Wave 1 / go-live dates** with Austin</li></ul> | 2026-06-15 – 2026-06-25 | **At risk** — Wave 1 missed 6/15; go-live unverified | Reduced capacity; Wave 2 blocked on PD webhook (see Risks). |
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

| Wave | Feature | Scope | Account flag | UAT | Prod | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Wave 1 | Credit Card Management | Shows existing User SavedPayments; cart must include User **and** Account SavedPayments (valid / non-expired only). Assumes Payflow issues resolved. | Yes | 2026-06-22 | TBD | OC-9649/OC-9653 fixes in QA (2026-06-24); Islam unblocked on Add Account Card. Deploy **without cart** per Austin (2026-06-29). Michael packages for Hussein review (2026-06-30). |
| Wave 1 | Prefill Order form API | API to prefill order form | Yes | TBD | TBD | Scenario testing in progress (2026-06-30). |
| Wave 1 | Invoice Upload to S3 | On successful Request payment: upload with Type **Invoice**. Prod path: `Chartswap/Invoices`. | Yes | TBD | TBD | Validate VF bucket filtering — invoice filter may hide provider cost on portal. |
| Wave 2 | Status Retrieval API | Method to build response body; also used for Status Sync Job payload. | — | TBD | TBD | Webhook integration has not been communicated to us yet from their side. |
| Wave 2 | Status Sync Job | Scheduled / account-scoped status sync. | Yes | TBD | TBD | Webhook integration has not been communicated to us yet from their side. |
| Wave 3 | Auto-Pay via Credit Card | New payment flow (Transaction Reconciliation Project / TPR). If Request is in any cart and user pays via Auto-Pay, remove Request from **all** carts before Auto-Pay runs. | — | TBD | TBD | — |
| TBD | SSO | Single sign-on integration — requires PD metadata and config. | Yes | TBD | TBD | Release wave unknown; PD metadata, and config still missing — see Risks |
| TBD | Cart hiding | Hide cart UI when enabled. | Yes | TBD | TBD | Deferred from Wave 1 UAT deploy (2026-06-29). |
| TBD | Prevent Record Finder | Block Record Finder when enabled. | Yes | TBD | TBD | — |
| TBD | Suppress email notifications | Disable email notifications when enabled. | Yes | TBD | TBD | Account-flag behavior confirm with client (Salah) |
| TBD | Firm provider flow | Van-requested firm provider onboarding | Yes | TBD | TBD | Youssef testing on dedicated sandbox account (2026-06-29); Michael + Sarah building unified deploy doc. |

---

## Open delivery blockers — payment bugs (2 in QA)

*Process (2026-06-30 standup):* When handing a bug to QA, dev should demo the fix with the tester first to reduce ping-pong. Use **Blocked** (not Re-open) when fix is merged but retest cannot proceed — preserves reopen analytics. **Multi-QA rule:** consult bug opener before assign/reopen; close original bug when scope is fixed and **open new bug** for distinct issues.

*Synced from Jira epic [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) on 2026-06-30 (live refresh).*

**Thirteen open bugs** on the epic. **Two Major bugs** below block provider sign-off or ShareCare/RR flows. **Eleven others** in QA — excluded per severity/scope: OC-9575, OC-9654 (Minor); OC-9656, OC-9674 (Medium/workaround — OC-9674 **closed** 2026-06-30); OC-9649, OC-9652, OC-9653, OC-9659 (Wave 1 payment — in QA); OC-9683, OC-9684, OC-9686, OC-9688 (Backlog/UI — in QA, unassigned to Islam).

### ShareCare

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9676](https://ontellus.atlassian.net/browse/OC-9676) | Sharecare Subpoena: PD user autopay fails — request stuck Pending Payment, no transaction | **QA** | Mohamed Hamed | **New 2026-06-28** — Major. **Update 2026-06-29:** Michael + Sarah fixed; Sarah closed in standup — Jira still **QA**. **Update 2026-06-30:** Sarah sent back to **Hamed** for **status-transition** fix; team agreed to close autopilot-scope bug and open new bug for distinct transition issues |

### Record Retrieval

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9630](https://ontellus.atlassian.net/browse/OC-9630) | CNR document not visible to requester after No-Records **Rejected** — requester cannot download no-records evidence | **QA** | Michael Girgis | **New 2026-06-21** — Major — no workaround. **Update 2026-06-24:** Youssef retested — CNR visible and request creation OK; **empty file also uploads** — not closing until Michael reviews *(still QA 2026-06-30)* |

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

### Declined-card / UI (in QA — excluded from blockers)

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9683](https://ontellus.atlassian.net/browse/OC-9683) | Standard provider: Request More Info button missing on provider page | **QA** | Islam Fathy | **New 2026-06-29** — needs Youssef to confirm expected behavior on standard provider UAT (2026-06-30 standup) |
| [OC-9684](https://ontellus.atlassian.net/browse/OC-9684) | PFP Provider: Sync Message not updated after Request More Info | **QA** | Islam Fathy | Michael fixed sync-message/range — Islam retesting (2026-06-30) |
| [OC-9686](https://ontellus.atlassian.net/browse/OC-9686) | After decline + card replace: UI message on request page shows wrong info | **QA** | Islam Fathy | **New 2026-06-29** |
| [OC-9688](https://ontellus.atlassian.net/browse/OC-9688) | After card replacement: re-initiation of declined transaction shows **$0.00** total | **QA** | Islam Fathy | **New 2026-06-29** — Michael investigating with Islam (2026-06-30) |

---

## Current Focus

| Member | Focus |
| --- | --- |
| Michael | Finish **free-place / replace card** (one at a time); configurable queue threshold; **declined-card** bugs with Islam; **bug 87** invoice-date race; send **deploy packages** to Hussein tonight; OC-9630 empty auth file review |
| Sarah | On **vacation from 2026-06-30** — bug 87 PFP race documented on scenario sheet before leave; sent Hamed ShareCare bug back for status fix |
| Islam | **Business UAT scenarios**; retest sync-message fix; **declined-card** + **bug 83** with Michael; report Jira create-bug access issue |
| Youssef | Firm provider flow on dedicated account; cross-firm SSO escalation; confirm **Request Info button** expected behavior for Islam bug 83 |
| Hamed | ShareCare **status/telephony** fix (fresh laptop); close autopilot-scope bug per team agreement; open new bug for transition issues |
| Salah | Apply root-cause labels via Cursor; confirm **go-live slip** with Austin; enforce multi-QA bug hygiene; verify time logs |

---

## Risks & challenges

Each item below is stated as a **condition → consequence**, with a mitigation that addresses that specific consequence.


| #   | Risk / challenge                                                                                                                                                                                                                                                                                                               | Mitigation                                                                                                                                                                                                                                                                 | Severity |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| 1   | **Pre-UAT missed 06/14 forecast; Wave 1 UAT missed 6/15; go-live target 2026-06-30 reached without Austin-confirmed revised dates.** Open CNR/ShareCare QA bugs remain and Sarah on vacation — June go-live not achievable without re-baseline.                                                                                          | <ul><li>Salah confirm slip duration with Austin immediately</li><li>Re-baseline Pre-UAT and Prod forecast once Austin responds</li><li>Prioritize OC-9630 empty-file review and Hamed ShareCare status fix</li><li>Michael demo fixes with testers before QA handoff</li></ul> | High     |
| 2   | **End-to-end testing against the PD lower env cannot start.** PD has not responded on lower-environment access, so BAU/E2E validation hasn't begun — only provider-level sandbox testing is underway. The integration risks being validated late, or not before go-live. **Escalation deadline was 2026-06-08** — no response confirmed (Maria engaged 06-08; still awaiting internal PD reply).                                                         | <ul><li>Follow up with Katherine; keep mocking the integration in the meantime</li><li>Escalate to Austin / Van that go-live is at risk if the needed access is not received</li></ul>                                                                                | High     |
| 3   | **SSO cannot be configured or release-planned.** PD has not provided the SSO metadata and configuration required for sandbox/UAT access, leaving the SSO release wave undefined and blocking UAT sign-off. **Cross-firm data boundary** raised 2026-06-29 — user authenticated via one firm's form ID may access another firm's requests.                                                                                                                     | <ul><li>Track as a PD dependency</li><li>Youssef escalate cross-firm boundary to Nabuya / PD IdP team</li><li>Escalated to Austin / PD contacts</li><li>Hold UAT sign-off until SSO config is in place</li></ul>                                                                                                                                                     | High     |
| 4   | **Wave 2 dates may slip (Status Retrieval API & Status Sync Job).** PD has not yet communicated the webhook integration details these features depend on, so the 06/17 UAT / 06/22 prod targets may move. **Escalation deadline was 2026-06-10** — no PD response confirmed in standup.                                                                                                                      | <ul><li>Request webhook details from PD; track alongside the SSO dependency</li><li>Re-baseline Wave 2 dates once received</li><li>Escalate to Austin if still not received after 06/10</li></ul>                                                                                                 | Medium   |
| 5   | **Provider scope uncertainty.** Pharmacy and other provider paths discovered in code; unclear if in scope vs legacy. Expanding scope could delay Pre-UAT on the 7 known providers. **Updox** now deprioritized per Austin (likely not on production). **Firm provider** flow now requested by Van — scope addition mid-stream.                                                                                                                      | <ul><li>Limit focus to STD, PFP, RR, Waystar, CIOX, ShareCare unless Van/Nabuya confirms otherwise</li><li>Youssef test firm flow on dedicated account; Michael + Sarah unify deploy doc</li><li>Michael posted Pharmacy question to PD group; follow up with LeBon on Walmart/Pharmacy payment approach</li></ul>                                                                                                 | Low   |
| 6   | **Code updates can reopen fixed bugs and break previously passing scenarios.** Ongoing fixes and Austin-driven changes may regress areas already signed off in Pre-UAT, forcing duplicate retest cycles. PFP invoice-date/autopay race (bug 87 / OC-9687) exemplifies timing-sensitive regressions — **closed in Jira 2026-06-30** but Michael still investigating root cause.                                                                                                                      | <ul><li>Include detailed testing steps, expected results, and related areas to retest after updates in each story</li><li>Add screenshots of the resolution as evidence in a Jira comment when closing or handing off a fix</li><li>Adopt feature-branch + PR workflow (team session scheduled after Michael apply-date work)</li><li>Multi-QA: close original bug, open new for distinct issues; document transition state in comments</li></ul>                                                                                                 | High     |
| 7   | **Post-Atlassian migration Jira access gaps — partial progress.** Austin sent Jira/Bitbucket access (2026-06-29) — Salah verified login. Islam can view board but **cannot create bugs**; Youssef still lacks project space. Michael blocked on Salesforce mobile auth (needs Jay approval).                                                                                                                      | <ul><li>Salah escalate Islam/Youssef create-bug failures with Austin/IT</li><li>Michael contact Jay on Teams for Salesforce auth</li><li>Use BO board and Teams for interim coordination</li></ul>                                                                                                 | Medium   |
| 8   | **PD PatternData endpoint migration (point 0) may break dual-version testing.** PD changed PatternData to point 0 with UX updates (2026-06-25 meeting) — team must confirm both old and new endpoints work on same account before deploy.                                                                                                                      | <ul><li>Youssef validate both PD accounts independently and together on sandbox</li><li>Michael send admin config doc to Youssef when available</li><li>Do not deploy bundled PD+Payment until each path verified separately</li></ul>                                                                                                 | Medium   |
| 9   | **Reduced QA capacity mid-sprint.** Sarah on vacation from 2026-06-30; Hamed setting up fresh laptop; Youssef and Hussein absent from standup — only Islam + Michael actively testing.                                                                                                                      | <ul><li>Islam focus on business scenarios + declined-card retest with Michael</li><li>Michael prioritize payment bugs blocking Islam's queue</li><li>Salah backfill Youssef Jira logs until OC access restored</li><li>Defer non-blocking scenario work until Sarah returns</li></ul>                                                                                                 | Medium   |

---

## Standup action items (2026-06-30)

*From [ChartSwap Daily Stand-up — 2026-06-30](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-06-30.docx).*

| Owner | Action | Status |
| --- | --- | --- |
| **Hamed** | Fix ShareCare **telephony/status** bug — Sarah sent back for status-transition fix | Open |
| **Hamed** | **Close autopilot-scope bug** and open **new bug** for distinct status-transition issues | Open |
| **Islam** | Continue **business UAT scenarios** — mark scenario sheet with **bug ref** not "done" | Open |
| **Islam** | Retest Michael's **sync-message / range** fix and sign off | Open |
| **Islam** | Work with Michael on **declined-card** bugs — Accept button missing; **$0 amount** after replace | Open |
| **Islam** | Get **Youssef** to confirm **Request Info button** expected on standard provider UAT (**bug 83**) | Open |
| **Islam** | Report **Jira create-bug** failure (view OK, create fails) | Open |
| **Michael** | Finish **free-place / replace card** — **one card at a time** per Austin | Open |
| **Michael** | Make **place-request queue threshold** configurable (open queue after N requests) | Open |
| **Michael** | Investigate **bug 87** / **invoice-date** autopay–status **race condition** (Sarah PFP scenario) | Open |
| **Michael** | Send **component-separated deploy packages** to **Hussein** tonight | Open |
| **Michael** | Investigate **declined-card** bugs with Islam (Accept button, $0 amount, over-threshold) | Open |
| **Michael** | Review **[OC-9630](https://ontellus.atlassian.net/browse/OC-9630) CNR** empty auth file upload | Open |
| **Salah** | Apply **root-cause labels** on open bugs via Cursor (PIN on Teams) | Open |
| **Salah** | Confirm **go-live slip** with Austin — June 30 reached without revised dates | Open |
| **Salah** | Enforce **multi-QA bug hygiene** — consult opener before assign/reopen | Open |
| **Team** | Log **yesterday's time** to Excel + Jira before standup | Open |
| **Team** | **Multi-QA:** consult bug opener before assign/reopen; document transition state in comments | Open |
| **Youssef** | Confirm **Request Info button** expected on **standard provider UAT** for Islam **bug 83** | Open |
| **Islam** | **Closed all UI UAT scenarios** — continuing business flows | Done |
| **Michael** | Fixed **sync-message / between-request range** issue — Islam retesting | Done |
| **Michael** | Created **component-separated deploy packages** structure for Hussein | Done |
| **Michael** | Sent Islam **declined-card** scenario (differs from Youssef's original write-up) | Done |
| **Sarah** | Documented **bug 87** PFP race — requests 310/311 pass; 309 hits autopay/status race | Done |
| **Team** | Agreed **bug scope policy** — close original when fixed; open new bug for distinct issues | Done |
| **Team** | Agreed **one card at a time** replace — old bundled place-card approach rejected | Done |
