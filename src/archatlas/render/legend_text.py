"""Semantic defaults for the public catalogue, overridable by model authors."""
TYPE_RELATIONS = {
    "A1": ("Supports a capability", "支持业务能力"),
    "A2": ("Value-stage progression", "价值阶段推进"),
    "A9": ("Material or work flow", "物料或工作流"),
    "B1": ("Actor–use case association", "参与者与用例的关联"),
    "B3": ("Decomposes into", "分解为"),
    "C1": ("Application interaction", "应用间交互"),
    "C2": ("System interaction", "系统交互"),
    "C3": ("Container interaction", "容器间交互"),
    "C4": ("Component interaction", "组件间交互"),
    "C6": ("Interface interaction", "接口交互"),
    "D2": ("Data flow", "数据流"),
    "D3": ("Data transformation or transfer", "数据转换或传递"),
    "E2": ("Control flow", "控制流"),
    "E4": ("Handoff or next step", "移交或下一步骤"),
    "F2": ("Data flow", "数据流"), "G4": ("Delivery flow", "交付流程"),
}
FAMILY_RELATIONS = {
    "sequence": ("Request", "请求"), "er": ("Relationship", "实体关系"),
    "statechart": ("State transition", "状态转换"),
    "lanes": ("Sequence flow", "顺序流"), "tree": ("Progression", "阶段推进"),
}
EDGES = {
    "call": ("Interaction", "交互"), "data": ("Data flow", "数据流"),
    "async": ("Asynchronous message", "异步消息"), "message": ("Message flow", "消息流"),
    "dependency": ("Depends on", "依赖关系"), "assoc": ("Association", "关联关系"),
    "reply": ("Reply (dashed)", "返回（虚线）"),
}
STYLES = {
    "peer": ("Elements in scope", "范围内元素"),
    "primary": ("Element in focus", "重点展示的元素"),
    "external": ("External participant", "外部参与方"),
    "shared": ("Shared element", "共享元素"), "planned": ("Proposed element", "拟建元素"),
    "highlight": ("Highlighted element", "重点提示元素"),
}
GROUPS = {
    "boundary": ("System boundary", "系统边界"), "frame": ("Grouping boundary", "分组边界"),
    "layer": ("Architecture layer", "架构层"),
    "pool": ("Participant boundary", "参与方边界"), "lane": ("Responsibility lane", "职责泳道"),
}


def local(model, pair):
    return pair[1 if model["meta"].get("lang", "").startswith("zh") else 0]


def meaning(model, section, key, fallback):
    return model["meta"].get("legend_labels", {}).get(section, {}).get(key, local(model, fallback))


def edge_label(edge, model):
    family, code = model["layout"]["template"], model["meta"]["type"].upper()
    source = next((e for i, e in enumerate(model.get("edges", []))
                   if e.get("id", f"edge-{i + 1}") == edge.id), {})
    uncertain = source.get("evidence", {}).get("status", "verified") != "verified"
    reply = edge.kind == "reply" or (family == "sequence" and edge.kind == "call" and edge.dashed and not uncertain)
    semantic = "reply" if reply else edge.kind
    default = EDGES[semantic]
    contextual = (edge.kind == "call" or
                  (edge.kind == "assoc" and (family == "er" or code == "B1")) or
                  (edge.kind == "data" and code == "D3"))
    if not reply and contextual:
        default = TYPE_RELATIONS.get(code, FAMILY_RELATIONS.get(family, default))
    label = meaning(model, "edges", semantic, default)
    if uncertain:
        label += local(model, (" (unverified)", "（未经核实）"))
    elif edge.dashed and not reply:
        label += local(model, (" (dashed)", "（虚线）"))
    if edge.direction == "<->":
        label += local(model, (" (both directions)", "（双向）"))
    return label


def style_label(style, model):
    return meaning(model, "styles", style, STYLES[style])


def group_label(kind, model):
    default = GROUPS[kind]
    if kind in ("boundary", "frame"):
        default = {"F2": ("Trust boundary", "信任边界"),
                   "G1": ("Deployment boundary", "部署边界"),
                   "G3": ("Network boundary", "网络边界")}.get(model["meta"]["type"].upper(), default)
    return meaning(model, "groups", kind, default)
