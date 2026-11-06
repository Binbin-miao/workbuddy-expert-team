# NOTICE / 开源致谢

「精益求精服务（Excelsior）」不是从零发明的方法论。它的调度协议、审查门禁与技能库，是对一批优秀开源工程体系的**阅读、蒸馏与重新编排**。本文件逐一说明：

1. 引用了哪些上游仓库；
2. 每个上游仓库贡献了什么机制；
3. 哪些技能目录直接衍生自上游；
4. 各自的许可证要求。

---

## 一、上游项目清单（14 个）

| # | 上游项目 | 地址 | 许可证 | 本项目引用内容 |
|:-:|:---|:---|:---|:---|
| 1 | **ruvnet/ruflo** (Claude Flow) | https://github.com/ruvnet/ruflo | MIT | 提案先行门禁（Proposals, Not Orders）、并行文件独占写锁（Resource Claims Board）、SPARC 五步研发闭环、四步项目记忆蒸馏（RETRIEVE→JUDGE→DISTILL→CONSOLIDATE） |
| 2 | **gsd-build/get-shit-done** | https://github.com/gsd-build/get-shit-done | MIT | 极薄主理官（Thin Orchestrator）防上下文腐烂、四维前置调研（Stack / Features / Architecture / Pitfalls）、六段式结构化元提示词委派 |
| 3 | **affaan-m/ECC** | https://github.com/affaan-m/ECC | MIT | 规划/审查严格只读分离、`>80% 置信度` 审查过滤门槛 |
| 4 | **FoundationAgents/MetaGPT** | https://github.com/FoundationAgents/MetaGPT | MIT | `Code = SOP(Team)` 自然语言编程流水线、竞品/先例对标分析 |
| 5 | **bmad-code-org/BMAD-METHOD** | https://github.com/bmad-code-org/BMAD-METHOD | 上游仓库未附标准 LICENSE | 自适应流程体量（Right-Sized Process）、渐进式上下文交接（Progressive Context Handoff） |
| 6 | **github/spec-kit** | https://github.com/github/spec-kit | MIT | 《优雅代码与交互工程宪法》门禁（扁平卫语句、表驱动、Parse Don't Validate、成对接口对称性） |
| 7 | **mattpocock/skills** | https://github.com/mattpocock/skills | MIT | 证据先行压力访谈（Grilling）、统一语言 `GLOSSARY.md`、ADR 决策记录、曳光弹垂直切片拆解、深模块 TDD、科学缺陷诊断 |
| 8 | **DietrichGebert/ponytail** | https://github.com/DietrichGebert/ponytail | MIT | 六级极简决策阶梯（有原生组件绝不造轮子）、全仓减肥审计、刻意捷径技术债台账 |
| 9 | **pbakaus/impeccable** | https://github.com/pbakaus/impeccable | Apache-2.0 | 24 项 UI/UX 命令、4 大表面模式、62 条反 AI 廉价感（Anti-Slop）铁律 |
| 10 | **vercel-labs/agent-skills** | https://github.com/vercel-labs/agent-skills | 上游仓库未附标准 LICENSE | React/Next.js 40+ 条性能规则、Web Design Guidelines |
| 11 | **D4Vinci/Scrapling** | https://github.com/D4Vinci/Scrapling | BSD-3-Clause | 真实网页自适应抓取与反爬绕过能力 |
| 12 | **trailofbits/skills** | https://github.com/trailofbits/skills | **CC-BY-SA-4.0** | 差分安全审计（differential-review）、爆炸半径计算、审计上下文构建、Sharp Edges、变体分析 |
| 13 | **obra/superpowers** | https://github.com/obra/superpowers | MIT | 完工实证门禁、Git Worktree 隔离、科学对待代码审查反馈 |
| 14 | **supabase/agent-skills** | https://github.com/supabase/agent-skills | MIT | Postgres 最佳实践（Schema 设计、零停机迁移、RLS、索引、EXPLAIN） |

### 补充引用的上游（思路借鉴，未整目录衍生）

| 上游项目 | 地址 | 许可证 | 引用点 |
|:---|:---|:---|:---|
| **anthropics/skills** | https://github.com/anthropics/skills | 见仓库 | `mcp-builder`、`webapp-testing` 两个技能的原始规范 |
| **multica-ai/andrej-karpathy-skills** | https://github.com/multica-ai/andrej-karpathy-skills | 见仓库 | Karpathy 四大编码铁律 |
| **addyosmani/agent-skills** | https://github.com/addyosmani/agent-skills | 见仓库 | `/webperf` 先测量后优化审计 |
| **neondatabase/postgres-skills** | https://github.com/neondatabase/postgres-skills | 见仓库 | Postgres 慢查询与迁移实践 |

---

