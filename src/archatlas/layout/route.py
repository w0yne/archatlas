"""Deterministic, tuple-only orthogonal connector routing.

Automatic routes avoid unrelated rectangles with eight units of clearance. If
clearance is impossible, routing retries against their actual borders, then
raises ValueError if no route exists. Manual waypoints are the exact internal
points: they bypass obstacle avoidance but must form an orthogonal connector.
"""

from __future__ import annotations

from heapq import heappop, heappush
from math import isfinite
from typing import Iterable, Sequence

Point = tuple[float, float]
Rect = tuple[float, float, float, float]
__all__ = ["route", "segment_hits_rect", "crosses"]

_CLEARANCE = 8.0
_BEND = 40.0
_CROSSING = 200.0
_NORMAL = {"n": (0, -1), "e": (1, 0), "s": (0, 1), "w": (-1, 0)}


def _numbers(values: Sequence[float], size: int) -> tuple[float, ...]:
    try:
        result = tuple(float(value) for value in values)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError("Geometry must contain finite numbers") from exc
    if len(result) != size or not all(isfinite(value) for value in result):
        raise ValueError(f"Expected {size} finite coordinates")
    return result


def _rect(rect: Rect) -> Rect:
    x, y, w, h = _numbers(rect, 4)
    if w < 0 or h < 0:
        raise ValueError("Rectangle dimensions must be nonnegative")
    return x, y, w, h


def segment_hits_rect(a: Point, b: Point, rect: Rect, padding: float = 0) -> bool:
    """Whether a segment meets a rectangle's strict interior.

    Rectangles are (x, y, width, height). Boundary travel and corner touches
    are allowed. Padding expands all four sides; diagonal segments also work.
    """
    a, b = _numbers(a, 2), _numbers(b, 2)
    x, y, w, h = _rect(rect)
    padding = _numbers((padding,), 1)[0]
    if padding < 0:
        raise ValueError("Padding must be nonnegative")
    return _hits(a, b, (x - padding, y - padding, w + 2 * padding, h + 2 * padding))


def _hits(a: Point, b: Point, rect: Rect) -> bool:
    x, y, w, h = rect
    if w <= 0 or h <= 0:
        return False
    low, high = 0.0, 1.0
    for start, end, lower, upper in (
        (a[0], b[0], x, x + w), (a[1], b[1], y, y + h)
    ):
        delta = end - start
        if delta == 0:
            if not lower < start < upper:
                return False
        else:
            enter, leave = sorted(((lower - start) / delta, (upper - start) / delta))
            low, high = max(low, enter), min(high, leave)
            if low >= high:
                return False
    return True


def crosses(a: Point, b: Point, c: Point, d: Point) -> bool:
    """True for a proper interior crossing; touches/collinear overlaps are false."""
    a, b, c, d = (_numbers(point, 2) for point in (a, b, c, d))
    return _crosses(a, b, c, d)


def _crosses(a: Point, b: Point, c: Point, d: Point) -> bool:
    def side(p: Point, q: Point, r: Point) -> float:
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

    def opposite(x: float, y: float) -> bool:
        return (x < 0 < y) or (y < 0 < x)

    return opposite(side(a, b, c), side(a, b, d)) and opposite(
        side(c, d, a), side(c, d, b)
    )


def _orthogonal(points: Sequence[Point]) -> bool:
    return all(a != b and (a[0] == b[0] or a[1] == b[1])
               for a, b in zip(points, points[1:]))


def _simplify(points: Iterable[Point]) -> list[Point]:
    result: list[Point] = []
    for point in points:
        if result and point == result[-1]:
            continue
        while len(result) >= 2:
            a, b = result[-2:]
            straight = (a[0] == b[0] == point[0] or a[1] == b[1] == point[1])
            forward = ((b[0] - a[0]) * (point[0] - b[0])
                       + (b[1] - a[1]) * (point[1] - b[1])) > 0
            if not (straight and forward):
                break
            result.pop()
        result.append(point)
    return result


def _port(box: Rect, side: str, fraction: float) -> Point:
    x, y, w, h = box
    return {
        "n": (x + w * fraction, y),
        "e": (x + w, y + h * fraction),
        "s": (x + w * fraction, y + h),
        "w": (x, y + h * fraction),
    }[side]


def _outward(a: Point, b: Point, side: str) -> bool:
    nx, ny = _NORMAL[side]
    return (b[0] - a[0]) * nx + (b[1] - a[1]) * ny > 0


