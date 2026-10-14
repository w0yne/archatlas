"""Schema and relationship invariants; no model code is executed."""
import json
from pathlib import Path

from jsonschema import Draft202012Validator


class ModelError(ValueError):
    pass


def validate(model):
    schema = json.loads(Path(__file__).with_name("schema.json").read_text())
    errors = sorted(Draft202012Validator(schema).iter_errors(model), key=lambda e: str(e.path))
    if errors:
        error = errors[0]
        raise ModelError(f"{'/'.join(map(str, error.path)) or 'model'}: {error.message}")
    entities = model.get("nodes", []) + model.get("groups", [])
    ids = [n["id"] for n in entities]
    extra = [x["id"] for x in model.get("tables", []) + model.get("frames", [])]
    edge_ids = [e.get("id", f"edge-{i + 1}") for i, e in enumerate(model.get("edges", []))]
    if len(set(ids + extra + edge_ids)) != len(ids + extra + edge_ids):
        raise ModelError("IDs must be unique across nodes, groups, tables, frames and edges")
    groups = {g["id"]: g for g in model.get("groups", [])}
    for entity in entities:
        parent = entity.get("parent")
        seen = {entity["id"]}
        while parent:
            if parent not in groups:
                raise ModelError(f"{entity['id']}: unknown parent {parent}")
            if parent in seen:
                raise ModelError(f"{entity['id']}: containment cycle")
            seen.add(parent)
            parent = groups[parent].get("parent")
    for edge in model.get("edges", []):
        if edge["from"] not in ids or edge["to"] not in ids:
            raise ModelError("Edge endpoints must name an existing node or group")
    for node in model.get("nodes", []):
        if "event_type" in node and node["kind"] != "event":
            raise ModelError("event_type applies only to BPMN event nodes")
    for table in model.get("tables", []):
        if not table["columns"] or any(len(row) != len(table["columns"]) for row in table["rows"]):
            raise ModelError(f"{table['id']}: table rows must match non-empty columns")
    template = model["layout"]["template"]
    if template == "sequence":
        if groups or model.get("tables"):
            raise ModelError("Sequence uses frames, not containment groups or tables")
        node_ids = {n["id"] for n in model.get("nodes", [])}
        steps = [e.get("step", i + 1) for i, e in enumerate(model.get("edges", []))]
        if len(set(steps)) != len(steps):
            raise ModelError("Sequence steps must be unique")
        for item in model.get("frames", []) + model.get("activations", []):
            if item["from_step"] not in steps or item["to_step"] not in steps or item["to_step"] < item["from_step"]:
                raise ModelError("Sequence ranges must reference existing, ordered steps")
            if "node" in item and item["node"] not in node_ids:
                raise ModelError("Activation must reference a lifeline node")
    elif model.get("frames") or model.get("activations"):
        raise ModelError("Frames and activations require the sequence template")
    if model.get("tables") and template != "grid_table":
        raise ModelError("Tables require the grid_table template")
    if template == "lanes" and any(g["kind"] == "pool" for g in groups.values()):
        items = {item["id"]: item for item in entities}

        def pool(id):
            while id:
                item = items[id]
                if item.get("kind") == "pool":
                    return id
                id = item.get("parent")
            return None

        for edge in model.get("edges", []):
            a, b = pool(edge["from"]), pool(edge["to"])
            kind = edge.get("kind", "call")
            if kind == "message":
                if a is None or b is None or a == b:
                    raise ModelError("BPMN message flow must connect two different pools")
                if edge.get("dashed") is False or edge.get("dir", "->") != "->":
                    raise ModelError("BPMN message flow requires a dashed directed arrow")
            elif kind == "call":
                if a != b or any(items[id]["kind"] == "pool" for id in (edge["from"], edge["to"])):
                    raise ModelError("BPMN sequence flow cannot cross or terminate on pool boundaries")
    return model
