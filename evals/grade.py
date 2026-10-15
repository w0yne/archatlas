#!/usr/bin/env python3
"""Model grader: score finished runs with evals/rubric.md and evals/grader/prompt.md.

For every run directory (one `record.json` per run) under the given results dirs, the
grader builds one input file (scenario, rubric, trace facts, replies, produced files),
renders produced SVGs to PNG when CairoSVG is available, and asks a grader model
through Pi in an isolated sandbox (no tools, no session, no extensions). The answer is
saved as `grade.json` next to `record.json` (or the name given with --grade-file, which
keeps an earlier grade intact when re-scoring); existing grades are kept unless --force.

The grader model is chosen per graded host so that a run is not graded by the model
that produced it (`grader.models` in the hosts file):

  grader:
    provider: amazon-bedrock
    models: {claude: <model>, codex: <model>, pi: <model>}
    env: {AWS_REGION: us-west-2}
    pass_env: []

Usage: python3 evals/grade.py --hosts hosts.yaml RESULTS_DIR [RESULTS_DIR ...] [--jobs 4]
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from adapters import ADAPTERS  # noqa: E402
from adapters.base import Sandbox, isolated_env, jsonl  # noqa: E402
from run_eval import load_scenarios  # noqa: E402

PROMPT = HERE / "grader" / "prompt.md"
RUBRIC = HERE / "rubric.md"
MAX_REPLY, MAX_SVG, MAX_SVGS, MAX_IMAGES = 14000, 9000, 4, 3


def render_png(svg: Path, dest: Path) -> Path | None:
    # rsvg-convert first: CairoSVG mis-places centred text whose line mixes font-family
    # tspans (Latin + CJK), which made the grader see overflow that browsers do not show.
    rsvg = shutil.which("rsvg-convert")
    if rsvg:
        proc = subprocess.run([rsvg, "-w", "1400", str(svg), "-o", str(dest)], capture_output=True, timeout=120)
        if proc.returncode == 0 and dest.exists():
            return dest
    try:
        import cairosvg  # optional fallback
    except ImportError:
        return None
    try:
        cairosvg.svg2png(url=str(svg), write_to=str(dest), output_width=1400, unsafe=False)
        return dest
    except Exception:
        return None


def build_input(run_dir: Path, rec: dict, scenario: dict, tmp: Path,
                addenda: tuple[Path, ...] = ()) -> tuple[Path, list[Path]]:
    replies = []
    adapter_cls = ADAPTERS[rec["host"]]
    adapter = adapter_cls.__new__(adapter_cls)
    for p in sorted(run_dir.glob("turn*.events.jsonl"), key=lambda x: int(re.findall(r"\d+", x.name)[0])):
        texts = adapter.assistant_texts(jsonl(p.read_text(encoding="utf-8", errors="replace")))
        body = "\n\n---\n\n".join(texts)
        if len(body) > MAX_REPLY:  # keep the start (brief, wireframe) and the end (final reply)
            body = body[:MAX_REPLY // 2] + "\n\n[… middle omitted …]\n\n" + body[-MAX_REPLY // 2:]
        replies.append(f"### {p.name.split('.')[0]} (all agent messages, in order)\n{body}")
    if not replies and (run_dir / "final.txt").exists():
        replies.append((run_dir / "final.txt").read_text(encoding="utf-8", errors="replace")[:MAX_REPLY])
    out = run_dir / "out"
    svgs = sorted(out.rglob("*.svg")) if out.exists() else []
    files, images = [], []
    for p in sorted(out.rglob("*")) if out.exists() else []:
        if p.is_file():
            files.append(f"- {p.relative_to(out)} ({p.stat().st_size} bytes)")
    svg_text = []
    for svg in svgs[:MAX_SVGS]:
        svg_text.append(f"### {svg.relative_to(out)}\n```xml\n{svg.read_text(encoding='utf-8', errors='replace')[:MAX_SVG]}\n```")
        if len(images) < MAX_IMAGES:
            png = render_png(svg, tmp / (svg.stem + ".png"))
            if png:
                images.append(png)
    for p in (sorted(out.rglob("*.md")) + sorted(out.rglob("*.json")))[:3] if out.exists() else []:
        svg_text.append(f"### {p.relative_to(out)}\n```\n{p.read_text(encoding='utf-8', errors='replace')[:4000]}\n```")
    sc = {k: scenario.get(k) for k in ("id", "title", "prompt", "modes", "lang", "expected_types", "expect",
                                       "scripted_answers", "fixture", "environment")}
    text = "\n\n".join([
        PROMPT.read_text(encoding="utf-8"),
        *(p.read_text(encoding="utf-8") for p in addenda),
        "## SCENARIO\n```yaml\n" + yaml.safe_dump(sc, allow_unicode=True, sort_keys=False) + f"mode_run: {rec.get('mode')}\narm: {rec.get('arm')}\n```",
        "## RUBRIC\n" + RUBRIC.read_text(encoding="utf-8"),
        "## TRACE FACTS\n```json\n" + json.dumps({"trace": rec.get("trace"), "skill_loaded": rec.get("skill_loaded"),
                                                    "image_views_observable": ADAPTERS[rec["host"]].traces_image_views,
                                                    "turns": rec.get("turns"), "exit_codes": rec.get("exit_codes"),
                                                    "timed_out": rec.get("timed_out")}, ensure_ascii=False) + "\n```",
        "## AUTOMATIC CHECKS\n```json\n" + json.dumps(rec.get("svg_checks"), ensure_ascii=False) + "\n```",
        "## REPLIES\n" + ("\n\n".join(replies) or "(no reply)"),
        "## FILES\n" + ("\n".join(files) or "(no files under out/)") + "\n\n" + "\n\n".join(svg_text),
        f"Attached images: {len(images)} PNG render(s) of the SVGs above." if images else "No images attached.",
    ])
    inp = tmp / "grader-input.md"
    inp.write_text(text, encoding="utf-8")
    return inp, images


def parse_answer(events: str) -> tuple[dict | None, dict]:
    text, usage, cost = "", {"input": 0, "output": 0, "cache_read": 0}, 0.0
    for ev in jsonl(events):
        msg = ev.get("message") or {}
        if ev.get("type") == "message_end" and msg.get("role") == "assistant":
            u = msg.get("usage") or {}
            usage["input"] += u.get("input") or 0
            usage["output"] += u.get("output") or 0
            usage["cache_read"] += u.get("cacheRead") or 0
            cost += (u.get("cost") or {}).get("total") or 0
            t = "".join(c.get("text", "") for c in msg.get("content", []) if isinstance(c, dict) and c.get("type") == "text")
            text = t or text
    m = re.search(r"\{.*\}", text, re.S)
    try:
        return (json.loads(m.group(0)) if m else None), {"usage": usage, "cost_usd": round(cost, 5), "raw": text[-2000:]}
    except json.JSONDecodeError:
        return None, {"usage": usage, "cost_usd": round(cost, 5), "raw": text[-2000:]}


def grade_one(run_dir: Path, rec: dict, scenario: dict, cfg: dict, force: bool, grade_file: str = "grade.json",
              addenda: tuple[Path, ...] = ()) -> str:
    target = run_dir / grade_file
    if target.exists() and not force:
        return f"{run_dir.name}: kept"
    model = cfg["models"][rec["host"]]
    pi = shutil.which(cfg.get("binary", "pi"))
    with tempfile.TemporaryDirectory(prefix="archatlas-grade-") as d:
        sb = Sandbox(Path(d)).create()
        inp, images = build_input(run_dir, rec, scenario, sb.tmp, addenda)
        env = isolated_env(sb, pi, {"PI_CODING_AGENT_DIR": str(sb.home / ".pi/agent"), "PI_SKIP_VERSION_CHECK": "1",
                                    **cfg.get("env", {})}, cfg.get("pass_env", []))
        argv = [pi, "-p", "--mode", "json", "--no-tools", "--no-session", "--no-extensions", "--no-skills",
                "--no-mcp", "--no-context-files", "--no-prompt-templates", "--no-themes",
                "--provider", cfg["provider"], "--model", model,
                f"@{inp}", *[f"@{p}" for p in images], "Grade this run. Reply with the JSON object only."]
        proc = subprocess.run(argv, cwd=sb.workspace, env=env, capture_output=True, text=True, timeout=600)
    answer, meta = parse_answer(proc.stdout)
    result = {"grader_model": model, "images": len(images), "exit_code": proc.returncode, **meta,
              "grade": answer, "error": None if answer else (proc.stderr[-500:] or "no JSON in answer")}
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return f"{run_dir.name}: {'ok' if answer else 'FAILED'} ({model})"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--hosts", type=Path, required=True)
    ap.add_argument("results", type=Path, nargs="+")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--grade-file", default="grade.json", help="file name for the grade next to record.json")
    ap.add_argument("--host", action="append", default=[], help="only grade runs of this host (repeatable)")
    ap.add_argument("--addendum", action="append", type=Path, default=[],
                    help="extra instruction or reference file appended to the grader prompt (repeatable), "
                         "e.g. grader/visual-note.md and docs/STYLE.md")
    ap.add_argument("--scenario", action="append", default=[], help="only grade this scenario id (repeatable)")
    args = ap.parse_args(argv)
    if "/" in args.grade_file or not args.grade_file.endswith(".json"):
        ap.error("--grade-file must be a plain *.json file name")
    cfg = (yaml.safe_load(args.hosts.read_text(encoding="utf-8")) or {}).get("grader")
    if not cfg:
        ap.error("hosts file has no `grader` section")
    scenarios = load_scenarios()
    work = []
    for root in args.results:
        for rec_path in sorted(root.glob("*/record.json")):
            rec = json.loads(rec_path.read_text())
            if rec.get("error") or rec.get("scenario", "").startswith("T") or "exit_codes" not in rec:
                continue
            if (args.host and rec["host"] not in args.host) or (args.scenario and rec["scenario"] not in args.scenario):
                continue
            work.append((rec_path.parent, rec, scenarios[rec["scenario"]]))
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        for line in pool.map(lambda w: grade_one(*w, cfg, args.force, args.grade_file, tuple(args.addendum)), work):
            print(line, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
