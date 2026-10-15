import copy
import json
from pathlib import Path

from .validate import ModelError, validate


def resolve(model, labels):
    model = copy.deepcopy(model)

    def text(value):
        key = value[1:] if value.startswith("@") else value
        if value.startswith("@") and key not in labels:
            raise ModelError(f"Missing translation: {key}")
        return labels.get(key, value)

    for key in ("title", "subtitle", "description", "audience"):
        if key in model["meta"]:
            model["meta"][key] = text(model["meta"][key])
    for collection in ("nodes", "groups", "edges", "tables", "frames"):
        for item in model.get(collection, []):
            for key in ("label", "title", "sub", "guard"):
                if key in item:
                    item[key] = text(item[key])
            for key in ("tags", "attributes", "columns"):
                if key in item:
                    item[key] = list(map(text, item[key]))
            if "rows" in item:
                item["rows"] = [list(map(text, row)) for row in item["rows"]]
            for operand in item.get("operands", []):
                operand["guard"] = text(operand["guard"])
            if "chips" in item:
                item["chips"] = [text(chip) if isinstance(chip, str) else
                                 {**chip, "label": text(chip["label"])} for chip in item["chips"]]
            if isinstance(item.get("badge"), str):
                item["badge"] = text(item["badge"])
    for entry in model["meta"].get("legend", []):
        entry["label"] = text(entry["label"])
        if isinstance(entry.get("badge"), str):
            entry["badge"] = text(entry["badge"])
    for mapping in model["meta"].get("legend_labels", {}).values():
        for key, value in mapping.items():
            mapping[key] = text(value)
    return model


def load(path, lang=None):
    path = Path(path)
    model = validate(json.loads(path.read_text(encoding="utf-8")))
    lang = lang or model["meta"].get("lang", "en")
    if not lang or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_" for c in lang):
        raise ModelError("Language must be a locale identifier")
    labels = dict(model.get("labels", {}))
    translation = path.with_name(f"labels.{lang}.json")
    if translation.exists():
        external = json.loads(translation.read_text(encoding="utf-8"))
        if not isinstance(external, dict) or not all(isinstance(v, str) for v in external.values()):
            raise ModelError("Translation file must map keys to strings")
        labels.update(external)
    model = resolve(model, labels)
    model["meta"]["lang"] = lang
    return model
