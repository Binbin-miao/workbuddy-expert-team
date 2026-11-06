---
name: to-tickets
description: "Breaks a specification into end-to-end Tracer-Bullet vertical slice tickets with explicit Blocking Edges."
---

# /to-tickets — 曳光弹垂直切片工单拆解

## 核心铁律
1. **垂直切片（Vertical Slices）优于水平分层**：严禁按“先写全部数据库、再写全部后端、再写全部前端”拆分！每张工单必须端到端打通一个可独立运行验证的窄业务切片。
2. **显式依赖边（Blocking Edges）**：每张工单标明 `Blocked By` 与 `Blocks`，并计算出当前可立即开工的 **Ready Frontier**。
3. **自包含验收标准**：每张工单写明改动边界、TDD 行为断言与验收命令。
