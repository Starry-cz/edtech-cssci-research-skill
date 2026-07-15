# 任务模式与诊断协议

本文件只负责三件事：识别用户要进入的模式、确定最少资源组合、约定可交付输出。章节写作、主论证、终稿自检和审稿意见治理分别由其专门文件承担，避免同一规则在多处重复。

## 使用原则

1. 先选一个主模式；用户同时提出多项需求时，按“问题/理论—设计/证据—写作/交付”的依赖关系拆分。
2. 只有当前输出确实需要时才加载补充资源，不把参考文件当作通用背景材料全部复述。
3. 输出必须标出已知材料、待核验信息和结论边界；没有原始材料时，不补写事实或结果。
4. 所有模式继承同一发布状态：它在内部约束结论强度，不默认占据写作输出。`阻断` 时应提出修复设计与连锁清单，并仍可交付与当前证据相称的自然文本；只有用户要求投稿判断、或风险会改变当前主张时，才在稿外集中说明。`探索性可写` 时可给相称的实证结论与解释；`投稿就绪` 后才作提交判断。状态定义以 `SKILL.md` 为准。

五层分类与 `SKILL.md` 保持一致。每个模式只承担一个主要判断；只有当前输出确实依赖另一层的结论时，才显式联动相应模式或资源。

## 一、研究定位与主线

| 模式 | 何时进入 | 组合资源 | 核心输出 |
| --- | --- | --- | --- |
| `topic_diagnosis` | 只有热点、政策口号或实践困扰 | `topic-diagnosis-and-research-questions.md`、`problem-model-evidence-practice.md`、`external-evidence-and-research-positioning.md` | 七道质量门、对象、情境、机制、证据需求、候选问题与边界 |
| `research_question_refinement` | 题目宽泛、变量与过程混杂 | `topic-diagnosis-and-research-questions.md`、`research-paradigms.md`、`topic-question-evidence-canvas.md` | 主问题、相互依赖子问题、概念定义、可观察证据与不可回答部分 |
| `outline_building` | 不知如何组织论文或章节 | `chapter-synthesis.md`、`good-outline.md`、`weak-outline.md` | 章节功能表、论证顺序与章节间证据接口 |
| `argumentation_blueprint` | 主线不清、贡献悬空或需重构全文 | `academic-writing-and-revision.md`、`claim-evidence-validation-contract.md`、`argumentation-and-revision-workbook-template.md`、`claim-evidence-validation-matrix-template.md` | 问题—回答—证据—贡献—边界主张图与关键主张验证包 |

诊断信号：若题目只出现技术名称或政策口号，先回到 `topic_diagnosis`；若模型仅是要素罗列，先回到 `conceptual_model_building`；若全文各段各说各话，先进入 `argumentation_blueprint`，不要直接润色。

## 二、理论、模型与研究设计

| 模式 | 何时进入 | 组合资源 | 核心输出 |
| --- | --- | --- | --- |
| `conceptual_model_building` | 需要解释“为什么/在何种条件下” | `problem-model-evidence-practice.md`、`research-paradigms.md` | 构念边界、机制链、关系命题、替代解释与检验路径 |
| `practice_model_design` | 需提出教学、系统或实践模型 | `problem-model-evidence-practice.md`、`external-evidence-and-research-positioning.md` | 设计原则、活动链、实施条件和过程/结果证据 |
| `framework_defense` | 被质疑理论不足、框架不新或逻辑跳跃 | `problem-model-evidence-practice.md`、`academic-writing-and-revision.md` | 构念界定、关系依据、反例/替代解释和可证伪点 |

## 三、文献、数据与实证验证

| 模式 | 何时进入 | 组合资源 | 核心输出 |
| --- | --- | --- | --- |
| `literature_review_planning` | 尚未形成可复核的检索与纳排规则 | `literature-search-and-zotero.md`、`literature-review-matrix-template.md` | 检索式、来源、时间边界、纳排规则与编码方案 |
| `literature_search_to_review` | 文献很多但只是作者罗列，或需要精读一篇论文 | `literature-search-and-zotero.md`、`source-grounded-paper-reading.md`、`evidence-and-citation.md` | 主题矩阵、可定位阅读笔记、争议/缺口、主张—来源映射 |
| `citation_and_evidence_check` | 需核验关键引文或论据 | `evidence-and-citation.md` | 已核验/待核验/缺失的证据台账 |
| `education_data_analysis` | 处理问卷、前后测、课堂或平台数据，或需起草统计/图注 | `education-data-analysis.md`、`statistical-reporting-and-figure-evidence.md`、`education-data-analysis-report-template.md`、`claim-evidence-validation-matrix-template.md` | 数据审计、独立单位读出、分析计划、诊断、稳健性与报告边界 |
| `interpretable_ml_analysis` | 做预测、分类、SHAP 或特征解释 | `interpretable-machine-learning.md`、`hierarchical-ml-interpretation.md`、`interpretable-ml-report-template.md`、`abstract-argument-card-template.md` | 内部判定风险，再给切分与泄漏控制、模型比较、解释图、稳定性和复现边界；必要时于稿外说明风险 |

