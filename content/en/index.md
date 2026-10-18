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

Start small: [C2](/types/c2-system-context) → [C3](/types/c3-container-diagram) → [E1](/types/e1-sequence-diagram) → [G1](/types/g1-deployment-diagram). Add [F1 identity delegation](/types/e1-sequence-diagram#variant-f1) and [F2 threat modelling](/types/d2-data-flow-diagram#variant-f2) when the question needs them. There are 25 core entries, 10 named variants and 5 method references; all 40 stable codes and old links remain supported.

<p class="atlas-intro">An atlas of architecture diagram types, and an agent skill that turns a clear question into a useful, evidence-backed picture.</p>

[Find the right diagram →](/choose) · [Browse all types](/types/) · [Use the skill](/use/)

<Figure :svg="workflow" caption="A drawing workflow, not a promise of automatic correctness." />

## An atlas organized around your questions {#explore}

A context diagram explains a system's surroundings. A sequence explains one interaction. A permission model explains authority. Start with what your reader needs to understand—not a favorite notation.

<p class="catalogue-count">{{ theme.catalogue.types.filter(type => type.catalogRole === 'core').length }} core entries · {{ theme.catalogue.types.filter(type => type.available.en).length }} reference pages available</p>

<div class="atlas-grid family-grid">
  <article v-for="(label, key) in Object.fromEntries(Object.entries(theme.catalogue.families).filter(([key]) => theme.catalogue.types.some(type => type.family === key && type.catalogRole === 'core')))" :key="key" class="type-card">
    <span class="type-code">{{ key }}</span>
    <h3><a :href="withBase('/types/#family-' + key)">{{ label.en }}</a></h3>
    <p>{{ theme.catalogue.types.filter(type => type.family === key && type.catalogRole === 'core').length }} types</p>
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

## AI-era sample

[Enterprise Service Assistant: 29 views](/use/ai-service-assistant)
