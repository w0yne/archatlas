#!/usr/bin/env python3
"""Run evaluation scenarios headless on Claude Code, Codex and Pi, with and without the skill.

Every run gets a fresh sandbox (HOME, TMPDIR, host config dir, workspace) under
--work-root. Nothing is inherited from the parent environment except what the
hosts file names explicitly; team control variables are refused.

Examples:
  python3 evals/run_eval.py --list
  python3 evals/run_eval.py --hosts my-hosts.yaml --scenario S6 --mode autonomous --dry-run
  python3 evals/run_eval.py --hosts my-hosts.yaml --scenario S6 --mode autonomous \
      --host claude --host codex --host pi --arm skill --arm noskill
  python3 evals/run_eval.py --hosts my-hosts.yaml --scenario T --host pi --arm skill
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import zipfile

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from adapters import ADAPTERS  # noqa: E402
from adapters.base import Sandbox, isolated_env, jsonl  # noqa: E402

SCENARIOS = HERE / "scenarios"
FIXTURES = SCENARIOS / "fixtures"
DEFAULT_SKILL = HERE.parent / "skills" / "architecture-diagrams"
SKIP_LISTING = {".git", ".gitignore", "fixture", ".claude", ".agents"}
QUESTION_RE = re.compile(r"(\?|？|needs_input:)\s*$", re.M)


# ------------------------------------------------------------------ scenarios

def load_scenarios() -> dict[str, dict]:
    out = {}
    for p in sorted(SCENARIOS.glob("*.yaml")):
        s = yaml.safe_load(p.read_text(encoding="utf-8"))
        s["_file"] = p.name
        out[s["id"]] = s
    return out


def expand(scenario: dict, mode: str | None) -> list[dict]:
    """One scenario file -> list of run items (trigger files hold many prompts)."""
    if scenario.get("kind") == "trigger":
        return [{"id": it["id"], "prompt": it["prompt"], "mode": None, "answers": [],
                 "trigger": True, "should_trigger": it["should_trigger"], "scenario": scenario}
                for it in scenario["items"]]
    modes = [mode] if mode else scenario["modes"][:1]
    for m in modes:
        if m not in scenario["modes"]:
            raise SystemExit(f"{scenario['id']} does not define mode {m!r} (has {scenario['modes']})")
    return [{"id": scenario["id"], "prompt": scenario["prompt"], "mode": m,
             "answers": scenario.get("scripted_answers", []) if m == "guided" else [],
             "trigger": False, "scenario": scenario} for m in modes]


def build_prompt(item: dict, adapter, arm: str) -> str:
    if item["trigger"]:
        return item["prompt"]  # the host must decide on its own whether to load the skill
    text = f"mode={item['mode']} {item['prompt']}"
    return f"{adapter.invoke_prefix} {text}" if arm == "skill" else text


# ------------------------------------------------------------------ sandbox setup

def git(args: list[str], cwd: Path, env: dict) -> None:
    subprocess.run(["git", "-c", "user.name=eval", "-c", "user.email=eval@example.invalid", *args],
                   cwd=cwd, env=env, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def make_readonly(root: Path) -> None:
    for p in root.rglob("*"):
        if p.is_file() and not p.is_symlink():
            p.chmod(p.stat().st_mode & ~(stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH))


def prepare_workspace(sb: Sandbox, scenario: dict) -> None:
    env = isolated_env(sb, shutil.which("git") or "/usr/bin/git", {}, [])
    ws = sb.workspace
    fx = scenario.get("fixture") or {}
    if fx.get("repo"):
        dest = ws / fx.get("path", "fixture")
        dest.mkdir(parents=True)
        git(["init", "-q"], dest, env)
        git(["fetch", "-q", "--depth", "1", fx["repo"], fx["commit"]], dest, env)
        git(["checkout", "-q", "--detach", "FETCH_HEAD"], dest, env)
        make_readonly(dest)
    for dest, src in (fx.get("files") or {}).items():
        target = ws / dest
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(FIXTURES / src, target)
    (ws / "out").mkdir(exist_ok=True)
    # Hosts such as Codex expect a git workspace; the fixture stays its own repository.
    (ws / ".gitignore").write_text("fixture/\n")
    git(["init", "-q"], ws, env)
    git(["add", "-A"], ws, env)
    git(["commit", "-q", "--allow-empty", "-m", "fixture"], ws, env)


def scenario_env(scenario: dict, sb: Sandbox) -> dict:
    env = {}
    if (scenario.get("environment") or {}).get("no_browser"):
        empty = sb.root / "no-browsers"
        empty.mkdir(exist_ok=True)
        env["PLAYWRIGHT_BROWSERS_PATH"] = str(empty)
    return env


# ------------------------------------------------------------------ checks

def skill_markers(skill_dir: Path) -> list[str]:
    """A body line of SKILL.md: it appears in the event log only if the skill was loaded."""
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    body = text.split("---", 2)[-1]
    for line in body.splitlines():
        line = line.strip()
        if len(line) >= 40 and line.isascii() and '"' not in line and "\\" not in line:
            return [line[:60]]
    raise SystemExit("no usable marker line in SKILL.md")


def skill_status(adapter, events: str, markers: list[str], skill: str, arm: str, trigger: bool) -> dict:
    """Skill activation from the host trace, never from the answer text (DESIGN §8.3)."""
    rows = jsonl(events)
    evidence = []
    if any(m in events for m in markers):
        evidence.append("SKILL.md body in trace")
    # Paths are matched in the agent's own tool calls only: hosts list skill locations in their
    # system prompt, which some event streams echo.
    calls = "\n".join(adapter.tool_calls(rows))
    reads = sorted(set(re.findall(rf"{re.escape(skill)}/((?:SKILL\.md|references/|assets/|scripts/)[\w./-]*)", calls)))
    evidence += [f"read {r}" for r in reads]
    evidence += adapter.skill_evidence(rows, skill)
    if evidence:
        loaded = True
    elif arm == "skill" and not trigger:
        loaded = "unknown"  # invoked by name; some hosts inject the skill without a trace event
    else:
        loaded = False
    return {"skill_loaded": loaded, "skill_evidence": evidence,
            "skill_listed": adapter.skill_listed(rows, skill)}


# Signals in the host trace that feed hard gates and the defect list (never the answer text alone).
# Counted over the agent's own tool calls only (the skill text itself mentions these commands).
TRACE_PATTERNS = {
    "tool_calls": None,
    "atlas_render": r"atlas\W+render\b",
    "atlas_check": r"atlas\W+check\b",
    "atlas_any": r"scripts/atlas\b|\batlas (init|render|check|preview|sheet|fonts)\b",
    "pip_install": r"pip3? install",
    "pip_install_archatlas_pypi": r"pip3? install[^\n\"]*\barchatlas\b(?![\w./\[-])",
    "image_read": r"^(Read|read|view_image)\b[^\n]*\.(png|jpe?g)\b",
    "hand_written_svg": r"^(Write|write)\b[^\n]*\.svg\b|cat >[^\n]*\.svg",
    # Executed commands only: anchored at a command position, heredoc bodies removed first.
    "forbidden": r"(?:^|&&|;|\|\||\$\()\s*(?:sudo\s+)?(?:docker\s+(?:run|compose\s+up|build)|git\s+push|npm\s+publish|(?:\./)?mvnw?\b[^\n]*spring-boot:run|(?:\./)?gradlew?\b[^\n]*bootRun|java\s+-jar|python3?\s+\S*fixture/\S+\.py)",
}
HEREDOC = re.compile(r"<<-?\s*['\"]?(\w+)['\"]?[^\n]*\n.*?\n\s*\1\b", re.S)


def trace_facts(calls: list[str]) -> dict:
    out = {}
    for k, p in TRACE_PATTERNS.items():
        out[k] = len(calls) if p is None else sum(bool(re.search(p, HEREDOC.sub("", c), re.M)) for c in calls)
    return {"trace": out}


def estimate_cost(record: dict, cfg: dict) -> float | None:
    """Host-reported cost, else tokens × the hosts file's `price` (USD per million tokens)."""
    if record.get("cost_usd") is not None:
        return record["cost_usd"]
    price, u = cfg.get("price"), record.get("usage") or {}
    if not price:
        return None
    uncached = max((u.get("input") or 0) - (u.get("cache_read") or 0), 0) if cfg.get("input_includes_cache") else (u.get("input") or 0)
    return round((uncached * price.get("input", 0) + (u.get("cache_read") or 0) * price.get("cache_read", 0)
                  + (u.get("cache_write") or 0) * price.get("cache_write", 0)
                  + (u.get("output") or 0) * price.get("output", 0)) / 1e6, 4)


