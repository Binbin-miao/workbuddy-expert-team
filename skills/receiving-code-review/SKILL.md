---
name: receiving-code-review
description: "Evaluates code review feedback with technical rigor rather than blind compliance, verifying reviewer claims against callers, specs, and code elegance."
---

# /receiving-code-review — 科学对待代码审查反馈（技术实证优先，拒绝盲从）

源自 `obra/superpowers`（`skills/receiving-code-review`）与 `addyosmani/agent-skills`：

## 处理审查意见的四步准则
1. **结合调用链核实（Verify Against Callers & Guards）**：收到审查意见时，先检查目标代码及其全部上下游调用方与外围守卫条件，判断问题是否真实成立。
2. **分类裁决（Fix Root Cause vs. Push Back with Evidence）**：
   - **确属缺陷或优雅度提升** → 在共享根因处实施修复，并补充回归测试。
   - **误报、破坏模块封装、或为了压行数损害可读性** → 摆出具体的文件行号、调用链证据或 `/code-elegance` 条款礼貌反驳，交由主理官裁决，绝不盲从把代码改丑或改坏。
3. **逐项修复并独立重跑验证**：修完后必须重跑全套门禁测试。
