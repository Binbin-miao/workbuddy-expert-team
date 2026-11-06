---
name: domain-modeling
description: "Extracts Ubiquitous Language, aligns domain entities and invariants, and maintains GLOSSARY.md."
---

# /domain-modeling — 领域建模与统一语言提炼

## 执行法则
1. **识别隐性概念**：消除需求与代码中的“同义不同名”和“同名不同义”。
2. **定义不变量（Invariants）**：明确核心实体、值对象、聚合根与合法状态跃迁边界。
3. **同步 `GLOSSARY.md`**：确保文档、类名、函数名、数据库字段与测试断言使用完全一致的领域词汇。
