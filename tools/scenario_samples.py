"""Manifest-driven hand-authored samples; no layout or model-schema extension."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENARIO = ROOT / "examples/ai-service-assistant"


def load_manifest() -> dict:
    manifest = json.loads((SCENARIO / "manifest.json").read_text())
    facts = json.loads((SCENARIO / manifest["scenario"]).read_text())
    glossary = json.loads((SCENARIO / manifest["glossary"]).read_text())
    if glossary["version"] != facts["version"]:
        raise ValueError("Stale shared glossary")
    for identity, entity in facts["entities"].items():
        if any(glossary["entries"][identity][lang] != entity["labels"][lang] for lang in ("en", "zh")):
            raise ValueError(f"Glossary label drift: {identity}")
    seen = set()
    headline_owners = set()
    for view in manifest["views"]:
        if view["id"] in seen:
            raise ValueError(f"Duplicate view {view['id']}")
        seen.add(view["id"])
        for field in ("source", "publication"):
            path = Path(view[field])
            if path.is_absolute() or ".." in path.parts:
                raise ValueError(f"Unsafe sample path: {view[field]}")
        for code in view["headlines"]:
            if code in headline_owners:
                raise ValueError(f"Duplicate headline: {code}")
            headline_owners.add(code)
        if view["languages"] != manifest["languages"]:
            raise ValueError(f"Incomplete languages: {view['id']}")
        for lang in view["languages"]:
            folder = SCENARIO / view["source"] / lang
            model = json.loads((folder / "diagram.json").read_text())
            expected = json.loads((folder / "expected.json").read_text())
            if expected["scenarioVersion"] != facts["version"]:
                raise ValueError(f"Stale scenario: {folder}")
            if model["meta"]["type"] != view["code"] or model["meta"]["lang"] != lang:
                raise ValueError(f"Wrong type/language: {folder}")
            entities, local = expected["entities"], expected.get("viewElements", {})
            if set(entities) & set(local) or set(entities) | set(local) != {n["id"] for n in model["nodes"]}:
                raise ValueError(f"Unmapped diagram entity: {folder}")
            if local != facts.get("viewElements", {}).get(view["id"], {}):
                raise ValueError(f"Local projection differs from shared facts: {folder}")
            for node in model["nodes"]:
                if node["id"] in entities:
                    entity = facts["entities"][entities[node["id"]]]
                    labels = [entity["labels"][lang], *entity.get("viewLabels", {}).get(lang, [])]
                else:
                    projection = local[node["id"]]
                    if (projection["kind"] not in {"task", "state", "gateway", "initial", "final", "event", "process", "note"}
                            or node["kind"] != projection["kind"]
                            or projection["contextEntity"] not in facts["entities"]
                            or not set(projection["sourceRefs"]) <= facts["invariants"].keys()):
                        raise ValueError(f"Invalid semantic projection: {folder}:{node['id']}")
                    if glossary["viewElements"][view["id"]][node["id"]] != projection["labels"]:
                        raise ValueError(f"Projection glossary drift: {folder}:{node['id']}")
                    labels = [projection["labels"][lang]]
                if node["label"] not in labels:
                    raise ValueError(f"Label drift: {folder}:{node['id']}")
            if not set(expected.get("roleEntities", [])) <= facts["entities"].keys():
                raise ValueError(f"Unknown table role: {folder}")
            if not set(expected.get("assumptions", [])) <= facts["assumptions"].keys():
                raise ValueError(f"Unknown teaching assumption: {folder}")
            if not set(expected["invariants"]) <= facts["invariants"].keys():
                raise ValueError(f"Unknown invariant: {folder}")
            if expected["invariants"] != view["rules"]:
                raise ValueError(f"Rule projection drift: {folder}")
            if not (folder / "diagram.svg").is_file():
                raise ValueError(f"Missing artwork: {folder}")
        en = json.loads((SCENARIO / view["source"] / "en/diagram.json").read_text())
        zh = json.loads((SCENARIO / view["source"] / "zh/diagram.json").read_text())
        topology = lambda m: (
            [(n["id"], n["kind"], n.get("parent")) for n in m["nodes"]],
            [(e["id"], e["from"], e["to"], e["kind"]) for e in m["edges"]])
        if topology(en) != topology(zh):
            raise ValueError(f"Bilingual topology differs: {view['id']}")
    return manifest


def sample_files(manifest: dict | None = None):
    """Yield source and public/samples-relative path; also used by packaging/tests."""
    manifest = manifest or load_manifest()
    for name in ("manifest.json", "scenario.json", "glossary.json"):
        yield SCENARIO / name, Path("ai-service-assistant") / name
    for view in manifest["views"]:
        for lang in view["languages"]:
            for name in ("diagram.svg", "diagram.json", "expected.json"):
                yield SCENARIO / view["source"] / lang / name, Path(view["publication"]) / lang / name
