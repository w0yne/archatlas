# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Verification status / 验证状态

- The first comparison of skill revision `3847acb` is complete and failed the release gate. Current-revision retesting/certification remains pending; see the [retained report](evals/reports/2026-10-14-first-full.md) and [release checklist](docs/RELEASE.md).
- 首轮对比已完成，修订 `3847acb` 未通过发布门槛；当前修订仍待复测与认证，不因构建成功而宣称质量通过。

### Fixed / 修正

- Built-site distribution now includes full third-party copyright/licence texts derived from emitted client modules, explicit embedded-icon notices and bilingual About links. Missing notices fail the build.
- 静态站点随构建交付实际模块及内嵌图标的完整许可通知，并提供双语入口；不再把开发依赖清单当成分发清单。
- Reviewed expanded selection aliases and the added developer multi-view recommendation in Chinese, without hand-editing generated blocks.
- 中文选图页已核对扩充别名及开发者多视图推荐，生成块仍由原生成器维护。

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
