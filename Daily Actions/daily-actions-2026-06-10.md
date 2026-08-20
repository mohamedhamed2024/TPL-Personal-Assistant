# Daily Actions — Pattern Data

**Source:** [ChartSwap Daily Stand-up — 2026-06-10](../Daily%20Standup%20Transcript/ChartSwap-Daily-Stand-up-2026-06-10.docx) · **As of:** 2026-06-10

---

## Unit testing / code coverage

| Owner | Action |
| --- | --- |
| **Michael Girgis** | Commit **missing test classes** to the active branch/repo; sit with **Islam** today to close the gap (Islam sent the list yesterday). |
| **Michael Girgis** | Send **Islam** only the **Wave 1 components** (Invoice upload, Prefill, CC Management) — not the full project package. |
| **Islam Fathy** | Start unit tests on classes with **zero coverage** while waiting on Michael (interfaces, etc.). |
| **Islam Fathy** | Prioritize coverage for the **three Wave 1 features** first; re-run the coverage report after missing classes are committed. |

---

## Pre-UAT bugs & testing

| Owner | Action |
| --- | --- |
| **Michael Girgis** | **Primary focus today:** fix **4 bugs** assigned to him (OC-9564, OC-9566, OC-9567, plus Heba's recurring-create ticket). Finish bugs before Austin transaction comments where possible. |
| **Michael Girgis** | **Retest** Heba's recurring-create scenario (2 new records — one passes, one fails); screenshots attached. |
| **Michael Girgis** | Check **Record Retrieval** settings with **Youssef** — pre-payment path completes request without record upload; confirm expected vs. bug. |
| **Michael Girgis** | **Unblock Youssef** on [OC-9567](https://ontellus.atlassian.net/browse/OC-9567) so he can change fields and run remaining Record Retrieval scenarios. |
| **Michael Girgis** + **Islam Fathy** | On **UAT**, verify whether an uploaded file appears in **Guards of Files** after reject/resubmit flow (compare with legacy/PROD behavior). |
| **Youssef Yahiya** | **Blocked** on broader Record Retrieval testing until OC-9567 is resolved; Record Retrieval core flow otherwise done. |
| **Youssef Yahiya** | Test **reject scenario** on UAT (provider still shows fulfill after reject; Guards of Files not updating for requester). |
| **Sarah Hassaan** | Finish **sandbox biology** conflicts; then work with Michael on **SOQL data test classes** on sandbox. |
| **Sarah Hassaan** | May take **backup-force** bug (Louis stalled) — needs ticket number and context from Michael/Mahmoud. |
| **Heba Magdy** + **Sarah Hassaan** | Walk through **status-update** testing together (Heba captured status screenshots for review). |
| **Mohamed Hamed** | **Pause ShareCare** until sandbox bucket fix; then resume testing with Michael's simulation. ShareCare and Updox (forced path) otherwise complete. |

---

## ShareCare sandbox — AWS bucket (blocker)

| Owner | Action |
| --- | --- |
| **Michael Girgis** + **Mohamed Hamed** | Fix ShareCare **sandbox bucket configuration** — sandbox requests were hitting **production AWS bucket** (client cost risk). Align bucket name logic before resuming ShareCare testing. |

---

## Austin comments / client demo

| Owner | Action |
| --- | --- |
| **Michael Girgis** | Review **new Austin VF comments** (items missed earlier) before today's demo; most yesterday's transaction comments done. |
| **Michael Girgis** + **Youssef Yahiya** | Re-raise **Payflow batching** on sandbox with **Austin** — 16+ concurrent requests on same card can block Payflow; Austin previously said not to worry; team wants controlled batch pipeline. |

---

## Jira time logging

| Owner | Action |
| --- | --- |
| **Mahmoud Salah** | Check **Michael's time entries** from yesterday (wrong field suspected); confirm where time is tracked. |
| **Michael Girgis** + **Sarah Hassaan** | Review time-logging together — Michael logged time yesterday; verify it appears in reports. |
| **Team** | Use **Magdy's placeholder ticket** for work that has no specific Jira ticket (Islam reminder). |

---

## Decisions (context — not new actions)

- **Bug load:** 4 bugs with Michael; Heba's recurring-create ticket stays **Save for**; one older Heba ticket may move to **Sarah** (backup-force).
- **Youssef Record Retrieval:** Core testing done; **OC-9567** blocks remaining scenario coverage.
- **Updox:** Forced-path testing complete (Hamed).
- **VF Apex simulation fix** for Hamed (Visa second segment): deferred — Michael stays on bugs first per Salah.
- **UAT Wave 1** target remains **2026-06-16** (Monday); coverage and bug fixes are on the critical path.
