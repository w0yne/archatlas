# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

**Skill**
- The `architecture-diagrams` skill: mode selection, brief, type choice, wireframe, render,
  check and review.
- Repository mode, which derives diagrams from evidence in a code repository.

**Content**
- A catalogue of 40 diagram types (A1–I2, plus the split types A9 and H3). Each type has
  aliases, facets and cited standards.
- A generated selection guide: decision tree, audience × question matrix and alias index.

**Renderer**
- The `atlas` CLI: render, check, preview, sheet and fonts doctor.
- A versioned model schema and SVG output with geometry, text-fit and contrast checks.

**Examples and site**
- Worked examples and per-type model templates.
- A bilingual documentation site (English first, Chinese mirror), built with VitePress.

**Tooling**
- An evaluation harness for Claude Code, Codex and Pi, run with and without the skill.
- Release tooling: a private-content lint, a deterministic skill zip with install checks,
  and third-party notices.
