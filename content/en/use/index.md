---
title: Install and use the skill
---
# Install and use the skill

The portable skill is named **architecture-diagrams**. It contains instructions, references and local helper entry points. The site is not required to use an installed skill.

::: warning Pre-release instructions
These steps describe installation from a complete, reviewed checkout or release bundle. This scaffold alone does not contain the renderer or packaged skill. Do not install an unrelated package just because it has a similar name.
:::

## Review before installing

Inspect the skill and scripts before allowing them to run. Use a trusted release, keep a copy of its version, and avoid duplicate installations under multiple discovery paths. The renderer targets Python 3.10+; a browser is optional for visual QA. Follow the bundle's dependency instructions.

## Claude Code

From the root of a complete bundle:

    mkdir -p ~/.claude/skills
    cp -R skills/architecture-diagrams ~/.claude/skills/

Start a new session and invoke:

    /architecture-diagrams mode=guided Help me choose a view for an online shop.

## Codex

    mkdir -p ~/.agents/skills
    cp -R skills/architecture-diagrams ~/.agents/skills/

Start a new session and invoke:

    $architecture-diagrams mode=autonomous Draw a system context for an online shop.

## Pi

    mkdir -p ~/.pi/agent/skills
    cp -R skills/architecture-diagrams ~/.pi/agent/skills/

Use /reload in an existing session, then invoke:

    /skill:architecture-diagrams mode=guided Show me the important architecture choices.

To try a complete skill folder for one run without copying it:

    pi --skill ./skills/architecture-diagrams

## Your first request

Say who will read the diagram, which question it should answer, whether it is current or proposed, the system boundary, and the output language. For example:

> Guided mode. Help a new developer understand how checkout communicates with payment and inventory. Use English labels. Do not infer a deployment topology.

Expect a type recommendation, wireframe, source model, rendered SVG and an explicit review status. If missing information changes the architecture's meaning, the agent should ask rather than silently invent it.

## Updating and removing

Replace only the installed architecture-diagrams folder with a reviewed release. To uninstall, remove that folder from the selected discovery location and restart/reload the host. Never remove the host's whole skills directory.

## Compatibility status

Documentation and CLI-help research covered Claude Code 2.1.285, Codex 0.160.1 and Pi 1.1.0. **These are not completed installation or output-quality certifications.** Cross-host release smoke tests remain pending.

Official host references: [Claude Code skills](https://code.claude.com/docs/en/skills), [Codex skills](https://developers.openai.com/codex/skills), [Pi skills](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/skills.md).

Next: [choose an interaction mode](./modes) or [derive views from code](./code-to-diagram).