## 二、技能目录 → 上游来源映射

`skills/` 下 45 个技能分为两类。

### A. 直接衍生自上游（保留原规范骨架，中文化并适配专家团调度）

| 技能目录 | 上游来源 | 上游许可证 |
|:---|:---|:---|
| `ask-matt` `grill-me` `grill-with-docs` `to-spec` `to-tickets` `triage` `wayfinder` `handoff` `implement` `implement-spec` `improve-codebase-architecture` `research` `prototype` `retro` `tdd` `code-review` `codebase-design` `diagnosing-bugs` `domain-modeling` `pr` `setup-matt-pocock-skills` `setup-pre-commit` | mattpocock/skills | MIT |
| `ponytail` `ponytail-audit` `ponytail-debt` `ponytail-gain` `ponytail-help` `ponytail-review` | DietrichGebert/ponytail | MIT |
| `impeccable` | pbakaus/impeccable | Apache-2.0 |
| `scrapling-official` | D4Vinci/Scrapling | BSD-3-Clause |
| `differential-review` `audit-context-building` | trailofbits/skills（融合 affaan-m/ECC 的置信度过滤） | CC-BY-SA-4.0 |
| `using-git-worktrees` `verification-before-completion` `receiving-code-review` | obra/superpowers（后者融合 addyosmani/agent-skills） | MIT |
| `karpathy-guidelines` | multica-ai/andrej-karpathy-skills | 见上游 |
| `mcp-builder` `webapp-testing` | anthropics/skills | 见上游 |
| `react-best-practices` | vercel-labs/agent-skills + addyosmani/agent-skills | 见上游 |
| `postgres-best-practices` | supabase/agent-skills + neondatabase/postgres-skills | MIT |

### B. 本项目原创编排（吸收多源思想，但结构与文字为原创）

| 技能目录 | 说明 |
|:---|:---|
| `ruflo-swarm-sparc` | 六大框架调度协议的融合重写：ruflo + GSD + BMAD + MetaGPT + ECC + Spec-Kit |
| `subagent-prompt-architecture` | 六段式元提示词委派框架（受 GSD XML 任务包与 Ruflo 契约启发） |
| `prior-art-research` | 开工前的开源先例检索流程（受 MetaGPT 竞品分析与 GSD 四维调研启发） |
| `code-elegance` | 优雅代码宪法（受 Spec-Kit 与 Ponytail 双向启发） |
| `elegant-delivery-docs` | 杂志级交付简报与架构接线文档规范 |

---

## 三、许可证合规说明

- 本项目原创部分（Agent 编排提示词、`plugin.json` 配置、README、NOTICE、以及上表 B 类技能）以 **MIT** 授权。
- **MIT / BSD-3-Clause** 来源：允许再分发与修改，需保留原作者版权声明 — 本文件即为该声明。
- **Apache-2.0** 来源（`pbakaus/impeccable`）：允许再分发，需保留版权与许可声明 — 本文件即为该声明。
- **CC-BY-SA-4.0** 来源（`trailofbits/skills`）：你**必须署名原作者**（已在本文件完成），且衍生作品需以相同许可证共享。对应技能为 `differential-review`、`audit-context-building`；若你将本项目用于商业分发，请单独审阅这两个目录的许可条款，或直接替换为自研实现。
- **上游未附标准 LICENSE** 的项目（`bmad-code-org/BMAD-METHOD`、`vercel-labs/agent-skills`）：本项目仅借鉴其公开描述的方法论概念（属于思想层面），未复制其代码文件；如原作者认为存在不当引用，请提 Issue，我们会立即调整或移除。

---

## 四、致谢

感谢以上所有作者把这些方法论公开出来。**没有这些前人的公开实践，就不会有这个专家团。** 如果你觉得本项目有用，请优先去给上面这些上游仓库点 Star —— 他们才是原创者。

- Matt Pocock — https://github.com/mattpocock
- Dietrich Gebert — https://github.com/DietrichGebert
- Paul Bakaus — https://github.com/pbakaus
- D4Vinci — https://github.com/D4Vinci
- Trail of Bits — https://github.com/trailofbits
- Jesse Vincent (obra) — https://github.com/obra
- ruvnet — https://github.com/ruvnet
- GSD / TÂCHES — https://github.com/gsd-build
- Affaan Mustafa — https://github.com/affaan-m
- MetaGPT Team — https://github.com/FoundationAgents
- BMAD Code Org — https://github.com/bmad-code-org
- GitHub Spec-Kit — https://github.com/github/spec-kit
- Vercel Labs — https://github.com/vercel-labs
- Supabase — https://github.com/supabase
- Anthropic — https://github.com/anthropics
- Addy Osmani — https://github.com/addyosmani
- Andrej Karpathy — https://github.com/karpathy
