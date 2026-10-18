"""Manifest-driven hand-authored samples; no layout or model-schema extension."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENARIO = ROOT / "examples/ai-service-assistant"


def load_manifest() -> dict:
    manifest = json.loads((SCENARIO / "manifest.json").read_text())
    facts = json.loads((SCENARIO / manifest["scenario"]).read_text())
    seen = set()
    for view in manifest["views"]:
        if view["id"] in seen:
            raise ValueError(f"Duplicate view {view['id']}")
        seen.add(view["id"])
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
            if set(expected["entities"]) != {n["id"] for n in model["nodes"]}:
                raise ValueError(f"Unmapped diagram entity: {folder}")
            for node in model["nodes"]:
                entity = facts["entities"][expected["entities"][node["id"]]]
                labels = [entity["labels"][lang], *entity.get("viewLabels", {}).get(lang, [])]
                if node["label"] not in labels:
                    raise ValueError(f"Label drift: {folder}:{node['id']}")
            if not set(expected["invariants"]) <= facts["invariants"].keys():
                raise ValueError(f"Unknown invariant: {folder}")
            if expected["invariants"] != view["rules"]:
                raise ValueError(f"Rule projection drift: {folder}")
            if not (folder / "diagram.svg").is_file():
                raise ValueError(f"Missing artwork: {folder}")
        en = json.loads((SCENARIO / view["source"] / "en/diagram.json").read_text())
        zh = json.loads((SCENARIO / view["source"] / "zh/diagram.json").read_text())
        topology = lambda m: (
            [(n["id"], n.get("parent")) for n in m["nodes"]],
            [(e["id"], e["from"], e["to"], e["kind"]) for e in m["edges"]])
        if topology(en) != topology(zh):
            raise ValueError(f"Bilingual topology differs: {view['id']}")
    return manifest


def sample_files(manifest: dict | None = None):
    """Yield source and public/samples-relative path; also used by packaging/tests."""
    manifest = manifest or load_manifest()
    for name in ("manifest.json", "scenario.json"):
        yield SCENARIO / name, Path("ai-service-assistant") / name
    for view in manifest["views"]:
        for lang in view["languages"]:
            for name in ("diagram.svg", "diagram.json", "expected.json"):
                yield SCENARIO / view["source"] / lang / name, Path(view["publication"]) / lang / name
