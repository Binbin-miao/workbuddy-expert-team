---
name: audit-context-building
description: "Builds deep entry-to-sink security context, detects insecure defaults and API sharp edges, and performs variant analysis across the codebase."
---

# /audit-context-building — 深度审计上下文构建、Sharp Edges 与全仓变体分析

源自 `trailofbits/skills`（融合 `audit-context-building`、`insecure-defaults`、`sharp-edges` 与 `variant-analysis`）：

## 核心方法论
1. **端到端数据流建模（Source-to-Sink Mapping）**：绘制从不可信输入源（Sources）到敏感操作汇点（Sinks：数据库写入、命令执行、外部请求、权限变更）的完整调用图。
2. **默认安全（Fail-Closed Defaults）与 Sharp Edges 检测**：
   - 当环境变量缺失、鉴权异常或配置解析失败时，系统必须默认拒绝访问（Fail-Closed），严禁回退至弱默认密钥或放行状态（Fail-Open）。
   - 拦截危险 API 误用（如弱随机数生成令牌、非恒定时间签名比对、静默吞掉异常的空 catch）。
3. **全仓变体分析（Variant Analysis — 捉一挖十）**：
   - 一旦在某处发现真实 Bug 或安全缺陷，立即提炼其代码特征并在全仓检索同类变体，一次性彻底根除。
