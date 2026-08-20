---
name: pmo-bug-closure-analysis
description: >-
  Perform a holistic post-closure analysis of a resolved/closed bug and publish a closure
  report. Reads the bug (a local defect file and/or its tracker issue, e.g. Jira), its
  requirement, story, acceptance criteria, ALL comments and the full status-transition
  changelog, related defects, and any other context you provide. Derives insights and
  metrics — validity (valid/invalid), root cause description, root cause category, reopen
  frequency, time-to-fix/cycle time, resolution, prevention/lessons — then posts (or updates
  in place on re-run) the summary as a comment on the bug and sets two tracker labels
  (validity + root-cause slug). Any field it cannot confidently extract is set to "Not Clear"
  so a human can fill it later. Use when the user asks to analyze a closed/resolved bug, run
  a post-mortem or root-cause analysis on a defect, generate a bug closure report, post a
  closure summary to a bug, or says "closure analysis", "bug post-mortem", or "RCA".
disable-model-invocation: true
---

# Bug Closure Analysis

Run a holistic post-closure analysis of a single resolved/closed bug, derive root-cause insights
and lifecycle metrics, write a local closure report, and post a concise closure summary as a
comment on the bug. The skill is tracker-agnostic; **Jira (Atlassian Cloud) is the worked example**
— substitute the equivalent operations of your tracker's MCP server or API.

**Core principle — never invent.** Every analysis field is either *evidenced* from the bug, its
comments, or its changelog, OR it is explicitly set to **`Not Clear`** so a human can fill it in
later. Never guess a root cause, a category, or a metric. "Not Clear" is a valid, expected output —
prefer it over a fabricated answer.

**Two classifications + two labels.** Every analysis decides (1) **validity** — is this a genuine
defect (`valid`) or not (`invalid`) — and (2) a single **root cause category** slug drawn from the
list that matches the validity verdict (see `references/root-cause-taxonomy.md`). The skill then sets
**two tracker labels** on the bug: the validity label and the root-cause slug.

**Idempotent — update, never duplicate.** Before posting, check whether a prior closure-analysis
comment already exists on the bug. If it does, **edit that comment and re-apply the labels with the
latest version of this analysis** instead of posting a new comment. One closure-analysis comment per
bug, always.

## Inputs

This skill is repo-layout agnostic and tracker-agnostic. You supply the bug reference and the context
to read; the skill never hardcodes board keys, field IDs, or project paths. Provide each input as a
**file path**, a **tracker key**, or **pasted content**, and name the integration to use.

| Input | How you provide it | Required? |
|-------|--------------------|-----------|
| **Bug reference** | A local defect id (e.g. `DEF-NNN`), a tracker key (e.g. `{board-key}-NNNN`), or a path to the defect `.md` file. | Yes |
| **Tracker integration** | Which MCP server or API talks to the tracker (e.g. an Atlassian MCP for Jira). Name it in chat. | Yes (to comment/label) |
| **Local defects location** | The folder holding defect files (conventionally `UAT/defects/`). Path or pasted content. | Optional |
| **Traceability context** | Story, requirements, decisions, and related-defect files the bug references. Provide paths or paste them. | Optional |
| **Credentials** | For direct REST calls, the skill reads tokens from **environment variables** you set — never from files in the repo. | Optional |

If neither a defect id, tracker key, nor file path is given, ask which bug to analyze. Traceability
inputs are optional — never block the analysis on them; mark what you cannot read as `Not Clear`.

## When NOT to run

- Bug is still **Open / In Progress** (not yet resolved/closed). Warn the user: a closure analysis
  needs a terminal state and a resolution. Offer to proceed anyway with most fields as `Not Clear`
  only if the user explicitly confirms.

## Input resolution

| Input | Action |
|-------|--------|
| `Analyze DEF-011` / a `DEF-NNN` id | Resolve to a local file in the defects location (e.g. `UAT/defects/DEF-NNN-*.md`); read its `tracking_id` for the tracker key |
| `Analyze {board-key}-NNNN` / a tracker key | Use the tracker issue as primary source; try to find a matching local defect file by `tracking_id` |
| A file path to a defect `.md` | Use it directly |
| "Closure analysis for {bug}" / "RCA for {bug}" / "post-mortem {bug}" | Same as above |
| "Analyze all closed defects" | Batch — iterate over resolved/closed defects (see Batch Mode) |

---