def _score(points: Sequence[Point], previous: Sequence[tuple[Point, Point]]) -> float:
    length = sum(abs(b[0] - a[0]) + abs(b[1] - a[1])
                 for a, b in zip(points, points[1:]))
    bends = sum((a[0] == b[0]) != (b[0] == c[0])
                for a, b, c in zip(points, points[1:], points[2:]))
    crossings = sum(_crosses(a, b, c, d) for a, b in zip(points, points[1:])
                    for c, d in previous)
    return length + _BEND * bends + _CROSSING * crossings


def _axes(a: Point, b: Point, boxes: Sequence[Rect], margin: float):
    xs = {a[0], b[0], (a[0] + b[0]) / 2, a[0] - margin, a[0] + margin,
          b[0] - margin, b[0] + margin}
    ys = {a[1], b[1], (a[1] + b[1]) / 2, a[1] - margin, a[1] + margin,
          b[1] - margin, b[1] + margin}
    for x, y, w, h in boxes:
        xs.update((x, x + w))
        ys.update((y, y + h))
    xs.update((min(xs) - margin, max(xs) + margin))
    ys.update((min(ys) - margin, max(ys) + margin))
    return sorted(xs), sorted(ys)


def _candidates(a: Point, b: Point, start: str, end: str,
                xs: Sequence[float], ys: Sequence[float], margin: float):
    yield [a, b]
    yield [a, (b[0], a[1]), b]
    yield [a, (a[0], b[1]), b]
    sa = (a[0] + _NORMAL[start][0] * margin, a[1] + _NORMAL[start][1] * margin)
    sb = (b[0] + _NORMAL[end][0] * margin, b[1] + _NORMAL[end][1] * margin)
    yield [a, sa, (sb[0], sa[1]), sb, b]
    yield [a, sa, (sa[0], sb[1]), sb, b]
    for x in xs:
        yield [a, (x, a[1]), (x, b[1]), b]
        yield [a, sa, (x, sa[1]), (x, sb[1]), sb, b]
    for y in ys:
        yield [a, (a[0], y), (b[0], y), b]
        yield [a, sa, (sa[0], y), (sb[0], y), sb, b]


def _visibility_route(a: Point, b: Point, start: str, end: str,
                      boxes: Sequence[Rect], previous: Sequence[tuple[Point, Point]],
                      xs: Sequence[float], ys: Sequence[float]) -> list[Point] | None:
    """Dijkstra on adjacent visible grid intersections, with arrival-axis state."""
    origin, goal = (xs.index(a[0]), ys.index(a[1])), (xs.index(b[0]), ys.index(b[1]))
    initial = (*origin, -1)
    distances = {initial: 0.0}
    parents: dict[tuple[int, int, int], tuple[int, int, int]] = {}
    queue = [(0.0, initial)]
    visibility: dict[tuple[Point, Point], bool] = {}
    while queue:
        cost, state = heappop(queue)
        if cost != distances[state]:
            continue
        ix, iy, incoming = state
        p = (xs[ix], ys[iy])
        if (ix, iy) == goal:
            points = [p]
            while state in parents:
                state = parents[state]
                points.append((xs[state[0]], ys[state[1]]))
            return _simplify(reversed(points))
        for jx, jy, axis in ((ix - 1, iy, 0), (ix + 1, iy, 0),
                             (ix, iy - 1, 1), (ix, iy + 1, 1)):
            if not (0 <= jx < len(xs) and 0 <= jy < len(ys)):
                continue
            q = (xs[jx], ys[jy])
            if incoming == -1 and not _outward(p, q, start):
                continue
            if (jx, jy) == goal and not _outward(q, p, end):
                continue
            edge = tuple(sorted((p, q)))
            if edge not in visibility:
                visibility[edge] = not any(_hits(p, q, box) for box in boxes)
            if not visibility[edge]:
                continue
            crossings = sum(_crosses(p, q, c, d) for c, d in previous)
            # A grid vertex may split a proper crossing across two graph edges.
            if incoming == axis:
                for c, d in previous:
                    if axis == 0 and c[0] == d[0] == p[0]:
                        crossings += min(c[1], d[1]) < p[1] < max(c[1], d[1])
                    elif axis == 1 and c[1] == d[1] == p[1]:
                        crossings += min(c[0], d[0]) < p[0] < max(c[0], d[0])
            extra = abs(q[0] - p[0]) + abs(q[1] - p[1])
            extra += _BEND * (incoming != -1 and incoming != axis) + _CROSSING * crossings
            following = (jx, jy, axis)
            next_cost = cost + extra
            if next_cost < distances.get(following, float("inf")):
                distances[following] = next_cost
                parents[following] = (ix, iy, incoming)
                heappush(queue, (next_cost, following))
    return None


