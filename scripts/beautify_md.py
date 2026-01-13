#!/usr/bin/env python3
"""
Simple beautifier for the PPTX->MD output created by scripts/pptx_to_md.py
- Adds a Table of Contents after the first H1
- Converts "**Notes:**" sections into Markdown blockquotes
- Ensures tidy spacing

Usage: python scripts/beautify_md.py path/to/file.md
"""
import re
import sys
import os

p = sys.argv[1]
with open(p, encoding='utf-8') as f:
    lines = f.read().splitlines()

out_lines = []
slides = []

slide_re = re.compile(r"^## Slide (\d+)(?:: (.*))?")

# First pass: collect slide headings and their indices
for i, ln in enumerate(lines):
    m = slide_re.match(ln)
    if m:
        num = int(m.group(1))
        title = m.group(2) or ''
        # create a slug for anchor
        slug = re.sub(r"[^a-z0-9]+", "-", (f"slide-{num}-{title}".lower())).strip('-')
        slides.append((num, title.strip(), slug))

# Insert TOC after first H1 if present
inserted_toc = False
i = 0
while i < len(lines):
    ln = lines[i]
    out_lines.append(ln)
    if not inserted_toc and ln.startswith('# '):
        # add TOC
        out_lines.append('')
        out_lines.append('## Table of Contents')
        out_lines.append('')
        for num, title, slug in slides:
            display = f"Slide {num}"
            if title:
                display += f": {title}"
            out_lines.append(f"- [{display}](#{slug})")
        out_lines.append('')
        inserted_toc = True
    i += 1

# Second pass: transform Notes into blockquotes and add anchor ids to slide headings
final_lines = []
in_notes = False
for ln in out_lines:
    m = slide_re.match(ln)
    if m:
        num = int(m.group(1))
        title = m.group(2) or ''
        slug = re.sub(r"[^a-z0-9]+", "-", (f"slide-{num}-{title}".lower())).strip('-')
        final_lines.append(f"## Slide {num}: {title} {{#{slug}}}")
        in_notes = False
        continue

    if ln.strip() == "**Notes:**":
        final_lines.append('> **Notes:**')
        in_notes = True
        continue
    if in_notes:
        if ln.strip() == '' or ln.strip() == '---':
            in_notes = False
            final_lines.append(ln)
        else:
            final_lines.append('> ' + ln)
        continue
    # normalize multiple blank lines to one
    final_lines.append(ln)

# Tidy: collapse more than two consecutive newlines
text = '\n'.join(final_lines)
text = re.sub(r"\n{3,}", '\n\n', text)

out_path = os.path.splitext(p)[0] + '_beautified.md'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Beautified file written to: {out_path}")
