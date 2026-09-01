# Salesforce deploy — Pattern Data daily progress

Standing rules for **deploy package** (changeset) columns, Path to UAT gates, and sandbox promotion. Apply unless standup or user explicitly overrides.

## Reader guide — for managers

ChartSwap runs on **Salesforce**. Code and configuration are not copied file-by-file like a typical web app; the team builds **outbound changesets** — Salesforce’s named **deploy packages** — and uploads them from one environment to the next.

| Term in report | Plain meaning |
| --- | --- |
| **Changeset / deploy package** | A bundled set of Salesforce components (code, screens, settings) prepared for upload to another environment |
| **Feature package** | The forward deploy — ships the new capability |
| **Rollback package** | A pre-built undo package — used if the deploy must be reversed quickly |
| **Properties package** | Optional toggles and account flags (on/off switches), when the feature needs config changes |
| **pddev (PD sandbox)** | Pattern Data development sandbox — where the team finishes and first-tests each feature |
| **UAT sandbox** | Pre-production test environment — where client-facing validation happens before go-live |
| **PR (pull request)** | Code review on Bitbucket — dev quality gate before packaging for Salesforce |
| **PATTERNDATA wordings** | Client-approved labels and text that must be signed off before the deploy package is attached |

**Per feature, expect up to three packages**, each roughly **2–8 hours** of dev/ops effort to build, upload, and validate. Features move to UAT **one at a time**, not in a single combined release.

**Status symbols in tables:** `✓` = built and validated · `Pending` = not yet done · `—` = not required for this feature

---

## Environments

| Environment | Plain name | Role |
| --- | --- | --- |
| **PD sandbox (pddev)** | Development sandbox | Finish feature code; first deploy-package validation |
| **UAT sandbox** | User acceptance testing | Client/UAT validation after pddev sign-off |
| **Production** | Live ChartSwap | After UAT sign-off and client approval per Austin's plan |

Promotion path: **pddev → UAT sandbox → Production** (each step must pass validation before the next).

---

## Per-feature deploy package set (3-pack)

Each Jira story (feature) typically needs:

| # | Package | What it contains | Required? |
| --- | --- | --- | --- |
| 1 | **Feature package** | Application code, tests, UI — ships the capability | Yes |
| 2 | **Rollback package** | Reversal of the same scope — safety net if deploy fails | Yes |
| 3 | **Properties package** | Feature flags, metadata, account settings | Only when the feature needs config toggles |

**Report shorthand** (dev tracker): `Feature ✓ · Rollback ✓ · Properties ✓`  
**Manager-friendly shorthand:** `Forward ✓ · Rollback ✓ · Settings ✓` (either is acceptable; be consistent within one report)

---

## Validation rules

1. Every package must be **uploaded and tested** on the **target environment** before that environment is marked complete.
2. Do **not** mark UAT as **Validated** until all required packages for that feature pass on UAT.
3. Note manual steps in **Next step** (e.g. a component that must be added by hand in Salesforce Setup).

---

## PATTERNDATA wordings gate

- **PATTERNDATA — PENDING WORDINGS** = client copy/labels awaiting approval
- Must be **approved** before attaching to the outbound package
- Tracker column: `Pending approval` → `Approved — attach to package`
- Blocks **UAT-ready** until approved

---

## UAT promotion strategy

- Promote **one feature at a time** — avoids a single large release that is hard to test or roll back
- Do **not** combine all Pattern Data features into one mega-package unless **Austin** explicitly agrees
- **Deployment order** comes from **Austin** (engineering manager) — update from Austin meeting transcript, not a fixed wave schedule
- Payment Management ([LNI-3137](https://datavant.atlassian.net/browse/LNI-3137)) is currently next for UAT per tracker — supersede when Austin reprioritizes

---

## Typical sequence per feature

1. Code complete on a feature branch  
2. Pull request opened → reviewed → merged  
3. Build Feature + Rollback (+ Properties if needed) packages from merged code  
4. Validate on **pddev**  
5. Client wordings approved → attach to package  
6. Upload to **UAT sandbox** → validate  
7. After all features pass UAT per Austin's plan: repeat package set for **Production**

If a story has **no open pull request**, mark **Ready — finalize code review & deploy packages** in the tracker.

---

## Delivery targets

| Milestone | Target date |
| --- | --- |
| All features on UAT sandbox | **2026-09-01** |
| Production go-live | **2026-09-08** |

Adjust **Forecast** in Status at a glance only when **Austin meeting** or standup confirms a slip.

---

## Reference docs (repo)

When available, cross-check packaging order against:
- `docs/deploy/pattern-data/PHASE1-CONSOLIDATED-CHANGESETS.md`
- Jira story comments linking Salesforce outbound package URLs on pddev
