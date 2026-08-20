# Daily Actions — Pattern Data

**Source:** [ChartSwap Daily Stand-up — 2026-06-16](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-2026-06-16.docx) · **As of:** 2026-06-16 · **Project:** Pattern Data

---

## Open actions

| Owner | Unit testing / code coverage | SOQL data test classes | Pre-UAT bugs & testing | Austin comments / client demo | Jira access — post-migration | CDP / time logging | Process — PR workflow & Jira comments | Leadership / capacity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Michael** | <ul><li>Remove unused voice-related classes</li><li><strong>Code review with Islam</strong> — deferred; Islam on leave <strong>6/16–6/17</strong></li><li>Review Islam's coverage report when he returns (3 classes still below 75%)</li></ul> | — | <ul><li>Fix <strong>VF invoice filter</strong> — provider cost not visible on ShareCare + RR (Youssef + Hamed blocked)</li><li>Demo fixes with testers before QA handoff</li></ul> | <ul><li>Remaining <strong>field-removal</strong> items — validate build first, then remove</li><li>Deferred Austin comments — send to Youssef in agreed format</li><li>Follow up Austin on <strong>merge / VoicePlus deploy</strong> — missing classes on master</li></ul> | <ul><li>OAuth / account access — add <strong>screenshot</strong> to Austin issue sheet (Salah assisting)</li></ul> | <ul><li>Add <strong>bullet-point detail</strong> to CDP / iGoals entries (not high-level only)</li><li>Review overloaded hours flagged by Hussein (~110%)</li></ul> | <ul><li>Investigate <strong>feature-branch + PR workflow</strong> with Salah</li></ul> | — |
| **Islam** | <ul><li>On leave <strong>2026-06-16 & 2026-06-17</strong> — reply on coverage report next week</li></ul> | — | — | — | — | <ul><li>CDP entries need more detail — Salah to follow up when back</li></ul> | — | — |
| **Sarah** | — | <ul><li><strong>Not started</strong> — CIOX data classes; wait until bug churn clears</li></ul> | <ul><li><strong>Heba Plus Card</strong> fix — push when Jira access restored</li></ul> | — | <ul><li>Still <strong>no project space access</strong>; Jessica also lacks access to grant permissions</li></ul> | — | — | — |
| **Youssef** | — | — | <ul><li>Retest complete — current fix batch <strong>stable</strong></li><li>Send Michael all deferred comments in agreed format</li><li>Ensure every open item is on the <strong>board</strong> (some only in chat)</li></ul> | <ul><li>Demo with Michael on remaining items — still deferred</li></ul> | <ul><li>Old token not working; need Ontellus admin with token permissions</li><li>Document issue on Austin access sheet</li></ul> | <ul><li>Fix CDP time — <strong>45 h</strong> flagged; reconcile with PTO day (~132% load)</li></ul> | — | <ul><li>Fill <strong>BO board</strong> activity template</li></ul> |
| **Hamed** | — | — | <ul><li>ShareCare report scenario OK — full retest after Michael's <strong>VF filter</strong> fix</li><li>No further testing today</li></ul> | — | <ul><li>Jira access still limited</li></ul> | — | — | <ul><li>Capacity session with Salah — split BO vs PD tasks; target gradual <strong>100% PD</strong></li><li>Prepare for Ontellus laptop transition</li></ul> |
| **Salah** | — | — | <ul><li>Update testing tracker when Youssef confirms board items</li></ul> | <ul><li>Ask Austin today on <strong>Wave 1 UAT slip</strong> + revised dates (partnership / Printshop dependency)</li></ul> | <ul><li>Escalate Jira access — Sarah, Youssef, Hamed, Jessica blocked</li><li>Add Michael's OAuth screenshot to Austin checklist</li></ul> | <ul><li>Backfill Excel time for month-to-date gaps; log interim work outside Jira until access restored</li><li>Get iGoals detail from Islam next week</li></ul> | <ul><li>Investigate PR adoption with Michael</li><li>Discuss <strong>Re-open reason</strong> field with Nabuya when he returns</li><li>Put Islam under <strong>Nancy station</strong> in Jira org — confirm with Islam</li></ul> | — |
| **Hussein** | — | — | — | — | — | <ul><li>Review team CDP / Jira hours vs expected capacity</li></ul> | <ul><li><strong>Demo before QA</strong> — dev must walk tester through fix before handoff</li><li>Drive Hamed + Salah task-split session to reduce tester overload</li></ul> | <ul><li>Share <strong>Heba / Reem</strong> case detail this week</li><li>Hamed gradual PD allocation — max ~30% BO worst case</li></ul> |
| **Team** | <ul><li>Wave 1 unit-test sign-off (Islam + Michael) — blocked on Islam leave</li></ul> | — | — | — | <ul><li>Each person document <strong>specific access issue</strong> on Austin sheet</li></ul> | <ul><li>Log CDP with <strong>specific bullet points</strong> (hooks, agentic org flow, etc.)</li><li>Internal work → Excel until Jira restored; transfer when access returns</li></ul> | <ul><li>When reopening bugs, document <strong>reopen reason</strong></li></ul> | — |

