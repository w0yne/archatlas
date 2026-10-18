# Changelog

## Unreleased — compatibility and environment isolation repair

- Restore every historical catalogue fragment, including named variants, method
  references and the former view-framework family; all links remain readable without JS.
- Enforce the complete baseline: 104 public HTML pages and all 2354 original IDs,
  including catalogue and other non-type pages, in each site build.
- Remove private environment identifier names from current public documentation,
  adapter code and tests. Replace product-specific prefix filtering with an exact
  provider-variable allowlist, protected sandbox roots and checked state paths.
- Extend the existing external private-name audit with explicit identifier-prefix
  entries, and inspect metadata for every commit rather than only the first diff.
  Keep audit lists outside the repository; findings redact matched terms.
- This is a forward-only repair. Previously published commits retain the former
  identifiers; no history has been rewritten. Intentional public contributor/repository
  references may match an external audit list and must be reported, not silently waived.

## Unreleased — integrated scenario and complete view set

- Integrate all 25 core views and four named variants, with 58 hand-authored EN/ZH SVGs;
  preserve AWS as G1 headline and add its separate generic hosting counterpart.
- Resolve teaching assumptions centrally in scenario/glossary version 2: ingestion,
  lifecycle, permissions, accountability, network, release/recovery, telemetry, data and interfaces.
- Validate semantic projections against shared definitions, publish all manifest entries,
  include the shared glossary in packages and add targeted S6/S11/S12 contract regressions.
- Historical scores/fixtures are unchanged. Production validation and independent review
  remain separate; these are illustrative diagrams, not deployed or benchmarked services.

## Catalogue consolidation foundation

- Consolidate discovery to 25 core entries, 10 named variants and 5 method references,
  preserving all 40 stable codes, bilingual legacy pages, anchors and historical samples.
- Keep identity and threat variants prominent; rename G1 Deployment & cloud architecture
  with a vendor-neutral recipe and a named AWS headline illustration.
- Add frozen fictional Enterprise Service Assistant facts and seven hand-authored sample
  views per language; validate manifest, shared labels/topology and byte-preserving copying.
- Package the same scenario and examples with the skill. Preserve historical eval revisions.
- The integrated candidate completes core/variant examples and contract synchronization.
  Independent review and release-level publication checks remain. See
  [decision](docs/decisions/2026-10-consolidation.md).


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
