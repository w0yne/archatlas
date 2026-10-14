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

    @property
    def rect(self):
        return (self.x, self.y, self.w, self.h)


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
