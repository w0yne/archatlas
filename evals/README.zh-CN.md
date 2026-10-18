# 评测

[English](README.md)

本目录是评测工具，用来检验 `architecture-diagrams` skill 能否让 agent 画出更好的架构图。每个场景都在 Claude Code、Codex 和 Pi 上以无交互方式运行两次：一次装了 skill，一次没装（见 DESIGN §8）。

## 内容

| 路径 | 说明 |
|---|---|
| `scenarios/s01…s10-*.yaml` | 10 个任务场景：提示词、模式、引导模式的预设回答、固定输入（fixture）、期望内容 |
| `scenarios/triggers.yaml` | 触发测试：6 条应当加载 skill 的提示词，6 条应当不加载的近似提示词 |
| `scenarios/fixtures/` | 小型合成输入文件（S9 使用） |
| `rubric.md` | 硬门槛，以及各维度 0–3 分的评分标准 |
| `run_eval.py` | 运行器：创建沙箱、准备 fixture、执行多轮对话、采集指标、输出 `results.json` 和 `report.md` |
| `adapters/{claude,codex,pi}.py` | 每个宿主一个适配器：配置、命令行、事件解析 |
| `grade.py`、`grader/prompt.md` | 模型评分：按 `rubric.md` 给每次运行打分，写入 `grade.json` |
| `report.py` | 把运行结果和评分汇总为 `reports/<名称>.md` 与 `.json` |
| `reports/` | 提交到仓库的报告；原始结果不进仓库 |
| `hosts.example.yaml` | 本地宿主配置文件的模板 |
| `tests/` | 工具本身的不变量测试 |

仓库场景 S7、S8 使用公开的 Apache-2.0 仓库，以完整 commit 固定版本。运行器把仓库只读地拉取到沙箱里，从不运行仓库中的代码。

## 运行

命令见英文版 README（包括从发布 zip 安装 skill、`--budget-usd` 费用上限、评分与汇总）。评分模型应与被评模型不同。结果写入 `evals/results/<时间戳>/`（已在 gitignore 中）。

每次运行保存以下文件：
- 每一轮的事件流、stderr 和命令行；
- 子进程环境变量的名称列表（不含值）；
- 最终回复；
- agent 产出的文件。

汇总表记录退出码、耗时、token 数、费用（宿主提供时）、澄清轮数、skill 加载证据，以及 SVG 硬门槛 G5 的检查结果。

**"skill 已加载"只根据宿主的事件轨迹判断，不看回答文本。** 轨迹中需要出现以下任一项：
- `SKILL.md` 正文；
- 读取了 skill 目录内的文件；
- Claude 的 `Skill` 工具调用。

如果按名称显式调用 skill，而宿主注入时没有留下事件，结果记为 `unknown`。

## 隔离

**沙箱目录**
- 每次运行都在 `--work-root` 下新建一个目录，内含独立的 HOME、TMPDIR、XDG 目录、宿主配置目录和一个 git 工作区。
- `--work-root` 要放在任何含 AGENTS.md 或 CLAUDE.md 的目录之外，因为宿主会向上层目录查找这些文件。

**环境变量**
- 子进程的环境从零构建，只包含：上面这些变量、hosts 文件中写明的 `env` 值、`pass_env` 里列出名字的变量。
- 以 `RCC_`、`CYBERWARE_`、`PI_`、`CLAUDE`、`CODEX_` 开头的变量一律不从父进程转发。

**清理与泄漏检查**
- 运行结束后删除沙箱。
- 然后扫描真实的宿主目录，查找运行期间有改动、且内容提到沙箱路径的文件。只要有命中，就判定失败。

**Codex 沙箱**
- 默认使用 `workspace-write`。
- 如果 bubblewrap 在当前机器上无法创建命名空间，就在 hosts 文件中设置 `sandbox: danger-full-access`。这时只靠临时目录隔离，所以完整评测要放在一次性的机器或容器里做。

## 收敛后的 AI 场景契约

S11/S12 使用未照抄样例的选型问题，覆盖审批/ACL 变化及明确不支持委托的身份前提；S6 保留安全评审基线。
运行 `python -m pytest -q evals/tests/test_ai_contracts.py` 复测选型路由与跨图契约。
这些确定性测试不调用智能体、不评分绘图，也不构成质量或性能对比；实时 S11/S12 使用现有 runner。
历史报告分数仍绑定其记录的 skill/场景修订。
