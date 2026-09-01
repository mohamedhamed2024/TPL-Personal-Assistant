#!/usr/bin/env python3
"""POST today's Pattern Data progress report as a Teams Adaptive Card.

Reads Daily Progress/pattern-data-delivery-progress-YYYY-MM-DD.md and builds a
full-width Adaptive Card 1.5 (targetWidth VeryWide + msteams Full) with native
Table elements, headings, lists, checklists, and links. Skips the Standup action
items section. Posts via TEAMS_WEBHOOK_URL (Power Automate incoming webhook);
splits into multiple messages when the payload exceeds the webhook size cap.

Loads repo-root .env.local if TEAMS_WEBHOOK_URL is not already in the environment.
Never print the webhook URL.

Usage (from repo root):
  py -3 .cursor/skills/pattern-data-daily-progress/scripts/post_progress_to_teams.py
  py -3 .cursor/skills/pattern-data-daily-progress/scripts/post_progress_to_teams.py --dry-run
  py -3 .cursor/skills/pattern-data-daily-progress/scripts/post_progress_to_teams.py --export-card
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

WEBHOOK_MAX_BYTES = 27000
HTTP_TIMEOUT = 30
POST_DELAY_SEC = 2.0
CELL_SOFT_LIMIT = 800
TEXTBLOCK_CHUNK = 1800

HEADING_SIZES = {1: "ExtraLarge", 2: "Large", 3: "Medium", 4: "Medium", 5: "Small", 6: "Small"}
SKIP_SECTIONS_FOR_CARD = ("standup action items", "how to read this report")
WIDE_TABLE_HINT = 5
TRACKER_MERGE_KEYS = frozenset(
    {
        "code review (pr)",
        "deploy packages",
        "client wordings",
        "pd sandbox",
        "uat sandbox",
    }
)
TRACKER_MERGE_LABELS = {
    "code review (pr)": "PR",
    "deploy packages": "Packages",
    "client wordings": "Wordings",
    "pd sandbox": "PD sandbox",
    "uat sandbox": "UAT sandbox",
}
TRACKER_MERGE_COLUMN = "Delivery gates"
ITALIC_RE = re.compile(r"(?<!\*)\*(?!\*)([^*]+?)(?<!\*)\*(?!\*)")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
UL_RE = re.compile(r"^([-*+])\s+(.*)$")
OL_RE = re.compile(r"^(\d+)[.)]\s+(.*)$")
TASK_RE = re.compile(r"^\[([ xX])\]\s+(.*)$")
HR_RE = re.compile(r"^(-{3,}|\*{3,}|_{3,})$")
TABLE_SEP_RE = re.compile(r"^:?-{3,}:?$")
FENCE_RE = re.compile(r"^```(\w*)\s*$")
DVI_URL = "https://datavant.atlassian.net/browse/DVI-1086"


def rewrite_relative_links(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        label, url = match.group(1), match.group(2).strip()
        if url.startswith(("http://", "https://", "mailto:")):
            return match.group(0)
        return label

    return LINK_RE.sub(repl, text)


def html_lists_to_ac_markdown(text: str) -> str:
    text = re.sub(r"<li[^>]*>", "\r- ", text, flags=re.I)
    text = re.sub(r"</li>", "", text, flags=re.I)
    text = re.sub(r"</?[uo]l[^>]*>", "", text, flags=re.I)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"</p>", "\n", text, flags=re.I)
    text = re.sub(r"<p[^>]*>", "", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(text).strip()


def to_ac_markdown(text: str) -> str:
    """Keep Teams TextBlock markdown (**bold**, _italic_, [links](url), lists)."""
    text = html_lists_to_ac_markdown(text)
    text = rewrite_relative_links(text)
    text = ITALIC_RE.sub(r"_\1_", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def md_inline_to_html(text: str) -> str:
    text = rewrite_relative_links(text)

    protected: list[str] = []

    def stash(chunk: str) -> str:
        protected.append(chunk)
        return f"\x00{len(protected) - 1}\x00"

    def protect_tag(match: re.Match[str]) -> str:
        return stash(match.group(0))

    text = re.sub(r"</?(?:ul|ol|li|br|p)[^>]*>", protect_tag, text, flags=re.I)

    def link_repl(match: re.Match[str]) -> str:
        label = html.escape(match.group(1))
        url = html.escape(match.group(2), quote=True)
        return stash(f'<a href="{url}">{label}</a>')

    text = LINK_RE.sub(link_repl, text)

    def bold_repl(match: re.Match[str]) -> str:
        return stash(f"<strong>{html.escape(match.group(1))}</strong>")

    text = re.sub(r"\*\*(.+?)\*\*", bold_repl, text)
    text = ITALIC_RE.sub(lambda m: stash(f"<em>{html.escape(m.group(1))}</em>"), text)
    text = html.escape(text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: protected[int(m.group(1))], text)
    return text


def truncate(text: str, limit: int) -> str:
    text = text.strip()
    if len(text) <= limit:
        return text
    return text[: max(0, limit - 1)].rstrip() + "…"


@dataclass
class Block:
    kind: str
    text: str = ""
    level: int = 0
    language: str = ""
    ordered: bool = False
    items: list[str] = field(default_factory=list)
    headers: list[str] = field(default_factory=list)
    rows: list[list[str]] = field(default_factory=list)


def _is_table_separator(line: str) -> bool:
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return bool(cells) and all(TABLE_SEP_RE.match(c.replace(" ", "")) for c in cells)


def _split_table_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _collect_list(lines: list[str], start: int) -> tuple[Block, int]:
    items: list[str] = []
    ordered = bool(OL_RE.match(lines[start].strip()))
    i = start
    while i < len(lines):
        stripped = lines[i].strip()
        if not stripped:
            break
        ul = UL_RE.match(stripped)
        ol = OL_RE.match(stripped)
        if ul:
            body = ul.group(2)
            task = TASK_RE.match(body)
            if task:
                mark = "☑" if task.group(1).lower() == "x" else "☐"
                items.append(f"{mark} {task.group(2)}")
            else:
                items.append(body)
        elif ol and ordered:
            items.append(ol.group(2))
        elif i > start and not ul and not ol and lines[i].startswith((" ", "\t")):
            items[-1] = items[-1] + " " + stripped
        else:
            break
        i += 1
    return Block(kind="list", ordered=ordered, items=items), i


def parse_blocks(markdown: str) -> list[Block]:
    lines = markdown.replace("\r\n", "\n").split("\n")
    blocks: list[Block] = []
    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        if not stripped:
            i += 1
            continue

        fence = FENCE_RE.match(stripped)
        if fence:
            lang = fence.group(1) or "PlainText"
            i += 1
            collected: list[str] = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                collected.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            blocks.append(Block(kind="code", text="\n".join(collected), language=lang))
            continue

        heading = HEADING_RE.match(stripped)
        if heading:
            blocks.append(Block(kind="heading", level=len(heading.group(1)), text=heading.group(2).strip()))
            i += 1
            continue

        if HR_RE.match(stripped):
            blocks.append(Block(kind="hr"))
            i += 1
            continue

        if stripped.startswith(">"):
            quoted: list[str] = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quoted.append(re.sub(r"^>\s?", "", lines[i].strip()))
                i += 1
            blocks.append(Block(kind="quote", text="\n".join(quoted)))
            continue

        if stripped.startswith("|"):
            table_lines: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            rows_raw = [_split_table_row(ln) for ln in table_lines if not _is_table_separator(ln)]
            if rows_raw:
                headers = rows_raw[0]
                width = len(headers)
                data = [row + [""] * (width - len(row)) for row in rows_raw[1:]]
                data = [row[:width] for row in data]
                blocks.append(Block(kind="table", headers=headers, rows=data))
            continue

        if UL_RE.match(stripped) or OL_RE.match(stripped):
            block, i = _collect_list(lines, i)
            blocks.append(block)
            continue

        para: list[str] = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt:
                break
            if (
                HEADING_RE.match(nxt)
                or HR_RE.match(nxt)
                or nxt.startswith("|")
                or nxt.startswith(">")
                or nxt.startswith("```")
                or UL_RE.match(nxt)
                or OL_RE.match(nxt)
            ):
                break
            para.append(nxt)
            i += 1
        blocks.append(Block(kind="para", text=" ".join(para)))
    return blocks


def _textblock(
    text: str,
    *,
    size: str | None = None,
    weight: str | None = None,
    spacing: str | None = None,
    subtle: bool = False,
    separator: bool = False,
    font: str | None = None,
) -> dict[str, Any]:
    block: dict[str, Any] = {"type": "TextBlock", "text": text or "—", "wrap": True}
    if size:
        block["size"] = size
    if weight:
        block["weight"] = weight
    if spacing:
        block["spacing"] = spacing
    if subtle:
        block["isSubtle"] = True
    if separator:
        block["separator"] = True
    if font:
        block["fontType"] = font
    return block


def _column_widths(headers: list[str]) -> list[dict[str, Any]]:
    weights: list[int] = []
    for header in headers:
        key = header.lower().replace("…", "").strip()
        if key in {
            "next step",
            "notes",
            "what's done",
            "what's left",
            "focus",
            "action",
            "it means",
            "risk / challenge",
            "mitigation",
            "feature / story",
            "status",
            "environment",
            "delivery gates",
        }:
            weights.append(4)
        elif key in {"story", "phase", "sub-task", "owner", "#", "assignee", "jira status"}:
            weights.append(3)
        else:
            weights.append(2)
    return [{"width": w} for w in weights]


def _table_cell(text: str, *, header: bool = False, small: bool = False) -> dict[str, Any]:
    item = _textblock(
        to_ac_markdown(text) or "—",
        size="Small" if small or header else None,
        weight="Bolder" if header else None,
    )
    cell: dict[str, Any] = {"type": "TableCell", "items": [item], "verticalContentAlignment": "Top"}
    if header:
        cell["style"] = "emphasis"
    return cell


def _table_element(block: Block, *, fallback_text: str) -> dict[str, Any]:
    wide = len(block.headers) >= WIDE_TABLE_HINT
    header_row = {
        "type": "TableRow",
        "cells": [_table_cell(h, header=True, small=wide) for h in block.headers],
    }
    data_rows = [
        {"type": "TableRow", "cells": [_table_cell(c, small=wide) for c in row]}
        for row in block.rows
    ]
    table: dict[str, Any] = {
        "type": "Table",
        "gridStyle": "accent",
        "firstRowAsHeader": True,
        "showGridLines": True,
        "columns": _column_widths(block.headers),
        "rows": [header_row, *data_rows],
        "spacing": "Small",
        "fallback": _textblock(fallback_text, spacing="Small"),
    }
    return {
        "type": "Container",
        "bleed": True,
        "items": [table],
    }


def _flatten_table(block: Block) -> str:
    lines = [" · ".join(to_ac_markdown(h) for h in block.headers)]
    for row in block.rows:
        lines.append(" · ".join(to_ac_markdown(c) for c in row if to_ac_markdown(c)))
    return "\n".join(lines)


def _list_text(block: Block) -> str:
    lines: list[str] = []
    for idx, item in enumerate(block.items, start=1):
        body = to_ac_markdown(item)
        prefix = f"{idx}. " if block.ordered else "- "
        if body.startswith(("☐ ", "☑ ")):
            prefix = "- "
        lines.append(prefix + body)
    return "\r".join(lines)


def blocks_to_ac_elements(blocks: list[Block]) -> list[dict[str, Any]]:
    elements: list[dict[str, Any]] = []
    for block in blocks:
        if block.kind == "heading":
            elements.append(
                _textblock(
                    to_ac_markdown(block.text),
                    size=HEADING_SIZES.get(block.level, "Medium"),
                    weight="Bolder",
                    spacing="Large" if block.level <= 2 else "Medium",
                    separator=block.level == 2,
                )
            )
        elif block.kind == "para":
            for chunk in chunk_text(to_ac_markdown(block.text), TEXTBLOCK_CHUNK):
                elements.append(_textblock(chunk, spacing="Small"))
        elif block.kind == "list":
            elements.append(_textblock(_list_text(block), spacing="Small"))
        elif block.kind == "table":
            elements.append(_table_element(block, fallback_text=_flatten_table(block)))
        elif block.kind == "quote":
            elements.append(
                {
                    "type": "Container",
                    "style": "emphasis",
                    "spacing": "Small",
                    "items": [_textblock(to_ac_markdown(block.text), subtle=True)],
                }
            )
        elif block.kind == "code":
            elements.append(
                {
                    "type": "CodeBlock",
                    "language": block.language or "PlainText",
                    "codeSnippet": block.text,
                    "fallback": _textblock(block.text or "—", font="Monospace"),
                }
            )
        elif block.kind == "hr":
            elements.append(_textblock(" ", separator=True, spacing="Medium"))
    return elements


def blocks_to_html(blocks: list[Block]) -> str:
    parts: list[str] = []
    for block in blocks:
        if block.kind == "heading":
            tag = f"h{min(block.level, 3)}"
            parts.append(f"<{tag}>{md_inline_to_html(block.text)}</{tag}>")
        elif block.kind == "para":
            parts.append(f"<p>{md_inline_to_html(block.text)}</p>")
        elif block.kind == "list":
            tag = "ol" if block.ordered else "ul"
            items = "".join(f"<li>{md_inline_to_html(item)}</li>" for item in block.items)
            parts.append(f"<{tag}>{items}</{tag}>")
        elif block.kind == "table":
            head = "".join(f"<th>{md_inline_to_html(h)}</th>" for h in block.headers)
            body_rows = []
            for row in block.rows:
                tds = "".join(f"<td>{md_inline_to_html(c)}</td>" for c in row)
                body_rows.append(f"<tr>{tds}</tr>")
            parts.append(f"<table><thead><tr>{head}</tr></thead><tbody>{''.join(body_rows)}</tbody></table>")
        elif block.kind == "quote":
            parts.append(f"<blockquote>{md_inline_to_html(block.text)}</blockquote>")
        elif block.kind == "code":
            parts.append(f"<pre><code>{html.escape(block.text)}</code></pre>")
        elif block.kind == "hr":
            parts.append("<hr/>")
    return "\n".join(parts)


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


def drop_sections_by_keywords(blocks: list[Block], keywords: tuple[str, ...]) -> list[Block]:
    """Omit report sections whose ## heading contains any keyword (case-insensitive)."""
    kept: list[Block] = []
    skipping = False
    for block in blocks:
        if block.kind == "heading":
            title = block.text.lower()
            if any(kw in title for kw in keywords):
                skipping = block.level <= 2
                if skipping:
                    continue
            elif block.level <= 2:
                skipping = False
        if not skipping:
            kept.append(block)
    return kept


