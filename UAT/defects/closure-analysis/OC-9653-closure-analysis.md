---
version: "1.0"
created: "2026-07-06"
last_updated: "2026-07-06"
updated_by: "Closure Analysis"
status: "active"
defect_id: ""
tracking_id: "OC-9653"
project: "ChartSwap / Pattern Data"
analysis_type: "post-closure"
validity: "valid"
root_cause_slug: "missing_implementation"
labels_applied: ["valid", "missing_implementation"]
not_clear_count: 0
---

# Closure Analysis — OC-9653 — Add Account Card shows Insufficient Privileges

## 1. Snapshot

| Field | Value |
|-------|-------|
| Tracking ID | OC-9653 |
| Title | Saved Payment Management — "Add Account Card" shows Insufficient Privileges instead of the secure card form |
| Reported / Closed | 2026-06-24 → 2026-07-06 |

## 2. Holistic Summary

Portal users clicking Add Account Card saw an access error instead of the Payflow secure card form. Two compounding issues: Payflow return URLs were built from the internal org domain (not the portal origin), and the portal profile had drifted to deny access to the relay page. Both were corrected and card save verified live.

## 3. Root Cause

| Field | Value | Source/Evidence |
|-------|-------|-----------------|
| Validity | valid | Confirmed Insufficient Privileges blocked card add for portal users |
| Root cause description | (1) `buildSecureTokenNvp` used `Url.getOrgDomainUrl()` for RETURNURL/CANCELURL/ERRORURL instead of the portal browser origin. (2) Chartswap Portal User profile had `SavedPaymentManagementRelay` page access disabled in org (drift from source). | Comment 113757 |
| Category slug | missing_implementation | Primary code gap — browser origin received but not threaded into Payflow return URLs |
| Labels applied | `valid`, `missing_implementation` | — |

## 4. Lifecycle Metrics

| Metric | Value | Computed from |
|--------|-------|---------------|
| Time to first response | ~3m | 2026-06-24T07:12:19 → 2026-06-24T07:15:23 |
| Resolution time | ~12.0d (wall-clock) | 2026-06-24T07:12:19 → 2026-07-06T05:46:18 |
| Cycle time | ~12.0d (wall-clock) | 2026-06-24T07:16:42 → 2026-07-06T05:46:18 |
| Time in progress | ~12.0d (wall-clock; QA wait dominated) | Progress + PCR + QA intervals |
| Reopen frequency | 0 | changelog |
| Status transition count | 14 | changelog |

## 5. Resolution & Verification

| Field | Value | Source/Evidence |
|-------|-------|-----------------|
| Resolution / fix description | Thread portal origin through `sanitizeSalesforceOrigin()` into Payflow URLs; redeploy profile with SavedPaymentManagementRelay page access enabled. | Comment 113757 |
| Fixed in | Apex deploy 0AfWL00000FQeAs0AL; profile deploy NoTestRun (43/43 tests) | Comment 113757 |
| Verified in | pddev — PD Firm 1; Add Account Card opens Payflow form; QA re-verified 2026-07-03 | Comments 113756, 114993 |
| Verified by | Michael Girgis | Comments 113756, 114993 |

## 6. Insights

- Related to OC-9649 (payment management cluster).
- Org profile drift (relay page access=false) was a secondary factor — release checklist item for UAT/prod noted in dev comment.
- Inner commit 5dfb3a663 referenced.

## 7. Prevention / Lessons Learned

- Payflow return URLs must use the portal site origin, never the internal my.salesforce.com host.
- Verify portal profile page-access settings in release promotion — org can drift from tracked source.

## 8. Fields Needing Human Input

*(none — all fields evidenced)*

## Changelog

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-07-06 | Closure Analysis | Initial closure analysis |