---

## Completed / done

| Owner | Unit testing / code coverage | SOQL data test classes | Pre-UAT bugs & testing | Austin comments / client demo | Jira access — post-migration | CDP / time logging | Process — PR workflow & Jira comments | Leadership / capacity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Michael** | <ul><li>Islam's merged unit-test work <strong>on sandbox</strong> for review when he returns</li></ul> | — | <ul><li>[OC-9615](https://ontellus.atlassian.net/browse/OC-9615) prefill logout PII fix — deployed pddev, in QA</li></ul> | — | <ul><li>Logged OAuth / merge issues on Austin access sheet</li></ul> | — | — | — |
| **Islam** | <ul><li>Wave 1 unit tests merged to feature branch before leave (~10 classes; 3 still below 75%)</li></ul> | — | — | — | — | — | — | — |
| **Youssef** | — | — | <ul><li>Retested open bugs — <strong>stable</strong> on current fix batch</li><li>[OC-9566](https://ontellus.atlassian.net/browse/OC-9566) retest OK — provider cost visibility pending filter fix</li></ul> | — | <ul><li>Filled Austin access issue sheet</li></ul> | — | — | — |
| **Hamed** | — | — | <ul><li>ShareCare <strong>report scenario</strong> retest OK</li></ul> | — | <ul><li>Logged access issues on Austin sheet</li></ul> | — | — | — |
| **Salah** | — | — | — | — | — | <ul><li>Shared Excel time sheet for interim logging</li></ul> | — | — |
| **Hussein** | — | — | — | — | — | <ul><li>Ran capacity review — flagged Michael / Youssef / Islam / Hamed overload</li></ul> | <ul><li><strong>Decision:</strong> demo fix with tester before QA handoff</li></ul> | — |

---

## Decisions (context — not new actions)

- **Islam leave:** Out **2026-06-16 & 2026-06-17**; code review and coverage report follow-up deferred to next week.
- **Wave 1 UAT:** Missed **2026-06-15** target — Salah confirming slip and revised dates with Austin today; partnership / Printshop item may push further.
- **Van demo:** Still postponed to **Monday 2026-06-22** (unchanged).
- **Pre-UAT forecast:** Re-baseline **2026-06-17** — pending Austin confirmation on UAT wave dates.
- **ShareCare / RR:** Provider cost hidden on VF by invoice filter — Michael fixing **2026-06-16**; Hamed + Youssef unblocked after fix.
- **Demo before QA:** Dev must demo fix with tester before QA handoff to reduce ping-pong.
- **Jira access:** Still unresolved post-migration; interim logging via Excel until restored.
- **Hamed capacity:** Gradual shift toward **100% PD**; BO share to taper; task split with Salah needed.
- **Updox:** Deprioritized per Austin (unchanged).
