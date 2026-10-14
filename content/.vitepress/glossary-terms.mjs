export const terms = [
  {
    "id": "system-overview",
    "name": {
      "en": "System overview",
      "zh": "系统概览"
    },
    "meaning": {
      "en": "Start with one system and its neighbours (C2). Use C1 for many applications or A7 for a business-level solution summary.",
      "zh": "单个系统与周边先用 C2；多应用全景用 C1，业务层方案概览用 A7。"
    }
  },
  {
    "id": "application-architecture",
    "name": {
      "en": "Application architecture",
      "zh": "应用架构"
    },
    "meaning": {
      "en": "An ambiguous name: C1 shows many applications; C3 shows the running applications and data stores of one system; C4 shows components inside one running application.",
      "zh": "这是有歧义的叫法：C1 展示多个应用，C3 展示单个系统的运行应用和数据存储，C4 展示单个运行应用内部的组件。"
    }
  },
  {
    "id": "container",
    "name": {
      "en": "Container",
      "zh": "容器"
    },
    "meaning": {
      "en": "In the C4 model, a runnable application or data store. It does not necessarily mean a Docker container.",
      "zh": "在 C4 model 中指可运行的应用或数据存储，不一定是 Docker 容器。"
    }
  },
  {
    "id": "component",
    "name": {
      "en": "Component",
      "zh": "组件"
    },
    "meaning": {
      "en": "A responsibility-bearing part inside one running application, not automatically a separate service or process.",
      "zh": "单个运行应用内部承担职责的部分，不自动等于独立服务或进程。"
    }
  },
  {
    "id": "logical",
    "name": {
      "en": "Logical architecture",
      "zh": "逻辑架构"
    },
    "meaning": {
      "en": "Responsibilities and their relationships without committing to physical hosting. A deployment view answers where those responsibilities run.",
      "zh": "先说明职责与关系，不承诺物理部署位置；部署视图才回答它们运行在哪里。"
    }
  },
  {
    "id": "layer-tier",
    "name": {
      "en": "Layer, tier and level",
      "zh": "层、部署层与层级"
    },
    "meaning": {
      "en": "A layer groups software responsibilities; a tier separates deployment. A level is an abstraction or decomposition depth. State which meaning is used.",
      "zh": "layer 按软件职责分层，tier 按部署分隔，level 指抽象或分解深度；应说明使用哪一种含义。"
    }
  },
  {
    "id": "estate",
    "name": {
      "en": "Application estate",
      "zh": "应用组合"
    },
    "meaning": {
      "en": "The collection of applications an organisation owns or operates. It is not one application.",
      "zh": "组织拥有或运营的一组应用，不是某一个应用。"
    }
  },
  {
    "id": "persona",
    "name": {
      "en": "Persona",
      "zh": "用户画像"
    },
    "meaning": {
      "en": "A representative user profile used to examine one experience or set of needs, not a real person’s private record.",
      "zh": "用于分析某类体验或需求的代表性用户描述，不是真实个人的私有记录。"
    }
  },
  {
    "id": "bpmn",
    "name": {
      "en": "BPMN semantics",
      "zh": "BPMN 语义"
    },
    "meaning": {
      "en": "Rules for interpreting process tasks, events, gateways, pools and messages. Use a plain flowchart when these precise rules are unnecessary.",
      "zh": "解释业务任务、事件、网关、池和消息的规则；不需要这些精确规则时，可使用普通流程图。"
    }
  },
  {
    "id": "trust-boundary",
    "name": {
      "en": "Trust boundary",
      "zh": "信任边界"
    },
    "meaning": {
      "en": "A change in who controls data or which identity and permissions are trusted. It is not automatically a network boundary.",
      "zh": "数据控制者或身份、权限信任假设发生变化的位置，不自动等于网络边界。"
    }
  },
  {
    "id": "promotion-gate",
    "name": {
      "en": "Promotion gate",
      "zh": "晋级检查"
    },
    "meaning": {
      "en": "A check or approval required before a tested release moves to another environment.",
      "zh": "经过测试的版本进入另一个环境前必须满足的检查或审批。"
    }
  },
  {
    "id": "lean",
    "name": {
      "en": "Lean value-stream mapping",
      "zh": "精益价值流图"
    },
    "meaning": {
      "en": "A method for examining work and waiting time across a delivery flow. It differs from a business-architecture value stream.",
      "zh": "检查交付流程中处理与等待时间的方法，不同于业务架构中的价值流。"
    }
  },
  {
    "id": "bounded-context",
    "name": {
      "en": "Bounded context",
      "zh": "限界上下文"
    },
    "meaning": {
      "en": "A boundary within which a team uses one coherent domain model and vocabulary. Another context may give the same word a different meaning.",
      "zh": "团队在其中使用一致领域模型和词汇的边界；另一个上下文可能对同一词采用不同含义。"
    }
  },
  {
    "id": "archimate",
    "name": {
      "en": "ArchiMate",
      "zh": "ArchiMate"
    },
    "meaning": {
      "en": "A modelling language for relationships across business, applications and technology. It is not the default first diagram for a newcomer.",
      "zh": "用于业务、应用与技术之间关系的建模语言，不是新手默认应画的第一张图。"
    }
  },
  {
    "id": "rummler-brache",
    "name": {
      "en": "Rummler–Brache-style swimlane",
      "zh": "Rummler–Brache 式泳道图"
    },
    "meaning": {
      "en": "A cross-functional process view that groups work by responsibility and highlights hand-offs. State the actual notation used rather than relying on the name alone.",
      "zh": "按职责组织工作并突出交接的跨职能流程视图；需要说明实际记法，而不能仅依赖名称。"
    }
  }
];
