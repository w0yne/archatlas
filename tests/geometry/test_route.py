"""Geometry contracts for the standalone orthogonal router."""

from copy import deepcopy

import pytest

from archatlas.layout.route import crosses, route, segment_hits_rect


def assert_clear(points, boxes, padding=0):
    assert len(points) >= 2
    for a, b in zip(points, points[1:]):
        assert a != b
        assert a[0] == b[0] or a[1] == b[1]
        assert not any(segment_hits_rect(a, b, box, padding) for box in boxes)


def test_straight_and_offset_slots():
    source, target = (0, 0, 20, 20), (100, 0, 20, 20)
    assert route(source, target, []) == [(20, 10), (100, 10)]
    paths = [route(source, target, [], from_port="e", to_port="w", slot=i, slots=3)
             for i in range(3)]
    assert [points[0] for points in paths] == [(20, 5), (20, 10), (20, 15)]
    assert [points[-1] for points in paths] == [(100, 5), (100, 10), (100, 15)]


def test_blockers_force_detour_with_clearance():
    source, target = (0, 40, 20, 20), (160, 40, 20, 20)
    obstacles = [(50, 0, 30, 90), (100, 20, 20, 100)]
    points = route(source, target, obstacles, from_port="e", to_port="w")
    assert points[0] == (20, 50)
    assert points[-1] == (160, 50)
    assert len(points) > 2
    assert_clear(points, obstacles, padding=8)
    assert_clear(points, [source, target])


def test_alternating_walls_require_visibility_graph():
    source, target = (10, 70, 10, 10), (180, 70, 10, 10)
    obstacles = [
        (-10, -10, 220, 10), (-10, 160, 220, 10),
        (-10, 0, 10, 160), (200, 0, 10, 160),
        (50, 0, 10, 120), (100, 40, 10, 120), (150, 0, 10, 120),
    ]
    points = route(source, target, obstacles, from_port="e", to_port="w")
    assert points[0] == (20, 75)
    assert points[-1] == (180, 75)
    assert len(points) >= 10
    assert_clear(points, obstacles, padding=8)
    assert_clear(points, [source, target])


@pytest.mark.parametrize("start", "nesw")
@pytest.mark.parametrize("end", "nesw")
def test_explicit_ports_and_outward_departure(start, end):
    source, target = (0, 0, 20, 20), (100, 80, 20, 20)
    first = {"n": (10, 0), "e": (20, 10), "s": (10, 20), "w": (0, 10)}
    last = {"n": (110, 80), "e": (120, 90), "s": (110, 100), "w": (100, 90)}
    normal = {"n": (0, -1), "e": (1, 0), "s": (0, 1), "w": (-1, 0)}
    points = route(source, target, [], from_port=start, to_port=end)
    assert points[0] == first[start]
    assert points[-1] == last[end]
    for a, b, side in ((points[0], points[1], start), (points[-1], points[-2], end)):
        assert sum((b[i] - a[i]) * normal[side][i] for i in (0, 1)) > 0
    assert_clear(points, [source, target])


@pytest.mark.parametrize("start,end", [("auto", "auto")] +
                         [(a, b) for a in "nesw" for b in "nesw"])
def test_self_loops_are_nonzero_and_stay_outside(start, end):
    box = (10, 10, 40, 30)
    obstacles = [(60, 0, 20, 60)]
    points = route(box, box, obstacles, from_port=start, to_port=end)
    assert len(points) >= 4
    assert points[0] != points[-1]
    assert_clear(points, [box])
    assert_clear(points, obstacles, padding=8)


def test_determinism_and_inputs_are_immutable():
    source, target = (0, 0, 20, 20), (120, 80, 20, 20)
    obstacles = [(40, 0, 20, 60), (80, 50, 20, 60)]
    previous = [[(30, -50), (30, 150)]]
    before = deepcopy((obstacles, previous))
    expected = route(source, target, obstacles, previous=previous)
    assert all(route(source, target, obstacles, previous=previous) == expected for _ in range(3))
    assert route(source, target, list(reversed(obstacles)), previous=previous) == expected
    assert (obstacles, previous) == before


def test_crossing_penalty_prefers_short_detour():
    source, target = (0, 0, 20, 20), (100, 0, 20, 20)
    previous = [((60, 0), (60, 20))]
    points = route(source, target, [], from_port="e", to_port="w", previous=previous)
    assert len(points) > 2
    assert not any(crosses(a, b, *previous[0]) for a, b in zip(points, points[1:]))
    assert_clear(points, [source, target])


def test_manual_waypoints_override_internal_route_and_obstacles():
    waypoints = [(40, 10), (40, -20), (80, -20), (80, 10)]
    before = deepcopy(waypoints)
    points = route((0, 0, 20, 20), (100, 0, 20, 20), [(35, -25, 10, 40)],
                   from_port="e", to_port="w", waypoints=waypoints)
    assert points == [(20, 10), *waypoints, (100, 10)]
    assert waypoints == before
    with pytest.raises(ValueError, match="orthogonally"):
        route((0, 0, 20, 20), (100, 0, 20, 20), [], waypoints=[(45, 32)])


def test_clearance_relaxes_for_narrow_gap():
    source, target = (0, 0, 20, 20), (24, 0, 20, 20)
    obstacles = [(20, -10, 4, 15), (20, 15, 4, 15)]
    points = route(source, target, obstacles, from_port="e", to_port="w")
    assert points == [(20, 10), (24, 10)]
    assert_clear(points, obstacles)


def test_impossible_port_raises_instead_of_crossing_box():
    with pytest.raises(ValueError, match="No obstacle-free route"):
        route((0, 0, 20, 20), (100, 0, 20, 20), [(19, 5, 10, 10)],
              from_port="e", to_port="w")


@pytest.mark.parametrize("a,b,expected", [
    ((-5, 5), (15, 5), True),
    ((-5, 0), (15, 0), False),
    ((-5, -5), (0, 0), False),
    ((-5, 5), (5, -5), False),
    ((0, 5), (10, 5), True),
    ((5, 5), (5, 5), True),
    ((0, 0), (0, 0), False),
    ((-5, -5), (15, 15), True),
])
def test_strict_interior_segment_intersection(a, b, expected):
    assert segment_hits_rect(a, b, (0, 0, 10, 10)) is expected
    assert segment_hits_rect(b, a, (0, 0, 10, 10)) is expected


def test_padding_and_degenerate_rectangle():
    assert not segment_hits_rect((-5, -1), (15, -1), (0, 0, 10, 10))
    assert segment_hits_rect((-5, -1), (15, -1), (0, 0, 10, 10), padding=2)
    assert not segment_hits_rect((-5, 5), (15, 5), (0, 0, 0, 10))


def test_crosses_excludes_touches_and_overlaps():
    assert crosses((0, 5), (10, 5), (5, 0), (5, 10))
    assert crosses((0, 0), (10, 10), (0, 10), (10, 0))
    assert not crosses((0, 5), (5, 5), (5, 0), (5, 10))
    assert not crosses((0, 5), (10, 5), (2, 5), (12, 5))


@pytest.mark.parametrize("kwargs", [
    {"from_port": "east"}, {"slots": 0}, {"slot": -1}, {"slot": 2, "slots": 2},
    {"waypoints": [(float("nan"), 10)]},
])
def test_invalid_arguments(kwargs):
    with pytest.raises(ValueError):
        route((0, 0, 20, 20), (100, 0, 20, 20), [], **kwargs)
