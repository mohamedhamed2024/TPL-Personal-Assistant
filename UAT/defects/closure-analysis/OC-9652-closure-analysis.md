---
version: "1.0"
created: "2026-07-06"
last_updated: "2026-07-06"
updated_by: "Closure Analysis"
status: "active"
defect_id: ""
tracking_id: "OC-9652"
project: "ChartSwap / Pattern Data"
analysis_type: "post-closure"
validity: "valid"
root_cause_slug: "missing_implementation"
labels_applied: ["valid", "missing_implementation"]
not_clear_count: 1
---

# Closure Analysis — OC-9652 — Patient prefill PHI not deleted on tab/window close

## 1. Snapshot

| Field | Value |
|-------|-------|
| Tracking ID | OC-9652 |
| Title | Patient prefill PHI is not deleted when the PatternData session ends (tab/window closed) |
| Reported / Closed | 2026-06-24 → 2026-07-06 |

## 2. Holistic Summary

Logout correctly cleared staged patient prefill PHI, but closing the browser tab left `Patient_Prefill_Data__c` rows behind — a privacy gap. The fix added a `sendBeacon` session-end path mirroring logout cleanup plus a scheduled sweep backstop for abnormal closes.

## 3. Root Cause

| Field | Value | Source/Evidence |
|-------|-------|-----------------|
| Validity | valid | Confirmed PHI persisted after tab close; privacy/HIPAA concern |
| Root cause description | Prefill PHI cleanup was wired only to `LogoutController.revokeAllOAuthSessions` (explicit logout); tab/window close never triggered deletion. | Comment 113797 |
| Category slug | missing_implementation | Session-end cleanup path never implemented for tab close |
| Labels applied | `valid`, `missing_implementation` | — |

## 4. Lifecycle Metrics

| Metric | Value | Computed from |
|--------|-------|---------------|
| Time to first response | ~15m | 2026-06-24T07:11:59 → 2026-06-24T08:27:10 |
| Resolution time | ~12.0d (wall-clock) | 2026-06-24T07:11:59 → 2026-07-06T05:45:55 |
| Cycle time | ~12.0d (wall-clock) | 2026-06-24T08:28:59 → 2026-07-06T05:45:55 |
| Time in progress | ~12.0d (wall-clock; QA wait dominated) | Progress + PCR + QA intervals |
| Reopen frequency | 0 | changelog |
| Status transition count | 15 | changelog |

## 5. Resolution & Verification

| Field | Value | Source/Evidence |
|-------|-------|-----------------|
| Resolution / fix description | PrefillCleanupService + PrefillSessionEndBeacon (pagehide/beforeunload sendBeacon) + PrefillCleanupSweepBatch (15-min scheduled backstop). | Comment 113797 |
| Fixed in | pddev deploy 0AfWL00000FQcDu0AL (PrefillSessionEndCleanupTest 10/10) | Comment 113797 |
| Verified in | pddev live — pagehide beacon deletes row; QA re-verified 2026-07-03 | Comments 113797, 114992 |
| Verified by | Michael Girgis | Comments 113796, 114992 |

## 6. Insights

- Related to OC-9664 (logout bypass) and OC-9252 (SSO idle timeout) — session lifecycle cleanup is a recurring theme.
- Beacon deliberately excludes `visibilitychange→hidden` to avoid firing on tab switch.

## 7. Prevention / Lessons Learned

- All session-termination paths (logout, tab close, timeout, crash) must trigger the same PHI cleanup predicate.
- Add a scheduled backstop for cleanup actions that depend on client-side signals.

## 8. Fields Needing Human Input

- [ ] Fixed in (PR/commit) — inner submodule commit + Bitbucket push noted pending in comment 113797

## Changelog

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-07-06 | Closure Analysis | Initial closure analysis |
