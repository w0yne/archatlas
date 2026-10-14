---
layout: doc
sidebar: false
aside: false
title: 先选对视图，再画方框
description: 架构图类型图谱与可移植的绘图 skill。
translationOf: en/index.md
sourceRev: 8ea75e8
reviewed: false
---
<script setup>
import { useData } from 'vitepress';
import workflow from '../.vitepress/fixtures/workflow.svg?raw';
const { theme } = useData();
</script>
<p class="atlas-kicker">架构，从意图出发</p>

# 先选对视图，再画方框

<p class="atlas-intro">一部架构图类型图谱，以及一个智能体 skill：把清晰的问题变成有用、有证据支撑的图。</p>

[使用 skill →](/zh/use/) · [浏览图谱 ↓](#explore) · [参与改进](/zh/improve/)

<Figure :svg="workflow" caption="这是一套绘图工作流，不保证结果自动正确。" />

## 一个问题，一个对的视图 {#explore}

上下文图说明系统的周边环境；时序图说明一次交互；权限模型说明权限归属。从读者需要理解什么出发，而不是从偏爱的表示法出发。

<p v-if="theme.catalogue.fixture" class="translation-banner">脚手架预览：完整的类型注册表和参考页面接入期间，这里先展示三个目录示例。这些卡片还不是可发布的参考内容。</p>

<div class="atlas-grid"><TypeCard v-for="type in theme.catalogue.types" :key="type.code" :type="type" /></div>

## 三种工作方式

- **选择图的类型。** 获得一个推荐视图、一个备选视图，以及各自的理由。
- **根据描述绘图。** 确定受众和边界，审阅线框图，然后渲染并检查。
- **读取代码仓库。** 把证据追溯到模型和选定的视图中。代码中的声明不能证明已部署的行为。

## SVG 优先，坦诚说明局限

首个目标是保留可编辑文字的 SVG 加模型 JSON。draw.io 和原生 PowerPoint 导出是未来的接口，目前不可用。几何检查通过不能代替语义复核或视觉复核。

这是早期的站点脚手架。渲染器、打包的 skill、完整目录和跨智能体发布评估正在分别接入。本站不暗示任何发布兼容性承诺。
