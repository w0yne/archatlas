# Output formats and how to add one

## What is supported now
| Format | Status | Notes |
|---|---|---|
| SVG (editable text) | **supported** | Primary output. Live `<text>`, stable element ids, `<title>`/`<desc>`, no scripts, no `foreignObject`, no external requests. |
| Model JSON | **supported** | The editable source. SVG is derived from it. |
| HTML page wrapper | **supported** (`export/html_page`) | A responsive/print wrapper around the SVG; not a second source of diagram meaning. |
| PNG preview | supported when a rasteriser exists | For review only; not a deliverable format. |
| draw.io, PowerPoint | **not implemented** | Interfaces and mapping notes only (below). Say so honestly; do not hand over a bitmap and call it editable. |

If the user asks for an unsupported format: deliver SVG plus model JSON, state what is missing, and offer the mapping below as a plan.

## Exporter interface (sketch)
```python
class Exporter(Protocol):          # src/archatlas/export/base.py
    name: str
    capabilities: dict             # e.g. {"editable_text": True, "editable_shapes": True, "connectors_attached": False}
    def export(self, scene: Scene, out: Path, opts: dict) -> dict: ...   # returns a small result record
```
`Scene` (`src/archatlas/layout/base.py`) is the resolved geometry plus semantics and localisation produced after layout (nodes with boxes and ports, edges with waypoints, groups, tables, legend). Exporters never re-run layout and never touch the model schema.

## Planned mappings (not yet implemented)
- **draw.io:** write uncompressed `mxGraphModel` XML — vertices and parent groups, edges with source and target ids, label cells, geometry from the scene. Keep objects editable; do not embed the SVG as an image. No promise of a lossless round trip back to the model.
- **PowerPoint:** native text boxes, shapes, groups and connectors (for example with `python-pptx`); convert canvas units to slide units once; re-check text fit after export; report effects that cannot be mapped instead of silently rasterising.
- **HTML:** embed the SVG with accessible prose; no separate semantics.

## Adding an exporter
1. Implement the protocol under `src/archatlas/export/`; declare honest capabilities.
2. Add a golden test from an example scene; add the row to the table above.
3. Document dependencies and limits in this file. Exporters must not need network access.
4. Keep language, topology, evidence status and diagram selection independent of the output format's idioms (CSS classes, EMUs, mxGraph styles).
