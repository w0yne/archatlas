---
layout: doc
sidebar: false
aside: false
title: Choose the view before drawing the boxes
description: An architecture-diagram atlas and a portable drawing skill.
---
<script setup>
import { useData, withBase } from 'vitepress';
import workflow from '../.vitepress/fixtures/workflow.svg?raw';
const { theme } = useData();
</script>
<p class="atlas-kicker">ARCHITECTURE, WITH INTENT</p>

# Choose the view before drawing the boxes

<p class="atlas-intro">An atlas of architecture diagram types, and an agent skill that turns a clear question into a useful, evidence-backed picture.</p>

[Find the right diagram →](/choose) · [Browse all types](/types/) · [Use the skill](/use/)

<Figure :svg="workflow" caption="A drawing workflow, not a promise of automatic correctness." />

## An atlas organized around your questions {#explore}

A context diagram explains a system's surroundings. A sequence explains one interaction. A permission model explains authority. Start with what your reader needs to understand—not a favorite notation.

<p class="catalogue-count">{{ theme.catalogue.types.length }} diagram types · {{ theme.catalogue.types.filter(type => type.available.en).length }} reference pages available</p>

<div class="atlas-grid family-grid">
  <article v-for="(label, key) in theme.catalogue.families" :key="key" class="type-card">
    <span class="type-code">{{ key }}</span>
    <h3><a :href="withBase('/types/#family-' + key)">{{ label.en }}</a></h3>
    <p>{{ theme.catalogue.types.filter(type => type.family === key).length }} types</p>
  </article>
</div>

## Three ways to work

- **Choose a diagram.** Get a recommended view, an alternative, and the reason for each.
- **Draw from a description.** Set the audience and boundaries, review a wireframe, then render and check.
- **Read a repository.** Trace evidence into a model and selected views. Code declarations are not proof of deployed behavior.

## Try a focused request

> Guided mode. Help a new developer understand checkout, payment and inventory. Recommend one view and explain what it leaves out.

From a reviewed clone, install the renderer before copying the skill:

    make setup
    . .venv/bin/activate
    atlas init C2 -o model.json
    atlas render model.json -o out/

The [installation guide](/use/) distinguishes clone and bundle layouts for Claude Code, Codex and Pi. Keep the Python environment active when starting the agent; the site is not required at runtime.

## SVG first. Honest about limits.

The initial target is editable-text SVG plus model JSON. draw.io and native PowerPoint exports are future interfaces, not available features. A clean geometry check does not replace semantic or visual review.

Version 0.1.0 is a pre-release in this repository: 40 diagram types in English and Chinese, the skill, SVG renderer, packer and evaluation harness are present. No PyPI package or public release bundle is published. The first three-host comparison is complete for skill revision 3847acb and did not meet the release gate. It does not certify the current revision: targeted retesting and release certification are pending. [Read the first-run report](/evaluation-report.txt). [See commands and current limits](/use/formats).
