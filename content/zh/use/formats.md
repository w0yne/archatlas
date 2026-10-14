---
title: 格式与故障排查
translationOf: en/use/formats.md
sourceRev: 9b3455f1532fa425f2412c0a4c828c086dae8092
reviewed: false
---
# 格式与故障排查

## 初始格式

当前渲染器从模型 JSON 生成 **保留可编辑文字的 SVG**。两者都要保留：渲染不会把源模型复制进输出目录。简单 HTML 外壳通过 Python exporter API 提供，没有 HTML CLI 命令。

**尚未承诺：** draw.io 导出、可编辑的 PowerPoint 导出、无损导入或往返编辑。在幻灯片中嵌入一张 SVG 图片，并不等同于原生可编辑的形状。

## 渲染与检查

在已审阅的克隆仓库中，`make setup` 安装开发及站点依赖，之后激活 `.venv`。如果只使用渲染器，创建并激活虚拟环境，然后在克隆根目录执行 `python -m pip install -e .`。项目尚未发布包，不要从 PyPI 安装同名包。

```sh
atlas init C2 -o model.json
atlas render model.json -o out/ --lang en --profile doc
atlas check out/diagram.svg --model model.json --lang en --fail-on warning --report out/findings.json
atlas fonts doctor
```

`init` 接受已提供的类型码或布局族，`--templates DIR` 可指定另一个模板目录。初始化会解析默认语言标签。`render` 写入 `out/diagram.svg` 和 `out/diagram.findings.json`；指定 SVG 文件名时，会生成同名 `.findings.json`。`check --lang` 核对 SVG 的语言，并按该语言加载模型标签，不会翻译已有 SVG。

需要 PNG、联系表或真实浏览器几何检查时，在克隆仓库中安装可选依赖：

```sh
python -m pip install -e '.[preview,browser]'
python -m playwright install chromium
atlas preview out/diagram.svg -o out/preview.png --scale 1
atlas sheet out/*.svg -o out/sheet.jpg
atlas check out/diagram.svg --model model.json --lang en --browser --report out/browser.findings.json
```

preview/sheet 使用 CairoSVG 和系统 Cairo；浏览器检查使用 Playwright、Chromium 及其平台库。浏览器检查阻断网络请求，在字体就绪后测量实际边界，但不证明语义或视觉质量正确。字体子集嵌入尚未实现。

退出码 **0** 表示通过所选阈值；默认 `--fail-on error` 下仍可能有警告。**1** 表示发现达到阈值的问题，**2** 表示输入、工具或依赖错误。`render` 可能先写出 SVG 再返回 1。报告列出问题、级别、元素 ID 和边界。应修改模型、重新渲染、检查新 SVG，再进行视觉复核。逐元素的 `allow` 理由不会消除错误，也不会改变失败阈值。

Schema 0.1 还支持作者编写及本地化的图例（`meta.legend`、`legend_mode`、`legend_labels`）、表格配小图、最小流程 rank 和可配置的 `layout.spacing`。参与者/用例图形及 BPMN 开始/结束事件边框已可用；process/dataset/job/pipeline 等描述性 kind 仍是普通卡片。泳道、状态、树图排名具有确定性，但属于启发式布局，不代表完整形式化记法。

## 缺少字体或中文字形

用 `atlas fonts doctor` 查看选用字体与 CJK 探针覆盖。`measured_with: estimate` 表示部分测量使用了保守估算，应如实说明。探针不代表全部 Unicode 覆盖，SVG 的可编辑文字也仍依赖查看环境的字体。仅设置 `--lang zh` 不会翻译英文常量：应提供翻译 key 和 `labels.zh.json`，再重新渲染。不要靠缩小所有标签解决裁切。

## 没有浏览器或不支持图像输入

文本检查和几何检查仍可运行。在支持时生成预览，交给人工或能读图的审阅者。报告**视觉复核待做**，绝不能仅凭命令执行成功就声称视觉检查通过。

## 图过于密集

回到读者的问题。折叠非重点细节，或把不同关注点拆分到不同视图中。`slide` 保持 1440×810 并报告溢出；`doc` 首选 1120px，可按内容增长，宽图警告阈值可配置。两者都不会自动分页。保留可查看的全尺寸图片，而不是让标签在小屏幕上无法辨认。
