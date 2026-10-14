---
title: Commands, formats and limits
---
# Commands, formats and limits

The repository provides the SVG renderer now. Install it from a reviewed clone with make setup or python -m pip install -e .; no project package is published on PyPI. [Installation](./index) explains the clone and bundle paths.

## Choose before rendering

[Not sure which diagram? Choose a view.](/choose) The same renderer supports different views, but a layout does not decide what your architecture means.

## Working commands

Run these from an activated checkout environment:

    atlas init C2 -o model.json
    atlas render model.json -o out/
    atlas check out/diagram.svg --model model.json --report out/findings.json
    atlas fonts doctor

The render command writes diagram.svg and diagram.findings.json. The explicit check writes the requested findings.json. Review each finding's severity, rule, element IDs, boxes and message. Exit codes: **0** no findings at the selected failure threshold; **1** findings at/above that threshold (error by default); **2** a tool error. Warnings still need review.

## Optional images and browser checks

For PNG previews and contact sheets, install the CairoSVG extra from the clone:

    python -m pip install -e '.[preview]'
    atlas preview out/diagram.svg -o out/preview.png
    atlas sheet out/diagram.svg -o out/sheet.jpg

CairoSVG may require system Cairo libraries. In an unpacked bundle, install the optional CairoSVG version documented in scripts/requirements.txt. Browser checks additionally require the browser extra and Chromium; availability does not constitute a visual review.

## Fonts and findings

Use fonts doctor to inspect available fonts and CJK coverage. A report with **measured_with: estimate** means fallback measurement was used, not that fit was verified with the intended font. Fix wrapping, layout and font selection rather than shrinking every label. Inspect the final image after changes.

## Supported output and limits

SVG retains editable text; keep model JSON as the source. Native draw.io/PPTX export and lossless round trips are not implemented. The HTML exporter is a library-level wrapper, not a CLI subcommand. Font-subset embedding is not implemented. Use atlas --help for the installed revision rather than assuming planned flags exist.

## No image input

Run available automated checks, produce a preview when possible, and ask a human or image-capable reviewer to inspect it. Report **visual review pending** until that happens. A successful build is not evidence that the diagram tells the right story.
