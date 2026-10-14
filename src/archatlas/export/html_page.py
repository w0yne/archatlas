from html import escape
from ..render import render_svg


class HTMLExporter:
    name = "html"
    capabilities = {"editable_text": True, "editable_shapes": True, "connectors_attached": False}

    def export(self, scene, out, opts=None):
        page = '<!doctype html><html lang="' + escape(scene.lang, quote=True) + '"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        page += "<title>" + escape(scene.title) + "</title>"
        page += "<style>body{margin:24px;font-family:sans-serif}svg{max-width:100%;height:auto}figure{margin:0}</style>"
        page += "<figure>" + render_svg(scene, (opts or {}).get("namespace"))
        page += "<figcaption>" + escape(scene.description) + "</figcaption></figure></html>\n"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")
        return {"path": str(out), "format": self.name}
