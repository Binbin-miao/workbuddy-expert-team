---
name: subagent-prompt-architecture
description: "Master-level meta-prompting framework (inspired by GSD XML task packets & Ruflo contracts): translates plain-language requests into structured 6-Block Subagent Prompts with Technical Pushback Rights."
---

# /subagent-prompt-architecture — 大白话意图解码与主理官六段式元提示词（Meta-Prompting）手册

融合 `gsd-build/get-shit-done` 的结构化任务元提示词（XML/Block Meta-Prompting）、`FoundationAgents/MetaGPT` 的自然语言转 SOP 机制与 `obra/superpowers` 的实证精神：

---

## 一、 大白话意图自动解码器（Colloquial-to-Engineering Auto-Translator）

用户只需用最自然的日常语言（大白话）描述想法，主理官在内部自动完成以下四项专业补全，无需用户懂技术术语或手动催促：

1. **自动补齐「开源与现有方案对标」**：用户说“做个某某功能/页面/插件”，主理官自动先安排检索 GitHub 同类高星开源项目、成熟库以及当前框架是否自带原生组件，拒绝闭门造车。
2. **自动补齐「隐性操作体验与防呆防线（Operational UX Ergonomics）」**：
   - 凡是耗时可能 >2 秒的操作（批处理、网络请求、数据迁移、AI 推理），自动补齐 **① 触发即时反馈（正在处理提示）、② 防并发重入互斥锁（防止用户连点触发双写污染）、③ 失败自动恢复与幂等去重**。
   - 凡是多步配置或切换流程，自动设计为最省心的**一键式闭环或自动后台同步**。
3. **自动补齐「全调用链与数据安全防线」**：
   - 凡涉及修改共享数据结构、存储方式或配置项，自动安排扫描全仓所有读取、写入、分页、清理与导出路径，确保向后兼容且零数据丢失。
   - 凡涉及远程部署或不可逆清理，自动补齐 **“分支差异比对 + 时间戳物理备份 + 进程重载验证”**。
4. **自动转化为「人话方案卡」**：向用户汇报方案时，隐藏繁琐的底层细节，只用通俗易懂的语言展示目标、开源参考、1~2 个带推荐项的选择题以及执行计划。

---

## 二、 主理官写给子专家的「黄金六段式元提示词（6-Block Meta-Prompt）」

**核心禁忌**：
- 严禁写 **“根因我已经查清，不要质疑，按我给的伪代码逐行照抄”**（独裁喂饭式 Prompt 会剥夺子专家的纠错能力，一旦主理官存在视野盲区，子专家会被迫把 Bug 写进代码）。
- 严禁写 **“去把某某功能实现了”**（甩手掌柜式模糊 Prompt 会导致子专家脱离上下文乱改）。

每次调用 `Agent` 或 `SendMessage` 委派子专家时，必须严格输出以下 6 个结构化区块：

```markdown
## <block 1: mission_and_ux> 任务使命与端到端用户体验
- **核心目标**：用一两句话说明本次子任务要解决的业务/技术问题。
- **用户体验与防呆要求**：触发方式是什么？耗时操作是否具备即时状态反馈与并发互斥锁？错误提示是否清晰可操作？

## <block 2: verified_facts_vs_proposal> 已核实客观事实 vs. 初步设计构想
- **[已核实客观事实（附精确 File:Line）]**：列出已通过源码或实测确认的文件路径、函数签名、数据结构与环境约束。
- **[初步设计构想（需你结合全仓代码复核）]**：列出主理官拟定的实现思路，明确标注哪些部分是待检验假设。

## <block 3: invariants_and_completeness> 核心不变量与全调用链闭环契约
- **不可破坏的不变量**：如数据零丢失、向后兼容性、写入与索引的崩溃原子性、状态水位线不重置。
- **全调用链扫描义务**：动手修改前，必须先 `grep` 目标模块/字段在全仓的**全部读取、写入、分页、删除与定时调用点**，确保无遗漏分支。

## <block 4: elegance_and_claims> 代码优雅度与文件独占锁（Resource Claims）
- **独占可写文件范围（Claims）**：明确本专家允许新建/修改的文件路径；列出当前工作区中严禁触碰的无关文件。
- **优雅代码准则（`/code-elegance`）**：顶部卫语句（Early Return）消除深层嵌套、声明式映射表（Lookup Table）代替冗长分支、边界一次性类型归一化（Parse, Don't Validate）、成对接口签名对称、可读性优先于压行数。

## <block 5: pushback_and_verification> 显式技术反驳权与对抗验证清单
- **强制技术反驳权（Mandatory Pushback Right）**：如果你在阅读源码时发现主理官的初步构想存在漏路径、并发竞态、分批饥饿、写队列中毒或破坏模块封装，**你必须拒绝盲从，直接采用正确的根治方案并在回传中说明原因**！
- **必测对抗场景**：列出必须通过自动化测试证明的边界条件（空值/零值/非法输入、中途异常恢复、重复触发幂等、权限边界）。

## <block 6: return_contract> 结构化回传契约（限 60 行内）
- 请按以下四项通过 `SendMessage` 回传：① 实际变更文件与优雅设计亮点；② 全量测试与门禁真实输出（含 Exit Code 与通过数）；③ 对原构想的纠偏/补漏说明；④ ⚠️ 残余风险与未检项。
```
