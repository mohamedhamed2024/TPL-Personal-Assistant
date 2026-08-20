# Pattern Data — delivery progress

**Go-live goal:** End of June 2026 · **Epic:** [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) · **As of:** 2026-06-01

---

## Executive summary

- **Pre-UAT is in progress** — original target **2026-05-21**, forecast complete **2026-06-14**.
- **4 of 7 provider types tested** on PD sandbox:
  - STD, PFP, and RR — tested **2026-05-25**
  - Way-Star — tested via simulated fulfilment (Sarah)
- **3 providers still need sandbox config** before testing: CIOX, ShareCare, Updox.
- **4 Major-2 defects open** — all RR/CIOX payment issues (Michael); Youssef retests after each fix.
- **Parallel work is possible** — BAU and UAT can start on ready types while Pre-UAT finishes the rest.
- **June go-live (2026-06-30) is unverified** — needs confirmation with Austin.
- **Client release plan received (2026-06-01)** — three promotion waves (6/15–6/17, 6/17–6/22, 6/22–6/25); see [Client release plan](#client-release-plan-received-2026-06-01).
- **Current focus:**
  - **Michael** — Apply payment management updates to reflect on the BAU CC page
  - **Sarah & Islam** — provider sandbox config + Bug fixes
  - **Youssef** — QA retest (~0.5 day per bug)
  - **Van** — BAU/UAT on ready types
  - **Sarah** — Way-Star E2E on UAT

---

## Status at a glance

| Phase | Owner | Status | What's done | What's left | Target | Forecast |
| --- | --- | --- | --- | --- | --- | --- |
| **Pre-UAT** | Youssef | In progress | <li>4/7 providers tested [STD, PFP, RR, and Waystar]</li><li> 4 Major open bugs</li> | <ul><li>Config setup</li><li> test CIOX, ShareCare, Updox</li><li>Fix & retest 4 open bugs</li></ul> | 2026-06-03 | **2026-06-14** |
| **PD Sandbox (BAU)** | Van | Not started | — | BAU flows — can start now on STD, PFP, RR, Way-Star in parallel | 2026-06-02 | **2026-06-08** |
| **UAT** | Van | Not started | — | All providers on UAT (~10 days) | 2026-06-14 – 2026-06-26 | On track if Pre-UAT closes 06/14 |
| **Production** | — | Not started | — | UAT sign-off | 2026-06-30 | Unverified |

**Program notes:**

- Still no response from PD on lower-environment testing.
- Still missing SSO metadata and webhook URL from PD.
- Youssef requested a demo with Van on **2026-05-24** — no response from Van to date.
- Austin plans to release features in chunks (not a single deployment) — aligns with [client release plan](#client-release-plan-received-2026-06-01).
- Expecting last-minute design changes from Austin that may drive rework and team retest.

---

## Client release plan (received 2026-06-01)

*Source: client release plan (Austin). Account-flagged items ship when enabled per account; dates below are environment promotion targets.*

**Review (vs program milestones):**

- **Wave 1 (UAT 6/15 → Prod 6/17):** Prefill Order form API, Credit Card Management, Invoice Upload — aligns with UAT start **2026-06-14** (one day after window opens).
- **Wave 2 (UAT 6/17 → Prod 6/22):** Status Retrieval API + Status Sync Job — same-day UAT; Prod before overall go-live **2026-06-30**.
- **Wave 3 (UAT 6/22 → Prod 6/25):** Auto-Pay via Credit Card (TPR) — overlaps open Pre-UAT payment defects (OC-9529–9532); cart-removal rule adds scope.
- **Account-only (no UAT/Prod date):** Cart hiding, Prevent Record Finder, Suppress email notifications, SSO — track as config/flag rollouts; SSO still an open PD dependency (see [Risks](#risks)).
- **Dependencies:** Credit Card Management assumes Payflow issues resolved; Auto-Pay tied to Transaction Reconciliation Project (TPR).
- **Open with client (`???`):** Account-level CC “Admin” add — who enables (User vs Contact)? Suppress email notifications — account-flag behavior TBD.


| Feature | Scope / notes | Account flag | UAT | Prod | Open items |
| --- | --- | --- | --- | --- | --- |
| Prefill Order form API | API to prefill order form | Yes | 2026-06-15 | 2026-06-17 | — |
| Credit Card Management | Shows existing User SavedPayments; cart must include User **and** Account SavedPayments (valid / non-expired only). Assumes Payflow issues resolved. | Yes | 2026-06-15 | 2026-06-17 | “Admin” ability to add Account-level CC — enabled by User/Contact? **Confirm with client.** |
| Invoice Upload to S3 | On successful Request payment: upload with Type **Invoice**. Prod path: `Chartswap/Invoices`. | Yes | 2026-06-15 | 2026-06-17 | — |
| Status Retrieval API | Method to build response body; also used for Status Sync Job payload. | — | 2026-06-17 | 2026-06-22 | — |
| Status Sync Job | Scheduled / account-scoped status sync. | Yes | 2026-06-17 | 2026-06-22 | — |
| Cart hiding | Hide cart UI when enabled. | Yes | N/A | N/A | No env promotion date — flag-only |
| Prevent Record Finder | Block Record Finder when enabled. | Yes | N/A | N/A | No env promotion date — flag-only |
| Suppress email notifications | Disable email notifications when enabled. | Yes | N/A | N/A | Account-flag behavior **confirm with client** |
| Auto-Pay via Credit Card | New payment flow (Transaction Reconciliation Project / TPR). If Request is in any cart and user pays via Auto-Pay, remove Request from **all** carts before Auto-Pay runs. | — | 2026-06-22 | 2026-06-25 | TPR dependency; overlaps OC-9529–9532 payment work |
| SSO | Single sign-on | — | N/A | N/A | PD metadata/config still missing — see Risks |

---

## Open delivery blockers — 4 Major-2 bugs

*Fix estimates by Michael · Retest estimates by Youssef · No Jira time logged on open items — estimates are planning targets.*

| Key | Summary | Status | Fix est. (Michael) | Retest est. (Youssef) | Target |
| --- | --- | --- | --- | --- | --- |
| [OC-9529](https://ontellus.atlassian.net/browse/OC-9529) | RR — AutoPay not triggered on 1st payment | In progress | ~1 day *(remaining)* | ~0.5 day | 2026-06-06 |
| [OC-9530](https://ontellus.atlassian.net/browse/OC-9530) | RR — status stays Pending Payment after 2nd payment | To-Do | ~1 day | ~0.5 day | 2026-06-09 |
| [OC-9531](https://ontellus.atlassian.net/browse/OC-9531) | RR — 2nd payment charged $57 instead of $20 + SORs | To-Do | ~1 day | ~0.5 day | 2026-06-11 |
| [OC-9532](https://ontellus.atlassian.net/browse/OC-9532) | CIOX — Completed after 2nd payment without processing | To-Do | ~1 day | ~0.5 day | 2026-06-13 |

**RR retest note:** OC-9530 and OC-9531 can be retested together in one session (~0.5 day total) once both fixes land.

**Total open fix effort:** ~4 days (Michael) · **Total retest effort:** ~2 days (Youssef, can overlap with config testing)

*3 Minor-4 bugs also open — not delivery-blocking.*

---

## Risks

| Risk | Mitigation | Severity |
| --- | --- | --- |
| **Michael on multiple tasks** — sandbox config (3 providers), RR payment fixes (3 bugs), CIOX fix (OC-9532), and one Austin comment all in flight ahead of the **06/14** Pre-UAT date | <ul><li>Assign bugs to Sarah & Islam, then config</li><li>Youssef retests as each item lands</li><li>Michael to focus on Austin's design updates</li></ul> | High |
| **Provider config may need investigation** — CIOX, ShareCare, and Updox must be configured correctly on PD sandbox; some settings are not straightforward | <lu><li>Time-box per provider (~1–2 days each)</li><li> escalate to Salah / Youssef if blocked</li></lu> | Medium |
| **E2E testing with PD not started yet on PD Sandbox** — BAU/E2E flows against PD sandbox have not begun; only provider-level sandbox testing is underway | <lu><li>Follow up with Katherine and continue mocking the integration</li><li>Escilate to Austin/Van that the do-live plan will be affected if we didn't get the needed items by <strong>2026-06-08</strong></li></lu> | High |
| **SSO metadata and configuration still missing from PD side** — SSO setup required for sandbox/UAT access is not yet provided by Pattern Data | <lu><li>Track as PD dependency</li><li> escalate to Austin / PD contacts</li><li> block UAT sign-off until SSO is in place</li></lu> | High |
---

## References

- [Testing Updates.md](./Testing Updates.md) — live status
- [pattern-data-delivery-plan-2026-06-02.md](./pattern-data-delivery-plan-2026-06-02.md) — full plan snapshot
- [Jira — open Sev-1/2 bugs](https://ontellus.atlassian.net/issues/?jql=%22Epic%20Link%22%20%3D%20OC-9223%20AND%20issuetype%20%3D%20Bug%20AND%20statusCategory%20!%3D%20Done%20AND%20%22Severity%20for%20the%20bugs%20(Business)%22%20in%20(%22Critical-1%22%2C%20%22Major%20with%20not%20workaround-2%22))
