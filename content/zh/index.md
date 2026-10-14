---
layout: doc
sidebar: false
aside: false
title: 先选对视图，再画方框
description: 架构图类型指南与可移植的绘图 skill。
translationOf: en/index.md
sourceRev: bca58c9299c22a5a05f98bf81e38393e6e1d1713
reviewed: true
---
<script setup>
import { useData, withBase } from 'vitepress';
import workflow from '../.vitepress/fixtures/workflow.zh.svg?raw';
const { theme } = useData();
</script>
<p class="atlas-kicker">架构，从意图出发</p>

# 先选对视图，再画方框

<p class="atlas-intro">一部架构图类型指南，以及一个绘图 skill：把清晰的问题变成有用、有证据支撑的图。</p>

[找到合适的图 →](/zh/choose) · [浏览全部类型](/zh/types/) · [使用 skill](/zh/use/)

<Figure :svg="workflow" caption="这是一套绘图工作流，不保证结果自动正确。" />

## 按你的问题组织图型 {#explore}

上下文图说明系统与外部的关系；时序图说明一次交互；权限模型说明谁能做什么。先想读者需要理解什么，再选表示法。

<p class="catalogue-count">{{ theme.catalogue.types.length }} 类图 · {{ theme.catalogue.types.filter(type => type.available.zh).length }} 篇中文参考文档</p>

<div class="atlas-grid family-grid">
  <article v-for="(label, key) in theme.catalogue.families" :key="key" class="type-card">
    <span class="type-code">{{ key }}</span>
    <h3><a :href="withBase('/zh/types/#family-' + key)">{{ label.zh }}</a></h3>
    <p>{{ theme.catalogue.types.filter(type => type.family === key).length }} 类图</p>
  </article>
</div>

## 三种工作方式

- **选择图型。** 获得推荐视图、备选视图及各自理由。
- **根据描述绘图。** 明确读者和边界，先审线框，再渲染与检查。
- **读取仓库。** 把证据对应到模型和视图；代码声明不等于部署实况。

## 试一个具体请求

> 引导模式。帮助新开发者理解结账、支付和库存。推荐一种视图，并解释它不展示什么。使用中文标签。

从审阅过的克隆先安装渲染器，再复制 skill：

    make setup
    . .venv/bin/activate
    atlas init C2 -o model.json
    atlas render model.json -o out/

[安装说明](/zh/use/)区分 Claude Code、Codex、Pi 的源码与打包文件安装路径。启动代理时保持 Python 环境激活；使用 skill 不依赖站点运行。

## SVG 优先，坦诚说明限制

首个输出是保留可编辑文字的 SVG 与模型 JSON。draw.io 和原生 PowerPoint 导出属于未来接口，目前不可用。几何检查不能代替语义或视觉复核。

仓库中的 0.1.0 为预发布版本：40 类图的中英文文档、skill、SVG 渲染器、打包工具和评测框架已经存在。尚未发布 PyPI 包或公开发布压缩包；针对 skill 修订 3847acb 的首轮三宿主对比评测已完成，但未通过发布门槛。它不代表当前修订的结论：当前版本的针对性复测与发布认证仍待完成。[查阅首轮报告](/evaluation-report.txt)。[查看命令与限制](/zh/use/formats)。
