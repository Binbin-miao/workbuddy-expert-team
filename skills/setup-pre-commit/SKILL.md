---
name: setup-pre-commit
description: "Configures fast, deterministic pre-commit hooks for linting, typechecking, and critical tests."
---

# /setup-pre-commit — 确定性提交前防线配置

## 配置原则
1. 保持极速（秒级完成）：仅针对 Staged 变更执行格式化、静态类型检查、Linter 与核心冒烟测试。
2. 确保幂等与跨平台可用，拦截低级机械错误流入主干。
