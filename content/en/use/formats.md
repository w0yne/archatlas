---
title: Formats and troubleshooting
---
# Formats and troubleshooting

## Initial format

The current renderer produces **SVG with editable text** from model JSON. Keep both: rendering does not copy the source model into the output directory. A simple HTML wrapper is available through the Python exporter API, not an HTML CLI command.

**Not yet promised:** draw.io export, editable PowerPoint export, lossless import, or round-trip editing. Embedding one SVG image in a slide is not equivalent to native editable shapes.

## Rendering and checks

From a reviewed clone, `make setup` installs development/site dependencies into the checkout environment; activate `.venv` afterwards. For renderer-only use, create and activate a virtual environment and run `python -m pip install -e .` from the clone root. Do not install a similarly named PyPI package: this project has no published package yet.

```sh
atlas init C2 -o model.json
atlas render model.json -o out/ --lang en --profile doc
atlas check out/diagram.svg --model model.json --lang en --fail-on warning --report out/findings.json
atlas fonts doctor
```

`init` accepts an available type code or a layout family; `--templates DIR` selects another template directory. It resolves default-language labels. `render` writes `out/diagram.svg` and `out/diagram.findings.json`; a named SVG output instead gets a matching `.findings.json`. `check --lang` checks the SVG's language and loads model labels for that locale; it does not translate an existing SVG.

For PNG/contact sheets and real browser geometry checks, install the optional dependencies from the clone:

```sh
python -m pip install -e '.[preview,browser]'
python -m playwright install chromium
atlas preview out/diagram.svg -o out/preview.png --scale 1
atlas sheet out/*.svg -o out/sheet.jpg
atlas check out/diagram.svg --model model.json --lang en --browser --report out/browser.findings.json
```

Preview/sheet use CairoSVG and system Cairo; browser checking uses Playwright, Chromium and its platform libraries. Browser checks run offline and measure actual bounds after fonts are ready. They do not establish semantic correctness or visual quality. Font-subset embedding is not implemented.

Exit **0** means success at the selected threshold, so warnings may remain with the default `--fail-on error`; **1** means findings at/above the threshold; **2** means an input/tool/dependency failure. `render` may write an SVG before returning 1. Reports list findings, severities, element IDs and boxes. Fix the model, render again, re-check the new SVG and then inspect it visually. Element-specific `allow` reasons do not suppress errors or change the exit threshold.

Schema 0.1 also supports authored/localised legends (`meta.legend`, `legend_mode`, `legend_labels`), table panels beside a small diagram, minimum flow ranks and configurable `layout.spacing`. Actor/use-case glyphs and BPMN start/end event borders are available; descriptive process/dataset/job/pipeline kinds are ordinary cards. Lane/state/tree ranking is deterministic but heuristic. The renderer does not guarantee complete formal notation.

## Missing fonts or Chinese glyphs

Use `atlas fonts doctor` to inspect selected fonts and CJK probe coverage. `measured_with: estimate` means some measurement used a conservative estimate; report it. The probe is not all-Unicode coverage, and an SVG's live text still depends on the viewer's fonts. Literal English does not become Chinese just by setting `--lang zh`: supply translation keys and `labels.zh.json`, then re-render. Do not fix clipping by shrinking all labels.

## No browser or no image input

Text and geometry checks can still run. Generate a preview when supported, and hand it to a human or image-capable reviewer. Report **visual review pending**, never visual pass based solely on a successful command.

## A diagram is too dense

Return to the reader's question. Collapse non-focus detail or separate concerns into different views. `slide` keeps 1440×810 and reports overflow; `doc` prefers 1120px and can grow, with a configurable wide-view warning limit. Neither automatically paginates. Keep the full-size image available rather than making labels unreadable on a small screen.
