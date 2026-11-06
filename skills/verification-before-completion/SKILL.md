---
name: verification-before-completion
description: "Enforces Obra Superpowers' strict completion gate: never claim a task or test passes without running the exact verification command and reading its full output."
---

# /verification-before-completion — 完工前强制实证门禁

源自 `obra/superpowers`（`skills/verification-before-completion`），用于彻底消灭“凭感觉宣布大功告成”的幻觉：

## 完工铁律（The Iron Law of Completion）
**没有任何未经当前终端实测输出的“应该修好了”、“测试肯定能过”或“逻辑看起来没问题”！**

## 结单前强制五步闭环
1. **明确证明命令**：确定能够直接证明当前改动成功的命令（单元测试、集成测试、类型检查、Linter 或真实运行探针）。
2. **最后一次修改后实测**：在最后一次修改任何代码或配置文件**之后**，亲自运行验证命令（哪怕只改了一行也必须重跑）。
3. **读取完整输出与退出码**：核实真实的 Exit Code 0、通过用例数量与实际输出。
4. **逐条核对需求契约**：对照《开工方案卡》或 `SPEC.md` 验收标准，确认零遗漏。
5. **实证交付**：在完工报告中展示真实运行的命令与结果数据；因环境限制无法运行的项目必须诚实标注为 `未运行（原因：...）`。
