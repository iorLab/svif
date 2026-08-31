# Repository Tree / 目录树

本页是 `iorLab/svif` 当前 `main` 的**完整文件级仓库结构说明**。README 中的仓库树只用于快速导航；这里把当前 tracked 目录与文件全部展开，并在右侧说明它们的职责。

维护规则：只要仓库新增、删除、移动文件，或者某个目录 / 文件的职责发生实质变化，就必须在同一个 change set 中同步更新本页；README 中的简略目录树若受影响，也必须一起更新。

> 本页解释的是当前 active `main`。Git 内部元数据（例如 `.git/`）不属于仓库 tracked 内容，因此不列出。

```text
svif/                                                     # Svif 产品主仓库
├── .agents/                                              # OpenAI/Codex workspace GitHub marketplace 入口
│   └── plugins/
│       └── marketplace.json                             # 将 marketplace import 映射到本仓库的 local ./plugin
│
├── .agnir/                                               # 本 Svif Project 的 canonical durable memory
│   ├── state.md                                          # 当前 Project 状态：已经做到哪里、哪些事实当前成立
│   ├── next-actions.md                                   # 下一次恢复时应该继续推进的工作
│   ├── decisions.md                                      # 已确认的产品 / 架构 / 文档等持久决策
│   └── evidence/                                         # 对重要实现、迁移、验证和 checkpoint 的持久证据
│       ├── 2026-08-27-mainline-implementation.md         # 新 main-line 实现落地证据
│       ├── 2026-08-27-repository-rename-checkpoint.md    # 仓库更名 / canonical identity checkpoint
│       ├── 2026-08-28-cloudflare-consolidation.md        # Cloudflare reference 并回 Svif 主仓库的证据
│       ├── 2026-08-28-founding-e2e.md                    # Agnir + ChatGPT + Cloudflare founding E2E 证据
│       ├── 2026-08-28-main-only-branch-cleanup-checkpoint.md # 只保留 main、历史分支改由 commit SHA 索引的 checkpoint
│       ├── 2026-08-28-plugin-migration-audit-checkpoint.md # Plugin 产品目标迁移审计 checkpoint
│       ├── 2026-08-28-product-architecture-runtime.md    # 产品架构与 executable runtime 基线证据
│       ├── 2026-08-28-readme-diagram-localization-checkpoint.md # 双语 README / Mermaid 本地化 checkpoint
│       ├── 2026-08-28-validation-2-static-success.md     # 早期 Validation 2 静态验证成功证据
│       └── checkpoint-2026-08-28-validation-2.md         # Validation 2 的持久 checkpoint 记录
│
├── .github/                                              # GitHub 托管侧自动化配置
│   └── workflows/
│       └── conformance.yml                               # CI：repository integrity、runtime tests、portable contracts
│
├── src/                                                  # Svif 可执行产品代码
│   └── svif/                                             # Python reference package
│       ├── __init__.py                                   # Python package 入口 / 公共导出边界
│       ├── runtime.py                                    # Orchestrator 核心：begin/run/complete、验证、权限、reconcile、checkpoint
│       ├── continuity/                                   # Continuity Provider 实现 / 适配层
│       │   ├── __init__.py                               # continuity 子包入口
│       │   └── agnir.py                                  # 当前 founding provider：Agnir repository/filesystem continuity
│       ├── execution/                                    # Execution Surface 桥接层
│       │   ├── __init__.py                               # execution 子包入口
│       │   └── chatgpt.py                                # 当前 founding surface：ChatGPT 结构化 begin/complete bridge
│       └── capabilities/                                 # Capability Provider：读取或改变外部真实系统
│           ├── __init__.py                               # capabilities 子包入口
│           └── cloudflare.py                             # 当前 founding provider：Cloudflare Workers actuation / observation
│
├── integrations/                                         # 面向具体平台 / provider 的产品包装与集成边界
│   ├── chatgpt/
│   │   └── README.md                                     # ChatGPT Apps SDK / MCP 集成方向、信任边界和包装说明
│   └── cloudflare/
│       ├── README.md                                     # Cloudflare Capability Provider 集成说明与安全边界
│       └── adapter.json                                  # Cloudflare adapter 的机器可读 operation / authority / failure descriptor
│
├── plugin/                                               # Agent Plugins 1.0 portable 分发包；当前为 Skill-first MVP
│   ├── plugin.json                                       # portable Plugin manifest：name/version/schema/author/repository metadata
│   ├── .codex-plugin/
│   │   └── plugin.json                                   # OpenAI/Codex 产品侧附加 manifest；复用同一 skills/，不复制 runtime
│   ├── README.md                                         # portable/package/distribution 校验、GitHub marketplace 路径、真实 client exercise 与证据边界
│   └── skills/
│       └── svif/
│           └── SKILL.md                                  # Svif 工作流 Skill：首次 Project continuity bootstrap、Agnir discovery/repair、lifecycle、provenance、authority、checkpoint
│
├── spec/                                                 # Svif 内部可移植产品 contracts
│   ├── CORE.md                                           # 编排生命周期、核心 invariants 与 product-kernel 语义
│   ├── PROJECT_BINDING.md                                # Project 如何声明 continuity / execution / capability bindings
│   ├── EVIDENCE.md                                       # Evidence、provenance、subject / target 对齐语义
│   └── CAPABILITY_ADAPTER.md                             # Capability Provider / adapter 的通用 contract
│
├── profiles/                                             # 在通用 contracts 上叠加的专门化行为
│   └── SOFTWARE_DELIVERY.md                              # 软件交付场景：verify → deliver → observe 等专门规则
│
├── schemas/                                              # Svif contracts 的机器可读 schema
│   ├── project-binding.schema.json                       # `project-binding/0.2` 的 JSON Schema
│   ├── capability-adapter.schema.json                    # capability adapter descriptor 的 JSON Schema
│   └── evidence-record.schema.json                       # portable EvidenceRecord 的 JSON Schema
│
├── tests/                                                # 可执行产品实现测试
│   ├── test_runtime.py                                   # Orchestrator kernel、authority、verification、lifecycle 行为
│   ├── test_agnir_continuity.py                          # Agnir Continuity Provider adapter 的 load / checkpoint / failure 行为
│   ├── test_chatgpt_surface.py                           # ChatGPT Execution Surface materialize / parse / identity 约束
│   ├── test_cloudflare_capability.py                     # Cloudflare provider 的 actuation / observation / subject-target 约束
│   ├── test_founding_e2e.py                              # founding Agnir + ChatGPT + Cloudflare 完整产品闭环
│   ├── test_plugin_agnir_discovery.py                    # Plugin Skill 在加载 continuity 前执行 Agnir compatibility/profile/Project identity 校验并锁定 discovery failure 语义
│   ├── test_plugin_component_discovery.py                # Agent Plugins 固定组件位置、直接子 Skill 发现与 MCP failure isolation 回归测试
│   ├── test_plugin_first_use_bootstrap.py                # 普通未初始化 Project 首次启用 Svif 时自动建立 Agnir + Svif durable binding 的回归测试
│   ├── test_plugin_installation_docs.py                  # 双语入口与 Plugin README 的安装证据边界 guardrail，含 GitHub marketplace 路径但禁止把 repository validation 写成 client validation
│   ├── test_plugin_openai_distribution.py                # OpenAI/Codex marketplace source、Codex manifest 与 portable identity metadata 一致性测试
│   └── test_plugin_package.py                            # Plugin manifest/Skill/package、filesystem failure isolation 与 Agnir activation boundary 验证
│
├── conformance/                                          # Portable contracts 的一致性验证，不等同于产品 runtime
│   ├── svif-0.2.md                                       # 当前 Svif 0.2 conformance baseline 的人类可读说明
│   ├── check_contracts.py                                # 对 schemas / fixtures / portable contract 语义执行检查
│   └── fixtures/                                         # conformance 输入样例
│       ├── evidence-chain-positive.json                  # 合法 evidence / provenance chain 正例
│       ├── evidence-chain-provenance-mismatch.json       # provenance 不匹配反例
│       └── adapters/                                     # 各类 adapter descriptor fixture
│           ├── delivery-provider.json                    # delivery / actuation provider fixture
│           ├── observation.json                          # independent observation adapter fixture
│           ├── verification.json                         # verification adapter fixture
│           └── workspace-scm.json                        # workspace / source-control capability fixture
│
├── checks/                                               # 仓库与产品结构完整性检查
│   └── check_repository.py                               # 防止关键模块、README、Plugin packaging、Agnir activation、canonical topology 漂移
│
├── history/                                              # 前身 / 已退休项目历史；仅作 lineage 与 provenance 记录
│   ├── PREDECESSOR.md                                    # ZeroLocal 等 Svif 前身 lineage 说明；通过 commit SHA 定位
│   ├── BRANCH_ARCHIVE.md                                 # 已删除分支及最终 tip SHA 的历史索引；main-only 治理记录
│   └── CLOUDFLARE_REFERENCE.md                           # 已退休独立 Cloudflare reference 仓库的迁移记录
│
├── AGENTS.md                                             # 最小 Agnir 激活 locator；只指向 README canonical Project Instructions
├── AGNIR.yaml                                            # 当前 repository-filesystem profile 下发现本 Project Agnir memory 的入口
├── SVIF.yaml                                             # 本 Project 的 `project-binding/0.2` serialization，并登记 active Plugin artifacts
├── ARCHITECTURE.md                                       # 详细产品架构、依赖方向、provider ownership 和 distribution 边界
├── README.md                                             # 英文项目入口与 canonical `Agnir Project Instructions`
├── README.zh-CN.md                                       # 简体中文项目入口；与英文版保持同一 canonical 产品语义
├── REPOSITORY_TREE.md                                    # 本文件：当前 main 的完整文件级仓库结构与职责说明
└── VERSION                                               # 当前 Svif development version
```

## 如何使用这张树

如果只是第一次理解 Svif，优先看 README 里的简略树即可；需要定位某个具体 contract、fixture、test、Plugin artifact、evidence 或 integration 文件时，再查本页。

本页不是第二套架构定义。**架构语义仍以 `ARCHITECTURE.md`、`spec/`、`SVIF.yaml` 和 canonical Agnir decisions/state 为准；本页负责把这些职责映射回仓库中的实际文件位置。**