## Workflow

```
┌────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌────────────────────┐
│ 1. Resolve │ → │ 2. Gather    │ → │ 3. Holistic  │ → │ 4. Build     │ → │ 5. Publish/Update  │
│    the bug │   │    context   │   │    analysis  │   │    report    │   │   comment + labels │
└────────────┘   └──────────────┘   └──────────────┘   └──────────────┘   └────────────────────┘
```

### Step 1 — Resolve the Bug

1. Identify the local defect file and/or the tracker key from the user input (see Input resolution).
2. If only a tracker key is given, search the defects location for a file whose frontmatter
   `tracking_id` matches; if none, proceed tracker-only and note the local file is absent.
3. Confirm the bug is in a terminal state (Resolved / Closed / Done). If not, see "When NOT to run".

### Step 2 — Gather Context (read everything before analyzing)

Read each source that exists. Do **not** skip sources to save effort — closure analysis depends on
breadth. If context is large, split reads across sub-agents (per the context-preservation rule)
rather than dropping any source.

**A. The bug itself**
- **Local defect file** (e.g. `UAT/defects/DEF-NNN-*.md`) — all sections, especially Severity,
  Traceability, Description, Root Cause Analysis, Resolution, and the Changelog.
- **Tracker issue** — fetch the full issue. With the Jira MCP, call `jira_get_issue` with:
  - `fields: "*all"`
  - `expand: "changelog,renderedFields"`
  - `comment_limit: 100`
  This returns description, status, resolution, assignee, labels, components, custom fields,
  **all comments**, and the **full changelog** (status transitions with timestamps and authors).
- If the changelog is truncated, fetch the complete history (with Jira, `jira_batch_get_changelogs`
  with the issue key and `limit: -1`) to get every history entry.

**B. Traceability sources** (resolve from the defect's Traceability section or tracker links/labels)
- **Story** — the related story file and/or tracker story. Read its acceptance criteria and scope.
- **Requirements** — the requirements document — the FR/NFR/BR IDs the bug violated.
- **Decisions** — any decision/ADR record the bug relates to.
- **Related defects** — files referenced by the defect, plus a scan of the defects location for the
  same component/area to assess recurrence.

**C. Supporting context (read on demand when relevant)**
- Project/architecture notes — architecture, actors, components.
- Risk register — whether this bug realized a known risk.
- Evidence files referenced by the defect (do not open binary images; just note their presence).

### Step 3 — Holistic Analysis

Read `references/root-cause-taxonomy.md` (categories) and `references/metrics-guide.md` (how to
compute lifecycle metrics from the changelog) **before** filling the report.

Derive every field in the closure report. For each one, apply the **Evidence-or-Not-Clear rule**:

> If the value is directly stated, or can be computed deterministically from changelog timestamps,
> or is unambiguously implied by the evidence → fill it and cite where it came from.
> Otherwise → write exactly **`Not Clear`** (optionally followed by a short note on what's missing,
> e.g. `Not Clear — no fix commit/PR referenced in comments`).

Key derivations:

| Insight | Source | If absent |
|---------|--------|-----------|
| **Validity** (`valid` / `invalid`) | Did the closing evidence treat it as a genuine defect? (see taxonomy Step 1) | `Not Clear` |
| Root cause description | Defect Root Cause section, resolution comment, dev comments | `Not Clear` |
| Root cause **category** (exactly ONE) | Map evidence to the list **matching the validity verdict** in `references/root-cause-taxonomy.md` | `Not Clear` |
| Reopen frequency | Count reopen transitions in changelog (see metrics-guide) | `0` if changelog present & none found; `Not Clear` if no changelog |
| Time to fix / cycle time | Changelog timestamps (created → resolved, in-progress duration) | `Not Clear` |
| Time to first response / triage | First comment / first transition out of the backlog status | `Not Clear` |
| Resolution / Fix description | Defect Resolution section, resolution comment | `Not Clear` |
| Fixed in (PR/commit/version/build) | Comments, defect "Fixed In" | `Not Clear` |
| Verified in | Defect "Verified In Run", verification comment | `Not Clear` |
| Prevention / lessons learned | Inferred ONLY from evidenced root cause | `Not Clear` |

**Validity ↔ category coupling:** first decide validity, then pick the single root-cause slug from
the matching list (Valid list for `valid`, Invalid list for `invalid`). The category slug must belong
to the chosen validity's list — never mix. If validity is `Not Clear`, the category is `Not Clear`
too, and no labels are set.

Use `references/closure-report-template.md` for the full field list and exact formatting.

### Brevity rules (keep the output short)

- **Be concise and direct.** The analysis adds *insight*, not a retelling of the ticket.
- **Never restate fields that already live on the ticket** (severity, priority, assignee, labels,
  components, status). The reader can see those on the tracker — do not duplicate them in the report
  or comment. Reference them only if they are part of an insight.
- Assign **exactly one** root cause category — no primary/secondary split.
- Keep the holistic summary to **2–3 direct sentences**.

### Step 4 — Build the Closure Report

1. Write/refresh a local report file (conventionally):
   ```
   UAT/defects/closure-analysis/DEF-NNN-closure-analysis.md
   ```
   (Create the `closure-analysis/` folder if missing.) Use the template, include frontmatter
   (version 1.0, status `active`) and a Changelog section per your versioning convention.
2. Fill every field per Step 3. Render `Not Clear` fields plainly so they are easy to find later.
3. Add a short **"Fields needing human input"** checklist at the end listing every `Not Clear`
   field, so whoever follows up knows exactly what to complete.

### Step 5 — Publish/Update the Comment + Apply Labels

This step is **idempotent**: if a prior closure analysis already exists on the bug, update it instead
of creating a duplicate.

**5a — Detect a prior analysis.** From the comments already fetched in Step 2 (`comment_limit: 100`),
find an existing closure-analysis comment by looking for the stable marker
`<!-- closure-analysis -->` (or, as a fallback, a comment whose body starts with
`## 🔍 Bug Closure Analysis`). Note its comment id if found.

**5b — Post or edit the comment.** Use the **Comment Format** below — a compact version of the
report, not the whole file. Always include the marker and the `Not Clear` items under "Open items for
review".
- **No prior comment found** → add a new comment (Jira: `jira_add_comment` with `issue_key`, `body`).
- **Prior comment found** → edit it in place (Jira: `jira_edit_comment` with `issue_key`,
  `comment_id`, refreshed `body`). Do **not** add a second comment.

**5c — Apply the two labels.** Set exactly two labels on the bug — the validity label (`valid` /
`invalid`) and the root-cause slug — via the tracker's update operation (Jira: `jira_update_issue`):
1. Take the issue's current `labels` (from the Step 2 fetch).
2. Remove any label that belongs to the skill's two managed enumerated sets (validity set +
   root-cause slug set from `references/root-cause-taxonomy.md`) so stale labels from a previous run
   are cleared. Leave all other labels untouched.
