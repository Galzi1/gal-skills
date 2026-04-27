"""
Two-column PDF text extractor using PyMuPDF.

Usage:
    python extract_columns.py <pdf_path> [--pages START-END] [--out output.md]

Reads each page in correct two-column order:
  1. Full-width blocks (title, abstract, section headers spanning both columns)
  2. Left-column blocks, top to bottom
  3. Right-column blocks, top to bottom

Requires: pip install pymupdf
"""

import sys
import argparse
import fitz  # PyMuPDF


FULLWIDTH_THRESHOLD = 0.75  # block spanning >75% of page width = full-width


def block_text(block):
    """Extract plain text from a PyMuPDF text block dict."""
    lines = []
    for line in block.get("lines", []):
        spans = [s["text"] for s in line.get("spans", []) if s["text"].strip()]
        if spans:
            lines.append(" ".join(spans))
    return "\n".join(lines)


def classify_block(block, page_width):
    """Return 'full', 'left', or 'right' based on block x-position."""
    x0, _, x1, _ = block["bbox"]
    width = x1 - x0
    if width / page_width >= FULLWIDTH_THRESHOLD:
        return "full"
    midpoint = page_width / 2
    # Use the block's center to decide column
    center = (x0 + x1) / 2
    return "left" if center < midpoint else "right"


def extract_page(page):
    """Return ordered text for a single page."""
    pw = page.rect.width
    blocks = [b for b in page.get_text("dict")["blocks"] if b["type"] == 0]

    full_blocks = sorted(
        [b for b in blocks if classify_block(b, pw) == "full"],
        key=lambda b: b["bbox"][1],
    )
    left_blocks = sorted(
        [b for b in blocks if classify_block(b, pw) == "left"],
        key=lambda b: b["bbox"][1],
    )
    right_blocks = sorted(
        [b for b in blocks if classify_block(b, pw) == "right"],
        key=lambda b: b["bbox"][1],
    )

    parts = []
    for b in full_blocks:
        t = block_text(b).strip()
        if t:
            parts.append(t)
    for b in left_blocks:
        t = block_text(b).strip()
        if t:
            parts.append(t)
    for b in right_blocks:
        t = block_text(b).strip()
        if t:
            parts.append(t)

    return "\n\n".join(parts)


def parse_page_range(spec, total_pages):
    """Parse '3-7' or '5' into a list of 0-based page indices."""
    if spec is None:
        return list(range(total_pages))
    if "-" in spec:
        start, end = spec.split("-", 1)
        return list(range(int(start) - 1, min(int(end), total_pages)))
    return [int(spec) - 1]


def main():
    parser = argparse.ArgumentParser(description="Two-column PDF extractor")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--pages", help="Page range, e.g. 1-5 or 3", default=None)
    parser.add_argument("--out", help="Output file path (default: stdout)", default=None)
    args = parser.parse_args()

    doc = fitz.open(args.pdf_path)
    page_indices = parse_page_range(args.pages, len(doc))

    output_parts = []
    for i in page_indices:
        page = doc[i]
        page_text = extract_page(page)
        if page_text.strip():
            output_parts.append(f"<!-- Page {i + 1} -->\n{page_text}")

    result = "\n\n---\n\n".join(output_parts)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"Saved to {args.out}", file=sys.stderr)
    else:
        print(result)


if __name__ == "__main__":
    main()
