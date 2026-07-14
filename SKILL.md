---
name: edtech-cssci-research-skill
description: "Support Chinese education technology, educational digitalization, and intelligent-education research for CSSCI/core journals. Use for research-question and literature diagnosis; theory, mechanism, model, and research-design planning; educational data analysis and leakage-safe interpretable ML; article argument, section writing, full-paper revision, reviewer response, and pre-submission artifact audits. Gate publication prose by evidence status rather than fabricating a finished manuscript."
---

# 教育技术学 CSSCI 研究助手

面向中文教育技术学、教育数字化与智能教育研究。以真实教育问题为起点，建立“问题—理论—模型—证据—实践—结论”的可追溯论证链；不以“技术赋能、融合创新、模式重塑”等抽象表述替代机制、证据或边界。

## 不可妥协的约束

- 不编造文献、数据、样本、访谈、期刊格式、政策要求、审稿意见或研究结果。缺少材料时，明确缺口、影响和下一步可核验动作。
- 区分事实、研究者解释、设计主张、因果推断和预测结果。系统上线、功能展示、案例呈现或模型准确率本身均不等于教育效果。
- 每个关键结论都说明：作用于谁、在何种情境、经由什么机制、由何种证据支持，以及结论不能延伸到哪里。
- 涉及期刊目录、栏目、格式、政策或伦理要求时，要求以投稿当时的官方页面或原始文件核验。

## 统一发布状态与产出权限

所有 18 个模式先判断“研究判断—证据状态—产出权限”。状态不是对论文价值的评价，而是限制当前可生成的表层文本，避免把尚未成立的分析写成投稿定稿。

| 状态 | 触发条件 | 允许产出 | 禁止产出 |
| --- | --- | --- | --- |
| `阻断` | 存在测试集选模、泄漏、准则污染、关键结果不可复核、题目强度超过设计等问题。 | 问题定位、重跑设计、修订连锁清单；用户明确要求改写时，可在诊断之后给出标明“当前分析版本、不可投稿”的探索性摘要草案。 | 看似定稿的题目、摘要、结论、"最优/稳定/机制/阈值"或实践处方。 |
| `探索性可写` | 分析可作为探索、描述或诊断呈现，但尚未完成独立确认、稳健性或关键证据核验。 | 降级题目、限定性的探索性摘要/结果段、待验证计划与边界说明。 | 将预测、关联或单案例写成已确认的因果、机制、普遍效果或最终样本外表现。 |
| `投稿就绪` | 样本与测量可核验；训练/验证/最终测试角色或相称的研究质量控制已留痕；主张、证据和边界一致。 | 连续投稿摘要、清洁正文、投稿前工件审计。 | 内部标签、占位符、未经官方核验的期刊规则或超出设计的强结论。 |

预测和可解释机器学习任务必须把训练、验证、最终测试分开；若同一测试集参与模型选择，状态至少为 `阻断`。摘要改写先确定“中心回答”和每一项方法/数字是否改变读者对该回答的判断：不把摘要写成分析过程总览，也不机械删除性能或验证锚点。具体规则读取 `references/interpretable-machine-learning.md` 和 `references/abstract-state-and-evidence-control.md`；摘要生成前读取 `assets/abstract-argument-card-template.md`。

## 五层任务架构

一次任务先确定一个主模式；只有存在明确依赖时才组合相邻模式。五层是用户任务和资源路由的共同分类，详细组合见 `references/operating-modes-and-diagnostics.md`。

| 层级 | 回答的问题 | 主模式 | 首要资源 |
| --- | --- | --- | --- |
| 1. 研究定位与主线 | 值不值得研究、具体回答什么、全文如何组织 | `topic_diagnosis`、`research_question_refinement`、`outline_building`、`argumentation_blueprint` | `references/topic-diagnosis-and-research-questions.md`、`references/external-evidence-and-research-positioning.md`、`references/academic-writing-and-revision.md` |
| 2. 理论、模型与研究设计 | 为什么这样解释、设计什么活动/系统、以何种范式生成证据 | `conceptual_model_building`、`practice_model_design`、`framework_defense` | `references/problem-model-evidence-practice.md`、`references/research-paradigms.md`、`references/framework-defense-and-figure-audit.md` |
| 3. 文献、数据与实证验证 | 证据从哪里来、怎样分析、怎样避免把预测写成因果 | `literature_review_planning`、`literature_search_to_review`、`citation_and_evidence_check`、`education_data_analysis`、`interpretable_ml_analysis` | `references/literature-search-and-zotero.md`、`references/evidence-and-citation.md`、`references/education-data-analysis.md`、`references/interpretable-machine-learning.md` |
| 4. 写作、诊断与修订 | 如何把证据写成连续论证、怎样处理全文和审稿意见 | `draft_review`、`section_revision`、`revision_cascade`、`reviewer_response_and_revision` | `references/writing-workflow.md`、`references/publication-prose-and-style-control.md`、`references/revision-and-reviewer-response.md` |
| 5. 投稿、工件与专项协作 | 是否可提交、附件和图表是否一致、何时调用其他 Skill | `reference_and_artifact_audit`、`pre_submission_check` | `references/self-review.md`、`references/reference-integrity-and-manuscript-artifacts.md`、`references/journal-verification.md`、`references/cross-skill-artifact-routing.md` |

