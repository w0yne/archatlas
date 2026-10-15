"""Exporter-neutral resolved geometry, in CSS pixels."""
from dataclasses import dataclass, field


@dataclass
class Box:
    id: str
    x: float
    y: float
    w: float
    h: float
    role: str = "node"
    kind: str = "component"
    style: str = "peer"
    parent: str = ""
    dashed: bool = False
    event_type: str = ""
    shape: str = "card"
    tint: str = "app"
    band: bool = True
    header_height: float = 0
    header_width: float = 0

    @property
    def rect(self):
        return (self.x, self.y, self.w, self.h)

    @property
    def header_rect(self):
        return (self.x, self.y, min(self.header_width, self.w), self.h) if self.header_width else \
            (self.x, self.y, self.w, min(self.header_height, self.h))

    @property
    def glyph_rect(self):
        """Visible symbol bounds; rect also reserves an actor's label footprint."""
        if self.kind == "actor":
            if self.role == "legend-swatch":
                return self.rect
            return (self.x + self.w / 2 - 28, self.y, 56, 80)
        return self.rect

    @property
    def actor_parts(self):
        x, y, w, h = self.glyph_rect
        cx = x + w / 2
        return ((cx, y + h / 8, h / 8),
                [[(cx, y + h / 4), (cx, y + h * .675)],
                 [(x, y + h / 2), (x + w, y + h / 2)],
                 [(cx - w * 3 / 7, y + h), (cx, y + h * .675), (cx + w * 3 / 7, y + h)]])


@dataclass
class Text:
    id: str
    lines: list
    x: float
    y: float
    w: float
    h: float
    size: float = 16
    owner: str = ""
    role: str = "label"
    anchor: str = "start"
    style: str = "peer"
    runs: list = field(default_factory=list)
    source: str = ""
    line_widths: list = field(default_factory=list)
    weight: int = 400

    @property
    def left(self):
        return self.x - self.w * {"start": 0, "middle": 0.5, "end": 1}[self.anchor]

    @property
    def rect(self):
        return (self.left, self.y, self.w, self.h)


@dataclass
class Connector:
    id: str
    points: list
    source: str
    target: str
    style: str = "peer"
    direction: str = "->"
    dashed: bool = False
    kind: str = "call"
    marker_kind: str = ""
    badge: str = ""
    numbered: bool = False


@dataclass
class Scene:
    title: str
    description: str
    width: float
    height: float
    theme: str = "neutral"
    boxes: list = field(default_factory=list)
    texts: list = field(default_factory=list)
    edges: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    family: str = "sans-serif"
    measured_with: str = "estimate"
    allow: list = field(default_factory=list)
    lang: str = "en"
