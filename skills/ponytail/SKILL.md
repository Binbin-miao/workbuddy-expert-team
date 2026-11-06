---
name: ponytail
description: "Enforces the Ponytail smallest-complete-change philosophy, pre-code scope scan, and 6-step Decision Ladder."
---

# /ponytail — 最小完整变更与反过度设计核心法则

## 六级决策阶梯（命中即停）
1. 这个改动真的需要存在吗？
2. 当前代码库里已经有了吗？（强制先搜仓库复用）
3. 标准库或平台原生能力能直接做吗？
4. 项目已安装的现有依赖能做吗？（严禁为几行代码引新库）
5. 一眼能懂的几行内联代码能写完吗？
6. 以上都不行 → 写贴合仓库约定的最少且完整的生产代码。

## 绝对底线
绝不削减信任边界数据校验、防数据丢失错误处理、安全鉴权、无障碍（a11y）与高风险逻辑回归测试。有意捷径标记 `shortcut: <上限>, <升级触发条件>`。
