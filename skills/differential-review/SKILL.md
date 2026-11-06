---
name: differential-review
description: "Performs Trail of Bits security-focused differential review of code changes with ECC >80% confidence filtering, calculating blast radius and checking git blame context."
---

# /differential-review — 差分安全审计、爆炸半径计算与高置信度过滤

融合 `trailofbits/skills`（`differential-review`）与 `affaan-m/ECC`（`>80% Confidence Filtering`）：

## 核心审计四步法

### 1. 历史上下文溯源（Git Blame & Chesterton's Fence）
- 审查被修改或被删除的条件判断、权限校验、锁或输入清洗逻辑时，先查明原代码当初是为了防御什么问题而写的，防止因不了解背景而误拆安全护栏。

### 2. 爆炸半径计算（Blast Radius Calculation）
- 统计本次变更触及的函数/模块被多少上游入口调用，标注是否跨越**信任边界（Trust Boundary）**、是否涉及鉴权/加密/资金/数据库迁移/并发共享状态，据此动态调配审计深度。

### 3. 高危缺陷与并发漏洞猎杀（Vulnerability & Concurrency Hunting）
- **注入与越权**：SQL/命令注入、SSRF、路径穿越、水平/垂直越权（IDOR）、缺失多租户隔离。
- **状态与并发竞态**：Check-Then-Act（TOCTOU）竞态、重放风险、异步写入队列未捕获异常导致的队列永久中毒（Promise Queue Poisoning）、非原子多步写入导致的崩溃孤儿数据。
- **分批饥饿与死循环**：检查分页或批量任务是否存在游标未推进或固定切片导致的队列尾部饥饿（Starvation）。

### 4. >80% 置信度过滤（ECC Confidence Filter — 拒绝噪音）
- **只报告 >80% 确信会引发真实 Bug、安全漏洞、数据损坏、性能退化或严重破坏可维护性的问题**。
- 每个 Finding 必须附带**具体的触发输入/并发时序反例**与**最小优雅修复方案**；合并同类问题，绝不拿主观代码风格偏好凑数。
