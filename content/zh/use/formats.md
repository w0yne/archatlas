---
title: 命令、格式与限制
translationOf: en/use/formats.md
sourceRev: bca58c9299c22a5a05f98bf81e38393e6e1d1713
reviewed: true
---
# 命令、格式与限制

仓库中的 SVG 渲染器已经可用。请从审阅过的克隆运行 make setup 或 python -m pip install -e .；本项目尚未发布 PyPI 包。[安装说明](./index)区分源码与打包文件两种方式。

## 先选择，再渲染

[不确定该画哪种图？先选择视图。](/zh/choose) 同一个渲染器可以支持不同视图，但布局不能替你决定架构的含义。

## 可用命令

在已经激活的源码环境中运行：

    atlas init C2 -o model.json
    atlas render model.json -o out/
    atlas check out/diagram.svg --model model.json --report out/findings.json
    atlas fonts doctor

render 会写入 diagram.svg 和 diagram.findings.json；显式 check 会写入指定的 findings.json。逐项检查严重级别、规则、元素 ID、边界框和说明。退出码：**0** 没有达到失败阈值的发现；**1** 有达到阈值的发现（默认阈值为 error）；**2** 工具错误。warning 仍需要复核。

## 可选图片与浏览器检查

从源码安装 CairoSVG 预览依赖，即可生成 PNG 和联系表：

    python -m pip install -e '.[preview]'
    atlas preview out/diagram.svg -o out/preview.png
    atlas sheet out/diagram.svg -o out/sheet.jpg

CairoSVG 可能需要系统 Cairo 库。使用解压包时，安装 scripts/requirements.txt 注明的可选 CairoSVG 版本。浏览器检查还需要 browser 额外依赖与 Chromium；工具能运行不等于已经做过视觉复核。

## 字体与检查结果

使用 fonts doctor 查看字体与中文字符覆盖。报告中的 **measured_with: estimate** 表示采用了估算，不是用目标字体验证过文字适配。应调整换行、布局和字体，而不是把全部字缩小；修改后查看最终图片。

## 输出支持与限制

SVG 保留可编辑文字，模型 JSON 是源文件。原生 draw.io/PPTX 导出及无损往返尚未实现。HTML 导出目前是库接口，不是 CLI 子命令。字体子集嵌入尚未实现。请用 atlas --help 核对当前版本，不要假定规划中的参数已经可用。

## 没有图像输入能力时

运行可用的自动检查，条件允许时生成预览，并交给人工或支持图像的模型检查。在此之前标明**视觉复核待做**。构建成功不能证明图表达了正确含义。
