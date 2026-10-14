#!/usr/bin/env python3
"""Check the Chinese mirror against the English source and keep the glossary page current.

Checks (content/en/**/*.md is canonical; content/zh/ mirrors it with the same paths):
  error    a mirrored page is missing, or the structure differs: `{#id}` anchors,
           `<!-- skill: … -->` and `<!-- BEGIN/END GENERATED: … -->` markers (same order)
  error    translation front matter wrong: translationOf != en/<path>, reviewed not a
           boolean, sourceRev missing or not a commit
  error    the glossary page block is out of date (run with --write)
  warning  stale: the English page changed after the sourceRev commit (error with --release)
  warning  README/CONTRIBUTING pairs: heading levels differ
  note     glossary use: a term whose English form occurs in the EN page but whose
           Chinese rendering does not occur in the ZH page, or an `avoid` rendering is used.
           Notes never fail the run; they are review hints.

Usage:
  python3 tools/i18n_check.py [--release] [--notes] [--write]
Exit code: 0 clean (warnings/notes allowed), 1 errors, 2 tool error.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EN, ZH = ROOT / "content/en", ROOT / "content/zh"
GLOSSARY = ROOT / "content/data/glossary.yaml"
GLOSSARY_PAGE = ZH / "glossary.md"
PAIRS = (("README.md", "README.zh-CN.md"), ("CONTRIBUTING.md", "CONTRIBUTING.zh-CN.md"))

FRONT_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
STRUCT_RE = re.compile(r"\{#[\w-]+\}|<!-- skill: [^>]*-->|<!-- (?:BEGIN|END) GENERATED: \w+ -->")
BLOCK_RE = re.compile(r"(<!-- BEGIN GENERATED: glossary -->\n)(.*?)(<!-- END GENERATED: glossary -->)", re.S)
CODE_RE = re.compile(r"```.*?```|`[^`\n]*`", re.S)


def split(text: str) -> tuple[dict, str]:
    m = FRONT_RE.match(text)
    return (yaml.safe_load(m.group(1)) or {}, text[m.end():]) if m else ({}, text)


def git(*args: str) -> str | None:
    r = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def glossary_block(g: dict) -> str:
    rows = ["| English | 中文 | 说明 |", "|---|---|---|"]
    for t in sorted(g["terms"], key=lambda t: t["en"].lower()):
        note = t.get("note_zh") or t.get("note", "")
        if t.get("avoid"):
            note = (note + "；" if note else "") + "不用：" + "、".join(t["avoid"])
        rows.append("| " + " | ".join(c.replace("|", "\\|") for c in (t["en"], t["zh"], note)) + " |")
    rows += ["", "以下名称和缩写在中文里保持原文：" + "、".join(f"`{k}`" for k in g["keep"]) + "。"]
    return "\n".join(rows) + "\n"


def term_notes(g: dict, en_body: str, zh_body: str) -> list[str]:
    en_text, zh_text = CODE_RE.sub("", en_body), CODE_RE.sub("", zh_body)
    out = []
    for t in g["terms"]:
        if "(" in t["en"]:  # sense-qualified entries, e.g. "process (DFD)", cannot be matched by text
            continue
        en_term = t["en"]
        if not re.search(rf"\b{re.escape(en_term)}\b", en_text, re.I):
            continue
        if t["zh"] not in zh_text and en_term.lower() not in zh_text.lower():
            out.append(f"'{t['en']}' → expected {t['zh']}")
        out += [f"'{t['en']}': avoided rendering {a}" for a in t.get("avoid", []) if a in zh_text]
    return out


def check_page(rel: Path, g: dict, release: bool, notes: bool) -> tuple[list, list, list]:
    errors, warnings, hints = [], [], []
    en_fm, en_body = split((EN / rel).read_text(encoding="utf-8"))
    zh_path = ZH / rel
    if not zh_path.exists():
        return [f"{rel}: missing Chinese page"], [], []
    zh_fm, zh_body = split(zh_path.read_text(encoding="utf-8"))
    if STRUCT_RE.findall(en_body) != STRUCT_RE.findall(zh_body):
        errors.append(f"{rel}: anchors/markers differ from English")
    if zh_fm.get("translationOf") != f"en/{rel.as_posix()}":
        errors.append(f"{rel}: translationOf should be en/{rel.as_posix()}")
    if not isinstance(zh_fm.get("reviewed"), bool):
        errors.append(f"{rel}: reviewed must be true or false")
    rev = str(zh_fm.get("sourceRev", ""))
    if not rev or git("cat-file", "-e", f"{rev}^{{commit}}") is None:
        errors.append(f"{rel}: sourceRev {rev!r} is not a commit")
    elif git("log", "--format=%h", f"{rev}..HEAD", "--", f"content/en/{rel.as_posix()}"):
        (errors if release else warnings).append(f"{rel}: English changed after sourceRev {rev}")
    if notes:
        hints += [f"{rel}: {n}" for n in term_notes(g, en_body, zh_body)]
    return errors, warnings, hints


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--release", action="store_true", help="treat stale translations as errors")
    ap.add_argument("--notes", action="store_true", help="list glossary-use notes (never fail)")
    ap.add_argument("--write", action="store_true", help="regenerate the glossary page block")
    args = ap.parse_args(argv)
    try:
        g = yaml.safe_load(GLOSSARY.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as e:
        print(f"cannot read glossary: {e}", file=sys.stderr)
        return 2
    errors, warnings, hints = [], [], []

    for en_page in sorted(EN.rglob("*.md")):
        e, w, h = check_page(en_page.relative_to(EN), g, args.release, args.notes)
        errors += e; warnings += w; hints += h
    mirrored = {p.relative_to(EN) for p in EN.rglob("*.md")}
    for zh_page in sorted(ZH.rglob("*.md")):
        rel = zh_page.relative_to(ZH)
        if rel not in mirrored and zh_page != GLOSSARY_PAGE:
            warnings.append(f"{rel}: Chinese page has no English source")

    if GLOSSARY_PAGE.exists():
        text = GLOSSARY_PAGE.read_text(encoding="utf-8")
        new = BLOCK_RE.sub(lambda m: m.group(1) + glossary_block(g) + m.group(3), text)
        if not BLOCK_RE.search(text):
            errors.append("glossary.md: missing GENERATED: glossary block")
        elif new != text:
            if args.write:
                GLOSSARY_PAGE.write_text(new, encoding="utf-8")
                print("wrote content/zh/glossary.md")
            else:
                errors.append("glossary.md: block is out of date (run tools/i18n_check.py --write)")

    for en_name, zh_name in PAIRS:
        heads = [[len(h) for h in re.findall(r"^(#+) ", (ROOT / n).read_text(encoding="utf-8"), re.M)]
                 for n in (en_name, zh_name) if (ROOT / n).exists()]
        if len(heads) == 2 and heads[0] != heads[1]:
            warnings.append(f"{zh_name}: heading levels differ from {en_name}")

    pages = len(mirrored)
    for label, items in (("error", errors), ("warning", warnings), ("note", hints)):
        for item in items:
            print(f"{label}: {item}")
    print(f"i18n_check: {pages} English pages, {len(errors)} errors, {len(warnings)} warnings, "
          f"{len(hints) if args.notes else 'not listed'} notes")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
