#!/usr/bin/env python3
"""Build historical rendered samples and manifest-driven hand-authored AI samples.

Inputs (single source):
  examples/ai-service-assistant/manifest.json               authored SVG/model pairs
  content/en/types/<code>-<slug>.md                          the list of types
  skills/architecture-diagrams/assets/templates/<code>.json  the model that draws the sample
  skills/architecture-diagrams/assets/templates/zh/<code>.json  optional Chinese labels: English label text -> Chinese

Outputs (generated copies; edit authored sources under examples/):
  content/public/samples/<code>-<slug>.svg                   English
  content/public/samples/<code>-<slug>.zh.svg                only when a Chinese label file exists

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
from scenario_samples import sample_files  # noqa: E402

PAGES = ROOT / "content/en/types"
TEMPLATES = ROOT / "skills/architecture-diagrams/assets/templates"
OUT = ROOT / "content/public/samples"


def render_all(target: Path) -> list[str]:
    problems, metrics = [], FontMetrics()
    for page in sorted(PAGES.glob("*.md")):
        code, _, _ = page.stem.partition("-")
        source = TEMPLATES / f"{code}.json"
        if not source.exists():
            problems.append(f"{page.name}: no model template for {code}")
            continue
        for lang in ("en", "zh"):
            labels = TEMPLATES / "zh" / f"{code}.json"
            if lang == "zh" and not labels.exists():
                continue
            with tempfile.TemporaryDirectory() as tmp:
                # The loader reads labels.<lang>.json beside the model, so give it a private copy of both.
                model = Path(tmp) / "diagram.json"
                model.write_bytes(source.read_bytes())
                if lang == "zh":
                    (Path(tmp) / "labels.zh.json").write_bytes(labels.read_bytes())
                svg = render_svg(layout(load(str(model), lang), metrics), f"{code.lower()}-{lang}")
                path = target / (page.stem + (".zh" if lang == "zh" else "") + ".svg")
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(svg, encoding="utf-8")
                for finding in check_svg(svg, metrics)["findings"]:
                    problems.append(f"{path.name}: {finding['severity']} {finding['rule']}: {finding['message']}")
                with contextlib.redirect_stdout(io.StringIO()):
                    if atlas(["check", str(path), "--model", str(model), "--report", f"{tmp}/report.json"]):
                        problems.append(f"{path.name}: the SVG does not match its model")
    # Author-owned artwork is checked and copied, never fed to auto layout.
    for source, relative in sample_files():
        path = target / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(source.read_bytes())
        if source.suffix == ".svg":
            for finding in check_svg(source.read_text(), metrics)["findings"]:
                problems.append(f"{relative}: {finding['severity']} {finding['rule']}: {finding['message']}")
            with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()):
                if atlas(["check", str(source), "--model", str(source.with_suffix(".json")),
                          "--report", f"{tmp}/report.json"]):
                    problems.append(f"{relative}: SVG/model contract failed")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--check", action="store_true", help="do not write; exit 1 on failed checks or stale samples")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) if args.check else OUT
        problems = render_all(target)
        # Compatibility assets are intentionally retained. A registry change must
        # never silently erase a formerly published download.
        names = {p.relative_to(target) for p in target.rglob("*") if p.is_file()}
        if args.check:
            for name in sorted(names):
                committed = OUT / name
                if not committed.exists():
                    problems.append(f"{name}: missing; run tools/build_samples.py")
                elif committed.read_bytes() != (Path(tmp) / name).read_bytes():
                    problems.append(f"{name}: stale; run tools/build_samples.py")
    for problem in problems:
        print(problem, file=sys.stderr)
    if problems:
        print(f"{len(problems)} problem(s)", file=sys.stderr)
        return 1
    print("samples up to date" if args.check else "samples written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
