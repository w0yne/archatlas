---
title: 安装与使用 skill
translationOf: en/use/index.md
sourceRev: 2389b26ba4db27b8a7bebafa0adfb5bc7da45a2f
reviewed: true
---
# 安装与使用 skill

archatlas 0.1.0 是**仓库内的预发布版本**：英文 skill、40 类图的参考文档、SVG 渲染器、打包工具和评测框架已经存在。尚未发布 PyPI 包，针对 skill 修订 3847acb 的首轮三宿主对比评测已完成，但未通过发布门槛。它不代表当前修订的结论：当前版本的针对性复测与发布认证仍待完成。[查阅首轮报告](/evaluation-report.txt)。

## 方式 A：使用经过审阅的源码克隆

在仓库根目录运行完整开发环境安装：

    make setup
    . .venv/bin/activate
    atlas --help

如果只需要渲染器，不需要站点开发依赖：

    python3 -m venv .venv
    . .venv/bin/activate
    python -m pip install -e .

之后按下表复制 skill 文件夹。**从已经激活的环境启动代理**，才能让 helper 找到已安装的渲染器。只复制源码中的 skill 文件夹不会安装 Python 依赖或渲染器库。不要运行 pip install archatlas：本项目尚未发布这个包名。

## 方式 B：使用经过验证的打包文件

在审阅过的克隆中生成打包文件：

    python tools/pack_skill.py --out dist --verify

解压选定的压缩包并进入解压目录。顶层文件夹是 **architecture-diagrams/**，不是 skills/architecture-diagrams/。其中包含 scripts/lib，但第三方 Python 依赖需要另行安装：

    python3 -m venv .venv
    . .venv/bin/activate
    python -m pip install -r architecture-diagrams/scripts/requirements.txt

将整个 architecture-diagrams 文件夹复制到下表的一个位置，并保持环境激活后再启动代理。安装前检查源码、压缩包校验值及脚本，不要用软件源中的同名包替代。

## 选择一个代理安装位置

| 代理 | 个人目录 | 显式调用 |
|---|---|---|
| Claude Code | ~/.claude/skills/architecture-diagrams/ | /architecture-diagrams |
| Codex | ~/.agents/skills/architecture-diagrams/ | $architecture-diagrams |
| Pi | ~/.pi/agent/skills/architecture-diagrams/ | /skill:architecture-diagrams |

例如，从已安装渲染器的克隆中复制：

    mkdir -p ~/.claude/skills
    cp -R skills/architecture-diagrams ~/.claude/skills/

若从解压包复制，改用 cp -R architecture-diagrams ~/.claude/skills/。Codex、Pi 使用表中对应目标目录，不要重复安装到多个发现位置。安装后重启代理；Pi 也可使用 /reload。

## 第一次请求与第一次渲染

[不确定该画哪种图？先选择视图。](/zh/choose)

> 引导模式。帮助新开发者理解结账、支付和库存。推荐一种视图，并解释它不展示什么。使用中文标签。

在源码克隆中验证已安装的渲染器：

    atlas init C2 -o model.json
    atlas render model.json -o out/
    atlas check out/diagram.svg --model model.json --report out/findings.json

渲染器可以从随附模板读取类型代码。请检查 findings 和实际图片；命令结束不代表质量合格。[命令与限制](./formats)说明可选预览依赖和退出码。

## 更新与卸载

只替换本 skill 的文件夹，更新其 Python 环境，再重启或重新加载代理。不要删除代理的整个 skills 目录。

## 兼容性状态

文档与帮助信息研究覆盖 Claude Code 2.1.285、Codex 0.160.1、Pi 1.1.0；这不代表跨代理输出质量认证已经完成。官方说明：[Claude Code](https://code.claude.com/docs/en/skills)、[Codex](https://developers.openai.com/codex/skills)、[Pi](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/skills.md)。
