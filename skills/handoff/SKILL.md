---
name: handoff
description: "Creates a high-signal, lossless context handoff summary across sessions, branches, or specialist agents."
---

# /handoff — 跨会话/跨阶段无损上下文交接

## 交接包必填结构
1. **当前目标与所处阶段**：已完成切片 vs. 待完成切片。
2. **已确认事实与拍板决策**：引用相关 `SPEC.md`、`GLOSSARY.md` 与 `docs/adr/`。
3. **关键代码位置与状态**：已修改文件、测试通过状态、已登记 `shortcut:` 技术债。
4. **下一步精确指令（Next Immediate Action）**：接手者无需重读全量历史即可立即执行的第一步。
