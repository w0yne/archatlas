#!/usr/bin/env python3
"""Build one self-contained HTML gallery of the SVGs that evaluation runs produced.

Each run's SVGs under out/ are inlined after sanitising (no scripts, event handlers,
foreignObject or external references; ids prefixed per figure so inline SVGs cannot
collide). Scores and the one-line verdict come from grade.json when present.

Usage: python3 evals/gallery.py RESULTS_DIR [RESULTS_DIR ...] --out gallery/index.html
       [--title "..."] [--intro "..."] [--before EARLIER_RESULTS_DIR ... --labels AFTER BEFORE]
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from adapters import ADAPTERS  # noqa: E402

SVG_NS = "http://www.w3.org/2000/svg"
XLINK = "{http://www.w3.org/1999/xlink}href"
DROP = {"script", "foreignObject", "iframe", "object", "embed", "audio", "video", "canvas"}
DIMS = ("semantic", "structure", "flow", "readability", "compliance", "honesty")
MAX_SVG_BYTES = 2_000_000

ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def sanitise_svg(text: str, prefix: str) -> str | None:
    """Return a safe inline <svg> string, or None if it cannot be parsed."""
    text = re.sub(r"<!DOCTYPE[^>]*>", "", text, flags=re.I)  # no external entities
    try:
        root = ET.fromstring(text)
    except ET.ParseError:
        return None
    if local(root.tag) != "svg":
        return None
    ids = {}
    for parent in list(root.iter()):
        for child in list(parent):
            name = local(child.tag) if isinstance(child.tag, str) else ""
            if name in DROP or not isinstance(child.tag, str):
                parent.remove(child)
                continue
            if name == "style" and re.search(r"@import|url\(\s*['\"]?(?!#)", child.text or "", re.I):
                parent.remove(child)
    for el in root.iter():
        for attr in list(el.attrib):
            value = el.attrib[attr]
            name = local(attr).lower()
            if name.startswith("on"):
                del el.attrib[attr]
            elif attr in ("href", XLINK) and not value.startswith("#") and not value.startswith("data:image/"):
                del el.attrib[attr]
            elif re.search(r"url\(\s*['\"]?(?!#)", value):
                del el.attrib[attr]
        if "id" in el.attrib:
            ids[el.attrib["id"]] = f"{prefix}-{el.attrib['id']}"
            el.attrib["id"] = ids[el.attrib["id"]]
    for el in root.iter():
        for attr, value in list(el.attrib.items()):
            if attr in ("href", XLINK) and value[1:] in ids:
                el.attrib[attr] = "#" + ids[value[1:]]
            elif "url(#" in value:
                el.attrib[attr] = re.sub(r"url\(#([^)]+)\)", lambda m: f"url(#{ids.get(m.group(1), m.group(1))})", value)
    for style in root.iter(f"{{{SVG_NS}}}style"):
        style.text = re.sub(r"#([A-Za-z][\w-]*)", lambda m: "#" + ids.get(m.group(1), m.group(1)), style.text or "")
    # Keep the intrinsic size: figures are shown at 100% in a scrollable frame, because
    # scaling wide figures down to the card makes their 11-12 px labels unreadable.
    vb = (root.get("viewBox") or "").replace(",", " ").split()
    if len(vb) == 4 and not root.get("width"):
        root.set("width", vb[2])
        root.set("height", vb[3])
    root.set("role", "img")
    return ET.tostring(root, encoding="unicode")


def load(dirs: list[Path]) -> list[dict]:
    runs = []
    for d in dirs:
        meta = json.loads((d / "results.json").read_text()).get("meta", {}) if (d / "results.json").exists() else {}
        for rec_path in sorted(d.glob("*/record.json")):
            rec = json.loads(rec_path.read_text())
            run_dir = rec_path.parent
            grade_path = run_dir / "grade.json"
            grade = (json.loads(grade_path.read_text()).get("grade") or {}) if grade_path.exists() else {}
            out = run_dir / "out"
            svgs = [p for p in sorted(out.rglob("*.svg")) if p.stat().st_size <= MAX_SVG_BYTES] if out.exists() else []
            rec.setdefault("skill_rev", meta.get("skill_rev"))
            runs.append({"rec": rec, "grade": grade, "svgs": svgs, "out": out})
    return runs


def mean_of(grade: dict) -> float | None:
    vals = [v for v in (grade.get("scores") or {}).values() if isinstance(v, (int, float))]
    return sum(vals) / len(vals) if vals else None


def panel(key: str, run: dict, label: str) -> str:
    """Scores, verdict and figures of one run; `key` keeps inline SVG ids unique on the page."""
    rec, grade = run["rec"], run["grade"]
    scores = grade.get("scores") or {}
    mean = mean_of(grade)
    gates = dict(grade.get("gates") or {})
    if not ADAPTERS[rec["host"]].traces_image_views:
        gates["G2"] = None  # same rule as report.py: this host's trace cannot show image views
    failed = [k for k, v in gates.items() if v is False]
    visual = grade.get("visual") or {}
    verdict = visual.get("verdict") or grade.get("notes") or "not graded"
    figs = []
    for j, svg in enumerate(run["svgs"]):
        safe = sanitise_svg(svg.read_text(encoding="utf-8", errors="replace"), f"{key}-{j}")
        body = safe if safe else '<p class="bad">SVG could not be parsed</p>'
        figs.append(f'<figure><div class="svg">{body}</div><figcaption>{html.escape(str(svg.relative_to(run["out"])))}</figcaption></figure>')
    if not figs:
        figs.append('<p class="bad">No SVG under out/</p>')
    score_cells = "".join(f"<td>{html.escape(str(scores.get(d, '–')))}</td>" for d in DIMS)
    issues = "".join(f"<li>{html.escape(str(x))}</li>" for x in (visual.get("issues") or []))
    return f"""<div class="panel">{f'<h3>{html.escape(label)}</h3>' if label else ''}
