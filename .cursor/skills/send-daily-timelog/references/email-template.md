# Email template — Daily Time Log

## .eml headers (all messages)

```text
To: {email}
Subject: OC Daily Time Log — {D Mon YYYY} — {Full Name}   # omit " — {Full Name}" for full team reports (all-salah, all-hussein, all-nabawy)
MIME-Version: 1.0
Content-Type: text/html; charset=UTF-8
Content-Transfer-Encoding: quoted-printable

{html body}
```

## Per-assignee HTML

```html
<html><body style="font-family:Segoe UI,Arial,sans-serif;font-size:14px;color:#222;">
<h2 style="margin-bottom:4px;">OC Daily Time Log — {D Mon YYYY}</h2>
<p style="color:#555;margin-top:0;">Hi <strong>{FirstName}</strong>, your OC subtask work logged on <strong>{D Mon YYYY}</strong> (day only, not cumulative). <strong>1d = 7h.</strong></p>
<hr/>

<h3 style="color:#0066cc;">Your total</h3>
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;font-size:14px;">
<tr style="background:#f0f4f8;"><th>Assignee</th><th>Total</th></tr>
<tr style="font-weight:bold;"><td>{Full Name}</td><td>{total}</td></tr>
</table>

<h3 style="color:#0066cc;margin-top:24px;">Your tasks</h3>
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;font-size:14px;">
<tr style="background:#f0f4f8;"><th>Task</th><th>Time spent ({D Mon})</th></tr>
<!-- one row per task -->
<tr><td><a href="https://ontellus.atlassian.net/browse/OC-XXXX">OC-XXXX</a> — {summary}</td><td>{time}</td></tr>
</table>

<hr/>
<p style="color:#888;font-size:12px;margin-top:24px;">From Daily TimeLog/Daily-Time-Log-YYYY-MM-DD.md</p>
</body></html>
```

## Full team report HTML (Salah, Hussein, Nabawy)

Same HTML for all three files; only the **To** header differs. Same intro as **daily-time-log** markdown: team-wide totals table, then full detail table (Assignee | Task | Time spent).

```html
<p style="color:#555;margin-top:0;">Subtasks in the OC project with work logged on <strong>{D Mon YYYY}</strong>. Time reflects worklog entries for that day only (not cumulative task totals). <strong>1d = 7h.</strong></p>
```

Sections: **Daily total by assignee** (include **All** row), **Detail by task**.

## Worked example

See `Daily TimeLog/emails-2026-06-28/` in the repo (Islam, Michael, Sara, all-salah, all-hussein, all-nabawy).