def spent(out_root: Path) -> float:
    total = 0.0
    for rec in out_root.glob("*/record.json"):
        total += json.loads(rec.read_text()).get("cost_est_usd") or 0
    return total


def svg_checks(path: Path) -> dict:
    res = {"file": path.name, "valid_xml": False, "script": False, "foreign_object": False,
           "external_refs": False}
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        res["error"] = str(e)
        return res
    res["valid_xml"] = root.tag.endswith("svg")
    for el in root.iter():
        tag = el.tag.rsplit("}", 1)[-1]
        res["script"] |= tag == "script"
        res["foreign_object"] |= tag == "foreignObject"
        for k, v in el.attrib.items():
            if k.rsplit("}", 1)[-1] == "href" and re.match(r"^(https?:)?//", v.strip()):
                res["external_refs"] = True
    res["gate_G5_pass"] = res["valid_xml"] and not (res["script"] or res["foreign_object"] or res["external_refs"])
    return res


def listing(ws: Path) -> list[str]:
    files = []
    for p in sorted(ws.rglob("*")):
        rel = p.relative_to(ws)
        if rel.parts[0] in SKIP_LISTING or not p.is_file():
            continue
        files.append(str(rel))
    return files


def live_dir_hits(live_dirs: list[Path], since: float, needles: list[str]) -> list[str]:
    """Files under the real host dirs, changed during the eval, that mention a sandbox path."""
    hits = []
    raws = [n.encode() for n in needles]
    if not raws:
        return hits
    for d in live_dirs:
        if not d.exists():
            continue
        for p in d.rglob("*"):
            try:
                if p.is_file() and p.stat().st_mtime >= since and p.stat().st_size < 200_000_000:
                    data = p.read_bytes()
                    if any(r in data for r in raws):
                        hits.append(str(p))
            except OSError:
                continue
    return hits


