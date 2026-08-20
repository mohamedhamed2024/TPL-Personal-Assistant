# Pattern Data — delivery progress

**Go-live goal:** End of June 2026 · **Epic:** [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) · **As of:** 2026-06-03

---

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Pre-UAT** | Youssef | In progress | <li>4/7 providers tested [STD, PFP, RR, and Waystar]</li><li>3 Major open bugs (2 in QA retest)</li> | <ul><li>Config setup for CIOX, ShareCare, Updox</li><li>Test CIOX, ShareCare, Updox</li><li>Retest OC-9529 & OC-9531; fix & retest OC-9532</li></ul> | 2026-05-21 | **2026-06-14** | CIOX, ShareCare, and Updox were originally excluded because the sandbox wasn't ready. They are now back in scope, but their configuration is still pending and non-trivial — the Salesforce sandbox is newly stood up and needs substantial config to match a full environment like pre-prod (see Challenge in Risks). |
| **PD Sandbox (BAU)** | Van | In progress | — | BAU flows — can start now on STD, PFP, RR, Way-Star in parallel | 2026-05-21 | **2026-06-02** | — |
| **UAT** | Van | Not started | — | <ul><li>Wave 1 (6/15): Prefill API, CC Management, Invoice Upload</li><li>Wave 2 (6/17): Status Retrieval API, Status Sync Job</li><li>Wave 3 (6/22): Auto-Pay via CC (TPR)</li></ul> | 2026-06-15 – 2026-06-25 | On track if Pre-UAT closes 06/14 | Wave 2 dates may be delayed as it depends on PD webhook details which is not provided yet (see Risks). |
| **Production** | — | Not started | — | UAT sign-off | 2026-06-30 | Unverified | — |

---

## Client release plan (received 2026-06-01)

*Source: client release plan (Austin). Account-flagged items ship when enabled per account.*

### Code releases

*Environment promotion targets by wave.*

| Wave | Feature | Scope | Account flag | UAT | Prod | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Wave 1 | Prefill Order form API | API to prefill order form | Yes | 2026-06-15 | 2026-06-17 | — |
| Wave 1 | Credit Card Management | Shows existing User SavedPayments; cart must include User **and** Account SavedPayments (valid / non-expired only). Assumes Payflow issues resolved. | Yes | 2026-06-15 | 2026-06-17 | Added new Contact/User-level flag to enable the saved payments page edit per contact. |
| Wave 1 | Invoice Upload to S3 | On successful Request payment: upload with Type **Invoice**. Prod path: `Chartswap/Invoices`. | Yes | 2026-06-15 | 2026-06-17 | — |
| Wave 2 | Status Retrieval API | Method to build response body; also used for Status Sync Job payload. | — | 2026-06-17 | 2026-06-22 | Dates may be pushed: webhook integration has not been communicated to us yet from their side. |
| Wave 2 | Status Sync Job | Scheduled / account-scoped status sync. | Yes | 2026-06-17 | 2026-06-22 | Dates may be pushed: webhook integration has not been communicated to us yet from their side. |
| Wave 3 | Auto-Pay via Credit Card | New payment flow (Transaction Reconciliation Project / TPR). If Request is in any cart and user pays via Auto-Pay, remove Request from **all** carts before Auto-Pay runs. | — | 2026-06-22 | 2026-06-25 | — |
| TBD | SSO | Single sign-on integration — requires PD metadata and config. | Yes | TBD | TBD | Release wave unknown; PD metadata, and config still missing — see Risks |
| TBD | Cart hiding | Hide cart UI when enabled. | Yes | TBD | TBD | — |
| TBD | Prevent Record Finder | Block Record Finder when enabled. | Yes | TBD | TBD | — |
| TBD | Suppress email notifications | Disable email notifications when enabled. | Yes | TBD | TBD | Account-flag behavior confirm with client (Salah) |

---

## Open delivery blockers — payment bugs (3 Major open)

Three **Major (no workaround)** payment bugs block Pre-UAT sign-off on **Retrieval (RR)** and **CIOX**. **OC-9529** and **OC-9531** are in **QA** awaiting **Youssef** retest; **OC-9532** is in **Progress** (**Sara Hassan**). Estimates below are planning targets — no time logged in Jira yet.

*Synced from Jira epic [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) on 2026-06-03.*

### Retrieval (RR) — 2 bugs

| Bug | What's wrong | Jira status | Assignee | Youssef (retest) | Target |
| --- | --- | --- | --- | --- | --- |
| [OC-9529](https://ontellus.atlassian.net/browse/OC-9529) | AutoPay not triggered on 1st payment | **QA** | Michael Girgis | ~0.5 day | 2026-06-06 |
| [OC-9531](https://ontellus.atlassian.net/browse/OC-9531) | 2nd payment charged $57 instead of $20 + SORs | **QA** | Michael Girgis | ~0.5 day | 2026-06-11 |

**Retest shortcut:** OC-9529 and OC-9531 can be retested together in one session (~0.5 day total).

### CIOX — 1 open

| Bug | What's wrong | Jira status | Assignee | Youssef (retest) | Target |
| --- | --- | --- | --- | --- | --- |
| [OC-9532](https://ontellus.atlassian.net/browse/OC-9532) | Request marked Completed after 2nd payment without processing | **Progress** | Sara Hassan | ~0.5 day | 2026-06-13 |

---

## Risks & challenges

Each item below is stated as a **condition → consequence**, with a mitigation that addresses that specific consequence.


| #   | Risk / challenge                                                                                                                                                                                                                                                                                                               | Mitigation                                                                                                                                                                                                                                                                 | Severity |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| 1   | **Late design changes from Austin could force rework.** Further scope or design updates from the client may require re-coding and full-team retest across Pre-UAT and the release waves, threatening the 06/14 date and June go-live.                                                                                          | <ul><li><strong>Michael </strong>dedicated to absorbing Austin's design updates</li><li>Track all changes against the [client release plan](#client-release-plan-received-2026-06-01)</li><li>Re-estimate affected waves before committing UAT dates</li><li> escalate if 06/14 or go-live is threatened</li></ul> | High     |
| 2   | **End-to-end testing against the PD lower env cannot start.** PD has not responded on lower-environment access, so BAU/E2E validation hasn't begun — only provider-level sandbox testing is underway. The integration risks being validated late, or not before go-live.                                                         | <ul><li>Follow up with Katherine; keep mocking the integration in the meantime</li><li>Escalate to Austin / Van that go-live is at risk if the needed access is not received by <strong>2026-06-08</strong></li></ul>                                                                                | High     |
| 3   | **SSO cannot be configured or release-planned.** PD has not provided the SSO metadata and configuration required for sandbox/UAT access, leaving the SSO release wave undefined and blocking UAT sign-off.                                                                                                                     | <ul><li>Track as a PD dependency</li><li> escalated to Austin / PD contacts</li><li>Hold UAT sign-off until SSO config is in place</li></ul>                                                                                                                                                     | High     |
| 4   | **Wave 2 dates may slip (Status Retrieval API & Status Sync Job).** PD has not yet communicated the webhook integration details these features depend on, so the 06/17 UAT / 06/22 prod targets may move.                                                                                                                      | <ul><li>Request webhook details from PD; track alongside the SSO dependency</li><li>Re-baseline Wave 2 dates once received</li><li> escalate if not received by 06/10 to hold the wave</li></ul>                                                                                                 | Medium   |
