#!/usr/bin/env python3
"""Post today's Pattern Data progress report summary to Teams.

Reads TEAMS_WEBHOOK_URL from the environment. Never prints, logs, or
commits the webhook URL.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]


def _progress_path_for_today() -> Path:
    today = date.today().isoformat()
    return REPO_ROOT / "Daily Progress" / f"pattern-data-delivery-progress-{today}.md"


def _extract_summary(markdown: str) -> tuple[str, str, str]:
    as_of = "unknown"
    m = re.search(r"\*\*As of:\*\*\s*(\d{4}-\d{2}-\d{2})", markdown)
    if m:
        as_of = m.group(1)

    uat = "n/a"
    m = re.search(r"\*\*(\d+/\d+)\*\*\s+features UAT-ready", markdown)
    if m:
        uat = m.group(1)

    austin = "carried forward"
    m = re.search(
        r"## Deployment plan \(Austin\).*?\n\| 1\s+\|\s+(.+?)\s+\|",
        markdown,
        re.DOTALL,
    )
    if m:
        austin = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", m.group(1)).strip()

    return as_of, uat, austin


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Post Pattern Data daily progress to Teams (webhook from env)."
    )
    parser.add_argument("--pr-url", required=True, help="Pull request URL to include in the post")
    args = parser.parse_args()

    webhook = os.environ.get("TEAMS_WEBHOOK_URL", "").strip()
    if not webhook:
        print("TEAMS_WEBHOOK_URL is not set; skipping Teams post.", file=sys.stderr)
        return 1

    progress_path = _progress_path_for_today()
    if not progress_path.is_file():
        print(f"Progress file not found: {progress_path}", file=sys.stderr)
        return 1

    markdown = progress_path.read_text(encoding="utf-8")
    as_of, uat, austin = _extract_summary(markdown)
    rel = progress_path.relative_to(REPO_ROOT)

    text = (
        f"**Pattern Data daily progress** ({as_of}) — Jira-only weekday sync\n\n"
        f"- File: `{rel}`\n"
        f"- UAT-ready: **{uat}**\n"
        f"- Austin priority 1: {austin}\n"
        f"- PR: {args.pr_url}\n\n"
        "Amr: please post the full progress markdown to Teams after standup "
        "(source file attached)."
    )

    payload = json.dumps({"text": text}).encode("utf-8")
    request = urllib.request.Request(
        webhook,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=30, context=ssl.create_default_context()) as resp:
            status = resp.status
            body = resp.read(256)
    except urllib.error.HTTPError as exc:
        print(f"Teams post failed: HTTP {exc.code}", file=sys.stderr)
        return 1
    except urllib.error.URLError:
        print("Teams post failed: network error", file=sys.stderr)
        return 1

    if status >= 300:
        print(f"Teams post failed: HTTP {status}", file=sys.stderr)
        return 1

    print("Teams post succeeded.")
    if body:
        # Incoming webhooks typically return "1"; do not echo request URL.
        print(f"Teams response: {body.decode('utf-8', errors='replace')[:80]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
