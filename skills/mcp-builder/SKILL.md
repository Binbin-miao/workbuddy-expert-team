---
name: mcp-builder
description: "Designs and builds high-quality, agent-ergonomic Model Context Protocol (MCP) servers and tools following Anthropic official patterns."
---

# /mcp-builder — 高质量 MCP Server 与 Agent 工具构建规范

源自 `anthropics/skills`（`skills/mcp-builder`）：

## 核心设计准则
1. **面向完整工作流封装（Deep Module Tools）**：围绕高层用户意图设计高信噪比工具，而非将底层碎片 CRUD 接口 1:1 暴露。
2. **严密自解释的输入 Schema**：使用 Pydantic / Zod 明确参数类型、默认值、约束与示例。
3. **输出控量与分页截断**：内置结果分页、字段过滤与长度截断，防止大体积原始数据撑爆模型上下文。
4. **可操作的错误反馈与安全注解**：报错时明确返回修正建议；准确标注 `readOnlyHint`、`destructiveHint` 与 `idempotentHint`。
