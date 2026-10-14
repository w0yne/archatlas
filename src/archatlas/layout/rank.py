"""Deterministic graph ranks and a small barycentre ordering heuristic."""

from itertools import combinations


def rank_graph(
    ids: list[str],
    edges: list[tuple[str, str]],
    hints: dict[str, int] | None = None,
) -> list[list[str]]:
    """Return layers indexed by zero-based rank, without changing the inputs.

    IDs must be unique; edge endpoints and hint keys must occur in ``ids``.
    Hints are nonnegative integer minimum ranks, not fixed positions. Empty
    layers are retained so their indices remain meaningful. Invalid inputs
    raise ValueError. Empty input returns [].

    Traverse roots and neighbours in original ID order, ignoring self-edges,
    duplicate edges and DFS back-edges for ranking. Longest-path ranks on the
    remaining DAG keep cyclic statecharts spread across layers. Callers retain
    all original edges for routing; this function returns only node placement.

    Up to four forward/backward barycentre sweep pairs reduce crossings between
    adjacent layers. Stable sorts preserve the current order on barycentre
    ties; equal crossing scores retain the earliest best ordering, starting
    with original ID order. Long edges constrain ranks but are not included in
    crossing reduction (no dummy nodes). This is a heuristic for small graphs,
    with quadratic crossing counts, not an optimal crossing/feedback-edge solver.
    """
    order = {node: index for index, node in enumerate(ids)}
    if len(order) != len(ids):
        raise ValueError("Node IDs must be unique")
    hints = {} if hints is None else hints
    for node, minimum in hints.items():
        if node not in order:
            raise ValueError(f"Unknown hint node: {node!r}")
        if type(minimum) is not int or minimum < 0:
            raise ValueError("Rank hints must be nonnegative integers")

    neighbours = {node: set() for node in ids}
    for source, target in edges:
        if source not in order or target not in order:
            raise ValueError(f"Unknown edge endpoint: {(source, target)!r}")
        if source != target:
            neighbours[source].add(target)
    adjacency = {
        node: sorted(targets, key=order.__getitem__)
        for node, targets in neighbours.items()
    }

    # Iterative DFS avoids a recursion limit on long chains. Only edges to an
    # active ancestor are discarded; cross-edges and forward edges are kept.
    state = dict.fromkeys(ids, 0)
    dag = {node: [] for node in ids}
    finished = []
    for root in ids:
        if state[root]:
            continue
        state[root] = 1
        stack = [(root, iter(adjacency[root]))]
        while stack:
            source, targets = stack[-1]
            target = next(targets, None)
            if target is None:
                state[source] = 2
                finished.append(source)
                stack.pop()
            elif state[target] != 1:
                dag[source].append(target)
                if state[target] == 0:
                    state[target] = 1
                    stack.append((target, iter(adjacency[target])))

    ranks = {node: hints.get(node, 0) for node in ids}
    for source in reversed(finished):
        for target in dag[source]:
            ranks[target] = max(ranks[target], ranks[source] + 1)
    layers = [[] for _ in range(max(ranks.values(), default=-1) + 1)]
    for node in ids:
        layers[ranks[node]].append(node)

    incoming = {node: [] for node in ids}
    outgoing = {node: [] for node in ids}
    bands = [[] for _ in layers]
    for source in ids:
        for target in dag[source]:
            if ranks[target] == ranks[source] + 1:
                incoming[target].append(source)
                outgoing[source].append(target)
                bands[ranks[source]].append((source, target))

    best = [layer[:] for layer in layers]
    best_score = _crossings(layers, bands)
    if best_score == 0:
        return best
    for _ in range(4):
        for forward in (True, False):
            indices = (range(1, len(layers)) if forward
                       else range(len(layers) - 2, -1, -1))
            neighbours = incoming if forward else outgoing
            for index in indices:
                reference = layers[index - 1 if forward else index + 1]
                positions = {node: pos for pos, node in enumerate(reference)}
                previous = {node: pos for pos, node in enumerate(layers[index])}

                def barycentre(node):
                    linked = neighbours[node]
                    return (sum(positions[other] for other in linked) / len(linked)
                            if linked else previous[node])

                layers[index].sort(key=barycentre)
            score = _crossings(layers, bands)
            if score < best_score:
                best = [layer[:] for layer in layers]
                best_score = score
                if score == 0:
                    return best
    return best


def _crossings(layers, bands):
    positions = {node: pos for layer in layers for pos, node in enumerate(layer)}
    return sum(
        (positions[a] - positions[c]) * (positions[b] - positions[d]) < 0
        for band in bands
        for (a, b), (c, d) in combinations(band, 2)
    )
