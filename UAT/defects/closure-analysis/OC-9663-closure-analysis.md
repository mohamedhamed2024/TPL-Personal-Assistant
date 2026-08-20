---
version: "1.0"
created: "2026-07-06"
last_updated: "2026-07-06"
updated_by: "Closure Analysis"
status: "active"
defect_id: ""
tracking_id: "OC-9663"
project: "ChartSwap / Pattern Data"
analysis_type: "post-closure"
validity: "valid"
root_cause_slug: "missing_implementation"
labels_applied: ["valid", "missing_implementation"]
not_clear_count: 0
---

# Closure Analysis — OC-9663 — Draft empty document row + no upload path

## 1. Snapshot

| Field | Value |
|-------|-------|
| Tracking ID | OC-9663 |
| Title | Draft request shows an empty Documents and Records row and has no direct upload path |
| Reported / Closed | 2026-06-24 → 2026-07-06 |

## 2. Holistic Summary

Saving a draft without a file left an empty nameless row in Documents and Records, and there was no direct way to upload to a saved draft. The fix filters empty `Upload__c` placeholder shells from the documents list and adds an Upload Files CTA on Draft status. The placeholder filter also catches fulfillment-side empty rows on rejected requests (origin-agnostic).

## 3. Root Cause

| Field | Value | Source/Evidence |
|-------|-------|-----------------|
| Validity | valid | Confirmed empty row on draft; no direct upload path |
| Root cause description | `RequestWizard.createRequest1` inserts an empty Upload__c shell; save-as-draft leaves it unpopulated. `RequestUtils.Uploads` had no `File_Name__c` guard, so placeholders rendered. No draft upload path existed in RRequestView. | Comment 113835 |
| Category slug | missing_implementation | Missing placeholder filter and missing draft upload UX |
| Labels applied | `valid`, `missing_implementation` | — |

## 4. Lifecycle Metrics

| Metric | Value | Computed from |
|--------|-------|---------------|
| Time to first response | ~33m | 2026-06-24T09:30:18 → 2026-06-24T10:03:10 |
| Resolution time | ~12.0d (wall-clock) | 2026-06-24T09:30:18 → 2026-07-06T06:01:53 |
| Cycle time | ~12.0d (wall-clock) | 2026-06-24T10:03:27 → 2026-07-06T06:01:53 |
| Time in progress | ~12.0d (wall-clock; QA wait dominated) | Progress + PCR + QA intervals |
| Reopen frequency | 0 | changelog |
| Status transition count | 15 | changelog |

## 5. Resolution & Verification

| Field | Value | Source/Evidence |
|-------|-------|-----------------|
| Resolution / fix description | `isEmptyPlaceholderUpload` filter in `filterUploadsForRequestStatus`; `IsDraft` + `DraftUploadId` + Upload Files link on RRequestView for Draft status. | Comment 113835 |
| Fixed in | pddev deploy; inner commit 0f4720c85; RequestUtils_Test passes | Comment 113835 |
| Verified in | REQ-23767154 (draft); REQ-23804518 (rejected re-verification) | Comments 113835, 113837 |
| Verified by | Michael Girgis | Comments 113834, 113836 |

## 6. Insights

- Pre-existing BAU behavior, not AutoPay-specific.
- Re-verified during OC-9630 CNR review — placeholder can originate from fulfillment side (provider-created), not just request creation; filter is origin-agnostic.
- Related to OC-9575.

## 7. Prevention / Lessons Learned

- Documents list queries must exclude empty placeholder shells (blank File_Name, Key, Attachment_Id).
- Draft requests need a direct upload path without re-running the full request wizard.

## 8. Fields Needing Human Input

*(none — all fields evidenced)*

## Changelog

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-07-06 | Closure Analysis | Initial closure analysis |
