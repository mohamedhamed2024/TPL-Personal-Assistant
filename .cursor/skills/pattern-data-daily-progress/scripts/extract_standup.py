#!/usr/bin/env python3
"""Extract plain text from standup / Austin / PD Review transcripts.

Supports .docx and already-plain files (.txt or no extension). Usage:
  python scripts/extract_standup.py "Transcript/ChartSwap Daily Stand up/ChartSwap-Daily-Stand-up-2026-06-07.docx"
  python scripts/extract_standup.py "Transcript/PDReviewWithAustin/PDReviewWithAustin-2026-08-20" -o _austin_extract.txt
Writes UTF-8 text to stdout or -o file.
"""
from pathlib import Path
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def extract_docx(docx_path: str) -> str:
    with zipfile.ZipFile(docx_path) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    paras = []
    for p in root.iter(W + "p"):
        texts = [t.text for t in p.iter(W + "t") if t.text]
        if texts:
            paras.append("".join(texts))
    return "\n".join(paras)


def extract(path: str) -> str:
    suffix = Path(path).suffix.lower()
    if suffix == ".docx":
        return extract_docx(path)
    return Path(path).read_text(encoding="utf-8")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: extract_standup.py <path-to-transcript> [-o output.txt]", file=sys.stderr)
        sys.exit(1)
    src_path = sys.argv[1]
    out_path = None
    if "-o" in sys.argv:
        out_path = sys.argv[sys.argv.index("-o") + 1]
    text = extract(src_path)
    if out_path:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(text)


if __name__ == "__main__":
    main()
