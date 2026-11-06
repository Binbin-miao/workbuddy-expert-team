---
name: scrapling-official
description: "Full-stack adaptive web scraping and intelligence engine using Scrapling (Fetcher, DynamicFetcher, StealthyFetcher, Spider, adaptive=True element relocation, and CLI)."
---

# /scrapling-official — Scrapling 自适应网页探测与并发采集手册

## 核心执行准则
1. **真实探测前置**：在编写任何解析器或测试前，必须先实地探测目标页面并保存真实 DOM/JSON 样本。
2. **最小成本分级 Fetcher**：静态接口优先用 `Fetcher` / `FetcherSession`（TLS 指纹伪装）；动态 JS 渲染用 `DynamicFetcher`；Cloudflare/强反爬用 `StealthyFetcher(solve_cloudflare=True)`；大规模并发与断点续爬用 `Spider`。
3. **自适应防改版**：启用 `adaptive=True` 与 `auto_save=True`，结合 CSS/XPath、`find_by_text`、`find_similar` 实现高韧性数据提取。
