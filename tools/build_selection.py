#!/usr/bin/env python3
"""Build the type-selection guide from the content model.

Inputs (single source):
  content/data/types.yaml           catalogue of diagram types and facets
  content/data/selection-tree.yaml  decision tree by question asked

Outputs (generated, do not edit by hand):
  skills/architecture-diagrams/references/selection.md   skill reference (English)
  content/data/choose.json                               data for the site choose page (EN + ZH)
  content/en/choose.md, content/zh/choose.md             blocks between GENERATED markers

Usage:
  python3 tools/build_selection.py           write outputs
  python3 tools/build_selection.py --check   exit 1 if an output is out of date
"""
from __future__ import annotations

import argparse
from copy import deepcopy
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TYPES_FILE = ROOT / "content/data/types.yaml"
TREE_FILE = ROOT / "content/data/selection-tree.yaml"
SELECTION_MD = ROOT / "skills/architecture-diagrams/references/selection.md"
REF_DIR = SELECTION_MD.parent / "types"
CHOOSE_JSON = ROOT / "content/data/choose.json"
CHOOSE_MD = {"en": ROOT / "content/en/choose.md", "zh": ROOT / "content/zh/choose.md"}

REQUIRED = ("code", "slug", "family", "names", "aliases", "question", "asks", "audiences",
            "levels", "phases", "scope", "formal", "standards", "neighbours", "research", "status")
LIST_FACETS = {"asks": "asks", "audiences": "audiences", "levels": "levels", "phases": "phases"}
FORMAL_KINDS = {"standard", "method", "convention"}
RESEARCH = {"done", "pending"}
STATUS = {"draft", "reviewed"}
CHANGE_KINDS = {"split", "rename", "scope", "fact"}
CODE_RE = re.compile(r"^[A-I][1-9][0-9]?$")
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


class ModelError(Exception):
    """The content model violates an invariant; the message lists every problem."""


def code_key(code: str) -> tuple[str, int]:
    return code[0], int(code[1:])


def norm(text: str) -> str:
    return " ".join(text.casefold().split())


def page(t: dict) -> str:
    """Site URL path segment (lower case)."""
    return f"{t['code'].lower()}-{t['slug']}"


def ref_file(t: dict) -> str:
    """Skill reference file name; matches the case-sensitive file in references/types/."""
    return f"{t['code']}-{t['slug']}.md"


def load(types_file: Path = TYPES_FILE, tree_file: Path = TREE_FILE) -> tuple[dict, dict]:
    with types_file.open(encoding="utf-8") as f:
        cat = yaml.safe_load(f)
    with tree_file.open(encoding="utf-8") as f:
        tree = yaml.safe_load(f)
    # Taxonomy remains in types.yaml; reader-specific advice belongs to the tree.
    cat = deepcopy(cat)
    terms = {norm(term['en']): term for term in cat.get('terms', [])}
    for term in tree.get('reader_terms', []):
        terms[norm(term['en'])] = term
    cat['terms'] = list(terms.values())
    for key in ('common_requests', 'matrix_overrides', 'phase_picks'):
        cat[key] = tree.get(key, [] if key != 'phase_picks' else {})
    validate(cat, tree)
    return cat, tree


def _bilingual(value, where: str, errors: list[str]) -> None:
    if not (isinstance(value, dict) and value.get("en") and value.get("zh")):
        errors.append(f"{where}: needs non-empty 'en' and 'zh'")