def limit_cells(blocks: list[Block], limit: int) -> list[Block]:
    out: list[Block] = []
    for block in blocks:
        if block.kind != "table":
            out.append(block)
            continue
        out.append(
            Block(
                kind="table",
                headers=[truncate(h, limit) for h in block.headers],
                rows=[[truncate(c, limit) for c in row] for row in block.rows],
            )
        )
    return out


def _normalize_header(header: str) -> str:
    return re.sub(r"\s+", " ", header.lower().strip())


def _is_story_tracker_table(headers: list[str]) -> bool:
    norms = [_normalize_header(h) for h in headers]
    if "delivery gates" in norms:
        return False
    return "story" in norms and any(n in TRACKER_MERGE_KEYS for n in norms)


def _merge_tracker_table(block: Block) -> Block:
    """Collapse PR / packages / wordings / sandbox columns into one bulleted cell."""
    if block.kind != "table" or not _is_story_tracker_table(block.headers):
        return block

    norms = [_normalize_header(h) for h in block.headers]
    merge_indices = [i for i, n in enumerate(norms) if n in TRACKER_MERGE_KEYS]
    if not merge_indices:
        return block

    first_merge = min(merge_indices)
    new_headers: list[str] = []
    for i, header in enumerate(block.headers):
        if i == first_merge:
            new_headers.append(TRACKER_MERGE_COLUMN)
        elif i not in merge_indices:
            new_headers.append(header)

    new_rows: list[list[str]] = []
    for row in block.rows:
        bullets: list[str] = []
        for i in merge_indices:
            label = TRACKER_MERGE_LABELS.get(norms[i], block.headers[i])
            value = row[i].strip() if i < len(row) else ""
            if value:
                bullets.append(f"- **{label}:** {value}")
        merged = "\n".join(bullets) if bullets else "—"
        new_row: list[str] = []
        for i, cell in enumerate(row):
            if i == first_merge:
                new_row.append(merged)
            elif i not in merge_indices:
                new_row.append(cell)
        new_rows.append(new_row)

    return Block(kind="table", headers=new_headers, rows=new_rows)


