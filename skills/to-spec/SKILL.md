---
name: to-spec
description: "Crystallizes grilling decisions and domain models into a comprehensive, verifiable technical specification."
---

# /to-spec — 技术规格书生成规范

## 标准章节结构
1. **Goals & Non-Goals**：明确本次交付范围与不做事项。
2. **Ubiquitous Language & ADRs**：关联 `GLOSSARY.md` 术语与 `docs/adr/` 决策。
3. **Deep Module Interfaces**：模块公开签名（极简）、内部隐藏职责、外部依赖接缝（Seams）。
4. **Data Schema & State Machine**：数据结构、持久化契约与全状态跃迁。
5. **UI/UX States & Edge Cases**：六大交互状态（Loading/Empty/Error/Success/Disabled/Permission）与异常降级。
6. **Verification & TDD Plan**：关键 Red-Green 测试断言列表与验收命令。