def validate(cat: dict, tree: dict) -> None:
    errors: list[str] = []
    facets = cat["facets"]
    types = cat["types"]
    codes = [t.get("code") for t in types]
    known = set(codes)

    for dup in sorted({c for c in codes if codes.count(c) > 1}):
        errors.append(f"duplicate code {dup}")
    slugs = [t.get("slug") for t in types]
    for dup in sorted({s for s in slugs if slugs.count(s) > 1}):
        errors.append(f"duplicate slug {dup}")

    alias_owner: dict[str, str] = {}
    for t in types:
        c = t.get("code", "?")
        missing = [k for k in REQUIRED if k not in t or t[k] in (None, "", [])]
        if missing:
            errors.append(f"{c}: missing {', '.join(missing)}")
            continue
        if not CODE_RE.match(c) or c[0] != t["family"]:
            errors.append(f"{c}: code must be <family letter><number> matching family {t['family']}")
        if t["family"] not in cat["families"]:
            errors.append(f"{c}: unknown family {t['family']}")
        if not SLUG_RE.match(t["slug"]):
            errors.append(f"{c}: slug {t['slug']!r} is not kebab-case")
        _bilingual(t["names"], f"{c}.names", errors)
        _bilingual(t["question"], f"{c}.question", errors)
        for field, facet in LIST_FACETS.items():
            bad = [v for v in t[field] if v not in facets[facet]]
            if bad:
                errors.append(f"{c}.{field}: unknown {bad}")
        if t["scope"] not in facets["scope"]:
            errors.append(f"{c}.scope: unknown {t['scope']}")
        if t["formal"].get("kind") not in FORMAL_KINDS or not t["formal"].get("basis"):
            errors.append(f"{c}.formal: needs kind in {sorted(FORMAL_KINDS)} and a basis")
        for s in t["standards"]:
            if not (s.get("name") and str(s.get("url", "")).startswith("https://")):
                errors.append(f"{c}.standards: each needs a name and an https url")
        bad = [n for n in t["neighbours"] if n not in known or n == c]
        if bad:
            errors.append(f"{c}.neighbours: unknown or self {bad}")
        if t["research"] not in RESEARCH:
            errors.append(f"{c}.research: must be one of {sorted(RESEARCH)}")
        if t["status"] not in STATUS:
            errors.append(f"{c}.status: must be one of {sorted(STATUS)}")
        for ch in t.get("changes", []):
            if ch.get("kind") not in CHANGE_KINDS or not ch.get("note"):
                errors.append(f"{c}.changes: each needs kind in {sorted(CHANGE_KINDS)} and a note")
        if "split_from" in t:
            if t["split_from"] not in known:
                errors.append(f"{c}.split_from: unknown {t['split_from']}")
            if not any(ch.get("kind") == "split" for ch in t.get("changes", [])):
                errors.append(f"{c}: split_from requires a 'split' change note")
        names = {norm(t["names"]["en"]), norm(t["names"]["zh"])}
        for lang in ("en", "zh"):
            for a in t["aliases"].get(lang, []):
                key = norm(a)
                if key in alias_owner and alias_owner[key] != c:
                    errors.append(f"alias {a!r} is on {alias_owner[key]} and {c}; move it to terms")
                alias_owner[key] = c
                if key in names:
                    errors.append(f"{c}: alias {a!r} repeats the canonical name")

    for term in cat.get("terms", []):
        _bilingual(term.get("note"), f"term {term.get('en')!r}.note", errors)
        if not term.get("en") or not term.get("zh"):
            errors.append(f"term {term!r}: needs en and zh")
        if not term.get("types") or any(x not in known for x in term["types"]):
            errors.append(f"term {term.get('en')!r}: types must be existing codes")
        for key in (norm(term.get("en", "")), norm(term.get("zh", ""))):
            if key in alias_owner:
                errors.append(f"term {key!r} is also an alias of {alias_owner[key]}")

    root = tree["root"]
    if set(root) != set(facets["asks"]):
        errors.append(f"tree branches {sorted(root)} must equal asks facets {sorted(facets['asks'])}")
    by_code = {t["code"]: t for t in types if "code" in t}
    reached: set[str] = set()
    for branch, leaves in root.items():
        for leaf in leaves:
            _bilingual(leaf.get("when"), f"tree {branch}.when", errors)
            if "hint" in leaf:
                _bilingual(leaf["hint"], f"tree {branch}.hint", errors)
            for c in leaf.get("types") or []:
                if c not in by_code:
                    errors.append(f"tree {branch}: unknown type {c}")
                    continue
                reached.add(c)
                if branch not in by_code[c].get("asks", []):
                    if not leaf.get('cross_facet_reason'):
                        errors.append(f"tree {branch}: {c} lacks asks facet {branch!r}; explain cross_facet_reason")
                    else:
                        _bilingual(leaf['cross_facet_reason'], f'tree {branch}.cross_facet_reason', errors)
            if not leaf.get("types"):
                errors.append(f"tree {branch}: leaf without types")
    unreached = sorted(known - reached, key=code_key)
    if unreached:
        errors.append(f"tree does not reach {unreached}")
    for q in tree.get("first_questions", []):
        _bilingual(q, "first_questions", errors)

    for row in cat.get('common_requests', []):
        _bilingual(row.get('request'), 'common request', errors)
        _bilingual(row.get('note'), 'common request note', errors)
        if row.get('first') not in known or any(c not in known for c in row.get('next', [])):
            errors.append('common request refers to an unknown type')
    cells = set()
    for row in cat.get('matrix_overrides', []):
        key = (row.get('audience'), row.get('ask'))
        if key in cells:
            errors.append('duplicate matrix override')
        cells.add(key)
        if row.get('audience') not in facets['audiences'] or row.get('ask') not in facets['asks']:
            errors.append('matrix override has unknown facets')
        if not row.get('types') or any(c not in known for c in row['types']):
            errors.append('matrix override has unknown types')
        _bilingual(row.get('note'), 'matrix override note', errors)
    for phase, picks in cat.get('phase_picks', {}).items():
        if phase not in facets['phases'] or not 2 <= len(picks) <= 4 or len(set(picks)) != len(picks) or any(c not in known for c in picks):
            errors.append('phase picks need a known phase and 2–4 known types')

    if errors:
        raise ModelError("\n".join(errors))


