#!/usr/bin/env python3
"""Build the condensed per-type skill references from the long-form type pages.

Input (single source):
  content/en/types/<code>-<slug>.md   one page per type, fixed section ids (docs/DESIGN.md section 4)

Output (generated, do not edit by hand):
  skills/architecture-diagrams/references/types/<code>-<slug>.md

A condense section whose page text is longer than its budget carries its own short text in a
`<!-- skill-text` ... `-->` comment block (invisible on the site); the generator uses that instead.

Each page marks every section with `<!-- skill: keep|condense|omit|path only (...) -->`.
The generator keeps the marked sections, removes citation markers such as [3][4], and enforces
the per-section and total line budgets of DESIGN section 4. It never shortens text: a section
that is over budget is an error that names the page and section, and the page is tightened.

Usage:
  python3 tools/build_skill_refs.py           write outputs (refuses when any page fails)
  python3 tools/build_skill_refs.py --check   exit 1 if a page is invalid, over budget, or an output is stale
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "content/en/types"
OUT = ROOT / "skills/architecture-diagrams/references/types"
TEMPLATES = ROOT / "skills/architecture-diagrams/assets/templates"

# Section id -> (heading kept in the reference, marker mode, line budget). DESIGN section 4, in page order.
SECTIONS = {
    "meaning": ("Meaning", "condense", 6),
    "choose": ("When to use and how to choose", "condense", 12),
    "notation": ("Notation and elements", "condense", 15),
    "practice": ("Best practices and anti-patterns", "condense", 12),
    "exemplars": (None, "omit", 0),
    "recipe": ("Drawing recipe", "keep", 25),
    "evidence": ("Evidence in a code repository", "keep", 10),
    "questions": ("Guided-mode questions", "keep", 8),
    "template": ("Template", "keep", 3),
    "sources": (None, "omit", 0),
    "sample": ("Sample", "path only", 1),
}
TOTAL_LINES = 110
MAX_TOKENS = 3000  # estimate: characters / 4; DESIGN aims at about 1,500 and the recipe alone is kept in full
HEADING_RE = re.compile(r"^## (.+?) \{#([a-z]+)\}\s*$")
MARKER_RE = re.compile(r"^<!-- skill: (keep|condense|omit|path only)\b.*-->\s*$")
CITATION_RE = re.compile(r"(?:\s*\[\d+(?:\s*[,–-]\s*\d+)*(?:\s*§[^\]]*)?\])+")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
TEMPLATE_LINE_RE = re.compile(r"Model template: `assets/templates/([A-Z]\d+)\.json` · Layout template: `([a-z_]+)`")


def split_page(text: str) -> tuple[dict, str, list[tuple[str, str, str, list[str]]]]:
    """Return front matter, H1 title and sections as (id, heading, marker mode, body lines)."""
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not match:
        raise ValueError("missing front matter")
    meta = yaml.safe_load(match.group(1))
    title, sections = "", []
    for line in match.group(2).split("\n"):
        heading = HEADING_RE.match(line)
        if heading:
            sections.append([heading.group(2), heading.group(1), None, []])
        elif line.startswith("# ") and not sections:
            title = line[2:].strip()
        elif sections:
            marker = MARKER_RE.match(line)
            if marker and sections[-1][2] is None and not any(x.strip() for x in sections[-1][3]):
                sections[-1][2] = marker.group(1)
            else:
                sections[-1][3].append(line)
    return meta, title, [tuple(s) for s in sections]


def strip_blank_edges(lines: list[str]) -> list[str]:
    while lines and not lines[0].strip():
        lines = lines[1:]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    return lines


def skill_variant(lines: list[str]) -> list[str] | None:
    """Return the lines of a `<!-- skill-text ... -->` block, if the section has one."""
    start = next((i for i, line in enumerate(lines) if line.strip() == "<!-- skill-text"), None)
    if start is None:
        return None
    end = next((i for i in range(start + 1, len(lines)) if lines[i].strip() == "-->"), None)
    return lines[start + 1:end] if end is not None else []


def clean(lines: list[str]) -> list[str]:
    out = []
    for line in strip_blank_edges(lines):
        line = CITATION_RE.sub("", line).rstrip()
        if line or (out and out[-1]):
            out.append(line)
    return out


def build_page(path: Path) -> tuple[str, list[str]]:
    """Return the reference text and the list of problems found in one page."""
    problems: list[str] = []
    name = path.name
    try:
        meta, title, sections = split_page(path.read_text(encoding="utf-8"))
    except ValueError as error:
        return "", [f"{name}: {error}"]
    for key in ("code", "slug", "question", "scope", "neighbours"):
        if not meta.get(key):
            problems.append(f"{name}: front matter lacks `{key}`")
    if problems:
        return "", problems
    if path.stem != f"{meta['code']}-{meta['slug']}":
        problems.append(f"{name}: file name does not match code-slug `{meta['code']}-{meta['slug']}`")
    ids = [s[0] for s in sections]
    if ids != list(SECTIONS):
        problems.append(f"{name}: section ids {ids} differ from the required order {list(SECTIONS)}")
        return "", problems

    body: list[str] = []
    for id, _, mode, lines in sections:
        heading, want_mode, budget = SECTIONS[id]
        if mode != want_mode:
            problems.append(f"{name}: section `{id}` is marked `{mode}`, expected `{want_mode}`")
            continue
        if heading is None:
            continue
        if mode == "path only":
            image = IMAGE_RE.search("\n".join(lines))
            if not image:
                problems.append(f"{name}: section `sample` has no image path")
                continue
            kept = [f"Figure: `{image.group(1).lstrip('/')}` (published with the site)"]
        else:
            variant = skill_variant(lines) if mode == "condense" else None
            kept = clean(lines if variant is None else variant)
        count = sum(1 for line in kept if line.strip())
        if count > budget:
            problems.append(f"{name}: section `{id}` has {count} lines, budget {budget}")
        if not count:
            problems.append(f"{name}: section `{id}` is empty")
        body += ["", f"## {heading}", *kept]

    template = next(s for s in sections if s[0] == "template")
    declared = TEMPLATE_LINE_RE.search("\n".join(template[3]))
    if not declared or declared.group(1) != meta["code"]:
        problems.append(f"{name}: Template section must start with the model template `{meta['code']}.json` and a layout template")
    else:
        model = TEMPLATES / f"{meta['code']}.json"
        if not model.exists():
            problems.append(f"{name}: {model.relative_to(ROOT)} does not exist")
        elif json.loads(model.read_text(encoding="utf-8"))["layout"]["template"] != declared.group(2):
            problems.append(f"{name}: layout template `{declared.group(2)}` differs from the one in {model.name}")

    neighbours = ", ".join(str(n) for n in meta["neighbours"])
    head = [
        f"# {title or meta['code']}",
        f"<!-- Generated from content/en/types/{path.name} by tools/build_skill_refs.py. Do not edit. -->",
        f"> {meta['question']}",
        f"Scope: {meta['scope']} Neighbours: {neighbours}.",
    ]
    catalogue = yaml.safe_load((ROOT / "content/data/types.yaml").read_text())["types"]
    row = next(t for t in catalogue if t["code"] == meta["code"])
    if row["catalogRole"] == "variant":
        head.append(f"Named variant of {row['target']['code']}; apply this reference's own recipe and checks.")
    elif row["catalogRole"] == "reference":
        head.append("Method reference: honour explicit requests; outside the default core catalogue.")
    children = [t for t in catalogue if t["catalogRole"] == "variant" and t["target"]["code"] == row["code"]]
    if children:
        head.append("Named variants (read their own recipes): " + "; ".join(
            f"{t['code']} — `references/types/{t['code']}-{t['slug']}.md`" for t in children) + ".")
    text = "\n".join(head + body) + "\n"
    if text.count("\n") > TOTAL_LINES:
        problems.append(f"{name}: reference has {text.count(chr(10))} lines, budget {TOTAL_LINES}")
    if len(text) // 4 > MAX_TOKENS:
        problems.append(f"{name}: reference is about {len(text) // 4} tokens, budget {MAX_TOKENS}")
    return text, problems


def build_all() -> tuple[dict[str, str], list[str]]:
    outputs, problems = {}, []
    pages = sorted(PAGES.glob("*.md"))
    if not pages:
        problems.append(f"no type pages in {PAGES.relative_to(ROOT)}")
    for page in pages:
        text, found = build_page(page)
        problems += found
        if text:
            outputs[page.name] = text
    return outputs, problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--check", action="store_true", help="do not write; exit 1 on invalid, over-budget or stale output")
    args = parser.parse_args()
    outputs, problems = build_all()
    if not args.check and not problems:
        OUT.mkdir(parents=True, exist_ok=True)
        for name in sorted(p.name for p in OUT.glob("*.md") if p.name not in outputs):
            (OUT / name).unlink()
        for name, text in outputs.items():
            target = OUT / name
            if not target.exists() or target.read_text(encoding="utf-8") != text:
                target.write_text(text, encoding="utf-8")
    if args.check:
        for name, text in outputs.items():
            target = OUT / name
            if not target.exists():
                problems.append(f"{target.relative_to(ROOT)} is missing; run tools/build_skill_refs.py")
            elif target.read_text(encoding="utf-8") != text:
                problems.append(f"{target.relative_to(ROOT)} is stale; run tools/build_skill_refs.py")
        for target in sorted(OUT.glob("*.md")):
            if target.name not in outputs:
                problems.append(f"{target.relative_to(ROOT)} has no source page")
    for problem in problems:
        print(problem, file=sys.stderr)
    if problems:
        print(f"{len(problems)} problem(s)", file=sys.stderr)
        return 1
    largest = max(len(text) for text in outputs.values()) // 4
    print(f"{len(outputs)} references {'up to date' if args.check else 'written'} (largest about {largest} tokens)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
