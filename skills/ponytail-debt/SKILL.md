---
name: ponytail-debt
description: "Scans the repository for shortcut: and ponytail: markers to compile a structured technical debt ledger with ceilings and upgrade triggers."
---

# /ponytail-debt — 刻意捷径与技术债台账盘点

## 执行步骤
扫描全仓 `shortcut:` 与 `ponytail:` 注释，按 `<file>:<line> — 简化内容 | 上限 (Ceiling) | 升级触发条件 (Upgrade Trigger)` 输出台账，并高亮缺失触发条件的条目。
