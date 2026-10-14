"""Check the actual SVG primitives, not a trusted precomputed pass flag."""
import json
import re
from xml.etree import ElementTree as ET

from .contrast import ratio
from ..fonts.measure import FontMetrics
from ..layout.route import segment_hits_rect, crosses


def overlap(a, b, tolerance=1):
    return min(a[0] + a[2], b[0] + b[2]) - max(a[0], b[0]) > tolerance and \
        min(a[1] + a[3], b[1] + b[3]) - max(a[1], b[1]) > tolerance


def contains(a, b, tolerance=1):
    return a[0] - tolerance <= b[0] and a[1] - tolerance <= b[1] and \
        a[0] + a[2] + tolerance >= b[0] + b[2] and a[1] + a[3] + tolerance >= b[1] + b[3]


def shape_box(element):
    tag = element.tag.rsplit("}", 1)[-1]
    f = lambda key, default=0: float(element.get(key, default))
    if tag == "rect":
        return f("x"), f("y"), f("width"), f("height")
    if tag == "ellipse":
        return f("cx") - f("rx"), f("cy") - f("ry"), 2 * f("rx"), 2 * f("ry")
    if tag == "polygon":
        points = [tuple(map(float, point.split(","))) for point in element.get("points", "").split()]
        xs, ys = zip(*points)
        return min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys)
    return None


