# Pattern Data — delivery progress

**Go-live goal:** End of June 2026 · **Epic:** [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) · **As of:** 2026-06-09

---

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Pre-UAT** | Youssef | In progress | <li>4/7 providers tested [STD, PFP, RR, and Waystar]</li><li>RR payment bugs cleared and retested (OC-9529, OC-9531 closed; full flow retest 2026-06-08)</li><li>CIOX payment bugs closed (OC-9532, OC-9552 closed 2026-06-08)</li><li>External providers testing in progress (Hamed with fulfillment simulation by Michael)</li> | <ul><li>Fix [OC-9562](https://ontellus.atlassian.net/browse/OC-9562) — ShareCare authorization blocked by SOQL limit (Michael; in fix)</li><li>Resume ShareCare, CIOX, and continue Updox testing on PD sandbox after applying fullfilment simulation by Michael</li></ul> | 2026-05-21 | **2026-06-14** | <li>Sandbox goal: **pre-fulfillment parity with UAT** — not chasing fulfillment simulation on sandbox. CIOX fulfillment gap accepted per 06-05 agreement; escalate only if new non-fulfillment issues surface.</li><li>External-provider fulfillment simulation deferred to UAT (Eric).</li><li>Automation paused — manual retest for now.</li><li>External providers to be tested with Michale's simulation (internal agreement)</li> |
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

## Open delivery blockers — payment bugs (0 blocked + 0 in QA)

*Process (2026-06-07 standup):* When handing a bug to QA, dev should demo the fix with the tester first to reduce ping-pong.

*Synced from Jira epic [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) on 2026-06-09 (live; re-checked for new bugs).*

One **Major** bug in fix — blocks ShareCare Pre-UAT testing (see below). [OC-9564](https://ontellus.atlassian.net/browse/OC-9564) (minor — Payment Management banner logic; workaround available) filed today; excluded per severity filter. [OC-9389](https://ontellus.atlassian.net/browse/OC-9389) (minor — DEC-050 reinitiation verifiability) remains in Progress; excluded.

### ShareCare

| Bug | What's wrong | Jira status | Assignee | Notes |
| --- | --- | --- | --- | --- |
| [OC-9562](https://ontellus.atlassian.net/browse/OC-9562) | Authorization submit fails with Too many SOQL queries (101) on `enterrequestdatasc` — blocks ShareCare workflow completion | **Progress** | Michael Girgis | **New 2026-06-09** — found during ShareCare sandbox testing; Major — no workaround |

---

## Current Focus

| Member | Focus |
| --- | --- |
| Michael | OC-9562 ShareCare SOQL fix + Austin's comments |
| Sarah | External-provider testing + code coverage |
| Islam | Code coverage |
| Hamed | External-provider testing |
| Youssef | Pre-UAT coordination / provider sign-off |
| Heba | Transaction updates testing |

---

## Risks & challenges

Each item below is stated as a **condition → consequence**, with a mitigation that addresses that specific consequence.


| #   | Risk / challenge                                                                                                                                                                                                                                                                                                               | Mitigation                                                                                                                                                                                                                                                                 | Severity |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| 1   | **Late design changes from Austin could force rework.** Further scope or design updates from the client may require re-coding and full-team retest across Pre-UAT and the release waves, threatening the 06/14 date and June go-live. **Michael** also carries Austin transaction comments, EPO branching alignment, and Autopay Tool UI (~55 story comments) — capacity may compete with absorbing Austin updates and fixing OC-9562.                                                                                          | <ul><li><strong>Michael</strong> dedicated to absorbing Austin's design updates</li><li>Track all changes against the [client release plan](#client-release-plan-received-2026-06-01)</li><li>Re-estimate affected waves before committing UAT dates</li><li>Escalate if 06/14 or go-live is threatened</li></ul> | High     |
| 2   | **End-to-end testing against the PD lower env cannot start.** PD has not responded on lower-environment access, so BAU/E2E validation hasn't begun — only provider-level sandbox testing is underway. The integration risks being validated late, or not before go-live. **Escalation deadline was 2026-06-08** — no response confirmed.                                                         | <ul><li>Follow up with Katherine; keep mocking the integration in the meantime</li><li>Escalate to Austin / Van that go-live is at risk if the needed access is not received</li></ul>                                                                                | High     |
| 3   | **SSO cannot be configured or release-planned.** PD has not provided the SSO metadata and configuration required for sandbox/UAT access, leaving the SSO release wave undefined and blocking UAT sign-off.                                                                                                                     | <ul><li>Track as a PD dependency</li><li> escalated to Austin / PD contacts</li><li>Hold UAT sign-off until SSO config is in place</li></ul>                                                                                                                                                     | High     |
| 4   | **Wave 2 dates may slip (Status Retrieval API & Status Sync Job).** PD has not yet communicated the webhook integration details these features depend on, so the 06/17 UAT / 06/22 prod targets may move. **Escalation deadline is tomorrow (2026-06-10).**                                                                                                                      | <ul><li>Request webhook details from PD; track alongside the SSO dependency</li><li>Re-baseline Wave 2 dates once received</li><li> escalate if not received by 06/10 to hold the wave</li></ul>                                                                                                 | Medium   |
| 5   | **Provider scope uncertainty.** Pharmacy and other provider paths discovered in code; unclear if in scope vs legacy. Expanding scope could delay Pre-UAT on the 7 known providers.                                                                                                                      | <ul><li>Limit focus to STD, PFP, RR, Waystar, CIOX, ShareCare, Updox unless Van/Nabuya confirms otherwise</li><li>Michael posted Pharmacy question to PD group</li><li>Hamed reviewing provider list Michael sends</li></ul>                                                                                                 | Low   |
