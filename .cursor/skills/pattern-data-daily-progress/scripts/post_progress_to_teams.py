#!/usr/bin/env python3
"""POST today's Pattern Data progress report as a Teams Adaptive Card.

Reads Daily Progress/pattern-data-delivery-progress-YYYY-MM-DD.md and POSTs a
Teams webhook envelope (type=message + attachments) whose content is an
Adaptive Card. Inlines the full report as TextBlocks — Teams cannot attach .md
or HTML. Loads repo-root .env.local if TEAMS_WEBHOOK_URL is not already in the
environment. Never print the webhook URL.

On HTTP 400, retries Adaptive Card as the JSON root (custom HTTP trigger +
Post adaptive card flows that call AdaptiveCard.FromJson on triggerBody()).

Usage (from repo root):
  python .cursor/skills/pattern-data-daily-progress/scripts/post_progress_to_teams.py --dry-run
  python .cursor/skills/pattern-data-daily-progress/scripts/post_progress_to_teams.py --pr-url URL
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

MAX_GLANCE = 1200
MAX_TEAM = 800
MAX_ACTIONS = 800
MAX_REPORT = 12000
TEXTBLOCK_CHUNK = 1800
MAX_CARD_BYTES = 22000
HTTP_TIMEOUT = 30


class _HTMLStripper(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._chunks: list[str] = []

    def handle_data(self, data: str) -> None:
        self._chunks.append(data)

    def get_text(self) -> str:
        return "".join(self._chunks)


def strip_html(text: str) -> str:
    parser = _HTMLStripper()
    parser.feed(text)
    parser.close()
    return parser.get_text()


def strip_md(text: str) -> str:
    text = strip_html(text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("**", "").replace("*", "")
    text = re.sub(r"`+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def html_lists_to_text(text: str) -> str:
    text = re.sub(r"<li[^>]*>", "- ", text, flags=re.I)
    text = re.sub(r"</li>", "\n", text, flags=re.I)
    text = re.sub(r"</?ul[^>]*>", "\n", text, flags=re.I)
    text = re.sub(r"</?ol[^>]*>", "\n", text, flags=re.I)
    return strip_html(text)


def markdown_to_card_text(markdown: str) -> str:
    """Flatten .md (including HTML lists/tables) into Adaptive Card TextBlock text.

    Teams flowbot cannot attach a file or render HTML inside the card.
    """
    lines: list[str] = []
    for raw in markdown.splitlines():
        stripped = raw.strip()
        if stripped == "---":
            continue
        if re.match(r"^\|?\s*[:\-| ]+\s*$", stripped):
            continue
        if stripped.startswith("|"):
            cells = [strip_md(c) for c in stripped.strip("|").split("|")]
            lines.append(" · ".join(c for c in cells if c))
            continue
        line = html_lists_to_text(raw)
        line = re.sub(r"^#{1,6}\s+", "", line)
        line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", line)
        line = line.replace("**", "")
        lines.append(line)
    text = "\n".join(lines)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def chunk_text(text: str, size: int) -> list[str]:
    if not text:
        return []
    chunks: list[str] = []
    remaining = text
    while remaining:
        if len(remaining) <= size:
            chunks.append(remaining)
            break
        split_at = remaining.rfind("\n", 0, size)
        if split_at < size // 2:
            split_at = size
        chunks.append(remaining[:split_at].rstrip())
        remaining = remaining[split_at:].lstrip("\n")
    return chunks


def load_env_local(repo: Path) -> None:
    """Load KEY=VALUE lines from .env.local without overriding existing env vars."""
    path = repo / ".env.local"
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def find_repo_root() -> Path:
    here = Path.cwd().resolve()
    for candidate in [here, *here.parents]:
        if (candidate / "Daily Progress").is_dir() and (candidate / "AGENTS.md").is_file():
            return candidate
    return Path(__file__).resolve().parents[4]


def section_body(markdown: str, heading: str) -> str:
    pattern = re.compile(
        rf"^##[^\n]*{re.escape(heading)}[^\n]*\n(.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    match = pattern.search(markdown)
    return match.group(1).strip() if match else ""


def parse_md_table(block: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    lines = [ln.strip() for ln in block.splitlines() if ln.strip().startswith("|")]
    if len(lines) < 2:
        return rows
    headers = [strip_md(c) for c in lines[0].strip("|").split("|")]
    for line in lines[1:]:
        if re.match(r"^\|?\s*:?-{3,}", line):
            continue
        cells = [strip_md(c) for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        row = {headers[i]: cells[i] if i < len(cells) else "" for i in range(len(headers))}
        rows.append(row)
    return rows


def truncate(text: str, limit: int) -> str:
    text = text.strip()
    if len(text) <= limit:
        return text
    return text[: max(0, limit - 1)].rstrip() + "…"


def as_of_date(markdown: str, fallback: str) -> str:
    match = re.search(r"\*\*As of:\*\*\s*(\d{4}-\d{2}-\d{2})", markdown)
    return match.group(1) if match else fallback


def uat_ready(markdown: str) -> str:
    match = re.search(r"UAT-ready progress:\*\*\s*\*\*([0-9]+/[0-9]+)", markdown)
    if match:
        return match.group(1)
    match = re.search(r"\*\*(\d+/\d+)\*\* features UAT-ready", markdown)
    return match.group(1) if match else "—"


def format_glance(rows: list[dict[str, str]]) -> str:
    lines: list[str] = []
    for row in rows:
        phase = row.get("Phase") or next(iter(row.values()), "")
        status = row.get("Status", "")
        notes = row.get("Notes") or row.get("What's left") or ""
        bit = f"{phase} — {status}" if status else phase
        if notes:
            bit += f": {notes}"
        lines.append(bit)
    return "\n".join(lines)


def format_named_table(rows: list[dict[str, str]], name_keys: tuple[str, ...], value_key: str) -> str:
    lines: list[str] = []
    for row in rows:
        name = ""
        for key in name_keys:
            if row.get(key):
                name = row[key]
                break
        if not name:
            name = next(iter(row.values()), "")
        value = row.get(value_key, "")
        lines.append(f"{name}: {value}" if value else name)
    return "\n".join(lines)


def build_adaptive_card(payload: dict[str, str]) -> dict:
    facts = [
        {"title": "As of", "value": payload["asOf"]},
        {"title": "UAT-ready", "value": payload["uatReady"]},
    ]
    body: list[dict] = [
        {
            "type": "TextBlock",
            "size": "Large",
            "weight": "Bolder",
            "text": payload["title"],
            "wrap": True,
        },
        {"type": "FactSet", "facts": facts},
        {
            "type": "TextBlock",
            "weight": "Bolder",
            "text": "Status at a glance",
            "spacing": "Medium",
        },
        {"type": "TextBlock", "text": payload["glance"] or "—", "wrap": True},
        {
            "type": "TextBlock",
            "weight": "Bolder",
            "text": "Team focus",
            "spacing": "Medium",
        },
        {"type": "TextBlock", "text": payload["teamFocus"] or "—", "wrap": True},
        {
            "type": "TextBlock",
            "weight": "Bolder",
            "text": "Open actions",
            "spacing": "Medium",
        },
        {"type": "TextBlock", "text": payload["actions"] or "—", "wrap": True},
        {
            "type": "TextBlock",
            "size": "Small",
            "text": payload["filePath"],
            "wrap": True,
            "spacing": "Medium",
        },
        {
            "type": "TextBlock",
            "weight": "Bolder",
            "text": "Full report",
            "spacing": "Large",
        },
    ]
    for chunk in chunk_text(payload.get("reportText", ""), TEXTBLOCK_CHUNK):
        body.append({"type": "TextBlock", "text": chunk or "—", "wrap": True, "spacing": "Small"})
    card: dict = {
        "type": "AdaptiveCard",
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2",
        "body": body,
    }
    if payload.get("prUrl"):
        card["actions"] = [
            {"type": "Action.OpenUrl", "title": "Open PR (full report)", "url": payload["prUrl"]}
        ]
    return card


def shrink_payload(fields: dict[str, str]) -> dict[str, str]:
    fields = dict(fields)
    for glance_limit, team_limit, actions_limit in (
        (MAX_GLANCE, MAX_TEAM, MAX_ACTIONS),
        (800, 500, 500),
        (400, 300, 300),
        (200, 150, 150),
    ):
        fields["glance"] = truncate(fields.get("glance", ""), glance_limit)
        fields["teamFocus"] = truncate(fields.get("teamFocus", ""), team_limit)
        fields["actions"] = truncate(fields.get("actions", ""), actions_limit)
        fields["reportText"] = truncate(fields.get("reportText", ""), MAX_REPORT if glance_limit == MAX_GLANCE else max(800, glance_limit * 8))
        encoded = json.dumps(build_body(fields), ensure_ascii=False).encode("utf-8")
        if len(encoded) <= MAX_CARD_BYTES:
            return fields
    return fields


def build_adaptive_card_root(fields: dict[str, str]) -> dict:
    """Adaptive Card object (used inside the Teams envelope, and as a 400 fallback)."""
    return build_adaptive_card(fields)


def wrap_teams_message(card: dict) -> dict:
    """Official Teams / Power Automate webhook envelope.

    Workflows that use "When a Teams webhook request is received" (or Send each
    adaptive card over triggerBody().attachments) return HTTP 400 if the root
    JSON is a raw AdaptiveCard instead of type=message.
    """
    return {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "contentUrl": None,
                "content": card,
            }
        ],
    }


def build_body(fields: dict[str, str]) -> dict:
    return wrap_teams_message(build_adaptive_card_root(fields))


def sanitize_error(text: str) -> str:
    """Strip URLs and signatures so 400 bodies never echo the webhook."""
    text = re.sub(r"https://[^\s\"']+", "[url]", text)
    text = re.sub(r"(?i)sig=[^&\s\"']+", "sig=[redacted]", text)
    return text[:500]


def post_json(url: str, body: dict) -> int:
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
            return int(resp.status)
    except urllib.error.HTTPError as exc:
        detail = sanitize_error(exc.read().decode("utf-8", errors="replace"))
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from None
    except urllib.error.URLError:
        raise RuntimeError("network error") from None


def post_card(url: str, fields: dict[str, str]) -> int:
    card = build_adaptive_card_root(fields)
    try:
        return post_json(url, wrap_teams_message(card))
    except RuntimeError as first:
        if not str(first).startswith("HTTP 400"):
            raise
        # Custom HTTP + Post-adaptive-card flows want AdaptiveCard as the root.
        return post_json(url, card)


def resolve_report(repo: Path, report_date: str, explicit: Path | None) -> Path:
    if explicit:
        path = explicit if explicit.is_absolute() else repo / explicit
        return path
    return repo / "Daily Progress" / f"pattern-data-delivery-progress-{report_date}.md"


def build_fields(markdown: str, report_path: Path, report_date: str, pr_url: str) -> dict[str, str]:
    glance_rows = parse_md_table(section_body(markdown, "Status at a glance"))
    team_rows = parse_md_table(section_body(markdown, "Team focus"))
    action_rows = parse_md_table(section_body(markdown, "Standup action items"))
    fields = {
        "title": "Pattern Data — delivery progress",
        "asOf": as_of_date(markdown, report_date),
        "uatReady": uat_ready(markdown),
        "glance": format_glance(glance_rows),
        "teamFocus": format_named_table(team_rows, ("Member",), "Focus"),
        "actions": format_named_table(action_rows, ("Owner",), "Action"),
        "prUrl": pr_url,
        "filePath": report_path.as_posix() if report_path.is_absolute() else str(report_path),
        "reportText": markdown_to_card_text(markdown),
    }
    try:
        fields["filePath"] = report_path.resolve().relative_to(find_repo_root()).as_posix()
    except ValueError:
        fields["filePath"] = report_path.name
    return shrink_payload(fields)


def main() -> None:
    parser = argparse.ArgumentParser(description="POST Pattern Data progress summary to Teams via Power Automate.")
    parser.add_argument("--date", help="Report date YYYY-MM-DD (default: today)")
    parser.add_argument("--file", type=Path, help="Explicit progress markdown path")
    parser.add_argument("--pr-url", default="", help="Pull request URL for the Open PR button")
    parser.add_argument("--webhook-url", default="", help="Override TEAMS_WEBHOOK_URL (do not log this)")
    parser.add_argument("--dry-run", action="store_true", help="Print JSON payload; do not POST")
    args = parser.parse_args()

    repo = find_repo_root()
    load_env_local(repo)
    report_date = args.date or date.today().isoformat()
    report_path = resolve_report(repo, report_date, args.file)
    if not report_path.is_file():
        print(f"Progress report not found: {report_path}", file=sys.stderr)
        sys.exit(2)

    markdown = report_path.read_text(encoding="utf-8")
    fields = build_fields(markdown, report_path, report_date, args.pr_url)
    body = build_body(fields)

    if args.dry_run:
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except (AttributeError, OSError):
            pass
        json.dump(body, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return

    webhook = args.webhook_url or os.environ.get("TEAMS_WEBHOOK_URL", "").strip()
    if not webhook:
        print(
            "TEAMS_WEBHOOK_URL is not set. Add it to .env.local (gitignored) or a Cloud Agent secret; do not commit it.",
            file=sys.stderr,
        )
        sys.exit(2)

    try:
        status = post_card(webhook, fields)
    except RuntimeError as exc:
        raise SystemExit(f"Teams webhook failed: {exc}") from exc
    print(f"Posted progress card for {fields['asOf']} (HTTP {status})")


if __name__ == "__main__":
    main()
