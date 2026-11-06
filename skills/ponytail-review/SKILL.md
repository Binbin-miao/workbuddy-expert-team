---
name: ponytail-review
description: "Read-only 6-dimension code review ordered by Correctness -> Safety -> Scale -> Tests -> Speed -> Simplicity."
---

# /ponytail-review — 六维精简与正确性审查

## 审查顺序与要求
1. 声明真实负载假设（单人脚本 vs. 并发服务）。
2. 按 `Bug → 安全风险 → 真实负载规模 → 缺失测试 → 性能回退 → 可删减冗余代码` 顺序审查 Diff 及上下游调用链。
3. 每个 Finding 必须附带可触发的具体反例与最小修复方案，末尾汇总 `⚠️ 风险与遗留`。
