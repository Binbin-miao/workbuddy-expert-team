---
name: ponytail-audit
description: "Full-repository read-only audit mapping entrypoints, data flows, high-cost failure risks, and removable over-engineering."
---

# /ponytail-audit — 全仓架构减肥与高危路径审计

## 执行步骤
1. 扫描入口与核心数据流，优先深挖资金、鉴权、写入与跨进程状态。
2. 全树检索确认零引用后，标记可删除的僵尸代码、多余抽象层与可替换为原生方案的冗余依赖（最多输出最关键 20 项）。
