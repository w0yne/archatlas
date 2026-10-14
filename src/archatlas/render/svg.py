"""Deterministic SVG, live escaped text, no active or remote content."""
from dataclasses import asdict
import hashlib
import json
import re
from xml.etree.ElementTree import Element, SubElement, tostring

from .theme import THEMES


def number(value):
    return f"{value:.3f}".rstrip("0").rstrip(".") or "0"


def render_svg(scene, namespace=None):
    data = asdict(scene)
    # Keep existing 0.1 SVG namespaces stable when the optional field is absent.
    for box in data["boxes"]:
        if not box["event_type"]:
            del box["event_type"]
    digest = hashlib.sha256(json.dumps(data, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:12]
    prefix = namespace or "atlas-" + digest
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", prefix):
        raise ValueError("SVG namespace must be an identifier")
    theme = THEMES[scene.theme]
    root = Element("svg", {"xmlns": "http://www.w3.org/2000/svg",
                          "viewBox": f"0 0 {number(scene.width)} {number(scene.height)}",
                          "width": number(scene.width), "height": number(scene.height),
                          "lang": scene.lang,
                          "role": "img", "aria-labelledby": prefix + "-document-title " + prefix + "-document-desc",
                          "data-archatlas": "0.1", "data-measured-with": scene.measured_with})
    SubElement(root, "title", {"id": prefix + "-document-title"}).text = scene.title
    SubElement(root, "desc", {"id": prefix + "-document-desc"}).text = scene.description
    SubElement(root, "metadata").text = json.dumps({"warnings": scene.warnings, "allow": scene.allow},
                                                 ensure_ascii=False, sort_keys=True)
    defs = SubElement(root, "defs")
    variants = sorted({(e.style, (e.marker_kind or e.kind) in ("async", "message", "reply")) for e in scene.edges})
    for style, open_arrow in variants:
        marker_id = f"{prefix}-marker-{style}-{'open' if open_arrow else 'arrow'}"
        colour = theme[style][1]
        marker = SubElement(defs, "marker", {"id": marker_id, "viewBox": "0 0 10 10",
                            "refX": "10", "refY": "5", "markerWidth": "8", "markerHeight": "8",
                            "markerUnits": "userSpaceOnUse", "orient": "auto-start-reverse"})
        SubElement(marker, "path", {"d": "M 0 0 L 10 5 L 0 10" + ("" if open_arrow else " Z"),
                                   "fill": "none" if open_arrow else colour, "stroke": colour,
                                   "stroke-width": "1.5"})
        circle = SubElement(defs, "marker", {"id": f"{prefix}-marker-{style}-circle", "viewBox": "0 0 10 10",
                            "refX": "5", "refY": "5", "markerWidth": "8", "markerHeight": "8",
                            "markerUnits": "userSpaceOnUse"})
        # One circle marker per style even when both filled/open variants occur.
        if sum(1 for s, o in variants if s == style and o < open_arrow):
            defs.remove(circle)
        else:
            SubElement(circle, "circle", {"cx": "5", "cy": "5", "r": "3.5",
                                         "fill": theme["canvas"], "stroke": colour, "stroke-width": "1.5"})
    SubElement(root, "rect", {"width": number(scene.width), "height": number(scene.height),
                             "fill": theme["canvas"], "data-role": "canvas"})
    for box in scene.boxes:
        if box.role == "label-bg":
            continue
        attrs = {"id": prefix + "-shape-" + box.role + "-" + box.id, "data-id": box.id, "data-role": box.role,
                 "data-parent": box.parent, "data-kind": box.kind,
                 "fill": theme["boundary" if box.role == "group" else box.style][0],
                 "stroke": theme["boundary" if box.role == "group" else box.style][1], "stroke-width": "1.5",
                 "data-box": " ".join(number(v) for v in box.rect)}
        if box.dashed:
            attrs["stroke-dasharray"] = "7 5"
        if box.kind == "actor":
            actor = SubElement(root, "g", {**attrs, "fill": "none", "stroke-linecap": "round"})
            (cx, cy, r), parts = box.actor_parts
            SubElement(actor, "circle", {"cx": number(cx), "cy": number(cy), "r": number(r),
                                         "fill": theme["canvas"]})
            for part in parts:
                SubElement(actor, "polyline", {"points": " ".join(f"{number(x)},{number(y)}" for x, y in part)})
        elif box.kind == "gateway":
            points = [(box.x + box.w / 2, box.y), (box.x + box.w, box.y + box.h / 2),
                      (box.x + box.w / 2, box.y + box.h), (box.x, box.y + box.h / 2)]
            SubElement(root, "polygon", {**attrs, "points": " ".join(f"{number(x)},{number(y)}" for x, y in points)})
        elif box.kind in ("event", "initial", "final", "use_case"):
            if box.kind == "event":
                attrs["data-event-type"] = box.event_type
                attrs["stroke-width"] = "4" if box.event_type == "end" else "1.5"
            if box.kind == "initial":
                attrs["fill"] = theme[box.style][1]
            SubElement(root, "ellipse", {**attrs, "cx": number(box.x + box.w / 2), "cy": number(box.y + box.h / 2),
                                         "rx": number(box.w / 2), "ry": number(box.h / 2)})
            if box.kind == "final":
                SubElement(root, "ellipse", {"cx": number(box.x + box.w / 2), "cy": number(box.y + box.h / 2),
                                             "rx": number(box.w / 2 - 6), "ry": number(box.h / 2 - 6),
                                             "fill": theme[box.style][1], "stroke": theme[box.style][1], "stroke-width": "2"})
        else:
            SubElement(root, "rect", {**attrs, "x": number(box.x), "y": number(box.y),
                                      "width": number(box.w), "height": number(box.h),
                                      "rx": "12" if box.kind in ("task", "state") else "4" if box.role == "node" else "0"})
    for edge in scene.edges:
        attrs = {"id": prefix + "-edge-" + edge.id, "data-id": edge.id,
                 "data-role": "frame-separator" if edge.kind == "frame-separator" else "edge",
                 "data-from": edge.source, "data-to": edge.target, "data-kind": edge.kind,
                 "points": " ".join(f"{number(x)},{number(y)}" for x, y in edge.points),
                 "fill": "none", "stroke": theme[edge.style][1], "stroke-width": "1.8",
                 "stroke-linejoin": "round"}
        marker_kind = edge.marker_kind or edge.kind
        marker = f"url(#{prefix}-marker-{edge.style}-{'open' if marker_kind in ('async', 'message', 'reply') else 'arrow'})"
        if edge.direction in ("->", "<->"):
            attrs["marker-end"] = marker
        if edge.direction == "<->":
            attrs["marker-start"] = marker
        elif marker_kind == "message":
            attrs["marker-start"] = f"url(#{prefix}-marker-{edge.style}-circle)"
        if edge.dashed:
            attrs["stroke-dasharray"] = "7 5"
        SubElement(root, "polyline", attrs)
    for box in scene.boxes:
        if box.role == "label-bg":
            SubElement(root, "rect", {"id": prefix + "-shape-label-bg-" + box.id, "data-id": box.id,
                         "data-role": "label-bg", "data-parent": box.parent,
                         "x": number(box.x), "y": number(box.y), "width": number(box.w), "height": number(box.h),
                         "fill": theme["canvas"], "fill-opacity": "0.92", "rx": "3"})
    for text in scene.texts:
        attrs = {"id": prefix + "-text-" + text.role + "-" + text.id, "data-id": text.id, "data-role": text.role,
                 "data-owner": text.owner, "x": number(text.x), "y": number(text.y + text.size),
                 "data-source": text.source,
                 "font-size": number(text.size), "font-family": scene.family,
                 "text-anchor": "start", "fill": theme["text"],
                 "data-text-box": " ".join(number(v) for v in text.rect)}
        element = SubElement(root, "text", attrs)
        for i, line in enumerate(text.lines):
            width = text.line_widths[i] if i < len(text.line_widths) else text.w
            left = text.x - width * {"start": 0, "middle": 0.5, "end": 1}[text.anchor]
            span = SubElement(element, "tspan", {"x": number(left),
                       "y": number(text.y + text.size + i * text.size * 1.4)})
            if text.runs and i < len(text.runs):
                for run in text.runs[i]:
                    run_attrs = {"font-family": run["family"]}
                    if "offset" in run:
                        run_attrs["x"] = number(left + run["offset"])
                    SubElement(span, "tspan", run_attrs).text = run["text"]
            else:
                span.text = line
    # Lifelines run behind execution bars; messages attach to the bar edges.
    # Keep every activation above the dashed lifeline and below message arrows.
    activations = [element for element in root if element.get("data-role") == "activation"]
    for element in activations:
        root.remove(element)
    insertion = next((i for i, element in enumerate(root)
                      if element.get("data-role") == "edge" and element.get("data-kind") != "lifeline"),
                     len(root))
    for offset, element in enumerate(activations):
        root.insert(insertion + offset, element)
    return tostring(root, encoding="unicode", short_empty_elements=True) + "\n"
