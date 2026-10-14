# Reviewing a rendered diagram

Keep semantic review (does the view tell the truth?) separate from geometry and
visual review (can the reader understand it?). Automated success proves neither.

## 1. Fixing loop

Model and semantic review → render → check the emitted SVG → fix the model →
re-render/re-check → preview and visual review. Review the exact final bytes.
From the skill folder, with its dependencies installed:

```sh
scripts/atlas render out/model.json -o out/ --lang en
scripts/atlas check out/diagram.svg --model out/model.json --lang en --fail-on warning --report out/findings.json
scripts/atlas check out/diagram.svg --model out/model.json --lang en --browser --report out/browser.findings.json
scripts/atlas preview out/diagram.svg -o out/preview.png
scripts/atlas sheet out/*.svg -o out/sheet.jpg
```

Browser checking needs the optional Playwright dependency and Chromium; previews
need CairoSVG/Cairo. Installation and exact output/exit-code rules: `rendering.md`.
`check --lang` does not translate an existing SVG. Missing tools are not a pass.

## 2. Semantic review

- Does the figure answer its audience's question at a consistent level?
- Do boundaries, element kinds and relationships match the described system?
- Are facts, inferences, proposals and target state distinguishable? Repository
  diagrams need traceable evidence for the elements and relationships.
- Do names, guards, cardinalities and numbered steps say what actually happens?
- Does the legend explain meanings? Override defaults with authored, localised
  legend labels when needed; do not expose renderer identifiers to the reader.
- Revisions: compare the labels before and after. Every user-written label is still present, in its
  original language (mixed English/Chinese stays mixed); none was deleted or translated to fit.
- Repository diagrams: every non-verified claim carries `evidence.status` in the model and is visibly
  marked (dashed edge, doc-only mark) on the figure.
- Companion views: does each one answer its own question in its own notation (for example F2 marks
  trust boundaries and the data crossing them), rather than regrouping the main view?
- Does the chosen notation require information this template cannot express?
  Do not claim complete UML/BPMN/ArchiMate conformance from a geometry check.

## 3. Automated geometry review

Reports contain counts and findings with id/severity/rule/elements/boxes/message.
Static checks cover measured text fit, overlaps, label backgrounds, connector
ports, unrelated boxes/labels crossed, contrast, membership and some hygiene.
Browser mode adds actual text/shape bounds after fonts are ready, offline.
Neither mode guarantees glyph identity or absence of tofu: inspect CJK text. In estimate mode
(`measured_with: estimate`) never state that Chinese/CJK text displays correctly unless you viewed a
preview rendered with a CJK-capable font.

Fix errors. Fix or explain warnings per element; model `allow` entries keep
reasons but do not suppress errors or alter the failure threshold. Exit 0 at the
default error threshold may still include warnings. Run `--fail-on warning` when
the acceptance condition requires none. A valid source model and matching
node/edge identities do not prove that every visible word or relationship is correct.

## 4. Visual review

Determine image support from the actual tool/API route, not just the model name.
If you can read images, start with the downscaled contact sheet, then inspect
full-size complex or flagged figures. Look for clipped/overlapping text, too-small
labels, ambiguous shared line segments, wrong arrow origins, missing glyphs,
indistinguishable styles, awkward spacing and the last figure in a set.

Open each image once, record element-specific findings immediately, and track the
session's image budget. After a correction, render new files and review them.
For large sets, delegate subsets only when delegation is available and permitted.

If you cannot read images, run the checks you can, produce previews when possible,
and hand them to an image-capable reviewer. State **visual review pending** with
paths and limitations. Never infer a visual pass from DOM/geometry checks. The
CLI always leaves visual_review pending; record a completed review separately
with exactly which images you inspected. Claim **visual review done** only when you
actually opened the rendered image file(s) in this session; list those file paths in
the delivery summary so the claim can be audited on any host. Reading SVG source or
check output is not a visual review.

## 5. Independent review and handoff

For consequential deliverables, an independent reviewer can assess the model and
rendered bytes without the author's explanation. Batch the findings into a revision.
Report: type/audience/state; checks and remaining findings; measured or estimated
fonts; visual review done/pending and its scope; verified/inferred/proposed content;
remaining questions. Deliver SVG with its model, plus previews when available.
