---
version: "1.0"
created: "2026-07-08"
last_updated: "2026-07-08"
updated_by: "Closure Analysis"
status: "active"
defect_id: ""
tracking_id: "OC-9654"
project: "ChartSwap / Pattern Data"
analysis_type: "post-closure"
validity: "valid"
root_cause_slug: "missing_implementation"
labels_applied: ["valid", "missing_implementation"]
not_clear_count: 1
---

# Closure Analysis — OC-9654 — Payment Management: Replace card reports "No active AutoPay requests are linked" when the card has New/Ordered requests

## 1. Snapshot

| Field | Value |
|-------|-------|
| Tracking ID | OC-9654 |
| Title | Payment Management: Replace card reports "No active AutoPay requests are linked" when the card has New/Ordered requests |
| Reported / Closed | 2026-06-24 → 2026-07-08 |

## 2. Holistic Summary

Replace Card falsely reported no linked AutoPay requests when a saved card had New/Ordered requests still in flight, blocking firms from moving those requests to a replacement card. The affected-requests query reused the OC-9574 charge-step status filter (Pending Payment / Buy Now) as the display/relink predicate; widening it to a terminal-status deny-list surfaced all active requests while leaving re-charge selection unchanged.

## 3. Root Cause

| Field | Value | Source/Evidence |
|-------|-------|-----------------|
| Validity | valid | Reproduced with 4 active requests (3 Ordered, 1 New); fix confirmed on portal |
| Root cause description | `SavedPaymentAutoPayService.CardDataLoader.loadAffectedRequests` filtered `Status__c IN ('Pending Payment','Buy Now')` — correct for re-charge but wrongly reused as the display/relink set, dropping New/Ordered requests and returning `noAffected`. | Description field, comment 113793 |
| Category slug | missing_implementation | Wrong status predicate applied to display/relink query |
| Labels applied | `valid`, `missing_implementation` | — |

## 4. Lifecycle Metrics

| Metric | Value | Computed from |
|--------|-------|---------------|
| Time to first response | ~29m | 2026-06-24T07:13:39 → 2026-06-24T07:42:48 (comment 113792) |
| Resolution time (created → done) | ~14.0d (wall-clock) | 2026-06-24T07:13:39 → 2026-07-08T05:37:23 |
| Cycle time (work start → done) | ~13.9d (wall-clock) | 2026-06-24T07:43:58 → 2026-07-08T05:37:23 |
| Time in progress | ~13.9d (wall-clock; QA wait dominated) | Progress/PCR/QA intervals from changelog |
| Reopen frequency | 1 | 2026-07-05 QA → Progress |
| Status transition count | 8 | changelog status transitions |

> Timestamps: created `2026-06-24T07:13:39.716-0500`; first Progress `2026-06-24T07:43:58.039-0500`; last Closed `2026-07-08T05:37:23.844-0500`.

## 5. Resolution & Verification

| Field | Value | Source/Evidence |
|-------|-------|-----------------|
| Resolution / fix description | Widened display/relink query to `Status__c NOT IN ('Completed','Complete','Cancelled','Rejected')`; re-charge selection unchanged via `ReinitiationChargeService.categorizeEligibility`. Tests added to `SavedPaymentAutoPayServiceTest` (19/19). | Comment 113793 |
| Fixed in (PR/commit/version/build) | Deploy `0AfWL00000FQuNh0AL` (RunSpecifiedTests) | Comment 113793 |
| Verified in (run/build) | pddev — portal walkthrough 2026-07-06; 4 active requests listed on replace screen | Comment 115216 |
| Verified by | Michael Girgis | Comments 113792, 115216 |

## 6. Insights

- Regression sibling of OC-9574 — fixing the charge-step allow-list for rejected requests inadvertently narrowed the display set.
- Single reopen after initial QA pass; second portal verification preceded final close.

## 7. Prevention / Lessons Learned

- Separate display/relink predicates from charge-eligibility predicates — never reuse a narrow charge-step filter as the affected-request display set.
- Add integration tests covering New/Ordered card-linked requests on the Replace flow, not only charge-step statuses.

## 8. Fields Needing Human Input

- [ ] Fixed in (PR/commit) — inner submodule commit + deploy-hub refresh noted pending in comment 113793

## Changelog

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-07-08 | Closure Analysis | Initial closure analysis; posted summary comment 115517 and set labels `valid`, `missing_implementation` on OC-9654 |
