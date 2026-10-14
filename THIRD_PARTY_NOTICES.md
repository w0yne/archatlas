# Third-party notices

archatlas is licensed under Apache-2.0 (see `LICENSE` and `NOTICE`). This file lists the
third-party software and material that archatlas uses or refers to, and their licences.
Audit date: 2026-10-14. Versions are the pins in `skills/architecture-diagrams/scripts/requirements.txt`,
`pyproject.toml` and `content/.vitepress/package-lock.json`.

## 1. Software

### Bundled in a release artifact

**Release zip** (`tools/pack_skill.py`): only archatlas's own code and text are inside.
Third-party packages are *installed* by the user from PyPI and are not redistributed.

**Built documentation site:**

The client build emits `THIRD_PARTY_LICENSES.txt` with the complete copyright and
permission texts, plus `third-party-manifest.json` listing the versions identified from
emitted JavaScript and CSS modules. Both are linked from the bilingual About/licences
pages. `LICENSE.txt`, `NOTICE.txt` and `THIRD_PARTY_NOTICES.txt` accompany them.

The build includes VitePress, Vue runtime packages, VueUse, MiniSearch, the SVG parser,
focus/marking utilities and the Vite preload helper. Even the unused search option's
emitted DocSearch CSS needs its notice. Do not equate installed dependencies with
distributed code: the generated manifest is the build inventory, not a lockfile count.

VitePress also embeds **Lucide icons (ISC), including Feather portions (MIT)** in CSS.
Their complete upstream notices are stored under `content/.vitepress/licenses/` and
appended to the generated text. DocSearch 3.8.2 omits its licence file from the npm
package; the version-specific upstream MIT text and provenance are recorded in
`licenses/overrides.json`. Missing licence text for a newly emitted package fails the
build rather than being replaced with a guessed permission notice.

### Python, runtime (installed by the user)

| Package | Version | Licence | Use | Apache-2.0 compatible |
|---|---|---|---|---|
| Pillow | 12.3.0 | MIT-CMU (HPND-style) | font measurement | yes, permissive |
| fontTools | 4.60.1 | MIT | glyph coverage, font metadata | yes |
| jsonschema | 4.26.0 | MIT | model validation | yes |
| └ attrs, referencing, rpds-py, jsonschema-specifications | (transitive) | MIT | jsonschema dependencies | yes |

### Python, optional or development only (not distributed)

| Package | Version | Licence | Use | Note |
|---|---|---|---|---|
| CairoSVG | 2.8.2 (optional `preview` extra) | LGPL-3.0-or-later | PNG previews | Optional; used as an unmodified library and never vendored or bundled. If a future artifact bundles it, the LGPL terms (licence text, replaceability) apply. |
| Playwright for Python | optional | Apache-2.0 | browser-based visual/font checks | The Chromium it downloads has its own licences. They are not redistributed by archatlas. |
| PyYAML | 6.0.3 | MIT | `tools/*.py`, `evals/` | development only |
| pytest | dev | MIT | tests | development only |

### Node, site build (dev dependencies, `content/.vitepress/package-lock.json`)

The lockfile includes platform-specific optional and transitive build dependencies;
its entry count is not a count of browser libraries. Direct development dependencies:

| Package | Pin | Licence | Role |
|---|---|---|---|
| vitepress | 1.6.4 | MIT | build and browser theme/router |
| vue | 3.5.44 | MIT | browser runtime |
| minisearch | 7.2.0 | MIT | browser local search |
| @xmldom/xmldom | 0.9.12 | MIT | SVG parsing, including browser code |
| yaml | 2.9.1 | ISC | build-time catalogue loading |
| markdown-it | 14.3.2 | MIT | Markdown build/lint |
| markdown-it-cjk-friendly | 3.0.0 | MIT | Markdown build/lint |

Development-only packages are installed by the maintainer, not copied wholesale into
the site. Check the generated manifest and full licence file for each release.

`@iconify-json/simple-icons` is pulled in by VitePress for social-link icons. The icon data
is CC0, but the icons depict third-party brand logos, which remain trademarks of their
owners. archatlas does not configure any of them.

## 2. Fonts

- **Not bundled:** no font files are in the repository or the release zip. SVG output names
  a font stack (for example Noto Sans, Noto Sans CJK SC, DejaVu Sans) and relies on fonts
  installed on the viewer's system.
- **Site:** uses the official VitePress `theme-without-fonts` entry. No Inter webfonts
  are emitted; viewer system fonts are used. The legal build check rejects unexpected
  font assets until their distribution terms are audited.
- **CI:** may install the Noto fonts (SIL Open Font License 1.1) to measure text. They are
  not redistributed.
- **Future font embedding:** the optional `--embed-font-subset` flag (DESIGN §5.2) would
  embed a subset of an OFL-1.1 font into an SVG. That is allowed. The font's copyright and
  licence must then be recorded in this file, and a renamed subset must not use a Reserved
  Font Name (the Noto fonts declare none).

## 3. Standards, notations and names referred to

The documentation and the skill describe diagram types defined or popularised by others.
They refer to these by name and cite them with links. No specification text, diagram, icon
or image from these sources is copied. Examples and samples are newly authored.

| Name | Owner / origin | Status of use |
|---|---|---|
| UML®, BPMN™, OMG® | Object Management Group | Trademarks used to identify the notations |
| ArchiMate®, TOGAF® | The Open Group | Registered trademarks used to identify the standards |
| C4 model | Simon Brown (c4model.com, website content CC BY 4.0) | Terminology used. Any adapted wording would need CC BY attribution; none is copied. |
| arc42 | arc42 (template CC BY-SA 4.0) | Section names are cited only. Template text must not be copied into Apache-2.0 files. |
| BIZBOK® | Business Architecture Guild | Trademark, cited |
| ISO, ISO/IEC, IEC, IEEE standards (e.g. ISO/IEC/IEEE 42010, ISO/IEC 19510, ISO 5807) | ISO / IEC / IEEE | Cited by number; no text reproduced |
| Domain-Driven Design pattern names | Eric Evans and the DDD community | Pattern names used descriptively |
| OpenTelemetry, OpenLineage, SLSA | CNCF / Linux Foundation projects | Names and concepts cited |
| AWS, Microsoft Azure, Google Cloud | their respective owners | Trademarks used to identify the providers; no provider icons included |
| Nielsen Norman Group, Lean Enterprise Institute, Atlassian and other publishers | their respective owners | Articles linked as references |

All other product names are trademarks of their respective owners. Their use does not
imply endorsement.

## 4. Evaluation fixtures

The evaluation scenarios fetch these public repositories at a pinned commit into a temporary
sandbox. They are **not** redistributed:

- `dockersamples/example-voting-app`: Apache-2.0
- `spring-projects/spring-petclinic`: Apache-2.0
