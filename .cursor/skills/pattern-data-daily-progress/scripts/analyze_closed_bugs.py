import json
import re
from collections import defaultdict
from pathlib import Path

INPUT = Path(
    r"C:\Users\MSalah\.cursor\projects\c-Users-MSalah-OneDrive-Ontellus-Desktop-TPL-Personal-Assistant\agent-tools\f567ff9c-cbd1-41ed-ae40-b21cdc16f071.txt"
)
OUTPUT = Path(
    r"C:\Users\MSalah\.cursor\projects\c-Users-MSalah-OneDrive-Ontellus-Desktop-TPL-Personal-Assistant\agent-tools\closed-bugs-analysis.txt"
)


def extract_fix_info(comments):
    all_text = "\n".join(c.get("body", "") or "" for c in comments)

    cat_match = re.search(r"\*\*Category:\*\*\s*([^\n*]+)", all_text)
    rc_section = re.search(
        r"### Root Cause\s*\n+([\s\S]*?)(?=\n### |\n\*\*Category|\n---|\Z)", all_text
    )
    fix_section = re.search(
        r"### (?:Resolution|Fixes Applied|Fix)\s*\n+([\s\S]*?)(?=\n### |\n---|\Z)",
        all_text,
    )

    category = cat_match.group(1).strip() if cat_match else None
    root_cause = None
    if rc_section:
        root_cause = re.sub(r"\s+", " ", rc_section.group(1).strip())[:500]

    fix = None
    if fix_section:
        fix = re.sub(r"\s+", " ", fix_section.group(1).strip())[:500]

    return category, root_cause, fix, all_text


def map_category(category, root_cause, fix, summary, all_text):
    text = " ".join(filter(None, [category, root_cause, fix, summary, all_text])).lower()

    if category and "not clear" not in category.lower():
        c = category.lower()
        if "coding" in c or "logic" in c or "code" in c:
            return "Application Logic / Code Defect"
        if "config" in c or "setting" in c or "metadata" in c:
            return "Missing or Incorrect Configuration"
        if "data" in c or "seed" in c or "test data" in c:
            return "Test Data / Data Quality Issue"
        if "ui" in c or "visual" in c or "display" in c or "frontend" in c:
            return "UI / Presentation Issue"
        if "integration" in c or "api" in c or "contract" in c or "schema" in c:
            return "Integration / API Contract Mismatch"
        if "security" in c or "permission" in c or "sharing" in c or "owd" in c:
            return "Security / Permissions / Sharing"
        if "environment" in c or "deploy" in c or "sandbox" in c:
            return "Environment / Deployment Gap"
        if "requirement" in c or "spec" in c or "design" in c:
            return "Requirements / Design Gap"
        if "duplicate" in c or "not a bug" in c or "expected" in c:
            return "Not a Bug / Expected Behavior"
        return category

    rules = [
        (
            "Missing or Incorrect Configuration",
            [
                "config",
                "setting",
                "metadata",
                "custom setting",
                "named credential",
                "remote site",
                "permission set",
                "profile",
                "feature flag",
                "org setting",
                "sites ",
                "site setting",
                "credential",
                "sso",
                "saml config",
            ],
        ),
        (
            "Security / Permissions / Sharing",
            [
                "with sharing",
                "without sharing",
                "owd",
                "sharing rule",
                "permission",
                "fls",
                "field level",
                "access denied",
                "insufficient",
                "portal user",
                "guest user",
            ],
        ),
        (
            "Integration / API Contract Mismatch",
            [
                "api contract",
                "payload",
                "webhook",
                "order init",
                "prospectpatient",
                "pattern data api",
                "field mapping",
                "schema",
                "integration",
                "external system",
                "callback",
                "rest api",
                "soap",
            ],
        ),
        (
            "Test Data / Data Quality Issue",
            [
                "test data",
                "seed data",
                "bad data",
                "stale data",
                "wrong data",
                "data issue",
                "record not found",
                "missing record",
                "orphan",
                "duplicate record",
                "staging record",
            ],
        ),
        (
            "UI / Presentation Issue",
            [
                "visualforce",
                "page layout",
                "button",
                "label",
                "display",
                "render",
                "ui ",
                "frontend",
                "css",
                "redirect",
                "visual force",
                "page error",
                "blank page",
                "load error",
            ],
        ),
        (
            "Payment / Billing Logic",
            [
                "payment",
                "invoice",
                "billing",
                "card",
                "stripe",
                "charge",
                "refund",
                "firm card",
                "saved payment",
                "transaction",
            ],
        ),
        (
            "Environment / Deployment Gap",
            [
                "not deployed",
                "deployment",
                "sandbox",
                "uat env",
                "missing package",
                "manifest",
                "branch not merged",
                "environment",
            ],
        ),
        (
            "Requirements / Design Gap",
            [
                "requirement",
                "acceptance criteria",
                "design gap",
                "spec",
                "not implemented",
                "missing implementation",
                "oversight",
            ],
        ),
        (
            "Not a Bug / Expected Behavior",
            [
                "not a bug",
                "by design",
                "expected behavior",
                "working as designed",
                "duplicate of",
                "user error",
                "tester error",
            ],
        ),
        (
            "Application Logic / Code Defect",
            [
                "null pointer",
                "exception",
                "bug in",
                "logic",
                "query",
                "soql",
                "dml",
                "controller",
                "apex",
                "cls",
                "trigger",
                "handler",
                "race condition",
                "order by",
                "missing null",
                "incorrect logic",
                "wrong field",
                "not cleared",
                "not populated",
                "failed to",
            ],
        ),
    ]

    for cat, keywords in rules:
        if any(k in text for k in keywords):
            return cat

    return "Uncategorized / Insufficient Comment Detail"


