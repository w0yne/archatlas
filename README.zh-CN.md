# archatlas

[English](README.md)

**选对架构视图，以证据绘图。**

archatlas 将架构图类型指南与名为 architecture-diagrams 的英文 Agent Skill 放在一起。文档以英文为主，中文镜像正在完善。

## 状态

目前为预发布阶段。站点骨架可以构建；完整目录内容、渲染器接入、skill 打包和跨代理评测仍在独立推进。不宣称已有公开软件包、生产就绪或完整中文覆盖。

## 能做什么

- 按读者和问题选择视图。
- 根据描述绘图，先看文字线框再渲染。
- 不执行仓库代码，以源码证据推导架构图。
- 分别检查几何布局、表达含义与实际图片。

初期目标是 SVG 与模型 JSON。draw.io/PowerPoint 原生导出及无损往返编辑尚未承诺。

## 安装 skill

从完整且经过审阅的源码或发布包中，把 architecture-diagrams 文件夹复制到**一个**发现目录：

| 代理 | 个人目录 | 显式调用 |
|---|---|---|
| Claude Code | ~/.claude/skills/architecture-diagrams/ | /architecture-diagrams |
| Codex | ~/.agents/skills/architecture-diagrams/ | $architecture-diagrams |
| Pi | ~/.pi/agent/skills/architecture-diagrams/ | /skill:architecture-diagrams |

授予执行权限前先检查脚本。安装后重启代理，Pi 也可使用 /reload。保留整个文件夹，不要只复制 SKILL.md。参阅[安装与首次使用（英文）](content/en/use/index.md)。

## 模式

**自主模式：**选择合理默认值并说明假设；缺失事实会改变含义时仍应提问。**引导模式：**逐步确认重要选择，先批准线框再渲染。未回答不等于同意。参阅[模式说明（英文）](content/en/use/modes.md)。

## 开发站点

使用 .nvmrc 指定的 Node 版本，然后运行：

    npm run site:install
    npm run check
    npm run build
    npm run site:preview

仅用于站点的 package 与锁文件位于 content/.vitepress，根目录命令委托至该目录；安装命令在那里运行 npm ci。Python/skill 用户不需要站点依赖。构建输出 content/.vitepress/dist 已被忽略。

构建后可运行 npm run preview:static --prefix content/.vitepress，生成不含脚本的阅读版，输出在忽略目录 dist/static-preview。该导出使用扁平页面路径，不含搜索和弹窗；正常站点构建仍保留这些交互。

中文镜像尚未完整时，语言菜单返回对应语言首页。默认基路径为 /archatlas/。其他仓库名或托管路径可设置 SITE_BASE。content/en 的页面重写为根路径，中文保留 /zh/。目录和侧栏读取 content/data/types.yaml；其尚不存在时使用明确标注的三项小样。没有正文的类型页不会产生无效链接。

骨架使用 VitePress 1.6.4。依赖审计目前报告上游开发服务器漏洞；开发/预览只在本机运行，不向不可信网络开放，公开发布前须复核升级。Pages 只部署静态文件，不运行 Vite 开发服务器。

## 兼容性与限制

文档和帮助信息研究覆盖 Claude Code 2.1.285、Codex 0.160.1、Pi 1.1.0；真正的安装冒烟测试和输出质量评测仍**待做**。构建成功不代表视觉复核完成。没有图像输入能力时，应明确视觉待复核并交给合适的评审者。

## 贡献与许可

参阅[贡献指南](CONTRIBUTING.zh-CN.md)、[社区准则](CODE_OF_CONDUCT.md)和[安全报告](SECURITY.md)。贡献使用 DCO 签署，不要求 CLA。原创代码、指令、文档和样例采用 Apache-2.0；第三方材料保留各自许可。只使用通用示例，不加入机密内容或私有路径。
