"""Offline command-line interface. Exit 0 clean, 1 findings, 2 tool error."""
import argparse
from io import BytesIO
import json
from pathlib import Path
import sys
from xml.etree import ElementTree as ET

from .check import check_svg
from .fonts import FontMetrics
from .layout import layout
from .model import load
from .render import render_svg

TEMPLATES = ("nested", "layered", "sequence", "lanes", "grid_table", "er", "statechart", "tree")


def save_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def failed(report, level):
    return any(f["severity"] in (("error", "warning") if level == "warning" else ("error",))
               for f in report["findings"])


def raster(svg, scale=1):
    from .check.report import check_svg
    report = check_svg(svg)
    if any(f["rule"] in ("unsafe-svg", "structure") for f in report["findings"]):
        raise ValueError("Refusing to rasterize unsafe or invalid SVG")
    try:
        import cairosvg
    except ImportError as error:
        raise RuntimeError("PNG preview needs CairoSVG: install archatlas[preview]") from error
    return cairosvg.svg2png(bytestring=svg.encode("utf-8"), scale=scale, unsafe=False)


def initial(template):
    model = {"archatlas": "0.1", "meta": {"type": template, "title": "Example diagram", "lang": "en"},
             "layout": {"template": template}}
    if template == "grid_table":
        model["tables"] = [{"id": "access", "columns": ["Role", "Read", "Edit"],
                            "rows": [["Reader", "Yes", "No"], ["Editor", "Yes", "Yes"]]}]
    else:
        kind = {"sequence": "lifeline", "er": "entity", "statechart": "state", "lanes": "task"}.get(template, "system")
        model["nodes"] = [{"id": "client", "kind": kind, "label": "Client"},
                          {"id": "service", "kind": kind, "label": "Service", "style": "primary"}]
        model["edges"] = [{"from": "client", "to": "service", "label": "Sends request"}]
        if template in ("layered", "lanes"):
            kind = "lane" if template == "lanes" else "layer"
            model["groups"] = [{"id": "first", "title": "Request", "kind": kind},
                               {"id": "second", "title": "Processing", "kind": kind}]
            model["nodes"][0]["parent"], model["nodes"][1]["parent"] = "first", "second"
    return model


def parser():
    root = argparse.ArgumentParser(prog="atlas", description=__doc__)
    commands = root.add_subparsers(dest="command", required=True)
    init = commands.add_parser("init")
    init.add_argument("template", choices=TEMPLATES)
    init.add_argument("-o", "--output", default="model.json")
    render = commands.add_parser("render")
    render.add_argument("model")
    render.add_argument("-o", "--output", required=True, help="Output directory or .svg path")
    render.add_argument("--lang")
    render.add_argument("--profile", choices=("slide", "doc"))
    render.add_argument("--namespace", help="Override deterministic SVG ID prefix when inlining")
    render.add_argument("--embed-font-subset", action="store_true")
    render.add_argument("--fail-on", choices=("error", "warning"), default="error")
    check = commands.add_parser("check")
    check.add_argument("svg")
    check.add_argument("--model")
    check.add_argument("--report", required=True)
    check.add_argument("--browser", action="store_true")
    check.add_argument("--fail-on", choices=("error", "warning"), default="error")
    preview = commands.add_parser("preview")
    preview.add_argument("svg")
    preview.add_argument("-o", "--output", required=True)
    preview.add_argument("--scale", type=float, default=1)
    sheet = commands.add_parser("sheet")
    sheet.add_argument("svgs", nargs="+")
    sheet.add_argument("-o", "--output", required=True)
    fonts = commands.add_parser("fonts")
    fonts.add_argument("action", nargs="?", choices=("doctor",), default="doctor")
    return root


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        if args.command == "init":
            save_json(args.output, initial(args.template))
        elif args.command == "fonts":
            print(json.dumps(FontMetrics().doctor(), indent=2, ensure_ascii=False))
        elif args.command == "render":
            if args.embed_font_subset:
                raise ValueError("Font subsetting is not implemented; output uses installed live fonts")
            model = load(args.model, args.lang)
            if args.profile:
                model["layout"]["profile"] = args.profile
            metrics = FontMetrics()
            scene = layout(model, metrics)
            svg = render_svg(scene, args.namespace)
            destination = Path(args.output)
            if destination.suffix.lower() != ".svg":
                destination = destination / "diagram.svg"
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(svg, encoding="utf-8")
            report = check_svg(svg, metrics)
            save_json(destination.with_suffix(".findings.json"), report)
            print(json.dumps({"svg": str(destination), "errors": report["errors"],
                              "warnings": report["warnings"], "visual_review": "pending"}))
            return int(failed(report, args.fail_on))
        elif args.command == "check":
            if args.browser:
                raise ValueError("Browser QA is not implemented; static checks do not prove visual correctness")
            svg = Path(args.svg).read_text(encoding="utf-8")
            report = check_svg(svg)
            if args.model and not any(f["rule"] in ("unsafe-svg", "structure") for f in report["findings"]):
                root = ET.fromstring(svg)
                model = load(args.model, root.get("lang"))
                expected_nodes = {n["id"] for n in model.get("nodes", []) + model.get("groups", [])}
                actual_nodes = {e.get("data-id") for e in root.iter() if e.get("data-role") in ("node", "group")
                                and e.get("data-kind") != "frame"}
                expected_nodes -= {g["id"] for g in model.get("groups", []) if g["kind"] == "frame"}
                expected_edges = {(e.get("id", f"edge-{i + 1}"), e["from"], e["to"])
                                  for i, e in enumerate(model.get("edges", []))}
                actual_edges = {(e.get("data-id"), e.get("data-from"), e.get("data-to")) for e in root.iter()
                                if e.get("data-role") == "edge" and e.get("data-kind") not in ("legend", "lifeline")}
                if expected_nodes != actual_nodes or expected_edges != actual_edges:
                    report["findings"].append({"id": f"finding-{len(report['findings']) + 1}", "severity": "error",
                                                "rule": "model-topology", "elements": [], "boxes": [],
                                                "message": "SVG node/edge identities differ from the supplied model"})
                    report["errors"] += 1
            save_json(args.report, report)
            print(json.dumps({"errors": report["errors"], "warnings": report["warnings"]}))
            return int(failed(report, args.fail_on))
        elif args.command == "preview":
            if not 0 < args.scale <= 4:
                raise ValueError("Preview scale must be greater than zero and at most four")
            destination = Path(args.output)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(raster(Path(args.svg).read_text(encoding="utf-8"), args.scale))
        elif args.command == "sheet":
            from PIL import Image, ImageDraw
            columns = min(3, len(args.svgs))
            rows = (len(args.svgs) + columns - 1) // columns
            cell_w, cell_h = min(520, 1600 // columns), min(330, 1600 // rows)
            sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), "white")
            draw = ImageDraw.Draw(sheet)
            for i, path in enumerate(args.svgs):
                image = Image.open(BytesIO(raster(Path(path).read_text(encoding="utf-8")))).convert("RGB")
                image.thumbnail((cell_w - 16, max(1, cell_h - 36)))
                x, y = (i % columns) * cell_w, (i // columns) * cell_h
                sheet.paste(image, (x + 8, y + 28))
                draw.text((x + 8, y + 7), Path(path).stem, fill="black")
            destination = Path(args.output)
            destination.parent.mkdir(parents=True, exist_ok=True)
            sheet.save(destination)
        return 0
    except (ValueError, RuntimeError, OSError, ImportError, KeyError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
