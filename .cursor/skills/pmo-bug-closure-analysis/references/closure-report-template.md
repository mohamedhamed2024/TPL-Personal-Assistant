# Closure Report Template

Use this structure for the local report (conventionally at
`UAT/defects/closure-analysis/DEF-NNN-closure-analysis.md`).

Rules:
- Every field is either evidenced or set to **`Not Clear`** (optionally with a short reason).
- Cite the source of each evidenced value in the "Source/Evidence" column where present.
- Keep frontmatter and the Changelog section per your versioning convention.

---

```markdown
---
version: "1.0"
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
updated_by: "AI Assistant"
status: "active"
defect_id: "DEF-NNN"
tracking_id: "TRACK-NNN"   # or "" if not pushed
project: "<project>"
analysis_type: "post-closure"
validity: "valid"          # valid | invalid | Not Clear
root_cause_slug: ""        # one slug from the matching taxonomy list, or "" if Not Clear
labels_applied: []         # the two managed labels set on the tracker, e.g. ["valid", "design_issue"]
not_clear_count: 0         # number of fields set to Not Clear
---

# Closure Analysis — DEF-NNN / TRACK-NNN — {Bug Title}

## 1. Snapshot

> Identifiers only — do NOT duplicate ticket fields (severity, priority, assignee, labels,
> components, status). Those are read directly from the tracker.

| Field | Value |
|-------|-------|
| Defect ID | DEF-NNN |
| Tracking ID | TRACK-NNN |
| Title | {title} |
| Reported / Closed | {date} → {date} |

## 2. Holistic Summary

{2–3 direct sentences: what the bug was and how it was resolved. Be brief — add insight, not a
retelling of the ticket.}

## 3. Root Cause

| Field | Value | Source/Evidence |
|-------|-------|-----------------|
| Validity | {valid / invalid / Not Clear} | {evidence} |
| Root cause description | {text or Not Clear} | {defect Root Cause section / comment id / Not Clear} |
| Category slug (exactly one) | {single slug from the matching taxonomy list or Not Clear} | {evidence} |
| Labels applied | `{validity}`, `{root-cause-slug}` (omit a label if its value is Not Clear) | — |

## 4. Lifecycle Metrics

| Metric | Value | Computed from |
|--------|-------|---------------|
| Time to first response | {dur or Not Clear} | {created → first comment/transition} |
| Resolution time (created → done) | {dur or Not Clear} | {created → done_time} |
| Cycle time (work start → done) | {dur or Not Clear} | {first In Progress → last Done} |
| Time in progress | {dur or Not Clear} | {sum of In Progress intervals} |
| Reopen frequency | {N / 0 / Not Clear} | {reopen transitions + dates} |
| Status transition count | {N or Not Clear} | {changelog} |

> Show the actual timestamps used so the math is auditable.

## 5. Resolution & Verification

| Field | Value | Source/Evidence |
|-------|-------|-----------------|
| Resolution / fix description | {text or Not Clear} | {defect Resolution section / comment} |
| Fixed in (PR/commit/version/build) | {ref or Not Clear} | {comment} |
| Verified in (run/build) | {ref or Not Clear} | {defect Resolution section / comment} |
| Verified by | {name or Not Clear} | {comment} |

## 6. Insights

{Bullet observations grounded in evidence: e.g., multiple reopens indicating an unstable fix,
escaped-defect test gap, config drift between environments, etc. If no insight can be supported by
evidence, write "Not Clear — insufficient recorded history".}

## 7. Prevention / Lessons Learned

{Concrete, evidence-grounded suggestions. If the root cause is Not Clear, this is also `Not Clear`.}

## 8. Fields Needing Human Input

> Every field set to **Not Clear** above is listed here so a reviewer can complete it.

- [ ] {field name} — {what's missing}
- [ ] ...

## Changelog

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | YYYY-MM-DD | AI Assistant | Initial closure analysis; posted summary comment {comment id} and set labels `{validity}`, `{slug}` on TRACK-NNN |
| 1.1 | YYYY-MM-DD | AI Assistant | Re-run — updated comment {comment id} in place and refreshed labels |
```