# ------------------------------------------------------------------ derived data

def sorted_types(cat: dict) -> list[dict]:
    return sorted(cat["types"], key=lambda t: code_key(t["code"]))


def matrix(cat: dict) -> dict[str, dict[str, list[str]]]:
    """audience -> asks -> codes (both facets present on the type)."""
    out: dict[str, dict[str, list[str]]] = {}
    for aud in cat["facets"]["audiences"]:
        out[aud] = {}
        for ask in cat["facets"]["asks"]:
            out[aud][ask] = [t["code"] for t in sorted_types(cat)
                             if aud in t["audiences"] and ask in t["asks"]]
    for row in cat.get('matrix_overrides', []):
        out[row['audience']][row['ask']] = row['types']
    return out


def by_phase(cat: dict) -> dict[str, list[str]]:
    return {p: [t["code"] for t in sorted_types(cat) if p in t["phases"]]
            for p in cat["facets"]["phases"]}


def alias_index(cat: dict) -> list[dict]:
    rows = []
    for t in sorted_types(cat):
        for lang in ("en", "zh"):
            for a in t["aliases"].get(lang, []):
                rows.append({"text": a, "lang": lang, "code": t["code"]})
    return sorted(rows, key=lambda r: (r["lang"], norm(r["text"])))


def choose_data(cat: dict, tree: dict) -> dict:
    keep = ("code", "slug", "family", "names", "question", "asks", "audiences",
            "levels", "phases", "scope", "research")
    return {
        "generated_from": ["content/data/types.yaml", "content/data/selection-tree.yaml"],
        "families": cat["families"],
        "facets": cat["facets"],
        "types": [{k: t[k] for k in keep} | {"page": page(t)} for t in sorted_types(cat)],
        "first_questions": tree["first_questions"],
        "common_requests": cat.get('common_requests', []),
        "matrix_overrides": cat.get('matrix_overrides', []),
        "phase_picks": cat.get('phase_picks', {}),
        "tree": tree["root"],
        "matrix": matrix(cat),
        "phases": by_phase(cat),
        "aliases": alias_index(cat),
        "terms": cat.get("terms", []),
    }


# ------------------------------------------------------------------ rendering

def _codes(codes: list[str], link, lang: str = 'en') -> str:
    return ('、' if lang == 'zh' else ', ').join(link(c) for c in codes) if codes else '–'


def render_common(cat: dict, lang: str, link) -> list[str]:
    first, later = ('先选', '再考虑') if lang == 'zh' else ('Start with', 'Then consider')
    colon, stop = ('：', '。') if lang == 'zh' else (': ', '. ')
    return [f"- **{row['request'][lang]}**{colon}{first}{colon}{link(row['first'])}{stop}"
            f"{later}{colon}{_codes(row.get('next', []), link, lang)}{stop}{row['note'][lang]}"
            for row in cat.get('common_requests', [])]


def render_audiences(cat: dict, lang: str, link) -> list[str]:
    result = []
    for audience, cells in matrix(cat).items():
        result += [f"<details><summary>{cat['facets']['audiences'][audience][lang]}</summary>", '']
        result += [f"- **{cat['facets']['asks'][ask][lang]}** {'：' if lang == 'zh' else ': '}{_codes(codes, link, lang)}"
                   for ask, codes in cells.items() if codes]
        result += ['', '</details>', '']
    return result


