# Time conversion — 1d = 7h

Jira’s `timeSpent` display uses **8h per day**. This project treats **1d = 7h** when building daily time logs.

## Parse `timeSpent` strings

Split tokens like `1d 2h`, `6h`, `1h 30m`, `4m`:

| Token | Minutes |
|-------|---------|
| `Nd`  | N × 420 (7 × 60) |
| `Nh`  | N × 60 |
| `Nm`  | N |

Sum minutes, then format for output.

## Do not use `timeSpentSeconds` when `d` is present

Example: `1d 2h` → Jira stores `36000` seconds (10h at 8h/day). Correct value here: **9h** (7 + 2).

When the string has no `d`, `timeSpentSeconds` may be used as a cross-check.

## Output formatting

Prefer Jira-style labels:

- Whole hours: `11h`, `6h`, `1h`
- Mixed: `1h 30m`, `45m`
- Omit zero components (`1h` not `1h 0m`)

## Examples

| `timeSpent` | Converted |
|-------------|-----------|
| `2h` | 2h |
| `1d 2h` | 9h |
| `1d` | 7h |
| `6h` | 6h |
| `1h 30m` | 1h 30m |
| `4m` | 4m |

Two worklogs `2h` + `1d 2h` on the same day → **11h** total for that task.
