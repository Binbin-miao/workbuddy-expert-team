---
name: prior-art-research
description: "Proactively searches GitHub repositories, open-source ecosystems, and reference products to extract proven architectures, native components, and pitfalls before building from scratch."
---

# /prior-art-research — 开源优秀项目与现成方案对标检索（拒绝闭门造车）

融合 `FoundationAgents/MetaGPT` 的竞品/先例分析与 `gsd-build/get-shit-done` 的四维前置调研（Stack / Features / Architecture / Pitfalls）：

## 一、 触发规则（1A + 2A 标准）
1. **必触发场景**：凡是**从零开发新功能/新插件/新工具/新网页、技术选型、跨模块存储/架构改造、对接第三方框架/SDK、或产品横向对比**，必须在写代码前先执行本检索！
2. **免触发场景**：纯修复本地既有代码的明确内部小 Bug，或单文件 ≤20 行的简单配置微调，直接查本地代码即可，无需浪费时间搜外部网页。

## 二、 四维深潜检索法（Search → Inspect Source → Extract Pattern → Adapt）

### 1. 多源精准检索（超越表面网页摘要）
- **GitHub 仓库与源码检索**：
  - 使用搜索工具查询 `<技术栈/框架> <功能关键词> github`、`site:github.com "<核心接口或事件名>"`。
  - 通过 GitHub REST API 或网页抓取直接检视高星开源项目的目录结构、核心源码文件、最新 Release Notes 与高赞 Issues：
    - `https://api.github.com/search/repositories?q=<keywords>&sort=stars&order=desc`
    - `https://api.github.com/repos/<owner>/<repo>/contents/<path>`
- **当前框架/生态原生能力排查**：
  - 检索目标框架或宿主环境是否已经内置了现成组件、工具类或已安装的依赖库（遵循 Ponytail 阶梯：有原生组件绝不手搓劣质替代品）。

### 2. 四维提炼产出（GSD 4-Dimension Synthesis）
将检索结果浓缩为 20 行以内的《开源对标简报》，直接供《开工方案卡》与架构设计使用：
- **Stack & Native Components（现成组件/库）**：有哪些开箱即用的原生组件或成熟库？
- **Features & UX Patterns（交互与功能标杆）**：优秀同类项目有哪些贴心的交互细节？
- **Architecture & Data Flow（架构与数据结构借鉴）**：它们如何组织状态、存储与扩展接口？
- **Pitfalls & Edge Cases（前人踩过的坑）**：Issues 或源码注释里揭示了哪些容易踩中的平台限制或兼容性陷阱？
