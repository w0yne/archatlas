"""Portable installed-font discovery, with stable ordering."""

from dataclasses import dataclass
import os
from pathlib import Path
import subprocess
import sys

from .coverage import collection_faces, font_info


@dataclass(frozen=True)
class FontFace:
    path: str
    index: int = 0
    family: str = ""
    style: str = "Regular"


def _priority(face: FontFace) -> tuple:
    family = face.family.lower()
    regular = face.style.lower() in ("regular", "normal", "book", "roman")
    preferred = (
        "noto sans", "dejavu sans", "liberation sans", "arial",
        "noto sans cjk sc", "source han sans sc", "pingfang sc",
        "microsoft yahei", "wenquanyi zen hei",
    )
    rank = preferred.index(family) if family in preferred else len(preferred)
    # Regional collections commonly place JP at index zero. Sort using the
    # family, never collection index, so SC precedes other Han variants.
    regional = 0 if family.endswith(" sc") else 1
    return (not regular, rank, regional, "mono" in family,
            "serif" in family, family, face.path, face.index)


def _os_font_roots() -> list[Path]:
    home = Path.home()
    if sys.platform == "win32":
        roots = [Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts"]
        if os.environ.get("LOCALAPPDATA"):
            roots.append(Path(os.environ["LOCALAPPDATA"]) / "Microsoft/Windows/Fonts")
        return roots
    if sys.platform == "darwin":
        return [Path("/System/Library/Fonts"), Path("/Library/Fonts"),
                home / "Library/Fonts"]
    data = Path(os.environ.get("XDG_DATA_HOME", str(home / ".local/share")))
    return [Path("/usr/share/fonts"), Path("/usr/local/share/fonts"),
            home / ".fonts", data / "fonts"]


def discover(paths=None) -> list[FontFace]:
    """Discover faces; explicit paths bypass fontconfig and OS searches."""
    faces = []
    if paths is None:
        try:
            result = subprocess.run(
                ["fc-list", "--format", "%{file}\t%{index}\t%{family}\t%{style}\n"],
                capture_output=True, text=True, check=True, timeout=10,
            )
            for line in result.stdout.splitlines():
                parts = line.split("\t")
                if len(parts) != 4:
                    continue
                path, index, family, style = parts
                if index.isdigit() and Path(path).is_file():
                    faces.append(FontFace(path, int(index), family.split(",")[0],
                                          style.split(",")[0]))
        except (OSError, subprocess.SubprocessError, UnicodeError):
            pass
        if faces:
            return sorted(set(faces), key=_priority)
        paths = []
        for root in _os_font_roots():
            if root.is_dir():
                paths.extend(path for path in root.rglob("*")
                             if path.suffix.lower() in {".ttf", ".otf", ".ttc", ".otc"})
    for path in paths:
        path = str(Path(path).expanduser())
        if not Path(path).is_file():
            continue
        try:
            if Path(path).suffix.lower() in {".ttc", ".otc"}:
                faces.extend(FontFace(path, index, family, style)
                             for index, family, style in collection_faces(path))
            else:
                family, style, _ = font_info(path)
                faces.append(FontFace(path, 0, family, style))
        except Exception:
            # Keep the candidate so measurement can report an unavailable
            # dependency or an unreadable font instead of crashing discovery.
            faces.append(FontFace(path))
    return sorted(set(faces), key=_priority)