def render_tree(cat: dict, tree: dict, lang: str, link) -> list[str]:
    asks = cat["facets"]["asks"]
    lines = []
    for branch, leaves in tree["root"].items():
        lines.append(f"- **{asks[branch][lang]}**")
        for leaf in leaves:
            line = f"  - {leaf['when'][lang]} → {_codes(leaf['types'], link, lang)}"
            if "hint" in leaf:
                line += ('。' if lang == 'zh' else '. ') + leaf['hint'][lang]
            lines.append(line)
    return lines


def render_matrix(cat: dict, lang: str, link) -> list[str]:
    f = cat["facets"]
    m = matrix(cat)
    head = [f["audiences"][a][lang] for a in f["audiences"]]
    lines = ["| " + ("Question" if lang == "en" else "问题") + " | " + " | ".join(head) + " |",
             "|---" * (len(head) + 1) + "|"]
    for ask in f["asks"]:
        cells = [_codes(m[a][ask], link, lang) for a in f["audiences"]]
        lines.append(f"| {f['asks'][ask][lang]} | " + " | ".join(cells) + " |")
    return lines


def render_phases(cat: dict, lang: str, link) -> list[str]:
    phases = cat["facets"]["phases"]
    result = []
    for phase, codes in by_phase(cat).items():
        picks = cat.get('phase_picks', {}).get(phase, codes[:3])
        rest = [code for code in codes if code not in picks]
        result.append(f"- **{phases[phase][lang]}** {'：' if lang == 'zh' else ': '}{_codes(picks, link, lang)}")
        if rest:
            result += [f"<details><summary>{'其他可选类型' if lang == 'zh' else 'Also useful'}</summary>", '', _codes(rest, link, lang), '', '</details>', '']
    return result


def render_terms(cat: dict, lang: str, link) -> list[str]:
    lines = []
    for term in cat.get("terms", []):
        label = term["en"] if lang == "en" else f"{term['zh']}（{term['en']}）"
        lines.append(f"- *{label}* → {_codes(term['types'], link, lang)}{'。' if lang == 'zh' else '. '}{term['note'][lang]}")
    return lines


def render_selection_md(cat: dict, tree: dict) -> str:
    by_code = {t['code']: t for t in cat['types']}
    def link(c: str) -> str:
        return c + ' ' + by_code[c]['names']['en']

    types = sorted_types(cat)
    out = [
        "<!-- Generated by tools/build_selection.py from content/data/types.yaml and",
        "     content/data/selection-tree.yaml. Do not edit by hand. -->",
        "# Choosing a diagram type",
        "",
        "Use this file to pick one or two types before drawing. Then read",
        "`types/<code>-<slug>.md` (for example `types/C3-container-diagram.md`) for the chosen type only.",
        "",
        "## 1. First questions",
        "",
    ]
    out += render_common(cat, 'en', link)
    out += ['', 'For a less common request, establish:', '']
    out += [f"{i}. {q['en']}" for i, q in enumerate(tree["first_questions"], 1)]
    out += ["", "In autonomous mode, infer the answers and state them as assumptions. "
            "In guided mode, ask them one at a time with a recommended default.", "",
            "## 2. Decision tree (by the question the figure must answer)", ""]
    out += render_tree(cat, tree, "en", link)
    out += ["", "Name the chosen type and one runner-up, each with a one-line reason. "
            "If the reader needs answers to two questions, draw two figures.", "",
            "## 3. Audience × question matrix", "",
            "Cells list types that suit both the audience and the question. A '–' means no type "
            "targets that pair: pick the type from the reader's question, then simplify it for the "
            "audience (fewer elements, business names, no protocols) and say that you simplified.", ""]
    out += render_matrix(cat, "en", link)
    out += ["", "## 4. Lifecycle phase", ""]
    out += render_phases(cat, "en", link)
    out += ["", "## 5. Ambiguous names people use", "",
            "These names do not identify one type. Ask which is meant, or pick one and say so.", ""]
    out += render_terms(cat, "en", link)
    out += ["", "## 6. Catalogue and aliases", "",
            "Formal: S = formal standard, M = published method, C = convention only. "
            "Research: `pending` means the type page is not yet based on phase-2 research. "
            "Reference `none yet`: no type reference exists; follow SKILL.md Step 4 for that case.", "",
            "| Code | Type | Reference | Formal | Answers | Also called |",
            "|---|---|---|---|---|---|"]
    for t in types:
        aliases = "; ".join(t["aliases"].get("en", []) + t["aliases"].get("zh", []))
        formal = t["formal"]["kind"][0].upper()
        pending = " (research pending)" if t["research"] == "pending" else ""
        ref = f"`types/{ref_file(t)}`" if (REF_DIR / ref_file(t)).exists() else "none yet"
        out.append(f"| {t['code']} | {t['names']['en']}{pending} | {ref} | {formal} | "
                   f"{t['question']['en']} | {aliases} |")
    return "\n".join(out) + "\n"