def compact_tracker_tables(blocks: list[Block]) -> list[Block]:
    return [_merge_tracker_table(b) if b.kind == "table" else b for b in blocks]


def prepare_blocks(markdown: str) -> list[Block]:
    """All report sections for the card except Standup action items."""
    blocks = parse_blocks(markdown)
    blocks = drop_sections_by_keywords(blocks, SKIP_SECTIONS_FOR_CARD)
    blocks = compact_tracker_tables(blocks)
    return limit_cells(blocks, CELL_SOFT_LIMIT)


def as_of_date(markdown: str, fallback: str) -> str:
    match = re.search(r"\*\*As of:\*\*\s*(\d{4}-\d{2}-\d{2})", markdown)
    return match.group(1) if match else fallback


def uat_ready(markdown: str) -> str:
    match = re.search(r"UAT-ready progress:\*\*\s*\*\*([0-9]+/[0-9]+)", markdown)
    if match:
        return match.group(1)
    match = re.search(r"\*\*(\d+/\d+)\*\* features UAT-ready", markdown)
    return match.group(1) if match else "—"


def targets_line(markdown: str) -> str:
    match = re.search(r"\*\*Targets:\*\*\s*(.+)", markdown)
    if not match:
        return "UAT 2026-09-01 · Prod 2026-09-08"
    return re.sub(r"\*\*", "", match.group(1)).strip()


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


