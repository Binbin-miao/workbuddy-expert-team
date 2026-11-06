---
name: grill-with-docs
description: "Conducts evidence-first structured Grilling while reading/updating repository docs (GLOSSARY.md, docs/adr/)."
---

# /grill-with-docs — 结合代码库与文档的结构化压力访谈

## 执行步骤
1. **静默事实扫描（Silent Fact Scan）**：先读取代码库、`GLOSSARY.md`、`docs/adr/`、测试与配置文件。**客观事实（Facts）自己查，严禁拿代码里能查到的事实去问用户**。
2. **决策树高杠杆提问（Decision-Tree Grilling）**：
   - 识别真正需要用户拍板的业务取舍与架构权衡（Decisions）。
   - 按影响范围从大到小排序，每轮聚焦 1~3 个核心分支问题。
   - 每个问题必须提供：**背景影响 + 2~3 个清晰选项及优劣对比 + 明确推荐项（Recommended）**。
3. **自主文档裁决与同步**：
   - 闭合设计树后，自主判断并向用户确认文档沉淀级别（Tier 1 免文档 / Tier 2 轻量 Glossary+ADR / Tier 3 完整 Spec+Tickets）。
   - 将确认的专有概念同步至 `GLOSSARY.md`，关键架构权衡写入 `docs/adr/NNN-<slug>.md`。