3. Add the current validity label and root-cause slug.
4. Update the issue with `fields` = `{"labels": [<the merged list>]}`.
- If validity is `Not Clear`, do not add a validity label. If the category is `Not Clear`, do not add
  a root-cause label. (Still clear stale managed labels.)

**5d — Record & report.** Update the local report's Changelog (note whether the comment was created or
edited and the labels applied) and tell the user the comment id and the two labels.

- If `tracking_id` is empty / there is no tracker issue, skip 5b–5c, save the local report only, and
  tell the user the bug has not been pushed to the tracker yet.

---

## Comment Format

Posted as a new comment, or refreshed in place on re-run (Markdown). Keep it concise; the full detail
lives in the local report.

```markdown
<!-- closure-analysis -->
## 🔍 Bug Closure Analysis — {DEF-NNN} / {tracker key}

**Analyzed by:** {user or "Closure Analysis"} · **Date:** {YYYY-MM-DD}

### Verdict
- **Validity:** {`valid` / `invalid` / `Not Clear`}
- **Labels applied:** `{validity}`, `{root-cause-slug}`

### Summary
{2–3 direct sentences: what the bug was and how it was resolved. No restating ticket fields.}

### Root Cause
- **Description:** {root cause or `Not Clear`}
- **Category:** {single slug from the matching taxonomy list or `Not Clear`}

### Lifecycle Metrics
| Metric | Value |
|--------|-------|
| Reopen frequency | {N or `Not Clear`} |
| Time to fix (cycle time) | {duration or `Not Clear`} |
| Time in progress | {duration or `Not Clear`} |
| Time to first response | {duration or `Not Clear`} |

### Resolution
- **Fix:** {resolution summary or `Not Clear`}
- **Fixed in:** {PR/commit/version or `Not Clear`}
- **Verified in:** {run/build or `Not Clear`}

### Prevention / Lessons
{1–3 bullets, or `Not Clear`}

### ⚠️ Open items for review (please fill)
- [ ] {each `Not Clear` field}

_Generated by the Bug Closure Analysis skill. This comment is updated in place on re-runs. Items marked **Not Clear** could not be derived from the bug, its comments, or its history — please complete them._
```

