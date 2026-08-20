# Pattern Data — delivery progress

**Go-live goal:** End of June 2026 · **Epic:** [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) · **As of:** 2026-07-08

---

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Pre-UAT** | Youssef | In progress | <li>**3 Major bugs closed** (2026-07-08 Jira sync): [OC-9715](https://ontellus.atlassian.net/browse/OC-9715) Submit-button gating, [OC-9575](https://ontellus.atlassian.net/browse/OC-9575) Draft submit, [OC-9654](https://ontellus.atlassian.net/browse/OC-9654) replace-card message — Youssef retest passed</li><li>[OC-9659](https://ontellus.atlassian.net/browse/OC-9659) **core logic validated** by Youssef (Islam fix pushed 2026-07-07)</li><li>Closure **analysis tags** applied to 2 bugs closed today</li> | <ul><li>**1 Major in Progress:** [OC-9659](https://ontellus.atlassian.net/browse/OC-9659) submission-gate **UI polish** → **Islam**</li><li>**1 Major in QA:** [OC-9676](https://ontellus.atlassian.net/browse/OC-9676) ShareCare — logic validated; **Hamed** to close</li><li>Michael: **[OC-9686](https://ontellus.atlassian.net/browse/OC-9686)** declined-card UI (Progress)</li><li>[OC-9562](https://ontellus.atlassian.net/browse/OC-9562) ShareCare SOQL → **Save for Later** (external provider config, not Pattern Data code)</li><li>Salah: **dev-process refresh** team call; **Jira access** follow-up for Youssef</li></ul> | 2026-05-21 | **2026-06-17** *(at risk — dates TBD pending Austin)* | <li>ShareCare **test 76** ([OC-9676](https://ontellus.atlassian.net/browse/OC-9676)) ready to close; **test 62** ([OC-9562](https://ontellus.atlassian.net/browse/OC-9562)) deferred — ShareCare courses/SOQL limit is external</li><li>Michael: post **Slack status** when actively working a ticket</li><li>Sarah started **firm provider + sharing rules** Apex per Austin</li> |
| **PD Sandbox (BAU)** | Van | In progress | — | BAU flows on STD, PFP, RR, Way-Star — parallel track | 2026-05-21 | **2026-06-02** | Van relying on UAT once code is promoted. |
| **UAT** | Van | In progress | <li>Islam progressing **business UAT scenarios** on PatternData sandbox</li><li>Michael **Wave 1 package** ready for Hussein review after Austin doc sign-off</li> | <ul><li>**Business scenarios** + declined-card bugs still open</li><li>Salah confirming **revised Wave 1 / go-live dates** with Austin</li><li>External-provider ShareCare items parked to **SF3** until UAT handover covers external profiles</li></ul> | 2026-06-15 – 2026-06-25 | **At risk** — Wave 1 missed 6/15; go-live unverified | Wave 2 blocked on PD webhook (see Risks). |
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

*Update 2026-07-08:* Sarah started **firm provider request + sharing rules** task under the epic (Austin notes + Michael's code context). ShareCare external-provider bugs ([OC-9562](https://ontellus.atlassian.net/browse/OC-9562)) parked to **Save for Later** — not Pattern Data scope on sandbox.

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
| TBD | Firm provider flow | Van-requested firm provider onboarding | Yes | TBD | TBD | Sarah building sharing-rules Apex; Youssef testing on dedicated sandbox account. |

---

## Open delivery blockers — payment bugs (1 in QA + 1 Major in Progress)

*Process (2026-07-08 standup):* Post **Slack status** when actively working a ticket. Michael confirms no pending code before closing bugs Youssef retested. ShareCare SOQL ([OC-9562](https://ontellus.atlassian.net/browse/OC-9562)) is external-provider config — park to **Save for Later**, not a Pattern Data sandbox blocker.

*Synced from Jira epic [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) on 2026-07-08 (live).*

**Four open bugs** on the epic (down from six on 2026-07-07). **Two Major bugs** below block provider sign-off or payment flows. **Two others** in Progress/QA — excluded per severity/scope: [OC-9562](https://ontellus.atlassian.net/browse/OC-9562) (ShareCare SOQL — external, SF3), [OC-9686](https://ontellus.atlassian.net/browse/OC-9686) (declined-card UI — Progress, minor).

### ShareCare

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9676](https://ontellus.atlassian.net/browse/OC-9676) | Sharecare Subpoena: PD user autopay fails — request stuck Pending Payment, no transaction | **QA** | Mohamed Hamed | **Update 2026-07-08:** Sarah + team agree logic validated (test 76). **Hamed** to close. Pattern Data flow working; status-transition path reviewed |

### Payment Management (Major in Progress)

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9659](https://ontellus.atlassian.net/browse/OC-9659) | Request submission stays enabled when firm has no valid card (submission gate not enforced) | **Progress** | Islam Fathy | **Update 2026-07-08:** Youssef retest — **core logic works**. Remaining: enable Submit button (not disabled) + popup when no valid card; fix initial no-card state. Islam completing UI per Youssef comments + design screenshot |

### ShareCare — external provider (excluded — Save for Later)

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9562](https://ontellus.atlassian.net/browse/OC-9562) | Sharecare workflow — authorization submit fails with Too many SOQL queries (101) | **QA** | Mohamed Hamed | **Update 2026-07-08:** ShareCare **courses limit** (4) causes SOQL governor errors — **not Pattern Data code**. Moved to **Save for Later (SF3)**; retest on UAT when external providers are in scope. Test 62 stays open |

### Declined-card UI (excluded from blockers)

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9686](https://ontellus.atlassian.net/browse/OC-9686) | After decline + card replace: UI message on request page shows wrong info | **Progress** | Michael Girgis | **Update 2026-07-08:** Michael in Progress — styling fixes not started yet. Post Slack when working |

---

## Current Focus

| Member | Focus |
| --- | --- |
| Michael | **[OC-9686](https://ontellus.atlassian.net/browse/OC-9686)** declined-card UI styling; final verify **[OC-9575](https://ontellus.atlassian.net/browse/OC-9575)** closed; **Wave 1 deploy** to UAT sandbox; post **Slack** on active tickets |
| Sarah | **Firm provider request + sharing rules** Apex (Austin task); close **[OC-9676](https://ontellus.atlassian.net/browse/OC-9676)** path with Hamed; log time with estimates |
| Islam | **[OC-9659](https://ontellus.atlassian.net/browse/OC-9659)** UI polish (enabled button + no-card popup); **business UAT scenarios** on PatternData sandbox |
| Youssef | Board cleanup retests complete; follow up **Jamie on Jira/OC access**; retest ShareCare **SF3** items when promoted |
| Hamed | Close **[OC-9676](https://ontellus.atlassian.net/browse/OC-9676)** after team sign-off |
| Salah | **SF3** ShareCare external bugs; schedule **dev-process refresh** call; **Jira tags** on closed bugs; confirm **go-live slip** with Austin; remind team to **log yesterday's time** |

---

## Risks & challenges

Each item below is stated as a **condition → consequence**, with a mitigation that addresses that specific consequence.


| #   | Risk / challenge                                                                                                                                                                                                                                                                                                               | Mitigation                                                                                                                                                                                                                                                                 | Severity |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| 1   | **Pre-UAT missed 06/14 forecast; Wave 1 UAT missed 6/15; go-live target 2026-06-30 reached without Austin-confirmed revised dates.** [OC-9715](https://ontellus.atlassian.net/browse/OC-9715) and [OC-9575](https://ontellus.atlassian.net/browse/OC-9575) **closed 2026-07-08**; [OC-9676](https://ontellus.atlassian.net/browse/OC-9676) + [OC-9659](https://ontellus.atlassian.net/browse/OC-9659) UI remain — June go-live not achievable without re-baseline.                                                                                          | <ul><li>Salah confirm slip duration with Austin immediately</li><li>Re-baseline Pre-UAT and Prod forecast once Austin responds</li><li>Close OC-9676 and finish OC-9659 UI this week</li><li>Michael post Slack when working tickets — reduce invisible WIP</li></ul> | High     |
| 2   | **End-to-end testing against the PD lower env cannot start.** PD has not responded on lower-environment access, so BAU/E2E validation hasn't begun — only provider-level sandbox testing is underway. The integration risks being validated late, or not before go-live. **Escalation deadline was 2026-06-08** — no response confirmed (Maria engaged 06-08; still awaiting internal PD reply).                                                         | <ul><li>Follow up with Katherine; keep mocking the integration in the meantime</li><li>Escalate to Austin / Van that go-live is at risk if the needed access is not received</li></ul>                                                                                | High     |
| 3   | **SSO cannot be configured or release-planned.** PD has not provided the SSO metadata and configuration required for sandbox/UAT access, leaving the SSO release wave undefined and blocking UAT sign-off. **Cross-firm data boundary** raised 2026-06-29 — user authenticated via one firm's form ID may access another firm's requests.                                                                                                                     | <ul><li>Track as a PD dependency</li><li>Youssef escalate cross-firm boundary to Nabuya / PD IdP team</li><li>Escalated to Austin / PD contacts</li><li>Hold UAT sign-off until SSO config is in place</li></ul>                                                                                                                                                     | High     |
| 4   | **Wave 2 dates may slip (Status Retrieval API & Status Sync Job).** PD has not yet communicated the webhook integration details these features depend on, so the 06/17 UAT / 06/22 prod targets may move. **Escalation deadline was 2026-06-10** — no PD response confirmed in standup.                                                                                                                      | <ul><li>Request webhook details from PD; track alongside the SSO dependency</li><li>Re-baseline Wave 2 dates once received</li><li>Escalate to Austin if still not received after 06/10</li></ul>                                                                                                 | Medium   |
| 5   | **Provider scope uncertainty.** Pharmacy and other provider paths discovered in code; unclear if in scope vs legacy. Expanding scope could delay Pre-UAT on the 7 known providers. **Updox** now deprioritized per Austin (likely not on production). **Firm provider** flow now requested by Van — Sarah started sharing-rules Apex (2026-07-08). **ShareCare external SOQL** ([OC-9562](https://ontellus.atlassian.net/browse/OC-9562)) parked to SF3 — not sandbox-blocking.                                                                                                                      | <ul><li>Limit focus to STD, PFP, RR, Waystar, CIOX, ShareCare unless Van/Nabuya confirms otherwise</li><li>Sarah continue firm provider Apex; Youssef test on dedicated account</li><li>Defer external-provider ShareCare bugs to UAT external-profile handover</li></ul>                                                                                                 | Low   |
| 6   | **Code updates can reopen fixed bugs and break previously passing scenarios.** Ongoing fixes and Austin-driven changes may regress areas already signed off in Pre-UAT, forcing duplicate retest cycles. Team now **re-verifies with Michael before closing** bugs Youssef spot-retested (2026-07-08).                                                                                                                      | <ul><li>Michael confirm no pending code before close; tell Youssef if sandbox redeploy needed</li><li>Include detailed testing steps and related retest areas in each story</li><li>Schedule dev-process refresh (branches/sandbox/PR workflow) after standup</li></ul>                                                                                                 | Medium     |
| 7   | **Post-Atlassian migration Jira access gaps — partial progress.** Salah re-sent **Jamie** email 2026-07-07 for Youssef OC access — Youssef to follow up. Islam can view board but **cannot create bugs**; **Youssef still lacks OC project access**. Michael blocked on Salesforce mobile auth (needs Jay approval).                                                                                                                      | <ul><li>Youssef follow up Jamie/Austin on OC access</li><li>Michael contact Jay on Teams for Salesforce auth</li><li>Use BO board and Teams for interim coordination</li></ul>                                                                                                 | Medium   |
| 8   | **PD PatternData endpoint migration (point 0) may break dual-version testing.** PD changed PatternData to point 0 with UX updates (2026-06-25 meeting) — team must confirm both old and new endpoints work on same account before deploy.                                                                                                                      | <ul><li>Youssef validate both PD accounts independently and together on sandbox</li><li>Michael send admin config doc to Youssef when available</li><li>Do not deploy bundled PD+Payment until each path verified separately</li></ul>                                                                                                 | Medium   |
| 9   | **UAT provider data may be incomplete for external profiles.** Michael fixed ShareCare provider based on **code**, not full UAT data — UAT provider config may be missing fields. Low priority to compare UAT vs sandbox when time allows.                                                                                                                      | <ul><li>Defer UAT provider gap analysis until external-profile UAT handover</li><li>Do not modify UAT data — only pull missing config to sandbox if found</li><li>Pattern Data core flow validated separately from ShareCare external SOQL</li></ul>                                                                                                 | Low   |

---

## Standup action items (2026-07-08)

*From [ChartSwap Daily Stand-up — 2026-07-08](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-07-08.docx).*

| Owner | Action |
| --- | --- |
| **Islam** | Complete **[OC-9659](https://ontellus.atlassian.net/browse/OC-9659)** UI polish — enable Submit button + popup when no valid card; fix initial no-card state |
| **Michael** | Work **[OC-9686](https://ontellus.atlassian.net/browse/OC-9686)** declined-card UI styling; post **Slack** when actively on a ticket |
| **Salah** | Move ShareCare **[OC-9562](https://ontellus.atlassian.net/browse/OC-9562)** + related external-provider bugs to **Save for Later (SF3)** |
| **Salah** | Schedule **dev-process refresh** team call (branches/sandbox/PR workflow from 2026-07-07) |
| **Salah** | Apply **analysis/scale Jira tags** on newly closed bugs |
| **Salah** | Remind team to **log yesterday's time** |
| **Sarah** | Continue **firm provider request + sharing rules** Apex (Austin task); **log time** with estimates |
| **Team** | Post **Slack status** when working a ticket |
| **Youssef** | Follow up **Jamie** on **Jira/OC access** (Salah re-sent email 2026-07-07) |
