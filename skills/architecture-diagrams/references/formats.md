# Output formats and exporter limits

| Format | Current interface | Limits |
|---|---|---|
| SVG | `atlas render model.json -o out/` | Live text/shapes; keep the model for semantic edits. Text appearance depends on installed fonts. |
| Model JSON | `atlas init C2 -o model.json` | Initializes a shipped template with resolved default-language labels; rendering does not copy the source model into out/. |
| PNG | `atlas preview out/diagram.svg -o out/preview.png` | Requires CairoSVG and system Cairo; raster preview, not editable shapes. |
| Contact sheet | `atlas sheet out/*.svg -o out/sheet.jpg` | Same preview dependency; downscaled to at most 1600px per dimension. |
| HTML wrapper | `HTMLExporter` Python API | Simple responsive SVG plus caption; no HTML CLI command and no print-pagination engine. |
| draw.io / PowerPoint | Not implemented | No CLI exporter, import or lossless round trip. A bitmap is not native editable shapes. |

Installation, CLI options, reports and the fixing loop are in `rendering.md`.
Install from the reviewed checkout or bundle; the project is not yet published
as a PyPI package. Renderer, preview and browser-check dependencies are distinct.
An unavailable optional dependency produces a tool error; it does not create a preview.

## HTML API example

Run with the installed checkout library, from a directory containing model.json:

```python
from pathlib import Path
from archatlas.model import load
from archatlas.layout import layout
from archatlas.export.html_page import HTMLExporter

scene = layout(load("model.json", "en"))
result = HTMLExporter().export(scene, Path("out/diagram.html"), {})
print(result)
```

The result record contains `path` and `format`. This wrapper keeps the SVG's
language and supplies its description as a caption. Inspect the final host page
at its intended sizes; a wrapper is not a new semantic source or proof of readability.

## Exporter interface

`src/archatlas/export/base.py` defines an `Exporter` protocol with `name`,
`capabilities` and `export(scene, out: Path, opts: dict) -> dict`. SVG and HTML
exporters declare editable_text/editable_shapes true and connectors_attached false:
editing an exported shape does not make its arrows follow it. `Scene` contains
resolved geometry, text, connectors, legends and localisation.

To add a format, implement that protocol, declare honest capabilities, verify a
representative scene, and update this table. Keep model meaning and layout separate
from format-specific units and idioms. Future draw.io would need native vertices,
groups and attached edges; PowerPoint would need native shapes/text/connectors,
one unit conversion and fresh text-fit checks. Neither is supplied today.