BLOCK_RE = re.compile(r"(<!-- BEGIN GENERATED: (\w+) -->\n)(.*?)(<!-- END GENERATED: \2 -->)", re.S)


def render_choose_blocks(cat: dict, tree: dict, lang: str = "en") -> dict[str, str]:
    by_code = {t["code"]: t for t in cat["types"]}
    prefix = "" if lang == "en" else f"/{lang}"

    def link(c: str) -> str:
        return f"[{c} {by_code[c]['names'][lang]}]({prefix}/types/{page(by_code[c])})"

    head = "| Code | Type | Answers |" if lang == "en" else "| 代码 | 类型 | 回答的问题 |"
    catalogue = [head, "|---|---|---|"]
    catalogue += [f"| [{t['code']}]({prefix}/types/{page(t)}) | {t['names'][lang]} | {t['question'][lang]} |"
                  for t in sorted_types(cat)]
    aliases = [f"- {r['text']} → {link(r['code'])}" for r in alias_index(cat) if r["lang"] == lang]
    blocks = {
        "common": render_common(cat, lang, link),
        "audiences": render_audiences(cat, lang, link),
        "questions": [f"{i}. {q[lang]}" for i, q in enumerate(tree["first_questions"], 1)],
        "tree": render_tree(cat, tree, lang, link),
        "matrix": render_matrix(cat, lang, link),
        "phases": render_phases(cat, lang, link),
        "terms": render_terms(cat, lang, link),
        "aliases": aliases,
        "catalogue": catalogue,
    }
    return {k: "\n".join(v) + "\n" for k, v in blocks.items()}


def fill_blocks(text: str, blocks: dict[str, str]) -> str:
    seen = set()

    def repl(m: re.Match) -> str:
        name = m.group(2)
        if name not in blocks:
            raise ModelError(f"choose.md: unknown generated block {name!r}")
        seen.add(name)
        return m.group(1) + blocks[name] + m.group(4)

    result = BLOCK_RE.sub(repl, text)
    missing = sorted(set(blocks) - seen)
    if missing:
        raise ModelError(f"choose.md: missing generated blocks {missing}")
    return result


def build(cat: dict, tree: dict, choose_md_texts: dict[str, str]) -> dict[Path, str]:
    """choose_md_texts: lang -> current choose page text (a language without a page is skipped)."""
    out = {
        SELECTION_MD: render_selection_md(cat, tree),
        CHOOSE_JSON: json.dumps(choose_data(cat, tree), ensure_ascii=False, indent=2) + "\n",
    }
    for lang, text in choose_md_texts.items():
        out[CHOOSE_MD[lang]] = fill_blocks(text, render_choose_blocks(cat, tree, lang))
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="fail if outputs are out of date")
    args = ap.parse_args(argv)
    try:
        cat, tree = load()
        outputs = build(cat, tree, {lang: p.read_text(encoding="utf-8")
                                    for lang, p in CHOOSE_MD.items() if p.exists()})
    except ModelError as e:
        print(f"content model errors:\n{e}", file=sys.stderr)
        return 1
    stale = [p for p, text in outputs.items()
             if not p.exists() or p.read_text(encoding="utf-8") != text]
    if args.check:
        for p in stale:
            print(f"out of date: {p.relative_to(ROOT)}", file=sys.stderr)
        return 1 if stale else 0
    for p in stale:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(outputs[p], encoding="utf-8")
        print(f"wrote {p.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
