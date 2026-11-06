---
name: karpathy-guidelines
description: "Enforces Andrej Karpathy's 4 LLM coding rules: No Silent Assumptions, No Over-Engineering, No Orthogonal Changes, and Explicit Verification."
---

# /karpathy-guidelines — Karpathy 四大编码防坑铁律

源自 `multica-ai/andrej-karpathy-skills`，用于根治大模型编码中最常见的四大顽疾：

## 四大核心铁律（Four Constitutional Rules）

### Rule 1: 严禁静默假设（No Silent Assumptions）
- 在动手修改任何代码前，必须先核实对需求、数据边界与上下文的理解。
- 凡是代码库里能查到的客观事实（Facts）自己静默查清；凡是存在多种合理解释的业务/架构分歧，必须在《开工方案卡》中向用户确认，严禁把未验证的猜测直接写进代码。

### Rule 2: 严禁过度工程（No Over-Engineering）
- **能完整解决问题且清晰易读的最简方案就是正确方案**。
- 严禁为了“未来可能的扩展性”发明无人调用的抽象层、泛型工厂、配置开关或多余封装。

### Rule 3: 严禁顺手修改无关代码（No Orthogonal Changes / Surgical Diffs）
- **外科手术式 Diff 纪律**：每一行 Diff 都必须直接服务于当前请求的目标。绝对禁止在修 Bug 或做功能时顺手重构旁边的无关模块、重排未触及文件的导入顺序、或修改无关代码格式。
- 若发现无关模块的潜在问题，在报告末尾的 `⚠️ 风险与遗留` 中单独指出，绝不混入当前变更集。

### Rule 4: 强制显式验证（Explicit Verification）
- 写完代码绝不等于任务完成。必须针对改动运行对应的测试、构建、类型检查或真实命令行验证，用真实输出证明改动有效且未破坏既有功能。
