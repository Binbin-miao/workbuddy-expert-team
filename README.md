# 🚀 精益求精服务 (Excelsior) v6.0 — 自主并发全能软件工程专家团队

> **“Zero Bloat, Maximum Craftsmanship.”** — 零膨胀、高匠心，听懂大白话、模型自主判断多 Agent 并发波次委派与双盲交叉验证的全能软件工程专家团。

本仓库为 **WorkBuddy** / **CodeBuddy** 的专家团队插件，内置 **1 位首席主理官 (`天枢`) + 5 位专职顶尖专家 (`璇玑` / `澄澈` / `浮光` / `玲珑` / `巧夺`)**，并全量注入 **46 项开源软件工程技能 (`skills/*/SKILL.md`)**，对所有编程语言与技术栈 **100% 开箱即用**。

## 🔗 一键安装与配置 (WorkBuddy)

如果你正在使用 WorkBuddy，可以通过下方按钮或复制分享链接快速将本插件添加到你的环境中：

- **一键使用 / 添加插件**：  
  [![使用插件](https://img.shields.io/badge/WorkBuddy-一键使用专家团-blue?style=for-the-badge&logo=codebuddy)](https://www.workbuddy.cn/work/launch/?sharecode=Y6QAJ8WUvUa4koEmjmaLdOJcFJhLoAuN66YQ8t_hGwBo7umTh-Jyl7zT9eex2VbI&expertname=%E7%B2%BE%E7%9B%8A%E6%B1%82%E7%B2%BE%E6%9C%8D%E5%8A%A1&buddy_type=workbuddy)
- **分享链接**：  
  `https://www.workbuddy.cn/work/launch/?sharecode=Y6QAJ8WUvUa4koEmjmaLdOJcFJhLoAuN66YQ8t_hGwBo7umTh-Jyl7zT9eex2VbI&expertname=%E7%B2%BE%E7%9B%8A%E6%B1%82%E7%B2%BE%E6%9C%8D%E5%8A%A1&buddy_type=workbuddy`

> **【首次使用请让 AI 自行安装所需技能】** 导入后首次对话，直接说一句「请先检查并自行安装你需要的技能」，专家团会补齐 46 项内置技能后再开工。

---

## ✨ v6.0 核心架构亮点

1. **模型自主判断多 Agent 并发波次调度（`/dispatching-parallel-agents` — 无需手动催促）**
   - **Tier 0 微任务免打扰直通**：纯问答、单条命令或单文件 ≤20 行明确微调，由主理官 **天枢** 直接单兵秒级办妥，零子代理通信开销。
   - **Tier 1~3 中大型任务全自动三波次并发（Wave Fan-Out / Fan-In）**：
     - **🌊 Wave 1 并行只读侦察波**：遇到代码审查、复杂 Bug 排查、性能优化或新功能设计，**天枢**自动在同一回合并发派出 **浮光**（外部开源对标与上游溯源）+ **璇玑**（全仓调用链与并发锁扫描）+ **澄澈**（安全爆炸半径与性能热点审计）+ **玲珑**（UI 生命周期审查）+ **巧夺**（**唯一编译/门禁实跑员**，其余只读专家禁跑重型编译以防锁争用卡死）。
     - **📋 Wave Barrier 1 方案卡确认门禁**：收齐侦察结果并剔除被证伪假设后，先呈交简明 **《任务理解与开工方案卡》**，经你点头确认后再动刀写代码。
     - **🌊 Wave 2 分片写锁并行实现波**：跨模块任务自动按目录分配互不重叠的文件写锁（Resource Claims），并发派出多个实现实例（如 `巧夺-Core` + `玲珑-UI` + `巧夺-Host`），主理官全程禁手不抢改工作树。
     - **🌊 Wave 3 同角色多实例双盲交叉验证波**：完工后自动并行派出 **澄澈**（静态差分审查）+ **巧夺-Verifier**（独立门禁复跑与沙箱化对抗测试，严禁污染主工作树）。
2. **大白话意图解码与隐性工程防呆（`/subagent-prompt-architecture`）**
   - 只需输入一句日常大白话，自动补齐耗时操作进度反馈、防并发重入互斥锁（RAII 自动释放）、读路径零写盘副作用、写前备份+写后校验+失败自动回滚事务、异步监听器卸载守卫（`disposed` guard）与 Single-Flight 缓存复用。
3. **优雅代码美学（`/code-elegance`）与杂志级交付文档（`/elegant-delivery-docs`）**
   - 强制采用顶部扁平卫语句（Early Return）、声明式映射表（Lookup Table）代替冗长分支、入口边界一次性类型归一化（Parse, Don't Validate）、成对接口签名对称，拒绝为压行数牺牲可读性。
   - 完工输出带 **ASCII 接线微图、设计取舍对比表、实测证据与回滚后路** 的交付卡，中大型改造自动沉淀独立 `.md` 架构接线指南。

---

## 👥 团队成员架构 (Team Roster)

| 头像徽标 | Agent ID | 角色代号 | 职责与核心内置技能 |
| :--- | :--- | :--- | :--- |
| **LEAD 首席主理官** | `lean-adaptive-engineering-team-lead` | **天枢 (Tianshu)** | **全局总指挥与波次调度师**：大白话意图解码、自主三波次并发委派、报《开工方案卡》确认、六段式元提示词撰写与最终交付（`dispatching-parallel-agents`、`ruflo-swarm-sparc`、`subagent-prompt-architecture`） |
| **GRILL 领域建模** | `domain-grilling-architect` | **璇玑 (Xuanji)** | **全调用链建模与架构接线专家**：全仓读写/删除/分页调用链穷尽扫描、并发锁与崩溃原子性不变量建模、曳光弹工单拆解与 `.md` 接线文档（`grill-with-docs`、`domain-modeling`、`to-spec`、`to-tickets`、`elegant-delivery-docs`） |
| **LEAN 极简代码** | `ponytail-simplicity-gatekeeper` | **澄澈 (Chengche)** | **极简主义、代码优雅度与安全差分审查官**：Ponytail 六级决策阶梯、Karpathy 外科手术边界、Trail of Bits 爆炸半径审计、性能热点排序与 `>80% 置信度` 审查（`ponytail`、`code-elegance`、`differential-review`、`audit-context-building`） |
| **WEB 对标检索** | `scrapling-web-intelligence` | **浮光 (Fuguang)** | **开源方案对标与网络情报专家**：GitHub 同类高星开源项目对标、上游仓库 Commits/Issues/PRs 差分溯源、官方文档取证与 Scrapling 自适应抓取（`prior-art-research`、`scrapling-official`、`webapp-testing`） |
| **UI/UX 审美总监** | `impeccable-design-director` | **玲珑 (Linglong)** | **视觉交互总监与前端生命周期专家**：Impeccable 24 项设计命令、62 条反 AI Slop 规则、组件交互死锁与监听器泄漏排查、React 性能优化与真实浏览器双端验证（`impeccable`、`react-best-practices`、`webapp-testing`） |
| **TDD 深模块研发** | `deep-module-tdd-engineer` | **巧夺 (Qiaoduo)** | **深度模块、优雅代码 TDD 与盲测复核工程师**：深模块封装、`/code-elegance` 优雅实现、Red-Green-Refactor TDD、科学缺陷诊断、唯一编译门禁实跑与沙箱化变异验证（`tdd`、`codebase-design`、`diagnosing-bugs`、`verification-before-completion`） |

---

## 🛠️ 内置 46 项技能索引 (Built-in Skill Index)

| 分类 | 内置技能名称 (`skills/*/SKILL.md`) |
| :--- | :--- |
| **多 Agent 并发与元提示词调度** | `dispatching-parallel-agents`、`ruflo-swarm-sparc`、`subagent-prompt-architecture`、`using-git-worktrees`、`handoff`、`wayfinder`、`triage` |
| **需求拷问、领域建模与规格拆票** | `ask-matt`、`setup-matt-pocock-skills`、`grill-with-docs`、`grill-me`、`domain-modeling`、`to-spec`、`to-tickets` |
| **开源对标检索与网页情报** | `prior-art-research`、`research`、`scrapling-official`、`mcp-builder` |
| **极简主义、代码优雅度与安全审计** | `code-elegance`、`karpathy-guidelines`、`ponytail`、`ponytail-review`、`ponytail-audit`、`ponytail-debt`、`ponytail-gain`、`ponytail-help`、`differential-review`、`audit-context-building` |
| **UI/UX 审美、前端性能与浏览器验证** | `impeccable`、`react-best-practices`、`webapp-testing`、`prototype` |
| **TDD 深模块研发、数据库与实证交付** | `codebase-design`、`improve-codebase-architecture`、`tdd`、`implement`、`implement-spec`、`diagnosing-bugs`、`postgres-best-practices`、`code-review`、`receiving-code-review`、`verification-before-completion`、`elegant-delivery-docs`、`pr`、`retro`、`setup-pre-commit` |

---

## 📦 本地安装与全局技能同步

1. 将本仓库克隆或解压至 WorkBuddy 插件目录：
   - Windows: `%USERPROFILE%\.workbuddy\plugins\marketplaces\my-experts\plugins\lean-adaptive-engineering`
   - macOS / Linux: `~/.workbuddy/plugins/marketplaces/my-experts/plugins/lean-adaptive-engineering`
2. （可选）在仓库根目录运行以下命令，可将包内全部 **46 个内置技能** 一键同步至全局 `~/.workbuddy/skills`：
   ```bash
   python install_skills.py
   ```

## 📜 许可证与开源致谢 (License & Notice)

本项目基于 [MIT License](LICENSE) 开源，相关上游开源工程方法论致谢详见 [NOTICE.md](NOTICE.md)。
