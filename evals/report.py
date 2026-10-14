#!/usr/bin/env python3
"""Aggregate evaluation results and grades into a Markdown + JSON report.

Usage:
  python3 evals/report.py RESULTS_DIR [RESULTS_DIR ...] --out evals/reports/<name>
      [--defects evals/reports/<name>.defects.md] [--title "..."]
Writes <name>.md and <name>.json. Raw results stay where they are (gitignored).
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from adapters import ADAPTERS  # noqa: E402
from adapters.base import jsonl  # noqa: E402
from run_eval import load_scenarios, skill_markers, skill_status, trace_facts  # noqa: E402

DIMS = ("semantic", "structure", "flow", "readability", "compliance", "honesty")
GATES = ("G1", "G2", "G3", "G4", "G5")


def load_runs(dirs: list[Path], markers: list[str] | None = None,
              grade_file: str = "grade.json") -> tuple[list[dict], list[dict]]:
    runs, metas = [], []
    for d in dirs:
        res = d / "results.json"
        if res.exists():
            metas.append(json.loads(res.read_text())["meta"])
        for rec_path in sorted(d.glob("*/record.json")):
            rec = json.loads(rec_path.read_text())
            # Relative to the results root's parent, so reports never carry local absolute paths.
            rec["_dir"] = str(rec_path.parent.relative_to(d.parent))
            g = rec_path.parent / grade_file
            rec["_rescored"] = g.exists() and grade_file != "grade.json"
            if not g.exists():
                g = rec_path.parent / "grade.json"
            rec["_grade"] = json.loads(g.read_text()) if g.exists() else None
            # Recompute trace facts from the saved events with the current adapters.
            events = "".join(p.read_text(encoding="utf-8", errors="replace")
                             for p in sorted(rec_path.parent.glob("turn*.events.jsonl")))
            adapter_cls = ADAPTERS[rec["host"]]
            rec["trace"] = trace_facts(adapter_cls.tool_calls(adapter_cls.__new__(adapter_cls), jsonl(events)))["trace"]
            if markers is not None:
                rec.update(skill_status(adapter_cls.__new__(adapter_cls), events, markers, "architecture-diagrams",
                                        rec["arm"], rec["scenario"].startswith("T")))
                if "should_trigger" in rec:
                    rec["trigger_pass"] = (rec["skill_loaded"] is True) == rec["should_trigger"]
            rec["renderer_used"] = any(f.endswith("findings.json") for f in rec.get("files", [])) or rec["trace"]["atlas_render"] > 0
            runs.append(rec)
    return runs, metas


def gates_of(rec: dict) -> dict:
    g = dict(((rec.get("_grade") or {}).get("grade") or {}).get("gates") or {})
    svgs = rec.get("svg_checks") or []
    g["G5"] = all(c.get("gate_G5_pass") for c in svgs) if svgs else None
    if rec["trace"]["forbidden"]:
        g["G4"] = False
    if g.get("G2") is False and not ADAPTERS[rec["host"]].traces_image_views:
        g["G2"] = None  # the host's trace cannot show image views, so a "no image read" verdict is unfounded
    return {k: g.get(k) for k in GATES}


def scores_of(rec: dict) -> dict:
    s = ((rec.get("_grade") or {}).get("grade") or {}).get("scores") or {}
    return {k: s.get(k) for k in DIMS}


def total(scores: dict) -> float | None:
    vals = [v for v in scores.values() if isinstance(v, (int, float))]
    return round(sum(vals) / len(vals), 2) if vals else None


def fmt(v, nd=2):
    if v is None:
        return "–"
    if isinstance(v, bool):
        return "pass" if v else "**FAIL**"
    if isinstance(v, float):
        return f"{v:.{nd}f}"
    return str(v)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("results", type=Path, nargs="+")
    ap.add_argument("--out", type=Path, required=True, help="output path without extension")
    ap.add_argument("--defects", type=Path, help="hand-written defects section to append")
    ap.add_argument("--title", default="Evaluation report")
    ap.add_argument("--skill-dir", type=Path, help="recompute skill-load evidence with this skill's SKILL.md")
    ap.add_argument("--grade-file", default="grade.json",
                    help="prefer this grade file per run (e.g. a re-score), falling back to grade.json")
    ap.add_argument("--baseline", type=Path,
                    help="an earlier report's JSON: adds before/after tables, and supplies the no-skill rows "
                         "for scenario/host pairs this run did not repeat")
    args = ap.parse_args(argv)
    scenarios = load_scenarios()
    runs, metas = load_runs(args.results, skill_markers(args.skill_dir) if args.skill_dir else None, args.grade_file)
    tasks = [r for r in runs if not r["scenario"].startswith("T")]
    trig = [r for r in runs if r["scenario"].startswith("T")]

    rows = []
    for r in sorted(tasks, key=lambda r: (int(r["scenario"][1:]), r["host"], r["arm"])):
        sc, gs = scores_of(r), gates_of(r)
        grade = (r.get("_grade") or {}).get("grade") or {}
        rows.append({
            "run": r["run"], "scenario": r["scenario"], "host": r["host"], "arm": r["arm"], "mode": r.get("mode"),
            "model": r.get("model"), "exit_codes": r.get("exit_codes"), "error": r.get("error"),
            "turns": r.get("turns"), "clarification_turns": r.get("clarification_turns"),
            "wall_s": r.get("wall_s"), "usage": r.get("usage"), "cost_usd": r.get("cost_est_usd"),
            "skill_loaded": r.get("skill_loaded"), "renderer_used": r["renderer_used"], "trace": r["trace"],
            "gates": gs, "gates_pass": all(v is not False for v in gs.values()), "scores": sc, "mean_score": total(sc),
            "type_chosen": grade.get("type_chosen"), "expected_types": scenarios[r["scenario"]].get("expected_types"),
            "grader_model": (r.get("_grade") or {}).get("grader_model"), "notes": grade.get("notes"),
            "defects": grade.get("defects"), "evidence_dir": r["_dir"], "rescored": r["_rescored"],
        })

    by = defaultdict(list)
    for x in rows:
        by[(x["host"], x["arm"])].append(x)
    summary = {}
    for (h, a), xs in sorted(by.items()):
        summary[f"{h}/{a}"] = {
            "runs": len(xs),
            "gate_pass": sum(x["gates_pass"] for x in xs),
            "median": {d: (statistics.median([x["scores"][d] for x in xs if isinstance(x["scores"][d], (int, float))])
                           if any(isinstance(x["scores"][d], (int, float)) for x in xs) else None) for d in DIMS},
            "mean_score": round(statistics.mean([x["mean_score"] for x in xs if x["mean_score"] is not None]), 2)
                          if any(x["mean_score"] is not None for x in xs) else None,
            "cost_usd": round(sum(x["cost_usd"] or 0 for x in xs), 2),
            "wall_s": round(sum(x["wall_s"] or 0 for x in xs)),
            "tokens_in": sum((x["usage"] or {}).get("input") or 0 for x in xs),
            "tokens_out": sum((x["usage"] or {}).get("output") or 0 for x in xs),
            "tokens_cache_read": sum((x["usage"] or {}).get("cache_read") or 0 for x in xs),
            "renderer_used": sum(bool(x["renderer_used"]) for x in xs),
        }
    baseline = json.loads(args.baseline.read_text(encoding="utf-8")) if args.baseline else None
    base_rows = (baseline or {}).get("runs", [])

    def find(xs, sid, h, arm):
        return next((x for x in xs if x["scenario"] == sid and x["host"] == h and x["arm"] == arm), None)

    deltas = []
    for sid in sorted({x["scenario"] for x in rows}, key=lambda s: int(s[1:])):
        for h in sorted({x["host"] for x in rows}):
            s = next((x for x in rows if x["scenario"] == sid and x["host"] == h and x["arm"] == "skill"), None)
            n = find(rows, sid, h, "noskill") or find(base_rows, sid, h, "noskill")
            if s and n and s["mean_score"] is not None and n["mean_score"] is not None:
                deltas.append({"scenario": sid, "host": h, "skill": s["mean_score"], "noskill": n["mean_score"],
                               "delta": round(s["mean_score"] - n["mean_score"], 2),
                               "skill_gates": s["gates_pass"], "noskill_gates": n["gates_pass"]})
    triggers = {}
    for h in sorted({r["host"] for r in trig}):
        xs = [r for r in trig if r["host"] == h and r.get("arm") == "skill" and "should_trigger" in r]
        tp = sum(r["should_trigger"] and r["skill_loaded"] is True for r in xs)
        fp = sum((not r["should_trigger"]) and r["skill_loaded"] is True for r in xs)
        pos = sum(r["should_trigger"] for r in xs)
        triggers[h] = {"runs": len(xs), "tp": tp, "fp": fp, "positives": pos, "negatives": len(xs) - pos,
                       "precision": round(tp / (tp + fp), 2) if tp + fp else None,
                       "recall": round(tp / pos, 2) if pos else None,
                       "gate_pass": tp >= 5 and fp <= 1,
                       "cost_usd": round(sum(r.get("cost_est_usd") or 0 for r in xs), 2),
                       "items": {r["scenario"]: r["skill_loaded"] for r in sorted(xs, key=lambda r: int(r["scenario"][1:]))}}
    grading_cost = round(sum(((r.get("_grade") or {}).get("cost_usd") or 0) for r in tasks), 2)
    run_cost = round(sum(x["cost_usd"] or 0 for x in rows) + sum(t["cost_usd"] for t in triggers.values()), 2)
    wins = defaultdict(lambda: [0, 0])
    for d in deltas:
        wins[d["host"]][0] += d["delta"] > 0
        wins[d["host"]][1] += 1

    compare = []
    for x in rows:
        b = find(base_rows, x["scenario"], x["host"], x["arm"])
        if b:
            compare.append({"scenario": x["scenario"], "host": x["host"], "arm": x["arm"],
                            "before": b["mean_score"], "after": x["mean_score"],
                            "delta": round(x["mean_score"] - b["mean_score"], 2)
                            if x["mean_score"] is not None and b["mean_score"] is not None else None,
                            "gates_before": b["gates_pass"], "gates_after": x["gates_pass"],
                            "failed_before": [k for k, v in b["gates"].items() if v is False],
                            "failed_after": [k for k, v in x["gates"].items() if v is False],
                            "scores_before": b["scores"], "scores_after": x["scores"]})

    data = {"title": args.title, "meta": metas[:1] and {k: metas[0].get(k) for k in ("skill_rev", "host_versions")},
            "models": sorted({f"{x['host']}={x['model']}" for x in rows}), "summary": summary, "deltas": deltas,
            "skill_wins": {h: {"wins": w, "of": n} for h, (w, n) in wins.items()},
            "triggers": triggers, "cost": {"runs_usd": run_cost, "grading_usd": grading_cost,
                                          "total_usd": round(run_cost + grading_cost, 2)},
            "live_dir_hits": sorted({h for m in metas for h in m.get("live_dir_hits", [])}),
            "baseline": {"title": baseline.get("title"), "skill_rev": (baseline.get("meta") or {}).get("skill_rev"),
                         "summary": baseline.get("summary"), "triggers": baseline.get("triggers")} if baseline else None,
            "compare": compare, "runs": rows}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.with_suffix(".json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    L = [f"# {args.title}", ""]
    if data["meta"]:
        versions = {}
        for m in metas:
            versions.update(m.get("host_versions") or {})
        data["meta"]["host_versions"] = versions
        L += [f"- Skill revision: `{data['meta'].get('skill_rev')}` (installed from the release zip built by `tools/pack_skill.py`)",
              f"- Hosts: {', '.join(f'{k} {v}' for k, v in sorted(versions.items()))}"]
    L += [f"- Models: {', '.join(data['models'])}",
          f"- Cost: runs ${run_cost} + grading ${grading_cost} = **${data['cost']['total_usd']}** (Claude Code and Pi report cost; Codex is estimated from tokens × list price)",
          f"- Live host directories touched by any sandbox: {len(data['live_dir_hits'])}", "",
          "## Headline", "",
          "| Host / arm | Runs | All gates pass | Mean score (0–3) | " + " | ".join(f"median {d}" for d in DIMS) + " | Renderer used | Cost $ | Wall s | Tokens in / out / cache read |",
          "|" + "---|" * (8 + len(DIMS))]
    for k, v in summary.items():
        L.append(f"| {k} | {v['runs']} | {v['gate_pass']} | {fmt(v['mean_score'])} | " +
                 " | ".join(fmt(v["median"][d], 1) for d in DIMS) +
                 f" | {v['renderer_used']} | {v['cost_usd']} | {v['wall_s']} | {v['tokens_in']} / {v['tokens_out']} / {v['tokens_cache_read']} |")
    L += ["", "Skill beats no-skill (higher mean score) per host: " +
          ", ".join(f"{h} {w}/{n}" for h, (w, n) in wins.items()) + " (release target: ≥ 8/10, DESIGN §8.5).", "",
          "## Trigger set", "", "| Host | Precision | Recall | TP | FP | Gate (≥5/6 TP, ≤1/6 FP) | Per item |", "|---|---|---|---|---|---|---|"]
    for h, t in triggers.items():
        items = " ".join(f"{k}:{'Y' if v is True else 'n'}" for k, v in t["items"].items())
        L.append(f"| {h} | {fmt(t['precision'])} | {fmt(t['recall'])} | {t['tp']}/{t['positives']} | {t['fp']}/{t['negatives']} | {fmt(t['gate_pass'])} | {items} |")
    if baseline:
        bt = baseline.get("triggers") or {}
        L += ["", f"## Before / after (baseline: {baseline.get('title')}, skill `{(baseline.get('meta') or {}).get('skill_rev')}`)", "",
              "All cells read before → after.", "",
              "| Host / arm | Gates pass | Mean score | " + " | ".join(f"median {d}" for d in DIMS) + " |", "|" + "---|" * (3 + len(DIMS))]
        for k, v in summary.items():
            b = (baseline.get("summary") or {}).get(k)
            if b:
                L.append(f"| {k} | {b['gate_pass']}/{b['runs']} → {v['gate_pass']}/{v['runs']} | {fmt(b['mean_score'])} → {fmt(v['mean_score'])} | " +
                         " | ".join(f"{fmt(b['median'][d], 1)} → {fmt(v['median'][d], 1)}" for d in DIMS) + " |")
        L += ["", "| Host | Trigger TP before → after | FP before → after |", "|---|---|---|"]
        for h, t in triggers.items():
            b = bt.get(h)
            if b:
                L.append(f"| {h} | {b['tp']}/{b['positives']} → {t['tp']}/{t['positives']} | {b['fp']}/{b['negatives']} → {t['fp']}/{t['negatives']} |")
        L += ["", "| Scenario | Host | Arm | Mean before | Mean after | Δ | Failed gates before | Failed gates after |",
              "|---|---|---|---|---|---|---|---|"]
        for c in sorted(compare, key=lambda c: (int(c["scenario"][1:]), c["host"], c["arm"])):
            delta = "–" if c["delta"] is None else f"{c['delta']:+.2f}"
            L.append(f"| {c['scenario']} | {c['host']} | {c['arm']} | {fmt(c['before'])} | {fmt(c['after'])} | {delta} | "
                     f"{', '.join(c['failed_before']) or '–'} | {', '.join(c['failed_after']) or '–'} |")
    L += ["", "## Skill vs no skill, per scenario and host (mean of graded dimensions)", "",
          *(["No-skill rows not repeated in this run come from the baseline report (same models and prompts).", ""]
            if baseline else []),
          "| Scenario | Host | Skill | No skill | Δ | Gates skill / no skill |", "|---|---|---|---|---|---|"]
    for d in deltas:
        L.append(f"| {d['scenario']} | {d['host']} | {d['skill']} | {d['noskill']} | {d['delta']:+.2f} | {fmt(d['skill_gates'])} / {fmt(d['noskill_gates'])} |")
    L += ["", "## All runs", "",
          "| Run | Exit | Gates G1–G5 | " + " | ".join(DIMS) + " | Type chosen (expected) | Skill loaded | Renderer | Clarify | Cost $ | Wall s |",
          "|" + "---|" * (9 + len(DIMS))]
    for x in rows:
        gates = " ".join(f"{k}:{'✓' if v is True else ('✗' if v is False else '–')}" for k, v in x["gates"].items())
        L.append(f"| {x['run']}{' (rescored)' if x['rescored'] else ''} | {fmt(x['exit_codes'])} | {gates} | " + " | ".join(fmt(x["scores"][d]) for d in DIMS) +
                 f" | {fmt(x['type_chosen'])} ({','.join(x['expected_types'] or [])}) | {fmt(x['skill_loaded'])} | {'yes' if x['renderer_used'] else 'no'} | {fmt(x['clarification_turns'])} | {fmt(x['cost_usd'])} | {fmt(x['wall_s'])} |")
    fails = [x for x in rows if not x["gates_pass"]]
    L += ["", "## Hard-gate failures", ""]
    L += [f"- **{x['run']}**: " + ", ".join(k for k, v in x["gates"].items() if v is False) + f" — {x['notes'] or ''}" for x in fails] or ["- none"]
    if args.defects and args.defects.exists():
        L += ["", args.defects.read_text(encoding="utf-8").rstrip()]
    L += ["", "Raw results (events, replies, outputs) stay in the gitignored results directories; "
          "`evidence_dir` in the JSON names each run's directory."]
    args.out.with_suffix(".md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"wrote {args.out.with_suffix('.md')} and .json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
