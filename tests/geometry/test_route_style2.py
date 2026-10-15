"""Anonymous W8d geometry and port/overlap contracts for style round two."""

from copy import deepcopy
import importlib
import json
from pathlib import Path

import pytest

router = importlib.import_module("archatlas.layout.route")
FIXTURES = Path(__file__).parents[1] / "fixtures/style2-routing"


@pytest.mark.parametrize("name,maximum", [
    ("s1-payment", 410),
    ("s1-support", 380),
    ("s7-results-push", 150),
    ("s8-alternative-a", 590),
    ("s8-alternative-b", 850),
])
def test_evaluation_routes_shorten_without_shared_strokes(name, maximum):
    data = json.loads((FIXTURES / f"{name}.json").read_text())
    original = deepcopy(data)
    points = router.route(*data["args"], **data["kwargs"])
    segments = list(zip(points, points[1:]))
    length = sum(abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in segments)
    assert length < maximum < data["baseline"]["length"]
    assert router.backtrack(points) <= data["baseline"]["backtrack"]
    assert len(points) - 2 <= data["baseline"]["bends"]
    for a, b in segments:
        assert a != b and (a[0] == b[0] or a[1] == b[1])
        assert not any(router.segment_hits_rect(a, b, box)
                       for box in data["args"][:2])
        assert not any(router.segment_hits_rect(a, b, box, padding=8)
                       for box in data["args"][2])
        for line in data["kwargs"]["previous"]:
            for c, d in zip(line, line[1:]):
                assert router._overlap(a, b, c, d) == 0
                assert not router.crosses(a, b, c, d)
    assert data == original
    source, target, obstacles = data["args"]
    assert router.route(source, target, list(reversed(obstacles)), **data["kwargs"]) == points


def test_visibility_search_keeps_requested_outward_departure(monkeypatch):
    # A directionless search can exit west, reverse to its origin and then
    # travel north; simplifying that bounce silently loses the requested exit.
    monkeypatch.setattr(router, "_candidates", lambda *args: ())
    source, target = (0, 0, 20, 20), (100, 0, 20, 20)
    points = router.route(source, target, [], from_port="w", to_port="w")
    assert points[0] == (0, 10)
    assert points[1][0] < points[0][0] and points[1][1] == points[0][1]
    assert points[-1] == (100, 10)
    assert points[-2][0] < points[-1][0] and points[-2][1] == points[-1][1]
    assert not any(router.segment_hits_rect(a, b, box)
                   for a, b in zip(points, points[1:]) for box in (source, target))


def test_grid_subdivision_cannot_hide_a_shared_stroke():
    # Several short overlaps still form one shared stroke after simplification.
    points = router._visibility_route(
        (0, 0), (2, 0), "e", "w", [], [((0, 0), (2, 0))],
        [0, .5, 1, 1.5, 2], [-1, 0, 1], allow_shared=False,
    )
    assert points is None


def test_manual_auto_ports_keep_exact_waypoints_and_center_ports():
    waypoints = [(40, 10), (40, 90)]
    assert router.route((0, 0, 20, 20), (100, 80, 20, 20), [],
                        waypoints=waypoints) == [(20, 10), *waypoints, (100, 90)]


def test_port_inside_a_previous_stroke_is_occupied_even_without_a_vertex():
    previous = [[(10, 10), (-20, 10)]]
    points = router.route((0, 0, 20, 20), (-100, 80, 20, 20), [],
                          from_port="w", previous=previous)
    assert points[0] != (0, 10)
    assert not any(router._overlap(a, b, *previous[0]) for a, b in zip(points, points[1:]))
