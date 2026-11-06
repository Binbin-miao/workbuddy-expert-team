---
name: diagnosing-bugs
description: "Diagnoses bugs and performance regressions scientifically: minimal reproduction, ranked hypotheses, targeted instrumentation, root-cause fix, and regression test."
---

# /diagnosing-bugs — 科学缺陷诊断闭环

## 四步排错铁律（严禁盲目猜改）
1. **最小化稳定复现**：固定触发输入与复现命令，建立秒级反馈循环。
2. **建立并排序假设**：列出最可能的 2~3 个根因假设。
3. **精准埋点/二分证伪**：用日志、断言或最小实验验证假设，定位共享根因（Shared Root Cause）。
4. **最小修复与回归锁死**：修复根因，清理调试埋点，并补上“旧代码必红、新代码必绿”的回归测试。
