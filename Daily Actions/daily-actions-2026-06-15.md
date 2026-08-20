# Daily Actions — Pattern Data

**Source:** [ChartSwap Daily Stand-up — 2026-06-15](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-06-15.docx) · **As of:** 2026-06-15

---

## Open actions

| Owner | Unit testing / code coverage | SOQL data test classes | Pre-UAT bugs & testing | Austin comments / client demo | Jira access — post-migration | CDP / time logging | Process — PR workflow & Jira comments | Leadership / capacity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Michael** | <ul><li>Remove unused voice-related classes</li><li>Sync with Islam on final class list</li><li><strong>Code review together</strong> with Islam</li></ul> | <ul><li>Prefer waiting until open bugs cleared before Sarah starts (avoid churn)</li></ul> | <ul><li>Fix <strong>ShareCare sandbox cost / full-film</strong> today</li><li>Hamed retries <strong>6/16</strong></li><li><strong>Heba Plus Card region</strong> fix — review with Sarah, push when Jira access restored</li></ul> | <ul><li>Remaining <strong>field-removal</strong> items — validate build first, then remove</li><li>Demo with Youssef on RR/CNR fixes</li></ul> | — | <ul><li>Log remaining <strong>internal work as CDP</strong> in Excel today (Hussein flagged gap from 6/16)</li></ul> | <ul><li>Investigate <strong>feature-branch + PR workflow</strong> with Salah</li></ul> | — |
| **Islam** | <ul><li>Confirm missing classes with Michael</li><li><strong>Code review together</strong> with Michael</li></ul> | — | — | — | — | <ul><li>Same CDP logging rules — meetings removed from CDP</li></ul> | — | — |
| **Sarah** | — | <ul><li><strong>Not started</strong> — may begin CIOX data classes</li><li>Investigate which classes need sandbox data vs. pass as-is</li><li>No PR demo until after demos</li></ul> | <ul><li>Heba Plus Card fix discussed — <strong>not pushed demo branch</strong></li><li>Push when Jira access restored</li></ul> | — | <ul><li>Logged into Atlassian but <strong>no project space access</strong></li><li>Permission requests unanswered</li></ul> | — | — | — |
| **Youssef** | — | — | <ul><li>Sit with Michael <strong>before demo</strong> on remaining fixes</li></ul> | <ul><li>Demo with Michael on remaining RR/CNR fixes before deploy</li></ul> | <ul><li>Lost write access — <strong>BO board only</strong></li></ul> | <ul><li>CDP items must say <strong>CDP</strong></li><li>Tie time to actual work, not generic placeholders</li></ul> | — | <ul><li>Fill <strong>BO board</strong> activity template with fixed per-position activities</li></ul> |
| **Hamed** | — | — | <ul><li><strong>ShareCare</strong> not retested yet</li><li>Retry after Michael's sandbox fix (<strong>6/16</strong>)</li></ul> | — | <ul><li>Jira access still limited</li></ul> | — | — | — |
| **Salah** | — | — | <ul><li>Update testing tracker when Youssef confirms completion</li></ul> | — | <ul><li>Escalate Jira access today </li><li>Sarah, Youssef, Hamed blocked</li></ul> | <ul><li>Add <strong>board tasks</strong> from Teams (items since 6/16)</li></ul> | <ul><li>Investigate PR adoption with Michael</li><li>Discuss <strong>Re-open reason</strong> custom Jira field with Nabuya when he returns</li></ul> | — |
| **Hussein** | — | — | — | — | — | — | — | <ul><li>Share <strong>Heba / Reem</strong> case detail this week</li></ul> |
| **Team** | <ul><li>Wave 1 unit-test sign-off (Islam + Michael) before UAT</li></ul> | — | — | — | <ul><li>Each person document <strong>their specific access issue</strong></li></ul> | <ul><li>Log CDP with <strong>specific names</strong> (hooks, agentic solution, XWI)</li><li>Internal work → Excel; client tasks → Jira board</li><li>Comply with Zoom logging rules</li></ul> | <ul><li>When reopening bugs, <strong>developer must document reopen reason</strong> (field or comment)</li></ul> | — |

---

## Completed / done

| Owner | Unit testing / code coverage | SOQL data test classes | Pre-UAT bugs & testing | Austin comments / client demo | Jira access — post-migration | CDP / time logging | Process — PR workflow & Jira comments | Leadership / capacity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Islam** | <ul><li>Pushed Wave 1 unit tests to feature branch (~10 new classes; ≥75% coverage)</li></ul> | — | — | — | — | — | — | — |
| **Michael** | — | — | — | <ul><li>Transaction comments <strong>done</strong></li><li>Invoice S3 validation working</li></ul> | — | — | <ul><li>Basic <strong>sandbox data script</strong> tested — ready for PR workflow</li></ul> | — |
| **Youssef** | — | — | <ul><li>Testing pass largely <strong>complete</strong></li><li>RR/CNR partially verified</li></ul> | — | <ul><li>Notified Jessica</li></ul> | — | — | — |
| **Hamed** | — | — | — | — | <ul><li>Account reactivated (Ontellus + Taafant)</li></ul> | — | — | — |
| **Hussein** | — | — | — | — | — | — | <ul><li><strong>Decision:</strong> code detail in <strong>PRs</strong>, not Jira bug comments</li><li>Jira keeps summary/root-cause only</li></ul> | <ul><li>Raise daily hours <strong>6 → 7</strong> (PTO 7; Ramadan 5+1)</li><li>Do not log PD external standup or leadership meetings</li></ul> |

---

## Decisions (context — not new actions)

- **Unit tests:** Islam pushed full Wave 1 coverage to feature branch; Michael + Islam code review pending; unused voice classes to be removed.
- **Pre-UAT forecast:** **06/14 missed** — re-baseline **2026-06-17**; Wave 1 UAT **06/15 at risk**.
- **ShareCare:** Blocked on Michael's cost/full-film sandbox fix; Hamed retries **2026-06-16**.
- **Updox:** Deprioritized per Austin (likely not on production).
- **PR workflow:** Team agrees in principle; Salah + Michael to finalize start date and data-script readiness.
- **Jira comments:** Too much code in bug comments — shift detail to PRs; keep Jira for business-level notes.
- **Re-open analysis:** Need structured reopen reason (custom field or mandatory comment) for bug analytics.
- **Van demo:** Postponed to **Monday 2026-06-22**.
