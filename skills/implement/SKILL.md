---
name: implement
description: "Implements a clear feature or single ticket end-to-end using Deep Modules, Red-Green-Refactor TDD, and Dual-Axis Review."
---

# /implement — 端到端精益实现流水线

## 标准步骤
1. 读取上下文、现有可复用代码（Ponytail 决策阶梯）与真实样本 Fixture。
2. 遵循 `/codebase-design` 设计深模块接口与清晰测试接缝。
3. 执行 `/tdd` 循环：Red（写失败测试） → Green（最小实现） → Refactor（测试保护下深化重构）。
4. 运行全量测试与静态检查，执行 `/code-review` 双轴自检后交付。
