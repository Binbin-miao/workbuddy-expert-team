---
name: ask-matt
description: "Routes engineering tasks to the right Matt Pocock workflow skill based on complexity, ambiguity, and current state."
---

# /ask-matt — 工程工作流智能路由指南

## 核心路由决策树
1. **需求存在模糊分支或跨模块权衡** → 先走 `/grill-with-docs`（无本地代码库时走 `/grill-me`）。
2. **需要梳理复杂业务概念与术语** → 走 `/domain-modeling` 更新 `GLOSSARY.md` 与 `docs/adr/`。
3. **需要将达成共识的方案固化为技术文档**：
   - 单次会话可完成的清晰任务 → 直接走 `/implement`（内置 `/tdd` + `/code-review`）。
   - 复杂/跨阶段/多模块工程 → 依次走 `/to-spec` 生成规格书 → `/to-tickets` 拆解曳光弹垂直切片工单 → `/implement-spec`。
4. **遇到疑难 Bug、偶发故障或性能退化** → 走 `/diagnosing-bugs`（复现 → 假设 → 埋点证伪 → 修复并补回归测试）。
5. **需要验证 UI 交互或状态机可行性** → 走 `/prototype` 构建一次性验证原型，再通过 `/handoff` 带回结论。
6. **存量代码库肥胖或模块浅化** → 走 `/improve-codebase-architecture` 寻找深模块（Deep Modules）合并机会。
7. **任务收尾与交付** → 走 `/code-review`（双轴审查） → `/pr`（单双向门分析） → `/retro`（沉淀规则至 `AGENTS.md`）。
