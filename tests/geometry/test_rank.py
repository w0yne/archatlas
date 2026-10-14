"""Contracts for graph ranks without geometry or rendering."""

from copy import deepcopy
from itertools import permutations

import pytest

from archatlas.layout.rank import rank_graph


def test_empty_isolated_and_stable_branch_order():
    assert rank_graph([], []) == []
    assert rank_graph(["z", "a", "m"], []) == [["z", "a", "m"]]
    assert rank_graph(
        ["root", "right", "left", "join", "alone"],
        [("root", "left"), ("root", "right"), ("left", "join"), ("right", "join")],
    ) == [["root", "alone"], ["right", "left"], ["join"]]


def test_longest_path_not_input_order_or_shortest_path():
    assert rank_graph(
        ["end", "middle", "start"],
        [("start", "end"), ("start", "middle"), ("middle", "end")],
    ) == [["start"], ["middle"], ["end"]]


def test_cycles_spread_deterministically_independent_of_edge_order():
    ids = ["idle", "active", "done", "outside"]
    edges = [("idle", "active"), ("active", "done"), ("done", "idle")]
    expected = [["idle", "outside"], ["active"], ["done"]]
    for shuffled in permutations(edges):
        assert rank_graph(ids, list(shuffled)) == expected
    # The back-edge is ignored for ranking, not removed from the caller's graph.
    assert edges[-1] == ("done", "idle")


def test_overlapping_cycles_keep_all_nodes_once():
    ids = ["a", "b", "c", "d"]
    edges = [("a", "b"), ("b", "a"), ("b", "c"), ("c", "a"),
             ("c", "d"), ("d", "b")]
    assert rank_graph(ids, edges) == [["a"], ["b"], ["c"], ["d"]]
    assert rank_graph(ids, list(reversed(edges))) == [["a"], ["b"], ["c"], ["d"]]


def test_self_edges_and_duplicates_do_not_affect_ranks_or_order():
    ids = ["a", "b", "c", "d"]
    edges = [("a", "d"), ("b", "c")]
    expected = [["a", "b"], ["d", "c"]]
    assert rank_graph(ids, edges) == expected
    assert rank_graph(ids, edges * 3 + [(node, node) for node in ids]) == expected


def test_crossing_reduction_preserves_barycentre_ties():
    assert rank_graph(
        ["a", "b", "x", "y", "z"],
        [("a", "z"), ("b", "x"), ("b", "y")],
    ) == [["a", "b"], ["z", "x", "y"]]
    # Both orders have one crossing: keep original order on equal scores.
    assert rank_graph(
        ["a", "b", "y", "x"],
        [("a", "x"), ("a", "y"), ("b", "x"), ("b", "y")],
    ) == [["a", "b"], ["y", "x"]]


def test_backward_sweep_resolves_crossing_left_by_forward_tie():
    # x and y both have barycentre 1, so a forward sweep keeps the crossing.
    assert rank_graph(
        ["a", "b", "c", "x", "y"],
        [("a", "y"), ("b", "x"), ("c", "y")],
    ) == [["b", "a", "c"], ["x", "y"]]


def test_minimum_hints_propagate_and_preserve_empty_layers():
    ids = ["start", "middle", "end", "alone"]
    edges = [("start", "middle"), ("middle", "end")]
    hints = {"start": 2, "middle": 1, "end": 6}
    before = deepcopy((ids, edges, hints))
    expected = [["alone"], [], ["start"], ["middle"], [], [], ["end"]]
    assert rank_graph(ids, edges, hints) == expected
    assert rank_graph(ids, edges, hints) == expected
    assert (ids, edges, hints) == before


def test_long_chain_does_not_require_recursive_traversal():
    ids = [str(index) for index in range(1200)]
    assert rank_graph(ids, list(zip(ids, ids[1:]))) == [[node] for node in ids]


@pytest.mark.parametrize("ids,edges,hints", [
    (["a", "a"], [], None),
    (["a"], [("a", "missing")], None),
    (["a"], [], {"missing": 0}),
    (["a"], [], {"a": -1}),
    (["a"], [], {"a": 1.5}),
    (["a"], [], {"a": True}),
])
def test_invalid_graph_or_hint_rejected(ids, edges, hints):
    with pytest.raises(ValueError):
        rank_graph(ids, edges, hints)