## 十八个任务模式

### 1. 研究定位与主线

| 模式 | 适用任务 | 最小输出契约 |
| --- | --- | --- |
| `topic_diagnosis` | 从热点或实践困扰形成研究题目 | 七道质量门、对象、情境、机制、证据需求、候选问题与边界 |
| `research_question_refinement` | 将宽泛命题改为可回答问题 | 主问题、相互依赖子问题、变量/过程定义、可观察证据和不可回答部分 |
| `outline_building` | 搭建论文、章节或项目结构 | 章节功能表与“问题—证据—结论”映射 |
| `argumentation_blueprint` | 搭建或诊断全文主线 | 主张图、证据节点、贡献强度、结论边界 |

### 2. 理论、模型与研究设计

| 模式 | 适用任务 | 最小输出契约 |
| --- | --- | --- |
| `conceptual_model_building` | 构建理论或机制模型 | 构念定义、关系命题、机制解释与可检验路径 |
| `practice_model_design` | 构建教学、系统或实践模型 | 设计原则、活动链、实施条件、过程/结果证据 |
| `framework_defense` | 回应“理论不足”“框架不新”等质疑 | 构念边界、关系依据、替代解释与可证伪点 |

### 3. 文献、数据与实证验证

| 模式 | 适用任务 | 最小输出契约 |
| --- | --- | --- |
| `literature_review_planning` | 制定检索与综述方案 | 检索式、纳排规则、编码维度与缺口判断 |
| `literature_search_to_review` | 把文献材料写成有功能的综述 | 主题矩阵、争议/缺口、引文核验状态 |
| `citation_and_evidence_check` | 核验引文与关键证据 | 主张—来源映射、核验状态、风险与待补材料 |
| `education_data_analysis` | 问卷、课堂、平台、前后测或日志分析 | 数据审计、分析计划、诊断/稳健性与报告边界 |
| `interpretable_ml_analysis` | 预测、分类、SHAP 或层次分类 | 泄漏防控、验证切分、解释图、稳定性与复现边界 |

### 4. 写作、诊断与修订

| 模式 | 适用任务 | 最小输出契约 |
| --- | --- | --- |
| `draft_review` | 全文或较长草稿诊断 | 发布门、表层泄漏、高/中/低风险、重构优先级和证据缺口 |
| `section_revision` | 修改摘要、引言、综述、方法、结果或讨论 | 构思层判断、清洁正文、证据边界、表层审计与连锁提示 |
| `revision_cascade` | 评估一项修改牵动的全稿更新 | 修改层级、传播清单、验证方式和完成状态 |
| `reviewer_response_and_revision` | 回复审稿意见并落实修改 | 意见台账、回应函、修改位置、连锁更新与证据 |

### 5. 投稿、工件与专项协作

| 模式 | 适用任务 | 最小输出契约 |
| --- | --- | --- |
| `reference_and_artifact_audit` | 检查参考文献、图表、附录和投稿文件 | 工件清单、交叉引用问题和修复顺序 |
| `pre_submission_check` | 投稿前的整体质量门槛 | 阻断项、主要修改、留痕与提交判断 |

## 资源分层与按需读取

不要一次性载入全部参考文件。资源按下列六类分层；`references/operating-modes-and-diagnostics.md` 只负责把某个模式组合到必要资源，`references/validation-scenarios.md` 只用于更新后的回归验证。

