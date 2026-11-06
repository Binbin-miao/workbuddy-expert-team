---
name: grill-me
description: "Relentlessly interviews the user to walk down every branch of the design tree until shared understanding is reached."
---

# /grill-me — 深度需求压力访谈（无代码库或纯设计阶段适用）

## 执行法则
1. **遍历设计决策树**：不放过任何关键边界条件（目标受众、核心用例、数据流、异常恢复、权限边界、非目标范围）。
2. **高信噪比交互**：每次提问给出具体候选方案与推荐理由，支持用户用简短指令（如“按推荐”、“1A 2B”）快速拍板。
3. **停止条件**：当且仅当所有影响架构与用户体验的关键分支全部闭合时停止提问，并给出清晰的拍板结论汇总与文档化建议。
