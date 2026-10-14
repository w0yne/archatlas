# Evaluations

[中文](README.zh-CN.md)

This harness checks whether the `architecture-diagrams` skill makes agents produce better
diagrams. It runs each scenario headless on Claude Code, Codex and Pi, once with the skill
installed and once without it (DESIGN §8).

## Contents

| Path | What it is |
|---|---|
| `scenarios/s01…s10-*.yaml` | Ten task scenarios: prompt, mode(s), scripted answers for guided mode, fixtures, expected content |
| `scenarios/triggers.yaml` | Trigger set: 6 prompts that should load the skill, 6 near misses that should not |
| `scenarios/fixtures/` | Small synthetic input files (S9) |
| `rubric.md` | Hard gates and 0–3 scores per dimension |
| `run_eval.py` | Runner: sandbox, fixtures, turns, metrics, `results.json` and `report.md` |
| `adapters/{claude,codex,pi}.py` | One adapter per host: config, command line, event parsing |
| `hosts.example.yaml` | Template for your local hosts file |
| `tests/` | Harness invariants (`python3 -m unittest discover -s evals/tests`) |

The repository scenarios S7 and S8 use public Apache-2.0 repositories pinned by full commit.
The runner fetches them read-only into the sandbox and never runs their code.

## Running

```sh
cp evals/hosts.example.yaml evals/hosts.local.yaml     # edit models and credentials (by variable name)
python3 evals/run_eval.py --list
python3 evals/run_eval.py --hosts evals/hosts.local.yaml --scenario S6 --mode autonomous --dry-run
python3 evals/run_eval.py --hosts evals/hosts.local.yaml --scenario S6 --mode autonomous \
    --host claude --host codex --host pi --arm skill --arm noskill
python3 evals/run_eval.py --hosts evals/hosts.local.yaml --scenario T --host claude   # trigger set
```

Results go to `evals/results/<timestamp>/` (gitignored). Each run has these files:

- `turnN.events.jsonl`, `turnN.stderr.txt` and `turnN.argv.json` for every turn
- `env-keys.json`: the names of the child's environment variables, never their values
- `final.txt`: the last reply
- `out/`: the files the agent produced
- `record.json`: the run's measurements

`results.json` and `report.md` summarise all runs. They record exit codes, wall time,
tokens, cost (where the host reports it), clarification turns, skill-load evidence and the
automatic SVG gate (G5). Raters add `scores.json` as described in `rubric.md`.

**Skill loaded** is taken from the host's trace, never from the answer text. The trace
must show one of these:

- the `SKILL.md` body;
- a read of a file in the skill directory;
- for Claude Code, a `Skill` tool call.

When the skill is invoked by name and the host injects it without a trace event, the value
is `unknown`.

## Isolation

Each run gets a fresh directory under `--work-root` (default: the system temp directory).
Keep it outside any folder that contains `AGENTS.md` or `CLAUDE.md`, because hosts load
those files from parent directories. The fresh directory contains:

- a `HOME`, `TMPDIR` and XDG directories;
- the host's configuration directory: `~/.claude`, `CODEX_HOME` or `PI_CODING_AGENT_DIR`;
- a git workspace.

The child process's environment is built from scratch. It receives only:

- the variables listed above;
- the literal `env` values from the hosts file;
- the variables named in `pass_env`.

Variables starting with `RCC_`, `CYBERWARE_`, `PI_`, `CLAUDE` or `CODEX_` are never
forwarded from the parent.

**Per-host details:**

- **Claude Code:** the skill is installed as a project skill in the workspace. The runner
  uses `--setting-sources project` and never `--bare`.
- **Codex:** the skill goes into the sandbox's `CODEX_HOME/skills`, with `--ignore-rules`.
  Single-turn runs add `--ephemeral`.
- **Pi:** the runner passes `--no-skills --no-extensions --no-mcp`. In the with-skill arm it
  also passes the skill explicitly with `--skill`. Single-turn runs add `--no-session`.

**Cleanup and leak check:** the sandbox is deleted afterwards unless you pass
`--keep-sandboxes`. At the end, the runner scans the real host directories (`~/.claude`,
`~/.codex`, `~/.pi`, or the paths given with `--live-dir`) for files that changed during the
run and mention a sandbox path. Any hit fails the run.

**Codex sandbox:** Codex uses `--sandbox workspace-write` by default. On machines where
bubblewrap cannot create namespaces, set `sandbox: danger-full-access` in the hosts file.
The run is then contained only by its temporary directory, so use a disposable machine or
container for full evaluations.
