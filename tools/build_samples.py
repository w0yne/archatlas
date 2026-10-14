#!/usr/bin/env python3
"""Render one sample SVG per diagram type for the site and the skill references.

Inputs (single source):
  content/en/types/<code>-<slug>.md                         the list of types
  examples/*/diagram.json                                   a worked example whose meta.type is the type code wins
  skills/architecture-diagrams/assets/templates/<code>.json otherwise the model template is rendered

Outputs (generated, do not edit by hand):
  content/public/samples/<code>-<slug>.svg                  English
  content/public/samples/<code>-<slug>.zh.svg               only when `labels.zh.json` sits beside the model

Every sample is checked with the renderer's own checks (warnings count as failures) and against its model.
SVG ids use a fixed namespace, so the output does not depend on the output path. Measured text depends on
the installed fonts: run `atlas fonts doctor` first, and expect --check to differ on a machine with other fonts.

Usage (needs the renderer on the path, e.g. `pip install -e .` or PYTHONPATH=src):
  python3 tools/build_samples.py           write outputs
  python3 tools/build_samples.py --check   exit 1 if a sample fails its checks or is out of date
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from archatlas.check import check_svg  # noqa: E402
from archatlas.cli import main as atlas  # noqa: E402
from archatlas.fonts import FontMetrics  # noqa: E402
from archatlas.layout import layout  # noqa: E402
from archatlas.model import load  # noqa: E402
from archatlas.render import render_svg  # noqa: E402

PAGES = ROOT / "content/en/types"
TEMPLATES = ROOT / "skills/architecture-diagrams/assets/templates"
EXAMPLES = ROOT / "examples"
OUT = ROOT / "content/public/samples"


def sources() -> dict[str, Path]:
    """Map type code to the model that draws its sample."""
    models = {path.stem: path for path in TEMPLATES.glob("*.json")}
    for path in sorted(EXAMPLES.glob("*/diagram.json")):
        models[json.loads(path.read_text(encoding="utf-8"))["meta"]["type"]] = path
    return models


def render_all(target: Path) -> list[str]:
    problems, models, metrics = [], sources(), FontMetrics()
    for page in sorted(PAGES.glob("*.md")):
        code, _, _ = page.stem.partition("-")
        model = models.get(code)
        if model is None:
            problems.append(f"{page.name}: no model template or example for {code}")
            continue
        for lang in ("en", "zh"):
            if lang == "zh" and not (model.parent / "labels.zh.json").exists():
                continue
            svg = render_svg(layout(load(str(model), lang), metrics), f"{code.lower()}-{lang}")
            path = target / (page.stem + (".zh" if lang == "zh" else "") + ".svg")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(svg, encoding="utf-8")
            report = check_svg(svg, metrics)
            for finding in report["findings"]:
                problems.append(f"{path.name}: {finding['severity']} {finding['rule']}: {finding['message']}")
            with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()):
                if atlas(["check", str(path), "--model", str(model), "--report", f"{tmp}/report.json"]):
                    problems.append(f"{path.name}: the SVG does not match its model")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--check", action="store_true", help="do not write; exit 1 on failed checks or stale samples")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) if args.check else OUT
        problems = render_all(target)
        names = {p.name for p in target.glob("*.svg")}
        if not args.check:
            for stale in sorted(p for p in OUT.glob("*.svg") if p.name not in names):
                stale.unlink()
        else:
            for name in sorted(names):
                committed = OUT / name
                if not committed.exists():
                    problems.append(f"{name}: missing; run tools/build_samples.py")
                elif committed.read_bytes() != (Path(tmp) / name).read_bytes():
                    problems.append(f"{name}: stale; run tools/build_samples.py")
            problems += [f"{p.name}: has no source" for p in sorted(OUT.glob("*.svg")) if p.name not in names]
    for problem in problems:
        print(problem, file=sys.stderr)
    if problems:
        print(f"{len(problems)} problem(s)", file=sys.stderr)
        return 1
    print("samples up to date" if args.check else "samples written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
