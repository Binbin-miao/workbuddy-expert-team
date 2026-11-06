---
name: implement-spec
description: "Executes a multi-ticket specification systematically along the Ready Frontier of Tracer-Bullet tickets."
---

# /implement-spec — 按依赖图谱推进多工单规格实现

## 标准步骤
1. 读取 `SPEC.md` 与工单依赖图（Blocking Edges），锁定当前无阻塞的 **Ready Frontier**。
2. 每次拾取一张垂直切片工单，严格按 `/implement`（`/tdd` + `/code-review`）闭环完成并验证。
3. 更新工单状态，解锁下一批 Ready 工单，直至整份规格全部高标准交付。
