"""Measured font fallback and greedy Latin/CJK wrapping."""

import math
import unicodedata

from .coverage import CJK_SAMPLE, font_info
from .discover import discover

_NO_START = frozenset("，。、）；：！？】》〉」』〕］｝,.;:!?)]}")
_NO_END = frozenset("（【《〈「『〔［｛([{")
_SOFT_HYPHEN = "\u00ad"
_CJK_FAMILIES = (
    "Noto Sans CJK SC", "Source Han Sans SC", "PingFang SC",
    "Microsoft YaHei", "WenQuanYi Zen Hei",
)


def _family_stack(names):
    # CSS quoted-string escaping; XML escaping remains the SVG writer's job.
    quoted = ['"' + name.replace("\\", "\\\\").replace('"', '\\"')
              .replace("\n", "\\a ").replace("\r", "\\d ") + '"'
              for name in dict.fromkeys(names)]
    return ", ".join(quoted + ["sans-serif"])


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


def _cjk(char):
    code = ord(char)
    return (0x1100 <= code <= 0x11FF or 0x2E80 <= code <= 0xA4CF
            or 0xAC00 <= code <= 0xD7FF or 0xF900 <= code <= 0xFAFF
            or 0xFE30 <= code <= 0xFE4F or 0xFF00 <= code <= 0xFFEF
            or 0x20000 <= code <= 0x323AF)


def _paragraphs(text):
    return text.replace("\r\n", "\n").replace("\r", "\n").expandtabs(4).split("\n")


def _positive(value, name):
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be a finite positive number")


class FontMetrics:
    """Measure with installed fonts in the same order as the SVG font stack.

    ``paths=None`` discovers system fonts; ``paths=[]`` forces estimates.
    ``lang="zh"`` (including zh region tags), or observing actual CJK text,
    enables an explicit CJK family stack even without optional dependencies.
    Verified runs retain their measured family; missing CJK runs use the stack.
    Missing dependencies or glyphs produce warnings, ``measured_with=estimate``
    and ``padding_factor=1.12``. Width itself does not include this box padding.
    Subset embedding is deferred; this API never downloads or embeds fonts.
    """

    def __init__(self, paths=None, lang="en"):
        self._cjk_text = lang.lower().replace("_", "-").split("-")[0] == "zh"
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
            if self._cjk_text:
                self._cjk_estimate()
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
        if self._cjk_text and not all(ord(c) in self._coverage for c in CJK_SAMPLE):
            self._warn("cjk-glyph-coverage", "CJK glyph coverage is unverified "
                       "or CJK measurement used conservative estimates.")

    def _warn(self, rule, message):
        warning = {"rule": rule, "message": message}
        if warning not in self.warnings:
            self.warnings.append(warning)

    def _estimate(self, rule, message):
        self.measured_with = "estimate"
        self.padding_factor = 1.12
        self._warn(rule, message)

    def _cjk_estimate(self):
        self._estimate("cjk-glyph-coverage", "CJK glyph coverage is unverified "
                       "or CJK measurement used conservative estimates.")

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
        """SVG/CSS family stack; CJK detection is retained for this instance."""
        names = list(_CJK_FAMILIES) if self._cjk_text else []
        names.extend(family for _, family, _ in self._faces)
        return _family_stack(names)

    def runs(self, text):
        """Resolve explicit font runs for SVG readers lacking font fallback.

        Family names, never local font paths, enter the exported document.
        Missing CJK runs contain a CSS family stack beginning with Noto Sans
        CJK SC, for readers that only honor the first family.
        """
        self._cjk_text = self._cjk_text or any(_cjk(c) for c in text)
        runs = []
        for char in text.replace(_SOFT_HYPHEN, ""):
            face = self._choice(char)
            if face is not None:
                family = self._faces[face][1]
            elif _cjk(char):
                family = _family_stack(_CJK_FAMILIES)
                self._cjk_estimate()
            else:
                family = "sans-serif"
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
        if any(_cjk(c) for c in text):
            self._cjk_estimate()
        return self._estimated_width(text, size)

    def width(self, text, size=16) -> float:
        """Return the maximum line advance in pixels (without box padding)."""
        _positive(size, "size")
        self._cjk_text = self._cjk_text or any(_cjk(c) for c in text)
        widths = []
        for line in _paragraphs(text.replace(_SOFT_HYPHEN, "")):
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

        Only whitespace, CJK boundaries and explicit soft hyphens permit a
        break. Oversized words/kinsoku groups remain intact, with a warning.
        Unused soft hyphens are hidden; a used one renders as a hyphen.
        """
        _positive(max_width, "max_width")
        _positive(size, "size")
        lines = []
        for paragraph in _paragraphs(text):
            chars = _clusters(paragraph.strip())
            if not chars:
                lines.append("")
                continue
            start = 0
            boundaries = self._break_positions(chars)
            while start < len(chars):
                best = None
                remaining = [end for end in boundaries if end > start]
                for end in remaining:
                    candidate = self._line_text(chars, start, end)
                    if self.width(candidate, size) <= max_width:
                        best = end
                    elif chars[end - 1] != _SOFT_HYPHEN:
                        # A discretionary hyphen can be wider than the rest
                        # of the word; try the next boundary before giving up.
                        break
                end = best or remaining[0]
                if best is None:
                    self._warn("font-wrap-overflow", "An indivisible text unit "
                               "exceeds the wrap width.")
                lines.append(self._line_text(chars, start, end))
                start = end
                while start < len(chars) and chars[start].isspace():
                    start += 1
        return lines

    def required_width(self, text, size=16) -> float:
        """Longest unbreakable unit in pixels, without box padding.

        Uses the same word, soft-hyphen and kinsoku boundaries as ``wrap``.
        A discretionary break includes the visible hyphen's advance.
        """
        _positive(size, "size")
        widths = [0.0]
        for paragraph in _paragraphs(text):
            chars = _clusters(paragraph.strip())
            start = 0
            for end in self._break_positions(chars):
                widths.append(self.width(self._line_text(chars, start, end).strip(), size))
                start = end
        return float(max(widths))

    @staticmethod
    def _line_text(chars, start, end):
        visible = "".join(chars[start:end]).replace(_SOFT_HYPHEN, "").rstrip()
        if (visible and end < len(chars) and chars[end - 1] == _SOFT_HYPHEN
                and not chars[end].isspace()):
            visible += "-"
        return visible

    @classmethod
    def _break_positions(cls, chars):
        return [
            end for end in range(1, len(chars) + 1)
            if (end == len(chars) or (
                chars[end] != _SOFT_HYPHEN
                and (chars[end - 1].isspace() or chars[end].isspace()
                     or chars[end - 1] == _SOFT_HYPHEN
                     or _cjk(chars[end - 1][0]) or _cjk(chars[end][0]))
                and cls._kinsoku_boundary(chars, end)))
        ]

    @staticmethod
    def _kinsoku_boundary(chars, end):
        if end == len(chars):
            return True
        # Ignore whitespace at the break when checking opening/closing marks.
        left = end - 1
        right = end
        while left >= 0 and (chars[left].isspace() or chars[left] == _SOFT_HYPHEN):
            left -= 1
        while right < len(chars) and (chars[right].isspace() or chars[right] == _SOFT_HYPHEN):
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
