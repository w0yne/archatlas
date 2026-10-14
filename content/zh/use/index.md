---
title: 安装与使用 skill
translationOf: en/use/index.md
sourceRev: 8ea75e8
reviewed: false
---
# 安装与使用 skill

这个可移植 skill 名为 **architecture-diagrams**，包含说明、参考资料和本地辅助入口。使用已安装的 skill 不需要本站。

::: warning 预发布说明
以下步骤描述的是从完整且经过审校的检出版本或发布包进行安装。本脚手架本身不包含渲染器，也不包含打包好的 skill。不要仅因名称相似就安装无关的软件包。
:::

## 安装前先审查

允许 skill 和脚本运行之前，先检查它们。使用可信的发布版本，记录其版本号，并避免在多个发现路径下重复安装。渲染器要求 Python 3.10+；浏览器仅用于视觉 QA，属可选项。请按发布包的依赖说明操作。

## Claude Code

在完整发布包的根目录下执行：

    mkdir -p ~/.claude/skills
    cp -R skills/architecture-diagrams ~/.claude/skills/

开启新会话并调用：

    /architecture-diagrams mode=guided 帮我为一家网店选择一个视图。

## Codex

    mkdir -p ~/.agents/skills
    cp -R skills/architecture-diagrams ~/.agents/skills/

开启新会话并调用：

    $architecture-diagrams mode=autonomous 为一家网店画一张系统上下文图。

## Pi

    mkdir -p ~/.pi/agent/skills
    cp -R skills/architecture-diagrams ~/.pi/agent/skills/

在已有会话中使用 /reload，然后调用：

    /skill:architecture-diagrams mode=guided 给我看看重要的架构选择。

如果只想在一次运行中试用完整的 skill 文件夹而不复制它：

    pi --skill ./skills/architecture-diagrams

## 你的第一个请求

说明谁会阅读这张图、它要回答什么问题、描述的是现状还是提议方案、系统边界，以及输出语言。例如：

> 引导模式。帮助一名新开发者理解结账如何与支付和库存通信。使用中文标签。不要推断部署拓扑。

预期会得到类型推荐、线框图、源模型、渲染好的 SVG，以及明确的复核状态。如果缺失的信息会改变架构的含义，智能体应当提问，而不是默默编造。

## 更新与卸载

只用经过审校的发布版本替换已安装的 architecture-diagrams 文件夹。卸载时，从所选的发现位置删除该文件夹，然后重启或重新加载宿主。切勿删除宿主的整个 skills 目录。

## 兼容性状态

文档与 CLI 帮助调研覆盖了 Claude Code 2.1.285、Codex 0.160.1 和 Pi 1.1.0。**这些并不是已完成的安装认证或输出质量认证。** 跨宿主的发布冒烟测试仍待进行。

宿主官方参考：[Claude Code skills](https://code.claude.com/docs/en/skills)、[Codex skills](https://developers.openai.com/codex/skills)、[Pi skills](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/skills.md)。

下一步：[选择交互模式](./modes)或[从代码推导视图](./code-to-diagram)。
