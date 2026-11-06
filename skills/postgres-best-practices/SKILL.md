---
name: postgres-best-practices
description: "Enforces Supabase and Neon Postgres 8-category best practices covering schema design, zero-downtime migrations, RLS security, indexing, EXPLAIN query plans, and pooling."
---

# /postgres-best-practices — 数据库 Schema、零停机迁移、RLS 安全与慢查询优化手册

融合 `supabase/agent-skills` 与 `neondatabase/postgres-skills`，适用于 PostgreSQL 及各类关系型数据库：

## 八大数据库工程铁律
1. **精确类型与约束**：时间统一用 `timestamptz`；金额用 `numeric` 或整数最小货币单位；主键优先 `bigint identity` 或 `UUIDv7`。
2. **零停机安全迁移**：大表建索引使用 `CONCURRENTLY`；分步新增非空约束（`NOT VALID` → `VALIDATE`）；迁移设置 `lock_timeout`。
3. **多租户隔离与 RLS 测试**：多租户表强制校验租户边界，并编写跨租户越权访问被拒绝的反向回归测试。
4. **外键与复合索引**：所有外键列必须建索引；复合索引遵循“等值列在前、范围/排序列在后”，高频过滤使用 Partial Index。
5. **消灭 N+1 与深分页慢查询**：严禁循环内查库；大数据集分页采用基于游标的 Keyset Pagination 取代大 `OFFSET`；结合 `EXPLAIN (ANALYZE, BUFFERS)` 实测优化。
6. **短事务原则**：严禁在数据库事务块内发起外部 HTTP 请求、文件上传或大模型调用。
7. **并发原子写入**：状态流转或扣减采用原子条件更新或 `FOR UPDATE SKIP LOCKED`；幂等写入采用 `ON CONFLICT`。
8. **向量与队列扩展**：合理配置 `pgvector` HNSW 索引与队列消费幂等性。
