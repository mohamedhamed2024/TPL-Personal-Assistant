import json
import re
from collections import defaultdict
from pathlib import Path

INPUT = Path(
    r"C:\Users\MSalah\.cursor\projects\c-Users-MSalah-OneDrive-Ontellus-Desktop-TPL-Personal-Assistant\agent-tools\f567ff9c-cbd1-41ed-ae40-b21cdc16f071.txt"
)
OUTPUT = Path(
    r"C:\Users\MSalah\.cursor\projects\c-Users-MSalah-OneDrive-Ontellus-Desktop-TPL-Personal-Assistant\agent-tools\closed-bugs-refined.txt"
)


def normalize(cat, summary, fix_text):
    s = " ".join(filter(None, [cat, summary, fix_text])).lower()
    if not cat or "not clear" in cat.lower():
        if any(
            k in summary.lower()
            for k in [
                "payment",
                "autopay",
                "card",
                "billing",
                "invoice",
                "transaction",
                "charge",
                "retry",
                "threshold",
            ]
        ):
            return "Payment / Billing Logic"
        if any(
            k in summary.lower()
            for k in ["webhook", "order init", "api", "payload", "prospectpatient"]
        ):
            return "Integration / API Contract"
        if any(
            k in s
            for k in [
                "config",
                "setting",
                "flag",
                "test data",
                "seed",
                "enablement",
                "credential",
            ]
        ):
            return "Environment / Test Data / Configuration"
        if any(
            k in summary.lower()
            for k in ["ui", "button", "display", "wording", "copy", "visualforce"]
        ):
            return "UI / Visualforce Presentation"
        if any(k in s for k in ["permission", "sharing", "access", "owd"]):
            return "Security / Permissions / Sharing"
        return "Insufficient Documentation"
    c = cat.lower()
    if "coding" in c or "logic defect" in c or "code" in c:
        return "Application Logic / Code Defect"
    if "ui / rendering" in c or "ui/" in c or "ux" in c:
        return "UI / Visualforce Presentation"
    if "security" in c or "permission" in c or "sharing" in c or "owd" in c:
        return "Security / Permissions / Sharing"
    if "integration" in c or "api contract" in c or "spec-vs-implementation" in c:
        return "Integration / API Contract"
    if "data / configuration" in c or "data/configuration" in c:
        return "Environment / Test Data / Configuration"
    if "build / deployment" in c or "release" in c or "env drift" in c:
        return "Deployment / Environment Drift"
    if "requirement" in c or "spec gap" in c:
        return "Requirements / Design Clarification"
    if "not a defect" in c or "works as designed" in c:
        return "Not a Defect / Works as Designed"
    if "concurrency" in c or "timing" in c or "stale" in c or "view-state" in c:
        return "Concurrency / Stale State"
    return cat


def main():
    with INPUT.open(encoding="utf-8") as f:
        data = json.load(f)

    cat_map = {}
    for issue in data["issues"]:
        key = issue["key"]
        summary = issue["fields"]["summary"]
        comments = issue["fields"].get("comment", {}).get("comments", [])
        all_text = "\n".join(c.get("body", "") or "" for c in comments)

        cat = None
        m = re.search(r"\*\*Category:\*\*\s*([^\n*]+)", all_text)
        if m:
            cat = m.group(1).strip()

        fix = None
        fm = re.search(r"\*\*Fix:\*\*\s*([^\n]+)", all_text)
        if fm:
            fix = fm.group(1).strip()[:250]

        rc = None
        rm = re.search(
            r"\*\*Description:\*\*\s*([^\n]+(?:\n(?!\* \*\*Category).+)*)",
            all_text,
        )
        if rm:
            rc = re.sub(r"\s+", " ", rm.group(1).strip())[:300]

        cat_map[key] = {
            "summary": summary,
            "category": cat,
            "fix": fix,
            "root_cause": rc,
            "has_closure": "Bug Closure Analysis" in all_text,
        }

    groups = defaultdict(list)
    for key, info in sorted(cat_map.items()):
        norm = normalize(info["category"], info["summary"], info["fix"] or "")
        groups[norm].append((key, info))

    with OUTPUT.open("w", encoding="utf-8") as f:
        closure_count = sum(1 for v in cat_map.values() if v["has_closure"])
        f.write(f"Total closed Pattern Data bugs: {len(cat_map)}\n")
        f.write(f"With PMO Bug Closure Analysis comment: {closure_count}\n\n")
        f.write("=== CATEGORY SUMMARY ===\n")
        for g in sorted(groups.keys(), key=lambda c: (-len(groups[c]), c)):
            f.write(f"{g}: {len(groups[g])}\n")

        for g in sorted(groups.keys(), key=lambda c: (-len(groups[c]), c)):
            f.write(f"\n\n## {g} ({len(groups[g])})\n\n")
            for key, info in groups[g]:
                f.write(f"### [{key}](https://ontellus.atlassian.net/browse/{key})\n")
                f.write(f"**{info['summary']}**\n\n")
                if info["category"]:
                    f.write(f"- **Jira closure category:** {info['category']}\n")
                if info["root_cause"]:
                    f.write(f"- **Root cause:** {info['root_cause']}\n")
                if info["fix"]:
                    f.write(f"- **Fix:** {info['fix']}\n")
                f.write("\n")

    print(f"Wrote {OUTPUT}")
    for g in sorted(groups.keys(), key=lambda c: (-len(groups[c]), c)):
        print(f"{len(groups[g]):2d} {g}")


if __name__ == "__main__":
    main()
