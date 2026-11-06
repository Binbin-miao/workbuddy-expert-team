---
name: using-git-worktrees
description: "Isolates parallel Tracer-Bullet slices, risky refactors, or exploratory prototypes in dedicated Git worktrees with clean baseline verification."
---

# /using-git-worktrees — Git Worktree 物理隔离工作流

源自 `obra/superpowers`（`skills/using-git-worktrees`），用于多工单并行推进、高风险重构或探索性原型时的工作区隔离：

## 标准操作流程
1. **创建隔离目录**：优先使用 `.worktrees/<slice-name>`（确保已加入 `.gitignore`）或同级目录，执行 `git worktree add -b <branch> <path> <base>`。
2. **基线测试验证（Clean Baseline Check）**：在动手改代码前，先在 Worktree 中跑一遍相关测试，确认基线状态全绿。
3. **独立验证与无损回收**：在隔离目录内完成开发与测试，合并或提取补丁后执行 `git worktree remove <path>` 保持主仓库整洁。
