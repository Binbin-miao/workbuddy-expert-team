---
name: tdd
description: "Enforces strict Red-Green-Refactor Test-Driven Development one vertical slice at a time."
---

# /tdd — 红-绿-重构测试驱动开发纪律

## 三步循环铁律
1. **Red（红）**：先写一个针对公开接口行为的自动化测试，运行并亲眼确认它因目标行为缺失而失败。
2. **Green（绿）**：编写刚好能让测试通过的最少生产代码，不提前过度抽象。
3. **Refactor（重构）**：在测试全绿保护下消除重复、深化模块封装，重构后立即重跑测试确认全绿。
