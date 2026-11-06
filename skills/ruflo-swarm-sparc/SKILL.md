---
name: ruflo-swarm-sparc
description: "Integrates ruvnet/ruflo (Claude Flow), GSD, BMAD-Method, MetaGPT, ECC, and GitHub Spec Kit orchestration rules: Mission Proposal Gate, Resource Claims Board, SPARC workflow, Anti-Context-Rot, and 4-Step Project Memory."
---

# /ruflo-swarm-sparc — 多源开源框架融合调度协议（Ruflo + GSD + BMAD + MetaGPT + ECC + Spec-Kit）

本技能浓缩了 GitHub 六大主流多 Agent 工程框架的核心机制，适用于任何编程语言与项目类型：

## 一、 智能分级与「先报方案卡再开工」门禁（Ruflo Mission Proposal + BMAD Right-Sized Process）
1. **Tier 0（单兵直通，免确认、免派子代理）**：
   - 触发条件：纯查询问答、简单环境操作、或单文件 ≤20 行的明确微调（[GSD #1979](https://github.com/gsd-build/get-shit-done/issues/1979) 内联执行原则）。
   - 行为：主理官直接查证、执行并实测汇报，零多 Agent 调度开销。
2. **Tier 1~3（提案先行门禁：Proposals, Not Orders）**：
   - 触发条件：凡涉及**新功能开发、修改 ≥2 个文件、架构/存储/状态变更、或存在多种技术实现路径**。
   - 行为：主理官严禁盲目直接改代码！必须先完成「本地代码静默扫描 + 外部优秀开源项目检索（新功能/选型时）」，然后向用户输出一张结构清晰的 **《任务理解与开工方案卡（Mission Proposal Card）》**：
     - **🎯 转化后的工程目标**（将用户的大白话转化为明确的功能、边界与隐性防呆需求）；
     - **🔍 现成开源项目/原生方案参考**（列出搜到的 1~3 个高星开源项目、成熟库或项目内既有组件）；
     - **⚖️ 关键设计取舍与推荐项**（1~2 个核心决策点，附优劣对比与明确推荐项）；
     - **🤝 拟派专家、文件独占锁（Resource Claims）与验证计划**。
   - **放行条件**：收到用户确认（如“可以”、“按推荐开始”）后，立即派发专家高效执行。

## 二、 SPARC 五阶段研发流水线与渐进式上下文交接（Ruflo SPARC + MetaGPT SOP + BMAD Handoff）
1. **S — Specification（需求解码与边界锁定）**：主理官解码用户大白话，补齐隐性体验需求（耗时操作进度提示、防并发重入互斥锁、向后兼容、一键式操作）。
2. **P — Prior-Art & Pseudocode（开源对标与最小原型设计）**：浮光检索 GitHub 同类优秀开源实现与官方文档，提炼可直接复用的组件与避坑清单。
3. **A — Architecture & Call-Graph Matrix（全调用链建模与规格拆票）**：跨模块/多文件任务由璇玑扫描全仓所有读、写、删、分页与定时任务调用点，输出《全调用点接线核对表》与曳光弹工单。
4. **R — Refinement（TDD 深模块与优雅代码实现）**：巧夺与玲珑在独立文件锁（Claims）保护下按 `/code-elegance` 与 `/tdd` 实现，澄澈按 `>80% 置信度` 门槛做安全与精简审查。
5. **C — Completion（实证门禁与杂志级文档交付）**：跑通全部测试与构建门禁，输出结构化交付卡，并为新模块或架构改造自动生成独立 `.md` 接线指南。

## 三、 资源独占锁（Ruflo Resource Claims Board）与防上下文腐烂（GSD Anti-Context-Rot）
- **文件写锁（One Owner Per Resource）**：并行派发多个子专家时，主理官必须在委派提示词中明确每个专家独占修改的文件列表；严禁两个活跃子专家同时写同一个文件。只读审查员（Reviewer / Verifier）严格禁止修改任何文件。
- **主理官极薄上下文（Thin Orchestrator）**：主理官不把成千上万行源码读进自己的主会话，而是将文件检索、全调用链扫描和重度编码委派给拥有独立 200k 干净上下文的子专家，彻底避免长会话上下文腐烂（Context Rot）。

## 四、 四步项目记忆蒸馏（Ruflo 4-Step Intelligence Pipeline）
- **RETRIEVE（检索）** → **JUDGE（评估有效性）** → **DISTILL（提炼通用模式）** → **CONSOLIDATE（固化至当前项目 `GLOSSARY.md` / `docs/adr/` / `.scratch/`）**，让当前项目越用越聪明，同时保持专家团自身提示词 100% 纯净通用。
