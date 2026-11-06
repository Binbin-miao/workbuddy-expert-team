---
name: webapp-testing
description: "Tests local web applications using Playwright to verify live DOM rendering, interactive flows, multi-viewport screenshots, and zero console/page errors."
---

# /webapp-testing — 基于真实浏览器的 Web 应用交互与视觉验证

源自 `anthropics/skills`（`skills/webapp-testing`），用真实浏览器（Playwright / Headless Chromium）取代静态代码盲猜：

## 核心验证工作流
1. **服务探测与生命周期管理**：检测本地服务端口或拉起临时测试服务，验证完毕后干净关闭。
2. **运行时零报错门禁（Zero Console/Page Errors）**：监听 `page.on("console")` 与 `page.on("pageerror")`，任何未捕获的 JS 异常、水合错误或静态资源 404 均视为门禁未通过。
3. **双视口截图与全状态演练**：在桌面端（1440×900）与移动端（375×812）视口下实际触发交互并截图，验证布局对齐、对比度、无横向溢出（`horizontalOverflow === 0`）及六大交互状态。