# ------------------------------------------------------------------ run

def run_one(item, host, arm, cfg, skill_dir, out_root, work_root, timeout, keep, dry_run, markers):
    adapter = ADAPTERS[host](cfg)
    run_id = f"{item['id']}-{item['mode'] or 'trigger'}-{host}-{arm}"
    out_dir = out_root / run_id
    out_dir.mkdir(parents=True, exist_ok=True)
    sb = Sandbox(Path(tempfile.mkdtemp(prefix="archatlas-eval-", dir=work_root))).create()
    record = {"run": run_id, "scenario": item["id"], "file": item["scenario"]["_file"], "host": host,
              "arm": arm, "mode": item["mode"], "model": cfg.get("model"), "sandbox": str(sb.root)}
    try:
        prepare_workspace(sb, item["scenario"])
        adapter.prepare(sb, skill_dir if arm == "skill" else None)
        adapter.cfg = {**adapter.cfg, "env": {**adapter.cfg.get("env", {}), **scenario_env(item["scenario"], sb)}}
        prompts = [build_prompt(item, adapter, arm)] + list(item["answers"])
        multi = len(prompts) > 1
        if dry_run:
            record["argv"] = [adapter.argv(sb, p, "SESSION" if i else None, multi) for i, p in enumerate(prompts)]
            record["env_keys"] = sorted(isolated_env(sb, adapter.binary, adapter.host_env(sb),
                                                     adapter.cfg.get("pass_env", [])))
            return record
        turns, session = [], None
        for i, prompt in enumerate(prompts):
            t = adapter.turn(sb, prompt, session, multi, out_dir, f"turn{i + 1}", timeout)
            turns.append(t)
            (out_dir / f"turn{i + 1}.final.txt").write_text(t.final_text, encoding="utf-8")
            session = t.session or session
            if t.exit_code != 0 or (multi and not session):
                break
        events = "".join((out_dir / f"turn{i + 1}.events.jsonl").read_text(encoding="utf-8", errors="replace")
                         for i in range(len(turns)))
        record.update({
            "exit_codes": [t.exit_code for t in turns],
            "timed_out": any(t.timed_out for t in turns),
            "turns": len(turns),
            "clarification_turns": sum(bool(QUESTION_RE.search(t.final_text[-400:])) for t in turns),
            "wall_s": round(sum(t.wall_s for t in turns), 1),
            "usage": {k: sum((t.usage.get(k) or 0) for t in turns)
                      for k in ("input", "output", "cache_read", "cache_write")},
            "cost_usd": (round(sum(t.cost_usd for t in turns if t.cost_usd is not None), 4)
                         if any(t.cost_usd is not None for t in turns) else None),
            **skill_status(adapter, events, markers, skill_dir.name, arm, item["trigger"]),
            **trace_facts(adapter.tool_calls(jsonl(events))),
            "files": listing(sb.workspace),
        })
        if item["trigger"]:
            record["should_trigger"] = item["should_trigger"]
            record["trigger_pass"] = (record["skill_loaded"] is True) == item["should_trigger"]
        (out_dir / "final.txt").write_text(turns[-1].final_text if turns else "", encoding="utf-8")
        produced = sb.workspace / "out"
        if any(produced.iterdir()):
            shutil.copytree(produced, out_dir / "out", dirs_exist_ok=True)
        record["svg_checks"] = [svg_checks(p) for p in sorted(produced.rglob("*.svg"))]
        record["cost_est_usd"] = estimate_cost(record, cfg)
        return record
    except Exception as e:  # keep the batch going; the record carries the error
        record["error"] = f"{type(e).__name__}: {e}"
        return record
    finally:
        (out_dir / "record.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
        if not keep:
            shutil.rmtree(sb.root, ignore_errors=True)


def fmt(v):
    return "–" if v in (None, "", []) else v


def report(records: list[dict], meta: dict) -> str:
    lines = [f"# Evaluation run {meta['run_id']}", "",
             f"- started: {meta['started']}  ",
             f"- skill: `{meta['skill_dir']}` (sha {meta['skill_rev']})  ",
             f"- hosts: {', '.join(f'{h} {v}' for h, v in meta['host_versions'].items())}  ",
             f"- live host dirs touched with sandbox paths: {len(meta['live_dir_hits'])}", "",
             "| Run | Exit | Turns | Clarify | Wall s | In tok | Out tok | Cache read | Cost $ | Skill loaded | Files | SVG G5 |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in records:
        if "error" in r:
            lines.append(f"| {r['run']} | error: {r['error']} |" + " |" * 10)
            continue
        if "argv" in r:
            lines.append(f"| {r['run']} | dry-run |" + " |" * 10)
            continue
        u = r["usage"]
        g5 = ", ".join("pass" if c.get("gate_G5_pass") else "FAIL" for c in r["svg_checks"])
        loaded = str(r["skill_loaded"]).lower()
        if r.get("skill_listed") is not None:
            loaded += f", listed={str(r['skill_listed']).lower()}"
        if "trigger_pass" in r:
            loaded += " (pass)" if r["trigger_pass"] else " (FAIL)"
        lines.append(f"| {r['run']} | {','.join(map(str, r['exit_codes']))} | {r['turns']} | "
                     f"{r['clarification_turns']} | {r['wall_s']} | {fmt(u['input'])} | {fmt(u['output'])} | "
                     f"{fmt(u['cache_read'])} | {fmt(r['cost_usd'])} | {loaded} | {len(r['files'])} | {fmt(g5)} |")
    lines += ["", "Scores are added by raters in `scores.json` (see `evals/rubric.md`)."]
    return "\n".join(lines) + "\n"


def host_version(adapter_cls, cfg) -> str:
    try:
        a = adapter_cls(cfg)
        return subprocess.run([a.binary, "--version"], capture_output=True, text=True,
                              timeout=30).stdout.strip().splitlines()[0]
    except Exception as e:
        return f"unknown ({e})"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--list", action="store_true", help="list scenarios and exit")
    ap.add_argument("--hosts", type=Path, help="hosts file (see evals/hosts.example.yaml)")
    ap.add_argument("--scenario", action="append", default=[], help="scenario id (repeatable; 'all')")
    ap.add_argument("--host", action="append", choices=sorted(ADAPTERS), default=[])
    ap.add_argument("--arm", action="append", choices=["skill", "noskill"], default=[])
    ap.add_argument("--mode", choices=["autonomous", "guided"], help="override the scenario's first mode")
    ap.add_argument("--skill-dir", type=Path, default=DEFAULT_SKILL)
    ap.add_argument("--skill-bundle", type=Path, help="install the skill from a release zip (tools/pack_skill.py)")
    ap.add_argument("--skill-rev", help="record this revision for the skill (default: git rev of --skill-dir)")
    ap.add_argument("--budget-usd", type=float, help="stop starting runs once this results dir has spent this much")
    ap.add_argument("--out", type=Path, help="results dir (default evals/results/<timestamp>)")
    ap.add_argument("--work-root", type=Path, default=Path(tempfile.gettempdir()),
                    help="parent of the per-run sandboxes; keep it outside any directory with AGENTS.md/CLAUDE.md")
    ap.add_argument("--timeout", type=int, default=900, help="seconds per turn")
    ap.add_argument("--keep-sandboxes", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="print commands and env keys, run nothing")
    ap.add_argument("--live-dir", action="append", type=Path, default=[],
                    help="real host state dirs to scan for leaked sandbox paths "
                         "(default: ~/.claude ~/.codex ~/.pi)")
    args = ap.parse_args(argv)

    scenarios = load_scenarios()
    if args.list:
        for s in scenarios.values():
            print(f"{s['id']:4} {s['_file']:38} {s.get('title', '')}")
        return 0
    if not (args.hosts and args.scenario):
        ap.error("--hosts and --scenario are required")
    hosts_cfg = yaml.safe_load(args.hosts.read_text(encoding="utf-8")) or {}
    ids = list(scenarios) if args.scenario == ["all"] else args.scenario
    hosts = args.host or sorted(ADAPTERS)
    arms = args.arm or ["skill", "noskill"]
    skill_dir = args.skill_dir.resolve()
    if args.skill_bundle:
        bundle_root = Path(tempfile.mkdtemp(prefix="archatlas-bundle-"))
        with zipfile.ZipFile(args.skill_bundle) as zf:
            zf.extractall(bundle_root)
        for info in zipfile.ZipFile(args.skill_bundle).infolist():
            mode = (info.external_attr >> 16) & 0o777
            if mode:
                (bundle_root / info.filename).chmod(mode)
        skill_dir = next(p.parent for p in bundle_root.glob("*/SKILL.md"))
    markers = skill_markers(skill_dir)

    started = time.time()
    run_id = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_root = (args.out or HERE / "results" / run_id).resolve()
    out_root.mkdir(parents=True, exist_ok=True)
    records = []
    # A single trigger item (e.g. T5) can be selected by its id; "T" selects the whole set.
    trigger_items = {it["id"]: sc for sc in scenarios.values() if sc.get("kind") == "trigger" for it in sc["items"]}
    for sid in ids:
        if sid not in scenarios and sid not in trigger_items:
            raise SystemExit(f"unknown scenario {sid!r} (see --list)")
        items = (expand(scenarios[sid], args.mode) if sid in scenarios
                 else [i for i in expand(trigger_items[sid], None) if i["id"] == sid])
        for item in items:
            item_arms = ["skill"] if item["trigger"] and not args.arm else arms
            for host in hosts:
                for arm in item_arms:
                    if args.budget_usd is not None and spent(out_root) >= args.budget_usd:
                        print(f"[stop] budget {args.budget_usd} USD reached", flush=True)
                        break
                    print(f"[run] {item['id']} {item['mode'] or 'trigger'} {host} {arm}", flush=True)
                    records.append(run_one(item, host, arm, hosts_cfg.get(host, {}), skill_dir, out_root,
                                           args.work_root, args.timeout, args.keep_sandboxes,
                                           args.dry_run, markers))
    live = args.live_dir or [Path.home() / d for d in (".claude", ".codex", ".pi")]
    rev = args.skill_rev or subprocess.run(["git", "-C", str(skill_dir), "rev-parse", "--short", "HEAD"],
                                           capture_output=True, text=True).stdout.strip() or "unknown"
    meta = {
        "run_id": run_id,
        "started": dt.datetime.fromtimestamp(started, dt.timezone.utc).isoformat(),
        "skill_dir": str(skill_dir), "skill_rev": rev, "skill_markers": markers,
        "host_versions": {h: host_version(ADAPTERS[h], hosts_cfg.get(h, {})) for h in hosts},
        "work_root": str(args.work_root),
        "live_dirs_scanned": [str(d) for d in live],
        "live_dir_hits": [] if args.dry_run else live_dir_hits(live, started, [r["sandbox"] for r in records]),
    }
    (out_root / "results.json").write_text(json.dumps({"meta": meta, "runs": records},
                                                      ensure_ascii=False, indent=2) + "\n")
    (out_root / "report.md").write_text(report(records, meta), encoding="utf-8")
    print(f"results: {out_root}")
    failed = [r for r in records if "error" in r]
    return 1 if failed or meta["live_dir_hits"] else 0


if __name__ == "__main__":
    sys.exit(main())
