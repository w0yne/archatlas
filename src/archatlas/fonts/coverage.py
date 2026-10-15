"""Read actual Unicode glyph coverage without eagerly importing fontTools."""

from functools import lru_cache

CJK_SAMPLE = "中文简体汉字架构图服务数据库，。、（）"


@lru_cache(maxsize=256)
def font_info(path: str, index: int = 0) -> tuple[str, str, frozenset[int]]:
    """Return family, style and cmap coverage for one face of a font file.

    ImportError and invalid-font errors are deliberately left to the caller,
    which can explain why it switched to conservative estimates.
    """
    from fontTools.ttLib import TTFont

    # Own the file handle even if the font parser fails during construction.
    with open(path, "rb") as source, TTFont(source, fontNumber=index, lazy=True) as font:
        names = font["name"]
        family = names.getBestFamilyName() or "Unnamed font"
        style = names.getBestSubFamilyName() or "Regular"
        cmap = font.getBestCmap() or {}
        coverage = frozenset(
            codepoint for codepoint, glyph in cmap.items()
            if glyph != ".notdef" and font.getGlyphID(glyph) != 0
        )
    return family, style, coverage


@lru_cache(maxsize=256)
def font_weight(path: str, index: int = 0) -> int:
    """Return the face's actual default weight, not a synthetic bold estimate."""
    from fontTools.ttLib import TTFont

    with open(path, "rb") as source, TTFont(source, fontNumber=index, lazy=True) as font:
        if "OS/2" in font:
            return int(font["OS/2"].usWeightClass)
        return 700 if font["head"].macStyle & 1 else 400


def collection_faces(path: str) -> list[tuple[int, str, str]]:
    """Inspect TTC/OTC face names, including regional CJK faces."""
    from fontTools.ttLib import TTCollection

    with open(path, "rb") as source:
        collection = TTCollection(source, lazy=True)
        try:
            return [
                (index, font["name"].getBestFamilyName() or "Unnamed font",
                 font["name"].getBestSubFamilyName() or "Regular")
                for index, font in enumerate(collection.fonts)
            ]
        finally:
            collection.close()