def encoded_size(payload: dict[str, Any]) -> int:
    return len(json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))


def assemble_card(
    blocks: list[Block],
    *,
    as_of: str,
    uat: str,
    targets: str,
    file_path: str,
    file_url: str,
    pr_url: str,
) -> dict[str, Any]:
    facts = [
        {"title": "As of", "value": as_of},
        {"title": "UAT-ready", "value": uat},
        {"title": "Targets", "value": targets},
    ]
    inner: list[dict[str, Any]] = [
        {
            "type": "Container",
            "style": "emphasis",
            "items": [
                _textblock("Pattern Data — delivery progress", size="Large", weight="Bolder"),
                {"type": "FactSet", "facts": facts, "spacing": "Small"},
            ],
        },
        *blocks_to_ac_elements(blocks),
    ]
    if file_path:
        inner.append(_textblock(f"Source: `{file_path}`", size="Small", spacing="Medium", subtle=True))
    body: list[dict[str, Any]] = [
        {
            "type": "Container",
            "bleed": True,
            "items": inner,
        }
    ]
    card: dict[str, Any] = {
        "type": "AdaptiveCard",
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.5",
        "targetWidth": "VeryWide",
        "msteams": {"width": "Full"},
        "body": body,
    }
    actions: list[dict[str, str]] = [
        {"type": "Action.OpenUrl", "title": "Open DVI-1086", "url": DVI_URL}
    ]
    if file_url:
        actions.append({"type": "Action.OpenUrl", "title": "Open report file", "url": file_url})
    if pr_url:
        actions.append({"type": "Action.OpenUrl", "title": "Open PR", "url": pr_url})
    card["actions"] = actions
    return card


