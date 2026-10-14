# 贡献指南

[English](CONTRIBUTING.md)

## 范围

优先提交能解决重复问题的小改动。提出图、规则或渲染功能前，先说明读者和问题。
不要将客户资料、私有路径、凭据或私人对话带入仓库。

## 来源与许可

原创通用示例。业界样例用链接，不直接复制图片。导入代码、字体或图标前检查其
实际许可，并保留署名。对项目原创材料的贡献使用 Apache-2.0。

## 内容与翻译

英文类型页是权威来源，不手改自动生成的 skill 引用。保留站点规定的章节 ID。
中文镜像使用相同路径和 ID，并记录 translationOf、sourceRev 和 reviewed；
未审稿件须明确标注。

## 开发环境

需要 Python 3.10+、Node（版本见 `.nvmrc`）和 GNU Make。在新克隆的仓库里运行：

```sh
make setup    # python3 -m venv .venv && pip install -e '.[dev]' && npm run site:install
make check    # 运行 CI 中的全部检查
```

`make check` 依次运行以下检查，CI 运行的也是这条命令：

1. 单元、几何、golden 和评测工具测试（`pytest`）；
2. 生成器检查（`build_selection`、`build_skill_refs`、`build_samples`，都带 `--check`）；
3. 翻译检查（`i18n_check`）；
4. 私有内容扫描，覆盖文件和全部历史（`lint_private --strict --history`）；
5. 打包 skill zip 并验证能否安装（`pack_skill --verify`）；
6. 站点检查与构建（`npm run check`、`npm run build`）。

也可以单独运行某一步：`make test`、`make generated`、`make i18n`、`make lint`、`make pack`、`make site`。

可选设置：
- **私有词表：**设置 `ARCHATLAS_PRIVATE_NAMES_FILE`，指向放在仓库外的词表。
- **发布构建：**使用 `make check I18N_FLAGS=--release`，过期的翻译会报错。
- **字体：**如需用真实字体测量文字，请安装 Noto Sans 和 Noto Sans CJK。

## 验证

检查受影响的图和页面在桌面端和手机端的效果。几何检查不能证明含义正确，也不能代表视觉效果。提交时请写明输入、预期行为、证据和剩余限制。收费的跨智能体评测只在可信的手动任务中运行。

## 开发者原创声明

签署提交表示你按 [DCO 1.1](https://developercertificate.org/) 认证贡献来源。
使用真实贡献身份运行 git commit -s；不要求 CLA。不要替别人签署，也不要提交
私人对话作为评测证据。

## 评审

维护者检查含义、来源、许可、可访问性和测试。请说明改动涉及安装、目录语义、
渲染结果还是翻译，并遵守 CODE_OF_CONDUCT.md 与 SECURITY.md。