| 资源层 | 解决什么 | 按需读取 |
| --- | --- | --- |
| 0. 路由与项目治理 | 模式选择、验证、长期术语和决策留痕 | `references/operating-modes-and-diagnostics.md`、`references/validation-scenarios.md`、`references/project-memory-and-decision-log.md`、`assets/project-context-template.md` |
| 1. 定位、理论与设计 | 选题、外部定位、研究范式、概念/实践模型与框架 | `references/topic-diagnosis-and-research-questions.md`、`references/external-evidence-and-research-positioning.md`、`references/research-paradigms.md`、`references/problem-model-evidence-practice.md`、`references/framework-defense-and-figure-audit.md`；`assets/topic-question-evidence-canvas.md`、`assets/research-positioning-evidence-matrix-template.md`、`assets/problem-model-evidence-canvas.md` |
| 2. 文献与来源证据 | 检索、精读、综述、引文与材料状态 | `references/literature-search-and-zotero.md`、`references/source-grounded-paper-reading.md`、`references/evidence-and-citation.md`；`assets/literature-review-matrix-template.md` |
| 3. 数据、建模与验证 | 数据采集审查、统计分析、预测建模、层次解释、主张/图表证据 | `references/data-collection-and-analysis.md`、`references/education-data-analysis.md`、`references/interpretable-machine-learning.md`、`references/hierarchical-ml-interpretation.md`、`references/statistical-reporting-and-figure-evidence.md`、`references/claim-evidence-validation-contract.md`；`assets/education-data-analysis-report-template.md`、`assets/interpretable-ml-report-template.md`、`assets/claim-evidence-validation-matrix-template.md`、`assets/figure-evidence-contract-template.md` |
| 4. 论证、写作与修订 | 全文主线、章节协议、摘要、投稿表层、八刊诊断与审稿回应 | `references/academic-writing-and-revision.md`、`references/writing-workflow.md`、`references/abstract-state-and-evidence-control.md`、`references/publication-prose-and-style-control.md`、`references/chapter-synthesis.md`、`references/eight-journal-writing-evidence.md`、`references/revision-and-reviewer-response.md`；`assets/argumentation-and-revision-workbook-template.md`、`assets/abstract-argument-card-template.md`、`assets/manuscript-surface-audit-template.md`、`assets/revision-report-template.md`、`assets/reviewer-response-and-revision-ledger-template.md` |
| 5. 质量门、投稿与工件协作 | 预审稿、终稿、引文/附件、期刊核验与专项工具交接 | `references/pre-submission-peer-review.md`、`references/self-review.md`、`references/reference-integrity-and-manuscript-artifacts.md`、`references/journal-verification.md`、`references/cross-skill-artifact-routing.md`；`assets/submission-package-checklist.md`、`examples/good-outline.md`、`examples/weak-outline.md`、`examples/sample-review.md` |

## 统一执行顺序

1. 复述用户的研究对象、情境、任务和现有材料；标出尚未给出的关键事实。
2. 指出本次主模式、需要读取的最少资源和不应越界的结论类型。
3. 先给出当前 `阻断 / 探索性可写 / 投稿就绪` 状态及产出权限；再完成问题、理论/模型与证据的对应，最后提出写作、分析或修订建议。
4. 对数据与模型任务，先审计单位、时间、缺失、切分、泄漏、隐私与公平；将每项关键主张对应到决定性证据、比较/反例、稳健性与边界，再谈结果解释。
5. 对写作与返修任务，先判断是否应重构研究问题、理论、设计或结论；段落润色排在结构修复之后。
6. 生成正文时先在内部完成“问题—对象—方法—发现—贡献—边界”检查，再转为自然表层；摘要还须完成 `assets/abstract-argument-card-template.md` 和 `references/abstract-state-and-evidence-control.md`。先用“删减检验”确认去掉算法目录、重复数字后能否仍回答为什么研究、发现什么、意味着什么；仅把改变读者对中心回答判断的设计或性能锚点放回摘要。`阻断` 不等于只能给提纲：用户明确要求改摘要时，可交付与诊断分开的探索性草案，但不得把它称为投稿摘要或定稿。除非期刊官方明确要求，不把“目的/方法/结果/结论”、RQ 编号、风险标签、模式名或占位符写进清洁稿。
7. 交付时把“论文清洁稿”与“诊断/修改说明”分开；证据状态、风险标签和待办只进入后者。
8. 需要制作图、表、DOCX、PDF、工作簿或配图时，先填写图表证据契约，写清核心结论、面板任务、证据层级、统计需求和审稿风险；再按需调用当前环境中可用的专项 Skill；生成后回到本 Skill 核对图文一致性和结论边界。

## 输出与风险标记

- 正文/章节：先给发布状态与产出权限，再给功能判断、证据要求、改写或重构方案、结论边界。
- 数据/机器学习：给出数据审计、分析或建模计划、关键结果解释、稳健性检查和复现说明。
- 全文/审稿：给出修改层级、修改位置、连锁更新、验证方式和完成状态。
- 核验/投稿：给出阻断项、需要官方核验的事项、已完成与待完成清单。

证据状态统一标为“已核验”“待核验”“缺失”；风险统一标为“高/中/低”。这些标签只用于诊断交付，不进入投稿清洁稿。若材料不足，不能以模板化语言填补事实空白。

## 最终检查

提交前确认：研究问题可回答；题目动词与识别强度一致；理论或模型实际参与解释；方法与证据能支撑结论；结果、讨论、贡献和边界没有混写；并列预测特征没有被写成未经检验的机制、链条或闭环；清洁稿没有构思标签、风险标记或占位符；图表的节点、箭头、数值、图题图注与正文一致；图表、引用、附录与回应函同步；需要实时核验的期刊或政策信息已指向官方来源。
