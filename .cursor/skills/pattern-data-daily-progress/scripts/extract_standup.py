#!/usr/bin/env python3
"""Extract plain text from ChartSwap standup docx. Usage:
  python scripts/extract_standup.py "Transcript/ChartSwap Daily Stand up/ChartSwap-Daily-Stand-up-2026-06-07.docx"
Writes UTF-8 text to stdout or -o file.
"""
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def extract(docx_path: str) -> str:
    with zipfile.ZipFile(docx_path) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    paras = []
    for p in root.iter(W + "p"):
        texts = [t.text for t in p.iter(W + "t") if t.text]
        if texts:
            paras.append("".join(texts))
    return "\n".join(paras)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: extract_standup.py <path-to.docx> [-o output.txt]", file=sys.stderr)
        sys.exit(1)
    docx_path = sys.argv[1]
    out_path = None
    if "-o" in sys.argv:
        out_path = sys.argv[sys.argv.index("-o") + 1]
    text = extract(docx_path)
    if out_path:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(text)


if __name__ == "__main__":
    main()