def route(
    source: Rect,
    target: Rect,
    obstacles: list[Rect],
    *,
    from_port: str = "auto",
    to_port: str = "auto",
    slot: int = 0,
    slots: int = 1,
    previous: Sequence[Sequence[Point]] = (),
    waypoints: Sequence[Point] = (),
) -> list[Point]:
    """Return an orthogonal polyline with endpoints on the requested box sides.

    Ports are ``n|e|s|w|auto``. Zero-based slots evenly spread ports along a
    side. ``previous`` is a sequence of polylines (two-point segments work too).
    Inputs are never mutated. Ties use coordinate order, independent of obstacle
    ordering. Automatic choices minimize length + 40*bends + 200*crossings among
    simple candidates; a visibility graph handles otherwise blocked routes.
    Same-side self-loops use two distinct ports within their slot.

    ValueError indicates invalid geometry, nonorthogonal manual waypoints, or
    boxes/explicit ports for which no obstacle-free route can be found.
    """
    source, target = _rect(source), _rect(target)
    if min(source[2:]) <= 0 or min(target[2:]) <= 0:
        raise ValueError("Source and target dimensions must be positive")
    if from_port not in (*_NORMAL, "auto") or to_port not in (*_NORMAL, "auto"):
        raise ValueError("Ports must be n, e, s, w, or auto")
    if (not isinstance(slot, int) or not isinstance(slots, int)
            or slots < 1 or not 0 <= slot < slots):
        raise ValueError("Require slots >= 1 and 0 <= slot < slots")
    obstacles = sorted(set(_rect(box) for box in obstacles))
    old_segments = []
    for polyline in previous:
        points = tuple(_numbers(point, 2) for point in polyline)
        old_segments.extend((a, b) for a, b in zip(points, points[1:]) if a != b)
    manual = tuple(_numbers(point, 2) for point in waypoints)
    pairs = []
    for start in _NORMAL if from_port == "auto" else (from_port,):
        for end in _NORMAL if to_port == "auto" else (to_port,):
            f = g = (slot + 1) / (slots + 1)
            if source == target and start == end:
                f, g = (slot + 0.65) / (slots + 1), (slot + 1.35) / (slots + 1)
            a, b = _port(source, start, f), _port(target, end, g)
            if a != b:
                pairs.append((a, b, start, end))
    if manual:
        candidates = [[a, *manual, b] for a, b, _, _ in pairs]
        valid = [points for points in candidates if _orthogonal(points)]
        if not valid:
            raise ValueError("Manual waypoints must connect the border ports orthogonally")
        return min(valid, key=lambda points: (_score(points, old_segments), points))

    margin = 2 * _CLEARANCE + slot * _CLEARANCE
    for padding in (_CLEARANCE, 0.0):
        boxes = [source, target] + [
            (x - padding, y - padding, w + 2 * padding, h + 2 * padding)
            for x, y, w, h in obstacles
        ]
        valid = []
        grids = []
        for a, b, start, end in pairs:
            if any(_hits(a, a, box) or _hits(b, b, box) for box in boxes):
                continue
            xs, ys = _axes(a, b, boxes, margin)
            # Previous edge extents provide lanes for avoiding costly crossings.
            xs = sorted(set(xs) | {p[0] + offset for edge in old_segments for p in edge
                                   for offset in (-_CLEARANCE, _CLEARANCE)})
            ys = sorted(set(ys) | {p[1] + offset for edge in old_segments for p in edge
                                   for offset in (-_CLEARANCE, _CLEARANCE)})
            grids.append((a, b, start, end, xs, ys))
            for candidate in _candidates(a, b, start, end, xs, ys, margin):
                points = _simplify(candidate)
                if len(points) < 2 or not _orthogonal(points):
                    continue
                if not (_outward(points[0], points[1], start)
                        and _outward(points[-1], points[-2], end)):
                    continue
                if not any(_hits(p, q, box) for p, q in zip(points, points[1:]) for box in boxes):
                    valid.append(points)
        if valid:
            return min(valid, key=lambda points: (_score(points, old_segments), points))
        for a, b, start, end, xs, ys in grids:
            points = _visibility_route(a, b, start, end, boxes, old_segments, xs, ys)
            if points:
                valid.append(points)
        if valid:
            return min(valid, key=lambda points: (_score(points, old_segments), points))
    raise ValueError("No obstacle-free route connects the requested ports")
