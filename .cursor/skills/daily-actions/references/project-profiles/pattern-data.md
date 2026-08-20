# Project profile — Pattern Data (ChartSwap)

Use when extracting actions from **ChartSwap Daily Stand up** transcripts in this workspace.

## Paths

| Item | Path |
| --- | --- |
| Actions output | `Daily Actions/daily-actions-YYYY-MM-DD.md` |
| Transcript | `Transcript/ChartSwap Daily Stand up/ChartSwap-Daily-Stand-up-YYYY-MM-DD.docx` |
| Extractor | `.cursor/skills/pattern-data-daily-progress/scripts/extract_standup.py` |

## Header

```markdown
# Daily Actions

**Source:** [ChartSwap Daily Stand-up — YYYY-MM-DD](../Transcript/ChartSwap%20Daily%20Stand%20up/ChartSwap-Daily-Stand-up-YYYY-MM-DD.docx) · **As of:** YYYY-MM-DD · **Project:** Pattern Data
```

## Owner rows (standard order)

| Standup name | Owner row |
| --- | --- |
| Michael Girgis | **Michael** |
| Islam Fathy | **Islam** |
| Sarah Hassaan | **Sarah** |
| Youssef Yahiya | **Youssef** |
| Mohamed Hamed | **Hamed** |
| Mahmoud Salah | **Salah** |
| Mohamed Ahmed | **Hussein** (never "Ahmed") |
| Whole team / unspecified | **Team** |

## Category columns (standard set)

| Column | Standup themes |
| --- | --- |
| **Unit testing / code coverage** | Wave 1 tests, coverage %, missing classes, code review, sign-off |
| **SOQL data test classes** | CIOX/data test classes, sandbox data dependencies |
| **Pre-UAT bugs & testing** | Provider testing, bug fixes, retests, demos with dev, testing tracker |
| **Austin comments / client demo** | VF/transaction comments, Invoice S3, field removal, client demo prep |
| **Jira access — post-migration** | Atlassian migration, permissions, BO board access, IT escalation |
| **CDP / time logging** | CDP names, internal work vs Jira board, Excel time sheet, board tasks |
| **Process — PR workflow & Jira comments** | Feature-branch + PR adoption, reopen reason field, Jira comment policy |
| **Leadership / capacity** | Hours policy, standup logging rules, capacity / resourcing updates |

Jira epic: [OC-9223](https://ontellus.atlassian.net/browse/OC-9223) — link keys as `[OC-####](https://ontellus.atlassian.net/browse/OC-####)`.
