---
name: code-elegance
description: "Enforces universal code elegance craftsmanship (GitHub Spec-Kit Constitution): flat guard clauses, declarative data-driven dispatch, boundary normalization ('Parse, Don't Validate'), symmetric APIs, and readability over line-count golf."
---

# /code-elegance — 优雅代码美学与结构对称性宪法

真正优秀的代码兼具 **Ponytail 的克制（无冗余抽象、无废代码）** 与 **工业级代码的优雅（清晰、对称、自解释、易演进）**。**优雅绝不等于把代码压成晦涩难懂的一行（Code Golf）**。

## 六大通用优雅代码铁律（Six Universal Pillars of Code Elegance）

### 1. 卫语句扁平化控制流（Guard Clauses Over Arrow Nesting）
- **消灭箭头型深层嵌套**：函数内部条件缩进控制在 2 层以内。
- 将空值、权限不足、前置条件不满足、冷却中等边缘分支在函数顶部用精炼的 `if (!isValid) return ...` 提前返回（Early Return），让核心主干逻辑（Happy Path）平铺在最外层，一眼到底。

### 2. 表驱动代替分支堆砌（Data-Driven Lookup Tables Over Branch Soup）
- 当出现 3 个以上结构相似的 `if / else if`、`switch` 分支、命令路由、状态转换或字段映射时，**将其提炼为声明式的常量配置表（Lookup Table / Schema Map）**。
- 用“静态数据表 + 5 行通用解释逻辑”取代几百行的条件分支，使新增规则变成纯粹的“表内加一行数据”。

### 3. 在边界一次性解析，内部零防御噪音（"Parse, Don't Validate" at the Boundary）
- **杜绝防御性代码散落全仓**：严禁在每个内部业务函数里重复写类型转换、正则切割或默认值回退（不仅丑陋，还极易因各处兜底不一致引发 `NaN` 或类型不匹配 Bug）。
- **边界归一化**：在**模块入口、配置加载器或序列化边界**一次性将外部原始输入清洗、校验并转换为强语义的标准内部数据结构；模块内部核心函数直接消费干净的数据，保持纯粹简明。

### 4. 接口对称性与单一抽象层级（API Symmetry & Single Level of Abstraction）
- **成对操作严格对称**：如 `open / close`、`read / write`、`enable / disable`、全量清理与局部清理，在函数命名、参数顺序和返回值结构上必须保持高度对称。
- **单一抽象层级（SLAP）**：高层业务编排函数只组合语义清晰的步骤函数，不混杂底层字节拼接、正则细节或原始 I/O 操作；当一个函数的行为需要靠布尔标志位（Boolean Flag Argument）大幅分叉时，拆分为两个职责单一的具名函数。

### 5. 自解释的领域命名与克制注释（Self-Documenting Naming & Why-Comments）
- 命名精准传达业务语义、类型特征与物理单位（如 `retentionDays`、`timeoutMs`、`isAuthorized`、`userIdsByGroup`），杜绝 `data`、`info`、`temp`、`handle`、`process` 等空洞词汇。
- 代码本身说明 `What` 和 `How`；注释只用来解释代码无法表达的 `Why`（业务权衡、协议怪癖或刻意捷径 `shortcut:`）。

### 6. 可读性永远高于压行数（Readability Beats Line Golf — 3A 铁律）
- **砍掉无用的抽象层，保留有用的语义层**。严禁为了少写 3~5 行代码而将具名业务常量强行内联、或将清晰的三步变换压缩成超过 100 字符的嵌套三元表达式与晦涩链式调用。
