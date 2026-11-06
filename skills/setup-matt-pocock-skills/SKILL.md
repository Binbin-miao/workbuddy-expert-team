---
name: setup-matt-pocock-skills
description: "Initializes repository documentation structure (GLOSSARY.md, docs/adr/, docs/agents/, .scratch/) on demand."
---

# /setup-matt-pocock-skills — 工程文档环境按需初始化

## 核心准则
1. **按需轻量初始化**：仅在主理 AI 判定任务属于 **Tier 2（轻量文档）** 或 **Tier 3（完整工程文档链）** 时按需创建目录，不在一次性小脚本任务中制造空目录噪音。
2. **标准目录结构**：
   - `GLOSSARY.md`：项目统一语言（Ubiquitous Language）词典。
   - `docs/adr/`：架构决策记录（ADR-001, ADR-002...）。
   - `docs/specs/` 或 `.scratch/`：技术规格书与本地曳光弹工单（`.scratch/tickets/`）。
   - `docs/agents/issue-tracker.md`：记录工单追踪方式（本地 `.scratch/` Markdown 模式或 GitHub Issues 模式）。