def main():
    with INPUT.open(encoding="utf-8") as f:
        data = json.load(f)

    issues = data.get("issues", [])
    results = []

    for issue in issues:
        key = issue["key"]
        fields = issue["fields"]
        summary = fields.get("summary", "")
        comments = fields.get("comment", {}).get("comments", [])
        category_raw, root_cause, fix, all_text = extract_fix_info(comments)
        mapped = map_category(category_raw, root_cause, fix, summary, all_text)
        results.append(
            {
                "key": key,
                "summary": summary,
                "category_raw": category_raw,
                "category": mapped,
                "root_cause": root_cause,
                "fix": fix,
                "comment_count": len(comments),
            }
        )

    by_cat = defaultdict(list)
    for r in results:
        by_cat[r["category"]].append(r)

    with OUTPUT.open("w", encoding="utf-8") as f:
        f.write(f"Total closed Pattern Data bugs: {len(results)}\n\n")
        f.write("=== SUMMARY BY CATEGORY ===\n")
        for cat in sorted(by_cat.keys(), key=lambda c: (-len(by_cat[c]), c)):
            f.write(f"{cat}: {len(by_cat[cat])}\n")
        f.write("\n")
        for cat in sorted(by_cat.keys(), key=lambda c: (-len(by_cat[c]), c)):
            f.write(f"\n\n## {cat} ({len(by_cat[cat])})\n")
            for r in sorted(by_cat[cat], key=lambda x: x["key"]):
                f.write(f"\n### {r['key']}: {r['summary']}\n")
                if r["category_raw"]:
                    f.write(f"Jira closure category: {r['category_raw']}\n")
                if r["root_cause"]:
                    f.write(f"Root cause: {r['root_cause']}\n")
                if r["fix"]:
                    f.write(f"Fix: {r['fix']}\n")
                f.write(f"Comments: {r['comment_count']}\n")

    print(f"Wrote {OUTPUT}")
    print(f"Total: {len(results)}")
    for cat in sorted(by_cat.keys(), key=lambda c: (-len(by_cat[c]), c)):
        print(f"{len(by_cat[cat]):2d} {cat}")


if __name__ == "__main__":
    main()
