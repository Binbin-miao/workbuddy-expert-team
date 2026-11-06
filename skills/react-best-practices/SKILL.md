---
name: react-best-practices
description: "Enforces Vercel Engineering's 40+ React/Next.js performance optimization rules, 100+ Web Design Guidelines, and Addy Osmani's measure-first /webperf audit."
---

# /react-best-practices — 前端架构性能、React/Next.js 最佳实践与 Web 设计准则

融合 `vercel-labs/agent-skills`（`react-best-practices` + `web-design-guidelines`）与 `addyosmani/agent-skills`（`/webperf`）：

## 核心前端工程准则
1. **消除请求瀑布流（Eliminate Waterfalls）**：无依赖请求并行发起（`Promise.all`）；服务端/路由层预取数据。
2. **最小化客户端边界**：优先 Server Components，仅在叶子交互节点使用 `'use client'`。
3. **消灭冗余 `useEffect` 状态同步**：能从 props/state 直接计算出的派生值一律在渲染期计算，严禁 `useEffect(() => setDerived(...))`。
4. **长列表与渲染性能**：长列表启用 `content-visibility: auto` 或虚拟滚动；静态 JSX 提升至组件外；避免全屏高开销 SVG 动态滤镜阻塞合成线程。
5. **100+ Web 交互细节**：筛选/搜索/分页状态同步至 URL SearchParams；表单支持回车提交、提交中防连点禁用、错误自动聚焦；首屏媒体显式声明宽高以保证 `CLS = 0`。
