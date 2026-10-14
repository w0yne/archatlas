---
title: 改进 skill
translationOf: en/improve/index.md
sourceRev: 8ea75e8
reviewed: true
---
# 改进 skill

有用的改动说明的是反复出现的问题，而不是某个项目独有的偏好。

## 贡献小而易审的改动

1. 描述误解或缺陷，以及目标读者。
2. 提供一个新的通用示例，或一个采用宽松许可的公开来源。
3. 修改最小范围的相关参考、模板或检查。
4. 运行 make check；如有影响，在两种语言下查看生成的图像。
5. 记录改进了什么、还有哪些不确定。

## 具体检查与错误指南报告

激活开发环境后，make check 会运行测试、生成器、翻译检查、私有内容检查、打包验证和站点构建。可单独运行：

    python -m pytest -q
    python tools/build_selection.py --check
    python tools/i18n_check.py
    python tools/lint_private.py --strict --history
    npm run check

不要为发布而关闭失败的检查。报告错误或歧义时，请提供类型代码、读者与问题、冲突原文、主要来源链接及最小修正建议。使用通用复现，通过仓库问题追踪器或维护者提交；不要附加私人架构图。

## 内容单一来源

详细的类型指南位于 content/en/types；简短的 skill 参考由其中选定的章节生成。不要手工编辑生成的副本。每个类型页面都保持稳定的章节 ID：meaning、choose、notation、practice、exemplars、recipe、evidence、questions、template、sources 和 sample。

## 来源、隐私与许可

不得包含客户记录、私有路径、凭据、会议记录或复制的专有图。链接到业界示例；复用图稿前请核对该素材的具体许可。代码、文档和原创示例采用 Apache-2.0；第三方材料沿用其自身条款。

## 翻译

英文为权威版本。中文页面镜像相同的路径和章节 ID，并带有 translationOf、sourceRev 和 reviewed 元数据。机器初稿要标记为审校中。应针对本地化标签重新布局，而不是假定英文的几何布局适合中文。

## 贡献协议

贡献采用 Developer Certificate of Origin（DCO），而非 CLA。请使用 git commit -s，以你真实的贡献身份签署提交。审查流程请阅读仓库中的 CONTRIBUTING 文档。

下一步：[评估改动](./evals)。
