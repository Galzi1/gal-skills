---
name: read-2col-pdf
description: Read and extract content from two-column PDF documents (academic papers, journal articles, conference proceedings, research papers) with correct reading order - left column top-to-bottom before right column. Use this skill whenever the user gives you a PDF that looks like an academic paper, a research article, an arXiv paper, a conference paper, or any document with a two-column layout. Also trigger when the user asks you to summarize, extract, or analyze a scientific paper PDF, when a PDF seems to have garbled or interleaved text, or when content from two side-by-side columns is appearing out of order. Always use this skill before reading any PDF that could plausibly be a journal article or multi-column document - it's better to apply it and not need it than to skip it and produce scrambled output.
---

# Two-Column PDF Reading Skill

Academic papers, journal articles, and conference proceedings almost always use a two-column layout. The naive approach - reading the page left-to-right, top-to-bottom as one wide block - interleaves text from both columns, producing incoherent output. This skill gives you a reliable method for reading these documents correctly.

## Core Principle

Two-column layout means: read the **entire left column** of a page from top to bottom, then move to the **top of the right column** and read it from top to bottom. Repeat for each page.

## Step-by-Step Process

### 1. Extract the PDF Text

**Primary method - Python script (always try this first):**

This bundled script uses PyMuPDF to extract text blocks with bounding box positions, then sorts them into correct column order deterministically. It works without any external tools like `pdftoppm`.

```bash
# Install dependency if needed (one-time)
pip install pymupdf

# Extract all pages
python <skill_dir>/scripts/extract_columns.py path/to/paper.pdf

# Extract specific pages
python <skill_dir>/scripts/extract_columns.py path/to/paper.pdf --pages 1-5

# Save to file
python <skill_dir>/scripts/extract_columns.py path/to/paper.pdf --out extracted.md
```

Replace `<skill_dir>` with the path to this skill's directory (find it with `Glob("**/read-2col-pdf/scripts/extract_columns.py")`).

The script outputs text in correct reading order: full-width header blocks first, then left column, then right column, per page.

**Fallback - Visual rendering:**

If the script fails (e.g., encrypted PDF, unusual encoding), try the `Read` tool:

```
Read(file_path="path/to/paper.pdf", pages="1-4")
```

This renders pages as images. If `pdftoppm` is missing on the system, this will fail - in that case, the script is the only viable method.

> If the user hasn't given you a file path, ask them to confirm the path before proceeding.

### 2. Identify the Layout

After extraction, verify the document is two-column by checking if the script's output looks correct:
- Full-width elements (title, authors, abstract) appear first
- Body text flows naturally sentence-by-sentence without topic jumps

Single-column documents (some theses, preprints, reports) will also extract correctly - the script handles them naturally since all blocks will be in the "left" or "full" category.

### 3. Process the Extracted Text

The script output is already in correct reading order. Your job is to:
1. Read through it and understand structure (sections, figures, tables)
2. Reconstruct the logical hierarchy (section headers, paragraphs, captions)
3. Join any words hyphenated at line breaks (e.g., "explo-\nration" → "exploration")
4. Note figure/table positions by their captions

### 4. Handle Special Elements

**Figures and Tables:**
- They may appear mid-column, spanning one column, or spanning both columns (full-width).
- Read the figure/table caption, which appears directly below (or sometimes above) the element.
- Note: "Figure 3: ..." or "Table 2: ..." - include captions in your output at the correct position in the reading flow.
- For content you cannot extract from a figure (e.g., a chart), describe what you see: dimensions, axis labels, trend, color encoding.

**Equations:**
- Numbered equations appear centered in their column or full-width. Include the equation number (e.g., `Eq. (3)`) when present.
- Write equations in LaTeX notation if you can, or in plain text if not.

**Footnotes:**
- Appear at the bottom of the column that contains their reference mark.
- Read footnotes after you finish the column body they belong to, before moving to the next column.

**Section headers and subsection headers:**
- Usually bold/larger text. They mark structural boundaries within a column - include them in the output.

**References section:**
- Usually at the end, often two-column. Read left column of references, then right column.

### 5. Reading Multi-Page Documents

The script handles the full document in one call. For very large documents (50+ pages) where you only need a section, use `--pages`:

```bash
python <skill_dir>/scripts/extract_columns.py paper.pdf --pages 3-8 --out section.md
```

If using the visual fallback (`Read` tool) instead, batch into ≤20 pages per call:
```
Read(file_path="paper.pdf", pages="1-10")
Read(file_path="paper.pdf", pages="11-20")
```

### 6. Output Format

Structure your output to mirror the document's logical hierarchy:

```
# [Paper Title]
**Authors:** ...
**Abstract:** ...

## 1. Introduction
[Left column content of intro section]
[Right column continuation of intro, if any]

## 2. Related Work
...

[Figure N: caption text]

## 3. Method
...
```

- Preserve section numbering from the paper.
- Mark figures/tables with `[Figure N: caption]` or `[Table N: caption]` inline where they appear in the flow.
- If a sentence is cut off at the bottom of a column and continues at the top of the next column or next page, join them seamlessly in your output.

## Common Pitfalls to Avoid

**Don't** read across both columns at once - this produces interleaved, nonsensical sentences.

**Don't** skip over figures - their captions and your description are part of the content.

**Don't** assume every page has the same layout - the first page often has a different structure (title + abstract full-width), and some pages may have a figure spanning both columns.

**Don't** stop at the first page when asked to "read the paper" - read all pages unless the user asks for something specific.

## When the User Asks for a Summary or Specific Section

You still need to read the full document (or at least the relevant pages) in column-correct order before summarizing. A summary produced from interleaved column text will miss or misattribute key points.

For specific sections: check the page range from the table of contents or by scanning section headers, then read just those pages using `pages="X-Y"`.

## Quick Reference

| Element | Action |
|---------|--------|
| Title / Abstract | Full width - read normally |
| Body text | Left column fully, then right column |
| Figure/Table | Note position, include caption, describe visual |
| Footnote | After column body, before switching columns |
| References | Left column of refs, then right column |
| Sentence split across columns | Join seamlessly |
