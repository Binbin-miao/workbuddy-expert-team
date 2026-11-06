---
name: dispatching-parallel-agents
description: "Autonomous Wave-Based Parallel Multi-Agent Orchestration (synthesizing obra/superpowers dispatching-parallel-agents, GSD wave execution, LangGraph fan-out/fan-in supersteps, and Ruflo resource claims). Automatically spawns concurrent subagents across orthogonal domains without user prompting."
---

# /dispatching-parallel-agents — 自主波次并发调度与多实例交叉验证协议

融合 `obra/superpowers`（`dispatching-parallel-agents` & `subagent-driven-development`）、`gsd-build/get-shit-done`（Wave-Based Parallel Execution）、`LangGraph`（Fan-Out / Fan-In Supersteps & Reducers）与 `ruvnet/ruflo`（Resource Claims Board）：

## 一、 核心原则：无需用户催促，主理官按任务矩阵自主并发（Autonomous Fan-Out）

主理官（天枢）**严禁被动等待用户输入“积极调用你的团队成员”或“用多个 Agent 交叉验证”**！收到任务后，自动按以下决策矩阵决定单兵还是并发扇出（Fan-Out）：

| 任务特征 | 调度模式 | 并发行为规范 |
|----------|----------|--------------|
| **Tier 0：微任务**<br>纯问答、单条简单命令、单文件 ≤20 行明确微调 | **单兵内联直通（0 子代理）** | 主理官直接完成并实测交付，避免为小事拉起多 Agent 的通信延迟 |
| **Tier 1~3：审查仓库 / 排查复杂 Bug / 性能优化 / 新功能开发 / 跨模块改造** | **强制三波次自主并发（Multi-Wave Fan-Out）** | 主理官**必须在同一回复回合内同时发出多个 `Agent` 工具调用**，让多个子专家在各自干净的上下文窗口中真正并行工作 |

---

## 二、 三波次并发执行架构与同步屏障（3-Wave Execution & Barriers）

```text
[Wave 1: 并行只读侦察波 (2~5 个并发 Agent 同回合发出)]
  ├─► 浮光 (WEB 对标检索)：外部开源方案、上游仓库差异、官方文档/API 取证（只读，禁跑编译）
  ├─► 璇玑 (GRILL 领域建模)：全仓读写/删除/分页调用链扫描、并发锁与崩溃原子性建模（只读，禁跑编译）
  ├─► 澄澈 (LEAN 极简代码)：安全爆炸半径、静默吞错、性能热点与版本差分回归审计（只读，禁跑编译）
  ├─► 玲珑 (UI/UX 审美总监)：[含界面时] 组件状态生命周期、异步监听器泄漏与可访问性审查（只读，禁跑编译）
  └─► 巧夺 (TDD 深模块研发)：【唯一门禁实跑员】执行编译/类型检查/测试套件，猎捕实现级 Bug
        │
        ▼ ════════════ [Wave Barrier 1：全员回传收齐 → 主理官天枢汇总对账] ════════════
  [向用户呈交《任务理解与开工方案卡》──► 等待用户拍板确认]
        │
        ▼ ════════════ [Wave Barrier 2：用户确认放行] ════════════════════════════════
[Wave 2: 按模块独占写锁并行实现波 (1~3 个并发 Agent，按目录正交切分)]
  ├─► 巧夺-Core：独占修改后端核心模块目录（Resource Claim A）
  ├─► 玲珑-UI：独占修改前端组件与交互层目录（Resource Claim B）
  └─► 巧夺-Host：独占修改宿主适配/CLI/路由接线层（Resource Claim C）
        │
        ▼ ════════════ [Wave Barrier 3：实现全部收口] ════════════════════════════════
[Wave 3: 同角色多实例双盲交叉验证波 (2~3 个并发只读 Verifier 同回合发出)]
  ├─► 澄澈-Reviewer：静态差分审查 git diff（>80% 置信度过滤，禁跑重型编译）
  ├─► 巧夺-Verifier-A：【唯一门禁复跑员】从干净状态重跑全套编译、测试与静态检查门禁
  └─► 巧夺-Verifier-B：测试真实性与对抗/变异验证（强制在 /tmp 或独立 Worktree 中进行，严禁污染主工作树！）
```

---

## 三、 并发调度的五条防踩踏铁律（Five Anti-Chaos Rules）

1. **同一回合扇出（Single-Turn Fan-Out）**：凡属同一波次且互不依赖的子任务，必须在**同一个模型回复回合中同时发出多个 `Agent` 调用**，绝不一个接一个串行等待。
2. **编译锁单点化（Single Gate-Runner Discipline）**：在 Rust（`cargo`）、C++、Go、Java 或大型前端工程中，多个子 Agent 同时运行编译/构建会争抢编译目录锁导致长达数十分钟的挂起！因此同一波次中**最多只允许指派 1 个 `巧夺` 实例运行编译/构建/全量测试**，其余并发专家必须在委派 Prompt 中被明确要求：`“全程静态阅读（grep/read/diff），禁止运行重型编译或测试命令”`。
3. **波次屏障（Strict Wave Barrier）**：在 Wave 1 的只读调研 Agent 全部返回之前，**绝对禁止提前启动 Wave 2 的代码写入**（防止实现写完才发现调研找出了架构级漏项而返工）。
4. **主理官禁手与文件独占锁（Orchestrator Hands-Off & Disjoint Claims）**：
   - Wave 2 并行实现时，不同子 Agent 的可写文件集合必须**两两互不相交（Disjoint File Sets）**，并在启动前锁定模块间接口契约；
   - **当任何实现或审查子 Agent 正在后台运行时，主理官（天枢）绝对禁止在主工作树上私自修改业务代码**，防止覆盖子 Agent 的在途工作或导致审查行号失效！
5. **沙箱化对抗与变异测试（Sandboxed Mutation Testing）**：
   - 当派出多个 `巧夺` 或 `澄澈` 实例做同角色多实例盲测或变异测试（验证“把生产代码改坏时测试能否变红”）时，**严禁在主工作树上直接改写文件或执行 `git checkout`**！一切破坏性探针与变异实验必须在系统临时目录（`/tmp/...`）或独立 Git Worktree（`.worktrees/...`）中执行。
