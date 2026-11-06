---
name: triage
description: "Triages incoming issues or bugs, classifies severity and root domain, and routes to the right workflow."
---

# /triage — 问题分诊与优先级判定

## 分诊流程
1. **复现与取证**：结合代码库定位问题所属模块、影响范围与严重级别（P0 阻断 / P1 严重 / P2 一般 / P3 建议）。
2. **路由判定**：明确小 Bug 直接走 `/diagnosing-bugs` + `/tdd` 修复；涉及需求变更或跨模块架构问题则转入 Grill 与 Spec 流程。