def build_adaptive_card(
    markdown: str,
    *,
    file_path: str = "",
    file_url: str = "",
    pr_url: str = "",
    report_date: str = "",
) -> dict[str, Any]:
    as_of = as_of_date(markdown, report_date or date.today().isoformat())
    uat = uat_ready(markdown)
    targets = targets_line(markdown)
    blocks = prepare_blocks(markdown)
    return assemble_card(
        blocks,
        as_of=as_of,
        uat=uat,
        targets=targets,
        file_path=file_path,
        file_url=file_url,
        pr_url=pr_url,
    )


def wrap_teams_message(card: dict[str, Any]) -> dict[str, Any]:
    """Official Teams / Power Automate webhook envelope."""
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


def envelope_size(card: dict[str, Any]) -> int:
    return encoded_size(wrap_teams_message(card))


def _unwrap_bleed_body(body: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if (
        len(body) == 1
        and body[0].get("type") == "Container"
        and body[0].get("bleed")
        and body[0].get("items")
    ):
        return list(body[0]["items"])
    return list(body)


def _wrap_bleed_body(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [{"type": "Container", "bleed": True, "items": items}]


def _is_section_heading(el: dict[str, Any]) -> bool:
    return (
        el.get("type") == "TextBlock"
        and el.get("weight") == "Bolder"
        and el.get("size") in ("Large", "ExtraLarge")
    )


def _group_body_by_sections(body: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
    groups: list[list[dict[str, Any]]] = []
    current: list[dict[str, Any]] = []
    for el in body:
        if _is_section_heading(el) and current:
            groups.append(current)
            current = [el]
        else:
            current.append(el)
    if current:
        groups.append(current)
    return groups


def split_card_for_webhook(card: dict[str, Any], max_bytes: int = WEBHOOK_MAX_BYTES) -> list[dict[str, Any]]:
    """Split at ## section boundaries so every report section lands in the channel."""
    if envelope_size(card) <= max_bytes:
        return [card]

    body = list(card.get("body") or [])
    actions = list(card.get("actions") or [])
    shared = {k: v for k, v in card.items() if k not in {"body", "actions"}}
    inner_body = _unwrap_bleed_body(body)

    def fits(items: list[dict[str, Any]], *, with_actions: bool = False) -> bool:
        probe = dict(shared)
        probe["body"] = _wrap_bleed_body(items)
        if with_actions and actions:
            probe["actions"] = actions
        return envelope_size(probe) <= max_bytes

    section_groups = _group_body_by_sections(inner_body)
    packed: list[list[dict[str, Any]]] = []
    part: list[dict[str, Any]] = []
    for group in section_groups:
        candidate = part + group
        if part and not fits(candidate):
            packed.append(part)
            part = list(group)
            if not fits(part):
                packed.extend(_split_elements(shared, group, max_bytes))
                part = []
        else:
            part = candidate
    if part:
        packed.append(part)

    total = len(packed)
    cards: list[dict[str, Any]] = []
    for idx, items in enumerate(packed, start=1):
        part_card = dict(shared)
        body_items = items
        if total > 1:
            body_items = [_continuation_header(idx, total), *items]
            if not fits(body_items, with_actions=(idx == total)):
                body_items = items
        part_card["body"] = _wrap_bleed_body(body_items)
        if idx == total and actions:
            part_card["actions"] = actions
        cards.append(part_card)
    return cards


def _split_elements(
    shared: dict[str, Any],
    elements: list[dict[str, Any]],
    max_bytes: int,
) -> list[list[dict[str, Any]]]:
    """Element-wise fallback when a single section exceeds the webhook cap."""
    chunks: list[list[dict[str, Any]]] = []
    current: list[dict[str, Any]] = []
    for element in elements:
        candidate = current + [element]
        probe = dict(shared)
        probe["body"] = _wrap_bleed_body(candidate)
        if current and envelope_size(probe) > max_bytes:
            chunks.append(current)
            current = [element]
        else:
            current = candidate
    if current:
        chunks.append(current)
    return chunks


def _continuation_header(part: int, total: int) -> dict[str, Any]:
    return {
        "type": "TextBlock",
        "text": f"Pattern Data — delivery progress · Part {part} of {total}",
        "weight": "Bolder",
        "size": "Medium",
        "wrap": True,
    }


def sanitize_error(text: str) -> str:
    """Strip URLs and signatures so 400 bodies never echo the webhook."""
    text = re.sub(r"https://[^\s\"']+", "[url]", text)
    text = re.sub(r"(?i)sig=[^&\s\"']+", "sig=[redacted]", text)
    return text[:500]


def post_json(url: str, body: dict[str, Any]) -> int:
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    try:
        with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
            return int(resp.status)
    except urllib.error.HTTPError as exc:
        detail = sanitize_error(exc.read().decode("utf-8", errors="replace"))
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from None
    except urllib.error.URLError:
        raise RuntimeError("network error") from None


def post_card(url: str, card: dict[str, Any]) -> int:
    try:
        return post_json(url, wrap_teams_message(card))
    except RuntimeError as first:
        if not str(first).startswith("HTTP 400"):
            raise
        return post_json(url, card)


def post_cards(url: str, cards: list[dict[str, Any]], *, delay_sec: float = POST_DELAY_SEC) -> list[int]:
    statuses: list[int] = []
    for index, card in enumerate(cards):
        statuses.append(post_card(url, card))
        if index < len(cards) - 1 and delay_sec > 0:
            time.sleep(delay_sec)
    return statuses


def resolve_report(repo: Path, report_date: str, explicit: Path | None) -> Path:
    if explicit:
        return explicit if explicit.is_absolute() else repo / explicit
    return repo / "Daily Progress" / f"pattern-data-delivery-progress-{report_date}.md"


def relative_report_path(report_path: Path) -> str:
    try:
        return report_path.resolve().relative_to(find_repo_root()).as_posix()
    except ValueError:
        return report_path.name


def dump_json(payload: dict[str, Any]) -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="POST Pattern Data progress as a Teams Adaptive Card (markdown preview).")
    parser.add_argument("--date", help="Report date YYYY-MM-DD (default: today)")
    parser.add_argument("--file", type=Path, help="Explicit progress markdown path")
    parser.add_argument("--pr-url", default="", help="Optional PR URL button")
    parser.add_argument("--file-url", default="", help="Optional URL for Open report file button")
    parser.add_argument("--webhook-url", default="", help="Override TEAMS_WEBHOOK_URL (do not log this)")
    parser.add_argument("--dry-run", action="store_true", help="Print webhook envelope JSON; do not POST")
    parser.add_argument("--export-card", action="store_true", help="Print Adaptive Card JSON only")
    parser.add_argument(
        "--post-delay",
        type=float,
        default=POST_DELAY_SEC,
        help=f"Seconds to wait between webhook parts (default {POST_DELAY_SEC})",
    )
    args = parser.parse_args()

    repo = find_repo_root()
    load_env_local(repo)
    report_date = args.date or date.today().isoformat()
    report_path = resolve_report(repo, report_date, args.file)
    if not report_path.is_file():
        print(f"Progress report not found: {report_path}", file=sys.stderr)
        sys.exit(2)

    markdown = report_path.read_text(encoding="utf-8")
    file_path = relative_report_path(report_path)
    card = build_adaptive_card(
        markdown,
        file_path=file_path,
        file_url=args.file_url,
        pr_url=args.pr_url,
        report_date=report_date,
    )
    webhook_cards = split_card_for_webhook(card)

    if args.export_card:
        dump_json(card)
        return
    if args.dry_run:
        if len(webhook_cards) == 1:
            dump_json(wrap_teams_message(webhook_cards[0]))
        else:
            dump_json({"parts": [wrap_teams_message(part) for part in webhook_cards]})
        return

    webhook = args.webhook_url or os.environ.get("TEAMS_WEBHOOK_URL", "").strip()
    if not webhook:
        print(
            "TEAMS_WEBHOOK_URL is not set. Add it to .env.local (gitignored) or a Cloud Agent secret; do not commit it.",
            file=sys.stderr,
        )
        sys.exit(2)

    try:
        statuses = post_cards(webhook, webhook_cards, delay_sec=args.post_delay)
    except RuntimeError as exc:
        raise SystemExit(f"Teams webhook failed: {exc}") from exc
    as_of = as_of_date(markdown, report_date)
    codes = ", ".join(str(s) for s in statuses)
    print(f"Posted progress card for {as_of} ({len(webhook_cards)} part(s), HTTP {codes})")


if __name__ == "__main__":
    main()
