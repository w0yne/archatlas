#!/usr/bin/env python3
"""Keep type-page front matter in step with the catalogue (content/data/types.yaml).

types.yaml is the single source for these front-matter fields of every
content/{en,zh}/types/*.md page:
  code, slug, family, names.en, names.zh, names.aliases, audiences, levels,
  phases, neighbours, formal.kind
Other front-matter fields (question, scope, formal.ref, status, translation
metadata) belong to the page.

Checks (default):
  - every page's synced fields equal the catalogue
  - catalogue neighbours are bidirectional
  - every neighbour code is explained in the page's #choose section (EN and ZH)
Usage:
  python3 tools/check_front_matter.py          check; exit 1 on drift
  python3 tools/check_front_matter.py --write  rewrite the synced fields from the catalogue
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / "content" / "data" / "types.yaml"
LANGS = ("en", "zh")
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
CHOOSE_RE = re.compile(r"\{#choose\}\n(.*?)(?=\n## |\Z)", re.S)


def expected(t: dict) -> dict:
    return {
        "code": t["code"], "slug": t["slug"], "family": t["family"],
        "names": {"en": t["names"]["en"], "zh": t["names"]["zh"],
                  "aliases": {"en": list(t["aliases"].get("en", [])), "zh": list(t["aliases"].get("zh", []))}},
        "audiences": list(t["audiences"]), "levels": list(t["levels"]), "phases": list(t["phases"]),
        "neighbours": list(t["neighbours"]), "formal.kind": t["formal"]["kind"],
    }


def actual(fm: dict) -> dict:
    names = fm.get("names") or {}
    return {
        "code": fm.get("code"), "slug": fm.get("slug"), "family": fm.get("family"),
        "names": {"en": names.get("en"), "zh": names.get("zh"), "aliases": names.get("aliases")},
        "audiences": fm.get("audiences"), "levels": fm.get("levels"), "phases": fm.get("phases"),
        "neighbours": fm.get("neighbours"), "formal.kind": (fm.get("formal") or {}).get("kind"),
    }


def pages(lang: str) -> list[Path]:
    return sorted((ROOT / "content" / lang / "types").glob("*.md"))


def split(path: Path) -> tuple[dict, str, str]:
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if not m:
        raise ValueError(f"{path}: missing front matter")
    return yaml.safe_load(m.group(1)) or {}, m.group(1), text[m.end():]


def synced(fm: dict, want: dict) -> dict:
    """Return the front matter with catalogue fields replaced, page fields kept in place."""
    out = {}
    for key, value in fm.items():
        if key == "level":
            out["levels"] = want["levels"]
        elif key == "formal":
            out["formal"] = {"kind": want["formal.kind"], **{k: v for k, v in (value or {}).items() if k != "kind"}}
        elif key in want:
            out[key] = want[key]
        else:
            out[key] = value
    for key in ("code", "slug", "family", "names", "audiences", "levels", "phases", "neighbours"):
        out.setdefault(key, want[key])
    out.setdefault("formal", {"kind": want["formal.kind"]})
    return out


def dump(fm: dict) -> str:
    return yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100000, default_flow_style=None).rstrip("\n")


def check(cat: dict) -> list[str]:
    types = {t["code"]: t for t in cat["types"]}
    problems = []
    for code, t in types.items():
        for n in t["neighbours"]:
            if code not in types.get(n, {}).get("neighbours", []):
                problems.append(f"types.yaml: {code} lists neighbour {n}, but {n} does not list {code}")
    for lang in LANGS:
        seen = set()
        for path in pages(lang):
            rel = path.relative_to(ROOT)
            fm, _, body = split(path)
            code = fm.get("code")
            if code not in types:
                problems.append(f"{rel}: code {code!r} is not in the catalogue")
                continue
            seen.add(code)
            want, have = expected(types[code]), actual(fm)
            for key in want:
                if want[key] != have[key]:
                    problems.append(f"{rel}: {key} differs from types.yaml (run tools/check_front_matter.py --write)")
            if "level" in fm:
                problems.append(f"{rel}: use `levels` (list), not `level`")
            m = CHOOSE_RE.search(body)
            mentioned = set(re.findall(r"\b([A-I][1-9])\b", m.group(1))) if m else set()
            for n in types[code]["neighbours"]:
                if n not in mentioned:
                    problems.append(f"{rel}: neighbour {n} is not explained in #choose")
        for code in sorted(set(types) - seen):
            problems.append(f"content/{lang}/types: no page for {code}")
    return problems


def write(cat: dict) -> int:
    types = {t["code"]: t for t in cat["types"]}
    changed = 0
    for lang in LANGS:
        for path in pages(lang):
            fm, raw, body = split(path)
            if fm.get("code") not in types:
                continue
            new = synced(fm, expected(types[fm["code"]]))
            if new != fm or "level" in fm:
                path.write_text(f"---\n{dump(new)}\n---\n{body}", encoding="utf-8")
                changed += 1
    return changed


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--write", action="store_true", help="rewrite synced fields from the catalogue")
    args = ap.parse_args(argv)
    cat = yaml.safe_load(CATALOGUE.read_text(encoding="utf-8"))
    if args.write:
        print(f"updated {write(cat)} page(s)")
    problems = check(cat)
    for p in problems:
        print(p, file=sys.stderr)
    print(f"check_front_matter: {len(problems)} problem(s)", file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
