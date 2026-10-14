---
title: Install and use the skill
---
# Install and use the skill

archatlas 0.1.0 is a **pre-release in this repository**: the English skill, 40 diagram references, SVG renderer, packer and evaluation harness exist. No PyPI release is available. The first three-host comparison is complete for skill revision 3847acb and did not meet the release gate. It does not certify the current revision: targeted retesting and release certification are pending. [Read the first-run report](/evaluation-report.txt).

## Option A: use a reviewed clone

From the repository root, the complete development setup is:

    make setup
    . .venv/bin/activate
    atlas --help

For the renderer only (without site development dependencies):

    python3 -m venv .venv
    . .venv/bin/activate
    python -m pip install -e .

Then copy the skill folder as shown below. **Start the agent from this activated environment** so its helper can import the installed renderer. Copying the source skill folder alone does not install Python dependencies or the renderer library. Do not run pip install archatlas: the package name is not published by this project.

## Option B: use a verified bundle

A bundle is produced from a reviewed clone with:

    python tools/pack_skill.py --out dist --verify

Unzip the chosen archive and enter the unpacked directory. Its top-level folder is **architecture-diagrams/**, not skills/architecture-diagrams/. It includes scripts/lib; third-party Python packages are installed separately:

    python3 -m venv .venv
    . .venv/bin/activate
    python -m pip install -r architecture-diagrams/scripts/requirements.txt

Copy that entire architecture-diagrams folder into one host location below. Keep the environment active when starting the agent. Review source, archive checksum and scripts before installation; do not substitute a similarly named registry package.

## Choose one host location

| Host | Personal location | Explicit invocation |
|---|---|---|
| Claude Code | ~/.claude/skills/architecture-diagrams/ | /architecture-diagrams |
| Codex | ~/.agents/skills/architecture-diagrams/ | $architecture-diagrams |
| Pi | ~/.pi/agent/skills/architecture-diagrams/ | /skill:architecture-diagrams |

For example, from a clone after installing its renderer:

    mkdir -p ~/.claude/skills
    cp -R skills/architecture-diagrams ~/.claude/skills/

From an unpacked bundle, use cp -R architecture-diagrams ~/.claude/skills/ instead. Use the corresponding destination for Codex or Pi; avoid duplicate discovery locations. Restart the agent after installation; Pi can use /reload.

## First request and first render

[Not sure which diagram? Choose a view first.](/choose)

> Guided mode. Help a new developer understand checkout, payment and inventory. Recommend one view and explain what it leaves out. Use English labels.

To exercise the installed renderer from the clone:

    atlas init C2 -o model.json
    atlas render model.json -o out/
    atlas check out/diagram.svg --model model.json --report out/findings.json

The renderer accepts type codes from shipped templates. Review findings and the actual image; a command finishing is not a quality guarantee. [Commands and limits](./formats) explain optional preview dependencies and exit codes.

## Updating and removing

Replace only this skill's folder with a reviewed version, update its Python environment, then restart/reload the host. Do not remove the host's entire skills directory.

## Compatibility status

Documentation/help research covered Claude Code 2.1.285, Codex 0.160.1 and Pi 1.1.0. These are not completed cross-host output-quality certifications. Official references: [Claude Code](https://code.claude.com/docs/en/skills), [Codex](https://developers.openai.com/codex/skills), [Pi](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/skills.md).