> Keep the `<!-- closure-analysis -->` marker as the **first line** of the comment so future runs
> can find and update this exact comment instead of posting a duplicate.

---

## Batch Mode

When the user asks to analyze multiple closed bugs:

1. Scan the defects location (and/or query the tracker) for defects in a terminal state.
2. Present a table of candidates and confirm scope before processing.
3. **Choose execution mode by volume:**
   - **Small set (≤ 5 bugs)** → process **sequentially** in this agent (one bug fully analyzed,
     commented, and labeled before the next) to keep context bounded.
   - **Large set (> 5 bugs)** → **split across sub-agents via the `Task` tool, assigning a maximum of
     5 bugs per sub-agent.** Chunk the confirmed list into groups of ≤ 5 and launch one sub-agent per
     group (in parallel when the groups are independent). Give each sub-agent a self-contained prompt
     that names its exact bug list and instructs it to run this same skill end-to-end for each bug —
     gather context, analyze, set the two labels, and post/update the single closure comment. This
     follows the context-preservation rule (never crunch context — split instead).
4. Collect each sub-agent's results, then print one combined summary table:
   `DEF-NNN | Tracker | Validity | Root Cause Slug | Comment (new/updated) | Reopens | Cycle Time | #Not Clear`.

---

## Reference Files

| File | When to read |
|------|--------------|
| `references/root-cause-taxonomy.md` | **Always** — to decide validity (`valid`/`invalid`) and assign the single root-cause slug + the two labels |
| `references/metrics-guide.md` | **Always** — to compute reopen frequency, cycle time, and other metrics from the tracker changelog |
| `references/closure-report-template.md` | **Always** — the full local report structure and field formatting |

## Integration with Other Skills

| Skill | Interaction |
|-------|-------------|
| `testing-uat-defects` | Creates the defect file this skill analyzes; provides the Root Cause and Resolution sections. |
| `pmo-push-artifact` | Pushes the defect to the tracker and sets `tracking_id`; this skill needs that key to comment. |
| `pmo-reports-generation` | May consume closure reports for quality/RCA reporting. |

## Scope Boundaries

| In Scope | Out of Scope |
|----------|--------------|
| Read bug, comments, full changelog, story, requirements, decisions, related defects | Fixing or reopening the bug |
| Compute lifecycle metrics from history | Transitioning the bug's status |
| Decide validity + derive root cause category from evidence | Inventing a validity/root cause when evidence is absent (use `Not Clear`) |
| Set the two managed labels (validity + root-cause slug) | Removing or changing labels outside the two managed sets |
| Write a local closure report | Pushing the defect file as a new issue (→ `pmo-push-artifact`) |
| Post — or update in place — the single closure summary comment | Editing the description or comments other than the skill's own closure comment |
| Mark unknowns as `Not Clear` | Assigning blame to individuals |

## Safety Rules

1. **Never fabricate.** Any field not evidenced from the bug / comments / changelog is `Not Clear`.
   Validity, root cause category, and therefore labels follow the same rule — no label is set for a
   `Not Clear` value.
2. **Read before analyzing.** Gather all context sources in Step 2 first; never analyze from the
   title alone.
3. **One comment per bug — update in place.** Always check for an existing closure-analysis comment
   (marker `<!-- closure-analysis -->`) and edit it on re-run; never post a duplicate.
4. **Labels: only the two managed sets.** The skill may add/remove only the validity labels
   (`valid` / `invalid`) and the root-cause slugs from the taxonomy. Never touch any other label.
5. **No PHI/PII** in the report or comment — mask/redact any sensitive data per your compliance rules.
6. **No blame** — describe process/technical root cause, not individual fault.
7. **Limited tracker writes only** — the only permitted writes are: post/edit the single closure
   comment and set the two managed labels. Never transition status, edit the description, change other
   fields, or delete anything.
8. **Sub-agent batching.** For large batches (> 5 bugs), split across sub-agents with **max 5 bugs per
   sub-agent** rather than crunching context.
