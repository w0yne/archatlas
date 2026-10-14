from pathlib import Path
from typing import Protocol

from ..layout.base import Scene


class Exporter(Protocol):
    name: str
    capabilities: dict

    def export(self, scene: Scene, out: Path, opts: dict) -> dict: ...
