from ..render import render_svg


class SVGExporter:
    name = "svg"
    capabilities = {"editable_text": True, "editable_shapes": True, "connectors_attached": False}

    def export(self, scene, out, opts=None):
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_svg(scene, (opts or {}).get("namespace")), encoding="utf-8")
        return {"path": str(out), "format": self.name}