数据任务的前置门槛：先明确分析单位、时间窗口、标签形成和数据来源；再检查缺失、重复、异常、切分、泄漏、隐私与公平。关键主张须有决定性证据、比较/反例、稳健性和边界的最小验证包。预测表现不能直接改写为教育因果效果，解释特征也不能直接等同于干预机制。

## 四、写作、诊断与修订

| 模式 | 何时进入 | 组合资源 | 核心输出 |
| --- | --- | --- | --- |
| `draft_review` | 需要诊断全文或长草稿，或希望做预审稿 | `academic-writing-and-revision.md`、`pre-submission-peer-review.md`、`publication-prose-and-style-control.md`、`self-review.md`、`eight-journal-writing-evidence.md` | 共同事实底稿、三视角风险综合、重构优先级、证据缺口与可选八刊共性诊断；按需给发布状态 |
| `section_revision` | 需修改摘要、引言、综述、方法、结果或讨论 | `writing-workflow.md`、`publication-prose-and-style-control.md`、`abstract-state-and-evidence-control.md`、`chapter-synthesis.md`、`abstract-argument-card-template.md` | 构思层判断、自然清洁正文、必要的证据边界、表层审计与连锁提示；按需说明当前产物类型 |
| `revision_cascade` | 一项修改可能牵动多处内容 | `academic-writing-and-revision.md`、`argumentation-and-revision-workbook-template.md` | 修改层级、传播清单、验证方式和完成状态 |
| `reviewer_response_and_revision` | 收到审稿意见或需准备回应函 | `revision-and-reviewer-response.md`、`reviewer-response-and-revision-ledger-template.md` | 意见台账、回应逻辑、修改位置、连锁更新与证据 |

修订顺序固定为：研究问题与主张、理论/模型、设计与证据、结果—讨论—贡献边界、章节结构、投稿表层、段落与措辞。内部诊断标签、结构标签和待办不得泄漏到论文清洁稿。审稿意见不能只给礼貌回应；每条意见都要标注它影响的层级，以及摘要、图表、附录、回应函是否需同步。

当任务需要“八刊风格诊断”时，不新增一个写作模式：在 `draft_review` 或 `section_revision` 中按需读取 `eight-journal-writing-evidence.md`，只输出同类研究可迁移的论证规则与不适用项，不作录用预测或现时收录判断。

## 五、投稿、工件与专项协作

| 模式 | 何时进入 | 组合资源 | 核心输出 |
| --- | --- | --- | --- |
| `reference_and_artifact_audit` | 核对参考文献、图表、附录、数据说明或投稿文件 | `reference-integrity-and-manuscript-artifacts.md`、`self-review.md`、`submission-package-checklist.md` | 工件清单、交叉引用问题、阻断项与修复顺序 |
| `pre_submission_check` | 投稿前需要整体质量判断 | `self-review.md`、`pre-submission-peer-review.md`、`reference-integrity-and-manuscript-artifacts.md`、`journal-verification.md` | 终稿门槛、预审稿风险、工件与官方核验项、提交判断与待办清单 |

期刊名称、目录、栏目、格式、伦理或政策要求属于待核验事实；除非用户提供官方材料或已完成实时核验，否则只能列为核验任务，不能作为确定要求写入稿件。

## 模式组合的常见边界

- “给我写一篇论文”不是单独模式：先以 `argumentation_blueprint` 或 `outline_building` 明确主线，再进入 `section_revision`。
- “模型/平台已经做出来了”优先进入 `practice_model_design`：补足设计理由与实施证据，不把功能清单包装为效果。
- “我跑出了显著性或 SHAP 图”优先进入 `education_data_analysis` 或 `interpretable_ml_analysis`：补足数据过程、验证与解释边界。
- “按意见改一下”优先进入 `reviewer_response_and_revision`；如意见触及主张、理论或设计，联动 `revision_cascade`。
