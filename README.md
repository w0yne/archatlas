# archatlas

[简体中文](README.zh-CN.md)

**Choose the right architecture view. Draw it from evidence.**

archatlas combines a diagram-type atlas with an English-language Agent Skill named architecture-diagrams. The documentation is English-primary with Chinese reference pages.

## Status

0.1.0 pre-release: the repository contains 40 diagram types in English and Chinese, the skill, working SVG renderer, packer and evaluation harness. The first three-host comparison is complete for skill revision 3847acb and did not meet the release gate. It does not certify the current revision: targeted retesting and release certification are pending. [Read the retained report](evals/reports/2026-10-14-first-full.md). No PyPI package or public release bundle is published.

## What it does

- Choose a view for an audience and question.
- Draw from a description, with a wireframe before rendering.
- Read a repository without executing its code, and trace evidence into diagrams.
- Check geometry and separately review meaning and the actual image.

SVG plus model JSON is the initial target. Native draw.io/PowerPoint export and round-trip editing are not yet supported promises.

## Install the skill

From a reviewed clone, install the renderer first:

    make setup
    . .venv/bin/activate
    atlas init C2 -o model.json
    atlas render model.json -o out/

For a renderer-only setup use a virtual environment and python -m pip install -e . instead of make setup. Keep the environment active when starting the agent, then copy skills/architecture-diagrams into **one** discovery location below. Do not install an unpublished package by name.

Alternatively, generate a verified ZIP with python tools/pack_skill.py --out dist --verify. Its unpacked root is architecture-diagrams/ (not skills/architecture-diagrams/), including scripts/lib. Install its scripts/requirements.txt in a virtual environment, then copy that whole root folder.

| Host | Personal location | Explicit invocation |
|---|---|---|
| Claude Code | ~/.claude/skills/architecture-diagrams/ | /architecture-diagrams |
| Codex | ~/.agents/skills/architecture-diagrams/ | $architecture-diagrams |
| Pi | ~/.pi/agent/skills/architecture-diagrams/ | /skill:architecture-diagrams |

Inspect scripts before granting execution permissions. Restart the host after installation; Pi can use /reload. Keep all bundled references/assets, not only SKILL.md. See [installation and first run](content/en/use/index.md).

## Modes

**Autonomous:** choose defaults and state assumptions; ask when a wrong guess changes meaning. **Guided:** walk through consequential choices and approve the wireframe first. Missing answers are never consent. See [modes](content/en/use/modes.md).

## Develop the site

Use the Node version in .nvmrc, then:

    npm run site:install
    npm run check
    npm run build
    npm run site:preview

The site-only package and lockfile live in content/.vitepress; the root package delegates these commands. The install command runs npm ci there. Python/skill users do not need the site dependency tree. Build output is content/.vitepress/dist (ignored).

For a script-free reading export after building, run npm run preview:static --prefix content/.vitepress. It writes flat, relocatable pages under the ignored dist/static-preview directory. Search and dialog controls are intentionally absent from that export; the regular site build retains them.

The language menu returns to the selected locale homepage; each locale has its own navigation. The default base is /archatlas/. Set SITE_BASE for another repository/custom hosting path. English source pages in content/en are rewritten to root URLs; Chinese stays under /zh/. Catalogue/sidebar links use the 40-type registry in content/data/types.yaml. Reader recommendations come from content/data/selection-tree.yaml. Missing future type pages are not linked.

The site uses VitePress 1.6.4. Its dependency audit currently reports upstream development-server advisories; keep dev/preview local, do not expose them to untrusted networks, and review dependency upgrades before a public release. Pages deploys static files, not the Vite development server.

## Compatibility and limits

Host documentation/help research: Claude Code 2.1.285, Codex 0.160.1, Pi 1.1.0. The retained first comparison used these hosts on revision 3847acb; it failed the release quality gate. Fresh packaged-install smoke tests and quality certification for the current revision remain pending. A successful build is not a visual review. Without image input, report visual review pending and hand previews to a suitable reviewer.

## Contribute and license

See [CONTRIBUTING](CONTRIBUTING.md), [community conduct](CODE_OF_CONDUCT.md) and [security reporting](SECURITY.md). Contributions require DCO sign-off, not a CLA. Newly authored code, instructions, docs and examples are Apache-2.0; third-party material retains its own license. Use generic examples only—no confidential content or private paths.
