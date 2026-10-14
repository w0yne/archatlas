"""Optional offline Chromium geometry checks; these are not a visual review."""
import re
from xml.etree import ElementTree as ET

from .report import contains, overlap, owner_fits


def _safe_root(svg):
    """Accept the renderer's passive SVG vocabulary before opening a browser."""
    if re.search(r"<!DOCTYPE|<!ENTITY|<\?", svg, re.I):
        raise ValueError("Browser check refuses declarations and processing instructions")
    try:
        root = ET.fromstring(svg)
    except ET.ParseError as error:
        raise ValueError("Browser check requires valid SVG") from error
    namespace = "{http://www.w3.org/2000/svg}"
    if root.tag != namespace + "svg" or root.get("data-archatlas") != "0.1":
        raise ValueError("Browser check currently requires a generated Archatlas SVG")
    tags = {"svg", "title", "desc", "metadata", "defs", "marker", "path",
            "rect", "ellipse", "circle", "polygon", "polyline", "g", "text", "tspan"}
    tags = {namespace + tag for tag in tags}
    for element in root.iter():
        if element.tag not in tags:
            raise ValueError("Browser check refuses active or unsupported SVG elements")
        for key, value in element.attrib.items():
            name = key.lower()
            if (name.startswith(("on", "{")) or name in {"href", "src", "style"}
                    or "javascript:" in value.lower()):
                raise ValueError("Browser check refuses active attributes and external references")
            if re.search(r"url\s*\(", value, re.I) and not re.fullmatch(r"url\(#[A-Za-z0-9_-]+\)", value):
                raise ValueError("Browser check refuses external paint resources")
    return root


_MEASURE = """async () => {
    await document.fonts.ready;
    const svg = document.querySelector('svg');
    function mapRect(element, box) {
        const matrix = element.getScreenCTM();
        if (!matrix) throw new Error('Missing SVG screen transform');
        const points = [[box.x, box.y], [box.x + box.width, box.y],
            [box.x, box.y + box.height], [box.x + box.width, box.y + box.height]]
            .map(([x, y]) => new DOMPoint(x, y).matrixTransform(matrix));
        const xs = points.map(p => p.x), ys = points.map(p => p.y);
        return [Math.min(...xs), Math.min(...ys),
                Math.max(...xs) - Math.min(...xs), Math.max(...ys) - Math.min(...ys)];
    }
    const shapeRoles = new Set(['node', 'group', 'cell', 'label-bg', 'activation']);
    const shapes = [...svg.querySelectorAll('[data-role]')]
        .filter(e => shapeRoles.has(e.dataset.role))
        .map(e => ({id: e.dataset.id, role: e.dataset.role,
                    parent: e.dataset.parent || '', kind: e.dataset.kind || '',
                    tag: e.localName,
                    box: mapRect(e, e.getBBox())}));
    const texts = [...svg.querySelectorAll('text')].filter(e => e.textContent.trim())
        .map(e => ({id: e.dataset.id, role: e.dataset.role,
                    owner: e.dataset.owner || '', box: mapRect(e, e.getBBox())}));
    return {canvas: mapRect(svg, svg.viewBox.baseVal), shapes, texts};
}"""


def _measure(svg):
    try:
        from playwright.sync_api import sync_playwright, Error
    except ImportError as error:
        raise RuntimeError("Browser QA needs archatlas[browser] and playwright install chromium") from error
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            try:
                context = browser.new_context(offline=True, java_script_enabled=False,
                                              service_workers="block",
                                              viewport={"width": 1440, "height": 900})
                context.route("**/*", lambda route: route.abort())
                page = context.new_page()
                page.set_default_timeout(10000)
                page.set_content(
                    '<!doctype html><meta http-equiv="Content-Security-Policy" '
                    'content="default-src \'none\'; base-uri \'none\'; form-action \'none\'">'
                    + svg, wait_until="load")
                # The timeout also bounds fonts.ready/evaluation, which does not
                # otherwise inherit Playwright's default locator timeout.
                return page.evaluate(
                    """() => Promise.race([
                        (""" + _MEASURE + """)(),
                        new Promise((_, reject) => setTimeout(
                            () => reject(new Error('SVG measurement timed out')), 10000))
                    ])""")
            finally:
                browser.close()
    except Error as error:
        raise RuntimeError("Chromium geometry check failed; ensure playwright install chromium "
                           f"has completed: {error}") from error


def check_browser(svg):
    """Return additional findings in CSS screen pixels for the supplied SVG."""
    _safe_root(svg)
    geometry = _measure(svg)
    findings = []

    def add(rule, message, elements, boxes):
        findings.append({"id": f"finding-{len(findings) + 1}", "severity": "error",
                         "rule": "browser-" + rule, "elements": elements,
                         "boxes": boxes, "message": message})

    shapes, texts, canvas = geometry["shapes"], geometry["texts"], geometry["canvas"]
    owners = {shape["id"]: shape for shape in shapes}
    for item in shapes + texts:
        if not contains(canvas, item["box"]):
            add("canvas-overflow", "Browser bounds extend outside the canvas", [item["id"]], [item["box"]])
    for text in texts:
        box, owner = text["box"], owners.get(text["owner"])
        if owner:
            if not owner_fits(owner["box"], box, owner.get("kind", ""), owner.get("tag", "")):
                add("text-overflow", "Browser text bounds exceed the padded owner",
                    [text["id"], owner["id"]], [box, owner["box"]])
            if owner.get("kind") == "actor" and owner.get("parent"):
                parent = owners.get(owner["parent"])
                if not parent or not contains(parent["box"], box):
                    add("boundary-membership", "Browser actor label exceeds its declared group",
                        [text["id"], owner["parent"]], [box])
        if text["role"] == "edge-label":
            backgrounds = [s for s in shapes if s["role"] == "label-bg" and s["parent"] == text["owner"]]
            # Font ink/line bounds differ from Pillow's advance/line-height
            # boxes. Check containment, not exact equality with static bounds.
            if len(backgrounds) != 1 or not contains(backgrounds[0]["box"], box):
                add("label-background", "Browser label bounds lack a covering background",
                    [text["id"], text["owner"]], [box] + [s["box"] for s in backgrounds])
        for shape in shapes:
            if shape["id"] != text["owner"] and shape["role"] in ("node", "cell") and overlap(box, shape["box"]):
                add("text-shape-overlap", "Browser text overlaps an unrelated shape",
                    [text["id"], shape["id"]], [box, shape["box"]])
    for i, text in enumerate(texts):
        for other in texts[i + 1:]:
            if overlap(text["box"], other["box"]):
                add("text-overlap", "Browser text bounds overlap",
                    [text["id"], other["id"]], [text["box"], other["box"]])
    peers = [s for s in shapes if s["role"] in ("node", "group", "cell")]
    for i, shape in enumerate(peers):
        for other in peers[i + 1:]:
            containment = (shape["role"] == "group" and contains(shape["box"], other["box"])) or (
                other["role"] == "group" and contains(other["box"], shape["box"]))
            if not containment and overlap(shape["box"], other["box"]):
                add("shape-overlap", "Browser bounds of unrelated shapes overlap",
                    [shape["id"], other["id"]], [shape["box"], other["box"]])
    return {"findings": findings, "errors": len(findings), "warnings": 0,
            "browser": {"status": "checked", "engine": "chromium", "units": "CSS pixels",
                        "checks": ["canvas", "text-fit", "overlap", "label-background"],
                        "visual_review": "pending"}}