<p class="meta">{html.escape(str(rec.get('model', '')))} · mode {html.escape(str(rec.get('mode')))} · skill {html.escape(str(rec.get('skill_rev', '')))} ·
cost ${rec.get('cost_est_usd') or 0:.2f} · {rec.get('wall_s') or 0:.0f} s · gates: {html.escape(', '.join(failed) + ' failed' if failed else 'all pass')}</p>
<p class="verdict"><b>Visual {html.escape(str(visual.get('score', '–')))}/3</b> · rubric mean {'–' if mean is None else f'{mean:.2f}'} — {html.escape(verdict)}</p>
<div class="scroll"><table><tr>{''.join(f'<th>{d}</th>' for d in DIMS)}<th>hierarchy</th><th>zones</th><th>visual readability</th></tr>
<tr>{score_cells}<td>{visual.get('hierarchy', '–')}</td><td>{visual.get('zones', '–')}</td><td>{visual.get('readability', '–')}</td></tr></table></div>
{f'<ul class="issues">{issues}</ul>' if issues else ''}
{''.join(figs)}
</div>"""


def card(i: int, run: dict, scenarios: dict, before: dict | None = None,
         labels: tuple[str, str] = ("", "")) -> str:
    rec = run["rec"]
    sc = scenarios.get(rec["scenario"], {})
    head = f"<h2>{html.escape(rec['scenario'])} · {html.escape(sc.get('title', ''))} · {html.escape(rec['host'])}</h2>"
    if before is None:
        return f'<section class="run" id="{html.escape(rec["run"])}"><header>{head}</header>{panel(f"g{i}", run, "")}</section>'
    a, b = mean_of(run["grade"]), mean_of(before["grade"])
    va, vb = (run["grade"].get("visual") or {}).get("score"), (before["grade"].get("visual") or {}).get("score")
    delta = (f"rubric {b:.2f} → {a:.2f}" if a is not None and b is not None else "rubric –") + f" · visual {vb} → {va}"
    return f"""<section class="run" id="{html.escape(rec['run'])}"><header>{head}<p class="delta">{labels[1]} → {labels[0]}: {html.escape(delta)}</p></header>
<div class="pair">{panel(f"g{i}a", run, labels[0])}{panel(f"g{i}b", before, labels[1])}</div></section>"""


CSS = """body{font-family:system-ui,-apple-system,"Segoe UI","Noto Sans","Noto Sans CJK SC",sans-serif;margin:0;color:#1f2937;background:#f6f7f9}
main{max-width:1860px;margin:0 auto;padding:24px}h1{font-size:28px;margin:8px 0}.intro{color:#4b5563;max-width:80ch}
nav ul{display:flex;flex-wrap:wrap;gap:6px;padding:0;list-style:none}nav a{display:block;padding:4px 10px;border-radius:12px;background:#d8e8ff;color:#03172e;text-decoration:none;font-size:13px}
.run{background:#fff;border:1px solid #d1d5db;border-radius:10px;padding:16px 20px;margin:20px 0}.run h2{font-size:20px;margin:0 0 4px}
.meta{color:#4b5563;font-size:13px;margin:0}.verdict{font-size:15px}.bad{color:#b34232}
table{border-collapse:collapse;font-size:12px;margin:6px 0}th,td{border:1px solid #e5e7eb;padding:3px 7px;text-align:center}th{background:#f3f4f6;font-weight:600}
.scroll{overflow-x:auto}.run,.verdict,.meta,.issues{overflow-wrap:anywhere}.issues{font-size:13px;color:#4b5563}figure{margin:14px 0}.svg{border:1px solid #e5e7eb;border-radius:6px;padding:8px;background:#fff;overflow:auto}
.svg svg{display:block;max-width:none;height:auto}
.pair{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,560px),1fr));gap:16px}.panel{min-width:0}
.panel h3{font-size:16px;margin:10px 0 2px}.delta{font-size:14px;margin:2px 0 0;color:#03172e}figcaption{font-size:12px;color:#6b7280;margin-top:4px}"""


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("results", type=Path, nargs="+")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--title", default="Skill test gallery")
    ap.add_argument("--intro", default="")
    ap.add_argument("--before", type=Path, action="append", default=[],
                    help="earlier results dir(s): each run is shown next to the earlier run of the same scenario and host")
    ap.add_argument("--labels", nargs=2, default=["After", "Before"], metavar=("AFTER", "BEFORE"))
    args = ap.parse_args(argv)
    from run_eval import load_scenarios
    scenarios = load_scenarios()
    runs = sorted(load(args.results), key=lambda r: (int(r["rec"]["scenario"][1:]), r["rec"]["host"]))
    nav = "".join(f'<li><a href="#{html.escape(r["rec"]["run"])}">{html.escape(r["rec"]["scenario"])} · {html.escape(r["rec"]["host"])}</a></li>' for r in runs)
    earlier = {(r["rec"]["scenario"], r["rec"]["host"]): r for r in load(args.before)}
    body = "\n".join(card(i, r, scenarios, earlier.get((r["rec"]["scenario"], r["rec"]["host"])) if args.before else None,
                          tuple(args.labels)) for i, r in enumerate(runs))
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(args.title)}</title><style>{CSS}</style></head><body><main>
<h1>{html.escape(args.title)}</h1><p class="intro">{html.escape(args.intro)}</p><nav><ul>{nav}</ul></nav>
{body}
</main></body></html>"""
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(page, encoding="utf-8")
    print(f"wrote {args.out} ({len(runs)} runs, {sum(len(r['svgs']) for r in runs)} figures)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
