---
name: prototype
description: "Builds fast, disposable exploratory prototypes to validate UI flows, state machines, or technical feasibility."
---

# /prototype — 快速验证原型构建

## 原型纪律
1. **明确待验证问题**：专为回答某个特定交互体验、布局表现或技术可行性而建。
2. **隔离与交接**：原型代码不冒充生产代码；验证得出结论后，通过 `/handoff` 将提炼出的设计结论交回 TDD 生产实现。
