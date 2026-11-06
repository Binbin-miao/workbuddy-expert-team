---
name: codebase-design
description: "Applies 'A Philosophy of Software Design': builds Deep Modules with simple interfaces, hides complexity, and defines errors out of existence."
---

# /codebase-design — 深模块软件设计法则

## 核心原则
1. **深模块（Deep Modules）**：接口极简稳定，内部封装复杂实现；坚决消灭只做参数转发的浅模块（Shallow Wrappers）。
2. **清晰接缝（Seams）**：将核心业务计算与外部 I/O 隔离在模块边界，使核心测试无需脆弱 Mock。
3. **定义错误出局（Define Errors Out of Existence）**：在模块内部吸收并优雅处理常规边界条件。
