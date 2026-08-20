---
name: send-daily-timelog
description: >-
  Generate HTML .eml files from an OC daily time log (one per assignee plus
  full team reports for Salah, Hussein, and Nabawy) and send via Outlook on Windows. Use when the
  user asks to email the time log, send daily timelog reminders, generate
  per-member time log emails, or send-daily-timelog.
disable-model-invocation: true
---

# Send Daily Time Log Emails

Turn `Daily TimeLog/Daily-Time-Log-YYYY-MM-DD.md` into per-assignee HTML emails, store them under `Daily TimeLog/emails-YYYY-MM-DD/`, and optionally send through Outlook.

**Prerequisite:** the dated markdown must exist. If missing, run **daily-time-log** first.

## Project paths

| Item | Path |
|------|------|
| Source report | `Daily TimeLog/Daily-Time-Log-YYYY-MM-DD.md` |
| Email output folder | `Daily TimeLog/emails-YYYY-MM-DD/` |
| Per-assignee file | `Daily-Time-Log-YYYY-MM-DD-{slug}.eml` |
| Full team report (Salah) | `Daily-Time-Log-YYYY-MM-DD-all-salah.eml` |
| Full team report (Hussein) | `Daily-Time-Log-YYYY-MM-DD-all-hussein.eml` |
| Full team report (Nabawy) | `Daily-Time-Log-YYYY-MM-DD-all-nabawy.eml` |
| Send script | `.cursor/skills/send-daily-timelog/scripts/send-emails.ps1` |

## Workflow

```
- [ ] 1. Determine target date (default: same date as latest time log or yesterday)
- [ ] 2. Read Daily-Time-Log-YYYY-MM-DD.md — parse assignees, totals, detail rows
- [ ] 3. Create emails-YYYY-MM-DD/ and write .eml files (one per assignee + all-salah + all-hussein + all-nabawy)
- [ ] 4. Send if requested (scripts/send-emails.ps1)
- [ ] 5. Report paths, recipients, and send status
```

### Step 1 — Target date

- **Default:** yesterday (match **daily-time-log** default) or the date the user names.
- Use the same `YYYY-MM-DD` in folder name, filenames, and email copy.

### Step 2 — Parse the markdown

From the source file:

1. **Daily total by assignee** — map `{displayName} → {total}`; skip the **All** row for per-person emails.
2. **Detail by task** — group rows by assignee: task link text, issue key, summary, time spent.

Date label for subjects and headers: `D Mon YYYY` (e.g. `22 Jun 2026`). Short column header: `(22 Jun)`.

### Step 3 — Generate .eml files

Create `Daily TimeLog/emails-YYYY-MM-DD/` if missing. Write or overwrite files; do not append.

**Per assignee** — one file each, containing only that person's total and task rows. Layout: [references/email-template.md](references/email-template.md).

**Full team reports** — same HTML for all three (totals + all detail rows; layout in [references/email-template.md](references/email-template.md)):

| File | To |
|------|-----|
| `Daily-Time-Log-YYYY-MM-DD-all-salah.eml` | `mahmoud.salah@integrant.com` |
| `Daily-Time-Log-YYYY-MM-DD-all-hussein.eml` | `Mohamed.Ahmed@integrant.com` (Hussein) |
| `Daily-Time-Log-YYYY-MM-DD-all-nabawy.eml` | `mnabawy@integrant.com` (Nabawy) |

**Recipients:** resolve per-assignee addresses from [references/recipient-map.md](references/recipient-map.md). Unknown assignees → `firstname.lastname@integrant.com` from Jira `displayName`; add confirmed addresses to the map.

**Filename slug:** lowercase, hyphenated display name (`Michael Girgis` → `michael-girgis`).

**HTML rules:**

- Escape `&` in summaries as `&amp;`.
- Jira links: `https://ontellus.atlassian.net/browse/OC-XXXX`.
- Greeting uses standup first name (`Hi **Michael**`) — see recipient map for overrides.
- Footer: `From Daily TimeLog/Daily-Time-Log-YYYY-MM-DD.md`.

If no assignees logged time, still write `all-salah.eml`, `all-hussein.eml`, and `all-nabawy.eml` with empty-state copy; skip per-person files.

### Step 4 — Send (when requested)

Run from project root — **always** use the script file; never inline `powershell -Command` with `$variables` (PowerShell strips them).

**All emails in folder:**

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ".cursor/skills/send-daily-timelog/scripts/send-emails.ps1" -EmlDir "Daily TimeLog/emails-YYYY-MM-DD"
```

**Single file** (e.g. after correcting an address):

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ".cursor/skills/send-daily-timelog/scripts/send-emails.ps1" -File "Daily TimeLog/emails-YYYY-MM-DD/Daily-Time-Log-YYYY-MM-DD-sara-hassan.eml"
```

**Outlook behavior:**

- Script uses Outlook COM (`GetActiveObject` then `New-Object`).
- First run may show **Programmatic Access Security** — user must click **Allow**.
- If send hangs >60s, stop the process; open drafts with `Start-Process` on each `.eml` and ask the user to click **Send**.
- Confirm in Outlook **Sent Items** when possible.

**Generate-only:** stop after Step 3 unless the user asks to send.

### Step 5 — Reply

Include:

1. Folder path and list of `.eml` files created or updated
2. Table of assignee → email → total
3. Send status per file (Sent / Failed / Draft opened)
4. Note if any address used the default `@integrant.com` pattern and should be verified

## Additional resources

- [references/email-template.md](references/email-template.md) — .eml headers and HTML structure
- [references/recipient-map.md](references/recipient-map.md) — confirmed Integrant addresses and greeting names
