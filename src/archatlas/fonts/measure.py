"""Measured font fallback and greedy Latin/CJK wrapping."""

import math
import unicodedata

from .coverage import CJK_SAMPLE, font_info
from .discover import discover

_NO_START = frozenset("，。、）；：！？】》〉」』〕］｝,.;:!?)]}")
_NO_END = frozenset("（【《〈「『〔［｛([{")


def _clusters(text):
    """Keep combining marks, variation selectors and ZWJ sequences together."""
    clusters = []
    for char in text:
        if clusters and (unicodedata.category(char).startswith("M")
                         or char == "\u200d" or clusters[-1].endswith("\u200d")):
            clusters[-1] += char
        else:
            clusters.append(char)
    return clusters


def _wide(char):
    return unicodedata.east_asian_width(char) in ("W", "F")


def _positive(value, name):
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be a finite positive number")


class FontMetrics:
    """Measure with installed fonts in the same order as the SVG font stack.

    ``paths=None`` discovers system fonts; ``paths=[]`` forces estimates.
    Missing dependencies or glyphs produce warnings, ``measured_with=estimate``
    and ``padding_factor=1.12``. Width itself does not include this box padding.
    Subset embedding is deferred; this API never downloads or embeds fonts.
    """

    def __init__(self, paths=None):
        self.warnings = []
        self.measured_with = "pillow"
        self.padding_factor = 1
        self._faces = []
        self._coverage = set()
        self._pending = iter(discover(paths))
        self._image_font = None
        self._font_cache = {}
        self._choice_cache = {}
        try:
            from PIL import ImageFont
            from fontTools import ttLib  # noqa: F401
            self._image_font = ImageFont
        except ImportError:
            self._estimate("font-dependency", "Pillow and fontTools are required "
                           "for verified measurement; using conservative estimates.")
            return
        # Prime Latin and Chinese fallback before callers read .family.
        required = {ord(c) for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                    "0123456789" + CJK_SAMPLE}
        while not required.issubset(self._coverage) and self._load_next():
            pass
        if not self._faces:
            self._estimate("font-unavailable", "No usable fonts found; using "
                           "conservative estimates and 12% extra box padding.")
        elif not all(ord(c) in self._coverage for c in CJK_SAMPLE):
            self._warn("font-cjk-coverage", "Installed fonts do not cover the full "
                       "CJK probe; missing glyphs will use conservative estimates.")

    def _warn(self, rule, message):
        warning = {"rule": rule, "message": message}
        if warning not in self.warnings:
            self.warnings.append(warning)

    def _estimate(self, rule, message):
        self.measured_with = "estimate"
        self.padding_factor = 1.12
        self._warn(rule, message)

    def _load_next(self):
        for face in self._pending:
            try:
                family, _, coverage = font_info(face.path, face.index)
                if not coverage.difference(self._coverage):
                    continue
                font = self._image_font.truetype(face.path, 16, index=face.index)
                font.getlength(" ")
            except Exception:
                self._warn("font-unreadable", "An installed font could not be "
                           "read or measured and was skipped.")
                continue
            self._faces.append((face, family, coverage))
            self._coverage.update(coverage)
            self._font_cache[(len(self._faces) - 1, 16)] = font
            return True
        return False

    @property
    def family(self):
        names = list(dict.fromkeys(family for _, family, _ in self._faces))
        # CSS quoted-string escaping; XML escaping remains the SVG writer's job.
        quoted = ['"' + name.replace("\\", "\\\\").replace('"', '\\"')
                  .replace("\n", "\\a ").replace("\r", "\\d ") + '"' for name in names]
        return ", ".join(quoted + ["sans-serif"])

    def runs(self, text):
        """Resolve explicit font runs for SVG readers lacking font fallback.

        Family names, never local font paths, enter the exported document.
        """
        runs = []
        for char in text:
            face = self._choice(char)
            family = self._faces[face][1] if face is not None else "sans-serif"
            if runs and runs[-1]["family"] == family:
                runs[-1]["text"] += char
            else:
                runs.append({"text": char, "family": family})
        return runs

    def _choice(self, char):
        if char in self._choice_cache:
            return self._choice_cache[char]
        code = ord(char)
        while True:
            for index, (_, _, coverage) in enumerate(self._faces):
                if code in coverage:
                    self._choice_cache[char] = index
                    return index
            if self._image_font is None or not self._load_next():
                self._choice_cache[char] = None
                return None

    @staticmethod
    def _estimated_width(text, size):
        return size * sum(
            0 if unicodedata.category(c).startswith("M") or c in "\u200c\u200d"
            else 0.5 if c.isspace() else 1
            for c in text
        )

    def _run_width(self, text, face_index, size):
        if face_index is not None:
            try:
                # Pillow accepts integer pixel sizes across supported versions.
                # Scale a larger size for fractional sizes instead of rounding.
                pixels = max(1, math.ceil(size))
                key = (face_index, pixels)
                if key not in self._font_cache:
                    face = self._faces[face_index][0]
                    self._font_cache[key] = self._image_font.truetype(
                        face.path, pixels, index=face.index)
                return float(self._font_cache[key].getlength(text)) * size / pixels
            except Exception:
                self._estimate("font-measurement", "A font could not measure this "
                               "text; using conservative estimates.")
        else:
            self._estimate("font-missing-glyph", "Some text has no verified font "
                           "coverage; using conservative estimates.")
        return self._estimated_width(text, size)

    def width(self, text, size=16) -> float:
        """Return the maximum line advance in pixels (without box padding)."""
        _positive(size, "size")
        widths = []
        for line in text.expandtabs(4).split("\n"):
            total, run, previous = 0.0, "", None
            for char in line.rstrip("\r"):
                selected = self._choice(char)
                if run and selected != previous:
                    total += self._run_width(run, previous, size)
                    run = ""
                run += char
                previous = selected
            if run:
                total += self._run_width(run, previous, size)
            widths.append(total)
        return float(max(widths, default=0))

    def wrap(self, text, max_width, size=16) -> list[str]:
        """Greedily wrap words/CJK; preserve explicit newlines.

        Break long words only when needed. An indivisible grapheme or kinsoku
        group may exceed the limit, with a warning, instead of losing text or
        creating a line that begins with closing punctuation.
        """
        _positive(max_width, "max_width")
        _positive(size, "size")
        lines = []
        for paragraph in text.replace("\r\n", "\n").replace("\r", "\n").expandtabs(4).split("\n"):
            chars = _clusters(paragraph.strip())
            if not chars:
                lines.append("")
                continue
            start = 0
            while start < len(chars):
                best, fitted = None, None
                stop = start + 1
                while stop <= len(chars):
                    candidate = "".join(chars[start:stop]).rstrip()
                    if self.width(candidate, size) > max_width:
                        break
                    if self._kinsoku_boundary(chars, stop):
                        fitted = stop
                        if (stop == len(chars) or chars[stop - 1].isspace()
                                or chars[stop].isspace()
                                or _wide(chars[stop - 1][0]) or _wide(chars[stop][0])
                                or chars[stop - 1] == "-"):
                            best = stop
                    stop += 1
                end = best or fitted
                if end is None:
                    end = max(start + 1, stop)
                    while end < len(chars) and not self._kinsoku_boundary(chars, end):
                        end += 1
                    self._warn("font-wrap-overflow", "An indivisible text unit "
                               "exceeds the wrap width.")
                lines.append("".join(chars[start:end]).rstrip())
                start = end
                while start < len(chars) and chars[start].isspace():
                    start += 1
        return lines

    @staticmethod
    def _kinsoku_boundary(chars, end):
        if end == len(chars):
            return True
        # Ignore whitespace at the break when checking opening/closing marks.
        left = end - 1
        right = end
        while left >= 0 and chars[left].isspace():
            left -= 1
        while right < len(chars) and chars[right].isspace():
            right += 1
        return ((left < 0 or chars[left][-1] not in _NO_END)
                and (right == len(chars) or chars[right][0] not in _NO_START))

    def doctor(self) -> dict:
        """Report selected usable faces and explicit probe-based CJK coverage."""
        supported = [c for c in CJK_SAMPLE if ord(c) in self._coverage]
        return {
            "fonts": [
                {"family": family, "path": face.path, "index": face.index,
                 "glyph_count": len(coverage),
                 "cjk_covered": sum(ord(c) in coverage for c in CJK_SAMPLE)}
                for face, family, coverage in self._faces
            ],
            "family": self.family,
            "cjk_coverage": {
                "sample": CJK_SAMPLE, "covered": len(supported),
                "total": len(CJK_SAMPLE),
                "missing": "".join(c for c in CJK_SAMPLE if ord(c) not in self._coverage),
                "complete": len(supported) == len(CJK_SAMPLE),
            },
            "mode": self.measured_with,
            "measured_with": self.measured_with,
            "padding_factor": self.padding_factor,
            "warnings": [dict(warning) for warning in self.warnings],
        }
