---
version: "1.0"
created: "2026-07-08"
last_updated: "2026-07-08"
updated_by: "Closure Analysis"
status: "active"
defect_id: "DEF-013"
tracking_id: "OC-9575"
project: "ChartSwap / Pattern Data"
analysis_type: "post-closure"
validity: "valid"
root_cause_slug: "design_issue"
labels_applied: ["valid", "design_issue"]
not_clear_count: 1
---

# Closure Analysis — DEF-013 / OC-9575 — Submit with AutoPay stays disabled on a saved Draft even when the authorization form is uploaded

## 1. Snapshot

| Field | Value |
|-------|-------|
| Defect ID | DEF-013 |
| Tracking ID | OC-9575 |
| Title | Submit with AutoPay stays disabled on a saved Draft even when the authorization form is uploaded |
| Reported / Closed | 2026-06-11 → 2026-07-08 |

## 2. Holistic Summary

Saved Drafts with a persisted signed authorization kept "Submit with AutoPay" disabled because the gate read the drift-prone `At_Least_1_Upload__c` cache flag instead of actual file presence. The fix derived authorization satisfaction from persisted upload fields (`uploadHasFile`), and subsequent reopens addressed a firm-card FLS gap under `WITH USER_MODE` that caused inconsistent portal gating before final QA close.

## 3. Root Cause

| Field | Value | Source/Evidence |
|-------|-------|-----------------|
| Validity | valid | Confirmed on REQ-23792608; QA re-verified 2026-07-08 with live screenshots |
| Root cause description | Submit-with-AutoPay enablement relied on the denormalized `At_Least_1_Upload__c` boolean (written inconsistently across ~30 sites) rather than persisted file fields; on save-as-draft reopen the flag stayed false despite `File_Name__c`/`Key__c`/`Status='Upload Complete'`. A later reopen also exposed `loadRequest()` `WITH USER_MODE` FLS blocking firm-card reads, causing inconsistent disabled states. | Description, comments 112901, 627-area technical comments |
| Category slug | design_issue | Gate keyed on a drift-prone denormalized flag instead of source-of-truth file fields |
| Labels applied | `valid`, `design_issue` | — |

## 4. Lifecycle Metrics

| Metric | Value | Computed from |
|--------|-------|---------------|
| Time to first response | ~3.2d | 2026-06-11T07:56:17 → 2026-06-14T20:08:00 (comment 112901, rendered) |
| Resolution time (created → done) | ~27.0d (wall-clock) | 2026-06-11T07:56:17 → 2026-07-08T07:54:49 |
| Cycle time (work start → done) | ~27.0d (wall-clock) | 2026-06-14 first Progress → 2026-07-08 Closed (multiple rework cycles) |
| Time in progress | Not Clear — multiple reopen/rework cycles | changelog spans 65 entries |
| Reopen frequency | 3 | 2026-06-23 QA→Backlog; 2026-07-01 QA→Backlog; 2026-07-06 QA→Progress |
| Status transition count | 20+ | changelog (65 total history entries) |

> Timestamps: created `2026-06-11T07:56:17.871-0500`; last Closed `2026-07-08T07:54:49.575-0500`.

## 5. Resolution & Verification

| Field | Value | Source/Evidence |
|-------|-------|-----------------|
| Resolution / fix description | `AutoPaySubmitController.uploadHasFile()` derives authorization from persisted file fields; `UploadToAmazon` page bindings use `uploadHasFile` instead of `At_Least_1_Upload__c`. Reopen fix restored firm-card gate and removed `WITH USER_MODE` from `loadRequest()` where FLS blocked card reads. | Comments 112901, 2026-07-07 technical comment |
| Fixed in (PR/commit/version/build) | Inner commits `76e5dba47`, `e68b2c86b`; deployed pddev | Comment 112901 |
| Verified in (run/build) | pddev live — REQ-23792608 enabled; 2026-07-08 QA screenshots (auth present, no-card disabled, modal with cards) | Comments 112901, 2026-07-08 QA attachments |
| Verified by | Michael Girgis | Multiple QA comments |

## 6. Insights

- Three reopens indicate unstable triage — one reopen was misattributed to missing firm card when authorization gate was already satisfied.
- Related to OC-9523 (missing-file gate) and OC-9659 (firm-card submission gate) — submit enablement is a multi-predicate surface.
- Derived-gate fix retroactively unblocked existing broken drafts without data backfill.

## 7. Prevention / Lessons Learned

- Derive submit gates from persisted source-of-truth fields, not denormalized cache flags maintained across many write paths.
- When combining authorization and firm-card predicates, ensure data-loading mode (FLS) does not silently zero out card reads used for UI gating.

## 8. Fields Needing Human Input

- [ ] Time in progress — sum of In Progress intervals across 3 reopens not computed (65-entry changelog)

## Changelog

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-07-08 | Closure Analysis | Initial closure analysis; posted summary comment 115518 and set labels `valid`, `design_issue` on OC-9575 |
