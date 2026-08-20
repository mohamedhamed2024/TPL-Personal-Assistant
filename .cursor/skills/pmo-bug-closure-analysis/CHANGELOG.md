# Changelog — pmo-bug-closure-analysis

All notable changes to this skill, latest first. Follows [SemVer](https://semver.org/).
The top version here must always match `version` in [`.openskills.json`](./.openskills.json).

## 1.0.0 — 2026-06-29

### Added
- Initial release. Migrated from a private Integrant workspace, scrubbed of all project/client/confidential content and generalized with placeholders and an `## Inputs` section so it works in any Integrant project.
- Post-closure holistic analysis of a resolved/closed bug with an **Evidence-or-Not-Clear** rule — every field is either evidenced or explicitly marked `Not Clear`.
- Two-tier classification: **validity** (`valid` / `invalid`) plus a single **root-cause slug** from the matching taxonomy list (`references/root-cause-taxonomy.md`), applied as two managed tracker labels.
- Lifecycle metrics computed from the tracker changelog (reopen frequency, cycle time, resolution time, time in progress, time to first response) per `references/metrics-guide.md`.
- Local closure report template (`references/closure-report-template.md`) and an idempotent closure comment that updates in place on re-run instead of duplicating.
- Batch mode that splits large sets (> 5 bugs) across sub-agents (max 5 bugs per sub-agent) per the context-preservation pattern.
