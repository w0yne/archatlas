---
layout: doc
sidebar: false
aside: false
title: Choose the view before drawing the boxes
description: An architecture-diagram atlas and a portable drawing skill.
---
<script setup>
import { useData } from 'vitepress';
import workflow from '../.vitepress/fixtures/workflow.svg?raw';
const { theme } = useData();
</script>
<p class="atlas-kicker">ARCHITECTURE, WITH INTENT</p>

# Choose the view before drawing the boxes

<p class="atlas-intro">An atlas of architecture diagram types, and an agent skill that turns a clear question into a useful, evidence-backed picture.</p>

[Use the skill →](/use/) · [Explore the atlas ↓](#explore) · [Help improve it](/improve/)

<Figure :svg="workflow" caption="A drawing workflow, not a promise of automatic correctness." />

## One question. The right view. {#explore}

A context diagram explains a system's surroundings. A sequence explains one interaction. A permission model explains authority. Start with what your reader needs to understand—not a favorite notation.

<p v-if="theme.catalogue.fixture" class="translation-banner">Scaffold preview: three catalogue examples are shown while the full type registry and reference pages are integrated. These cards are not release-ready references.</p>

<div class="atlas-grid"><TypeCard v-for="type in theme.catalogue.types" :key="type.code" :type="type" /></div>

## Three ways to work

- **Choose a diagram.** Get a recommended view, an alternative, and the reason for each.
- **Draw from a description.** Set the audience and boundaries, review a wireframe, then render and check.
- **Read a repository.** Trace evidence into a model and selected views. Code declarations are not proof of deployed behavior.

## SVG first. Honest about limits.

The initial target is editable-text SVG plus model JSON. draw.io and native PowerPoint exports are future interfaces, not available features. A clean geometry check does not replace semantic or visual review.

This is an early site scaffold. The renderer, packaged skill, complete catalogue and cross-agent release evaluation are being integrated independently. No release compatibility claim is implied.
