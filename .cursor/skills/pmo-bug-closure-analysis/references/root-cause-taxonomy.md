# Root Cause Taxonomy

Closure analysis produces **two** classifications for every bug, used both in the report/comment and
as the two tracker labels:

1. **Validity** — is this a genuine defect (`valid`) or not (`invalid`)?
2. **Root cause category** — exactly **one** slug from the matching list below.

The root-cause slug **must come from the list that matches the validity verdict**:
- `valid` → pick one slug from the [Valid bug](#valid-bug-root-causes) list.
- `invalid` → pick one slug from the [Invalid bug](#invalid-bug-root-causes) list.

If the evidence does not clearly support a verdict or a category, set that value to **`Not Clear`** —
do not force-fit. (When validity itself is `Not Clear`, the category is also `Not Clear`.)

## Table of Contents
- [Step 1 — Decide validity](#step-1--decide-validity)
- [Step 2 — Pick the root cause slug](#step-2--pick-the-root-cause-slug)
- [Valid bug root causes](#valid-bug-root-causes)
- [Invalid bug root causes](#invalid-bug-root-causes)
- [Label values](#label-values)

## Step 1 — Decide validity

| Verdict | Use when | Label |
|---------|----------|-------|
| **valid** | The reported behavior was a genuine defect — something was wrong in design, code, requirements, config, deployment, a dependency, or test coverage. | `valid` |
| **invalid** | Not a genuine product defect — could not be reproduced, the test/steps were wrong, the behavior was out of scope, or it is expected/as-designed behavior. | `invalid` |
| **Not Clear** | The closing evidence does not say whether it was a real defect. | *(no validity label set)* |

## Step 2 — Pick the root cause slug

1. Read the evidenced root cause (the defect's Root Cause section, the resolution comment, and
   developer comments).
2. From the list matching the validity verdict, match it to the closest slug using "Indicators".
3. If two slugs seem to fit, pick the single one that best describes the *origin* of the defect
   (why it was introduced).
4. If no slug is supported by evidence → `Not Clear`.

## Valid bug root causes

Pick exactly one when validity = `valid`.

| Slug | Indicators | Example |
|------|-----------|---------|
| **design_issue** | Correct code for a flawed design; wrong boundary, contract, data model, or UX/render design decision | A field gated on the wrong flag by design |
| **missing_implementation** | Required behavior was never built, or a coding/logic gap — wrong condition, missing branch, null handling, off-by-one | `if (featureEnabled)` instead of `if (featureEnabled || isException)` |
| **missing_requirement** | Missing, ambiguous, or wrong requirement/AC; behavior built to an unclear spec | AC didn't define behavior when the feature is disabled |
| **insufficient_testing** | Code was nearly correct but tests missed the case; an escaped defect / coverage gap | No test scenario covered the edge case |
| **third_party_issue** | Defect originates in an external library, platform, partner, or vendor system | A vendor API changed its response shape |
| **environment_missing_configuration** | Wrong/missing config, feature flag, environment value, infra setting, or seeded/master data | A feature flag set OFF when it should be ON for a customer segment |
| **deployment_issue** | Regression from a deploy, bad merge, missing migration, release/env drift | A deployment reverted the render condition |

## Invalid bug root causes

Pick exactly one when validity = `invalid`.

| Slug | Indicators | Example |
|------|-----------|---------|
| **non_reproducable** | Cannot be reproduced; no consistent repro steps; transient/one-off | Closed as cannot reproduce after retries |
| **wrong_testing** | Tester error — wrong steps, wrong test data, misread expected behavior, bad assertion | Tester used the wrong account/role so the section was correctly hidden |
| **descoped** | Behavior intentionally out of scope, deferred, or duplicate of tracked work | Closed because the feature was deferred to a later phase |
| **business_as_usual** | Works as designed / expected behavior; not a defect | Closed as expected behavior per the spec |

## Label values

The skill sets exactly **two** tracker labels on the bug, drawn only from these fixed sets:

- **Validity label** (one of): `valid`, `invalid`
- **Root cause label** (one slug): any value from the Valid or Invalid tables above.

These two enumerated sets are the *only* labels the skill manages. On a re-run it removes any
previously-applied label from these sets before applying the current pair, so labels stay in sync
with the latest analysis. All other labels on the issue are left untouched. If validity is
`Not Clear`, no validity label is set; if the category is `Not Clear`, no root cause label is set.