def check_svg(svg, metrics=None):
    metrics = metrics or FontMetrics()
    findings = []

    def add(rule, message, elements=(), boxes=(), severity="error"):
        findings.append({"id": f"finding-{len(findings) + 1}", "severity": severity, "rule": rule,
                         "elements": list(elements), "boxes": list(boxes), "message": message})

    if "<!DOCTYPE" in svg.upper() or "<!ENTITY" in svg.upper():
        add("unsafe-svg", "DTD/entity declarations are forbidden")
        return {"schemaVersion": 1, "findings": findings, "errors": 1, "warnings": 0}
    try:
        root = ET.fromstring(svg)
    except ET.ParseError as error:
        add("structure", str(error))
        return {"schemaVersion": 1, "findings": findings, "errors": 1, "warnings": 0}
    elements = list(root.iter())
    if root.get("data-archatlas") != "0.1":
        add("unsupported-geometry", "Static ownership checks require an Archatlas SVG; external SVG needs a browser/manual review")
    ids = [e.get("id") for e in elements if e.get("id")]
    if len(ids) != len(set(ids)):
        add("unique-ids", "Duplicate SVG ids")
    for name in ("title", "desc"):
        if not any(e.tag.rsplit("}", 1)[-1] == name and (e.text or "").strip() for e in elements):
            add("accessible-description", f"Missing non-empty {name}")
    for e in elements:
        tag = e.tag.rsplit("}", 1)[-1]
        if tag in ("script", "foreignObject", "image", "use", "style", "animate", "set"):
            add("unsafe-svg", f"Unsupported active/external element: {tag}")
        for key, value in e.attrib.items():
            local_key = key.rsplit("}", 1)[-1]
            if local_key.lower().startswith("on") or local_key in ("href", "src") or "javascript:" in value.lower():
                add("unsafe-svg", "Active or external reference")
            if "url(" in value and not re.fullmatch(r"url\(#[A-Za-z0-9_-]+\)", value):
                add("unsafe-svg", "External paint resource")
        if "transform" in e.attrib or "style" in e.attrib:
            add("unsupported-geometry", "Transforms/CSS need browser geometry; static check refuses a false pass")
        for attr in ("marker-start", "marker-end"):
            if attr in e.attrib:
                match = re.fullmatch(r"url\(#([A-Za-z0-9_-]+)\)", e.attrib[attr])
                if not match or match[1] not in ids:
                    add("marker-reference", "Unresolved marker", [e.get("data-id", "")])
    view = list(map(float, root.get("viewBox", "0 0 0 0").split()))
    if len(view) != 4 or view[2] <= 0 or view[3] <= 0:
        add("canvas", "Missing positive viewBox")
        view = [0, 0, 1120, 810]
    shapes, text_nodes, edges = {}, [], []
    canvas = next((e.get("fill") for e in elements if e.get("data-role") == "canvas"), "#ffffff")
    for e in elements:
        role, id = e.get("data-role", ""), e.get("data-id", "")
        if role in ("node", "group", "label-bg", "cell", "activation"):
            box = shape_box(e)
            if box:
                shapes[id] = (box, e)
                if not contains(view, box):
                    add("canvas-overflow", "Shape extends outside the canvas", [id], [box])
                stroke_background = canvas if e.get("data-kind") in ("initial", "final") else e.get("fill", canvas)
                if e.get("stroke", "none") != "none" and ratio(e.get("stroke"), stroke_background) < 3:
                    add("stroke-contrast", "Stroke contrast is below 3:1", [id], [box])
        if e.tag.rsplit("}", 1)[-1] == "text":
            size = float(e.get("font-size", 16))
            spans = list(e) or [e]
            boxes = []
            for span in spans:
                value = "".join(span.itertext())
                w = metrics.width(value, size)
                x, baseline = float(span.get("x", e.get("x", 0))), float(span.get("y", e.get("y", 0)))
                x -= w * {"start": 0, "middle": 0.5, "end": 1}.get(e.get("text-anchor", "start"), 0)
                boxes.append((x, baseline - size, w, size * 1.4))
            x, y = min(b[0] for b in boxes), min(b[1] for b in boxes)
            box = (x, y, max(b[0] + b[2] for b in boxes) - x, max(b[1] + b[3] for b in boxes) - y)
            text_nodes.append((id, box, e))
            if not contains(view, box):
                add("canvas-overflow", "Text extends outside the canvas", [id], [box])
        if role == "edge":
            points = [tuple(map(float, p.split(","))) for p in e.get("points", "").split()]
            if len(points) < 2:
                add("edge-geometry", "Connector has fewer than two points", [id])
            edges.append((id, points, e))
    for id, box, e in text_nodes:
        owner = e.get("data-owner", "")
        bg = shapes.get(owner)
        if bg and not contains((bg[0][0] + 4, bg[0][1] + 4, bg[0][2] - 8, bg[0][3] - 8), box):
            add("text-overflow", "Measured text does not fit its owner padded interior", [id, owner], [box, bg[0]])
        if ratio(e.get("fill", "#000000"), bg[1].get("fill", canvas) if bg else canvas) < (3 if float(e.get("font-size", 16)) >= 24 else 4.5):
            add("text-contrast", "Text contrast is too low", [id], [box])
        if e.get("data-role") == "edge-label":
            backgrounds = [(sid, rect) for sid, (rect, shape) in shapes.items()
                           if shape.get("data-role") == "label-bg" and shape.get("data-parent") == owner]
            expected = (box[0] - 5, box[1] - 4, box[2] + 10, box[3] + 8)
            if len(backgrounds) != 1 or any(abs(a - b) > 1 for a, b in zip(expected, backgrounds[0][1])):
                add("label-background", "Label background does not match measured text and anchor", [id, owner], [box])
        for other, (rect, shape) in shapes.items():
            if other != owner and shape.get("data-role") in ("node", "cell") and overlap(box, rect):
                add("text-shape-overlap", "Text overlaps an unrelated shape", [id, other], [box, rect])
        value = " ".join(e.itertext())
        if e.get("data-role") == "name" and ("•" in value or len(value.split()) > 14):
            add("label-hygiene", "Prefer short names without bullets or sentences", [id], severity="warning")
        if e.get("data-role") == "sub" and re.search(r"\b(draft|TBD|pending|v\d+)\b", value, re.I):
                add("working-note", "Working status belongs outside the figure", [id], severity="warning")
    for id, (box, e) in shapes.items():
        parent = e.get("data-parent")
        if e.get("data-role") in ("node", "group") and parent:
            if parent not in shapes or not contains(shapes[parent][0], box):
                add("boundary-membership", "Element is outside its declared group", [id, parent], [box])
    for i, (id, box, e) in enumerate(text_nodes):
        for other, rect, _ in text_nodes[i + 1:]:
            if overlap(box, rect):
                add("text-overlap", "Text boxes overlap", [id, other], [box, rect])
    shape_list = [(id, b, e) for id, (b, e) in shapes.items() if e.get("data-role") in ("node", "group", "cell")]
    for i, (id, box, e) in enumerate(shape_list):
        for other, rect, f in shape_list[i + 1:]:
            containment = (e.get("data-role") == "group" and contains(box, rect)) or \
                          (f.get("data-role") == "group" and contains(rect, box))
            if overlap(box, rect) and not containment:
                add("shape-overlap", "Unrelated shapes overlap", [id, other], [box, rect])
    edge_segments = []
    lifelines = {e.get("data-from") for _, _, e in edges if e.get("data-kind") == "lifeline"}
    for id, points, e in edges:
        source, target = e.get("data-from"), e.get("data-to")
        if e.get("data-kind") in ("lifeline", "legend"):
            continue
        if not points:
            continue
        for endpoint, point in ((source, points[0]), (target, points[-1])):
            if endpoint not in shapes:
                add("edge-endpoint", "Connector endpoint has no declared shape", [id, endpoint])
                continue
            x, y, w, h = shapes[endpoint][0]
            if endpoint in lifelines:
                # A message may end at the centre lifeline or its 10px activation.
                on_port = min(abs(point[0] - (x + w / 2 + delta)) for delta in (-5, 0, 5)) < 1
            else:
                on_port = ((abs(point[0] - x) < 1 or abs(point[0] - x - w) < 1) and y - 1 <= point[1] <= y + h + 1) or \
                          ((abs(point[1] - y) < 1 or abs(point[1] - y - h) < 1) and x - 1 <= point[0] <= x + w + 1)
            if not on_port:
                add("edge-port", "Connector does not terminate on its endpoint port", [id, endpoint], [shapes[endpoint][0]])
        excluded = {source, target}
        for endpoint in (source, target):
            while endpoint in shapes and shapes[endpoint][1].get("data-parent"):
                endpoint = shapes[endpoint][1].get("data-parent")
                excluded.add(endpoint)
        for a, b in zip(points, points[1:]):
            if a[0] != b[0] and a[1] != b[1]:
                add("orthogonal-route", "Connector segment is not orthogonal", [id])
            for sid, (rect, shape) in shapes.items():
                if sid in excluded or shape.get("data-role") in ("label-bg", "activation"):
                    continue
                if shape.get("data-role") == "group" and shape.get("data-kind") == "lane":
                    continue  # A lane partitions responsibility; flow may cross it.
                if shape.get("data-kind") == "frame" and contains(rect, (a[0], a[1], 0, 0)) and contains(rect, (b[0], b[1], 0, 0)):
                    continue
                if segment_hits_rect(a, b, rect, padding=2):
                    add("arrow-through-box", "Connector crosses an unrelated box", [id, sid], [rect])
            for tid, rect, text in text_nodes:
                if (text.get("data-role") == "group-title" and text.get("data-owner") not in (source, target)) or \
                   (text.get("data-role") == "edge-label" and text.get("data-owner") != id):
                    if segment_hits_rect(a, b, rect, padding=2):
                        add("arrow-through-label", "Connector crosses unrelated text", [id, tid], [rect])
            edge_segments.append((id, a, b))
    crossing_count = sum(1 for i, (id, a, b) in enumerate(edge_segments)
                         for other, c, d in edge_segments[i + 1:] if id != other and crosses(a, b, c, d))
    if crossing_count > 2:
        add("edge-crossings", f"{crossing_count} connector crossings; consider splitting the view", severity="warning")
    if sum(e.get("data-role") == "node" for _, e in shapes.values()) > 12:
        add("view-density", "More than 12 nodes in one view", severity="warning")
    metadata = next((e.text for e in elements if e.tag.rsplit("}", 1)[-1] == "metadata"), "{}")
    try:
        details = json.loads(metadata or "{}")
    except json.JSONDecodeError:
        details = {}
        add("structure", "Invalid metadata JSON")
    for warning in details.get("warnings", []):
        add(warning["rule"], warning["message"], warning.get("elements", []), severity="warning")
    for warning in metrics.warnings:
        if warning not in details.get("warnings", []):
            add(warning["rule"], warning["message"], severity="warning")
    for finding in findings:
        for allow in details.get("allow", []):
            if allow["rule"] == finding["rule"] and finding["elements"] == [allow["element"]]:
                finding["allow_reason"] = allow["reason"]
                # A documented allowance never hides an error.
    return {"schemaVersion": 1, "measured_with": metrics.measured_with,
            "crossings": crossing_count, "findings": findings,
            "errors": sum(f["severity"] == "error" for f in findings),
            "warnings": sum(f["severity"] == "warning" for f in findings)}
