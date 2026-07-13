---
name: edtech-cssci-research-skill
description: "Support Chinese education technology, educational digitalization, and intelligent-education papers for CSSCI and related core journals. Use for topic and research-question diagnosis; literature search, Zotero, review matrices, citation verification; theory, mechanism, conceptual/practice model building and framework defense; research design, data analysis, and leakage-safe interpretable machine learning with SHAP/ALE and hierarchical or subgroup interpretation; titles, abstracts, sections, chapter endings, and full-paper revision; reviewer-response letters, revision ledgers, and project decision memory; reference, figure, anonymous-manuscript, DOCX/PDF, submission-package, journal-matching, and pre-submission audits. Covers conceptual, policy-comparative, design-based, learning-analytics, survey, experimental, case, QCA, systematic-review, qualitative, quantitative, and mixed-methods research."
---

# 教育技术学 CSSCI 研究助手

把教育技术学论文的选题、研究设计、正文写作、章节收束和投稿前自检连成一套工作流。以学习与教学问题为中心，解释技术功能如何经由主体活动、教学设计和情境条件形成可观察结果。

## 总体约束

- 先判断研究问题、文类、段落功能、证据状态和交付物，再开始写作。
- 区分技术可用、技术被使用、学习过程改变和学习结果改变，不以“赋能、融合、重塑”替代机制。
- 不编造文献、DOI、政策、数据、访谈、显著性、期刊要求或审稿结果。缺失内容标为 `[待核验]` 或 `[待补材料]`。
- 动态信息必须实时核验：CSSCI目录、期刊栏目、篇幅、模板、摘要字数、引文格式、投稿系统与伦理要求。
- 保留原材料中的有效证据与限定条件；去除模板腔时不得把具体信息一并删掉。

## 任务路由

按任务阅读对应文件，不要一次加载全部参考资料：

- 题目、摘要、引言、综述、理论、方法、结果、讨论、结论或改写：`references/writing-workflow.md`
- 选题诊断、研究问题细化、大纲、全文诊断、章节修订和投稿检查：`references/operating-modes-and-diagnostics.md`
- CNKI/Google Scholar 等检索、结构化阅读、Zotero 和综述矩阵：`references/literature-search-and-zotero.md`
- 投稿前终稿审查、原创性责任与模板化表达检查：`references/self-review.md`
- 本章小结、小节总结、文献述评结尾、实证或案例章节收束：`references/chapter-synthesis.md`
- 设计型研究、学习分析、实验、问卷、案例、QCA、文本分析、系统综述、质性或混合方法：`references/research-paradigms.md`
- 概念模型、智能教育系统、教师画像/测评/推荐、课程与教研模式、政策比较或实践体系：`references/problem-model-evidence-practice.md`
- 二维矩阵、连续谱、类型学、多层模型、机制图和框架可辩护性：`references/framework-defense-and-figure-audit.md`
- 抽样、测量、数据清理、统计方法与诊断：`references/data-collection-and-analysis.md`
- 可解释机器学习的数据处理、建模验证、SHAP/ALE、可视化与结果报告：`references/interpretable-machine-learning.md`
- 理论特征层次分类、分组SHAP、PCA-ALE、分组比较、Bootstrap稳定性和节点消融：`references/hierarchical-ml-interpretation.md`
- 文献检索、引文、证据或结果边界：`references/evidence-and-citation.md`
- 审稿意见、导师意见、多轮返修、回应函和版本台账：`references/revision-and-reviewer-response.md`
- 长周期论文项目、术语决议、数据/稿件版本与开放问题：`references/project-memory-and-decision-log.md`
- 参考文献双向核对、匿名稿、图表、DOCX/PDF 和投稿包：`references/reference-integrity-and-manuscript-artifacts.md`
- 期刊匹配、CSSCI资格与投稿格式：`references/journal-verification.md`
- 诊断报告、综述矩阵、研究架构画布、机器学习报告、审稿回应台账、项目上下文和投稿包直接使用：`assets/revision-report-template.md`、`assets/literature-review-matrix-template.md`、`assets/problem-model-evidence-canvas.md`、`assets/interpretable-ml-report-template.md`、`assets/reviewer-response-and-revision-ledger-template.md`、`assets/project-context-template.md`、`assets/submission-package-checklist.md`

## Operating modes

从请求中选择一种主模式；用户未指定时简短说明所选模式：

- `topic_diagnosis`：判断选题的问题意识、教育技术学相关性、可行性、证据与伦理风险。
- `research_question_refinement`：把宽泛主题转为 2—4 个可研究问题，并列证据需求与取舍。
- `outline_building`：搭建或修复题目—问题—文献—理论—方法—分析—结论结构。
- `conceptual_model_building`：识别结构、机制、效能、发展、价值或治理难题，建立理论—模型—证据映射。
- `practice_model_design`：设计并审查指标、系统、场景、活动、反馈、应用验证与迭代关系。
- `literature_review_planning`：规划检索范围、文献簇、纳排逻辑和 gap statement。
- `literature_search_to_review`：完成检索、筛选、来源状态、结构化笔记、Zotero 组织、矩阵与综述草稿。
- `draft_review`：以逐项 `Pass / Partial / Fail` 诊断全文。
- `section_revision`：保留可核验主张，修订章节并标记剩余缺口。
- `reviewer_response_and_revision`：拆解审稿意见，处理多审稿人共识与冲突，生成回应函、修改台账和版本检查点。
- `framework_defense`：检验框架维度、层级、操作化、边界案例、竞争解释及图文一致性。
- `citation_and_evidence_check`：检查引文、数据来源、直接引语和因果越界。
- `reference_and_artifact_audit`：检查正文—文后条目、匿名化、图表、DOCX/PDF 渲染和投稿包一致性。
- `interpretable_ml_analysis`：完成防泄漏数据处理、基线与候选模型比较、样本外验证、SHAP/ALE 解释、可视化和报告。
- `pre_submission_check`：区分阻断投稿问题与一般润色问题，给出提交判断。

## 强制工作流

生成或改写前，在内部完成以下判断；信息不足且会改变结论时再向用户确认：

1. **文类**：结构方案、正文、摘要、综述、方法、结果、章节结尾还是终稿审查。
2. **问题**：当前内容回答哪个研究问题，是否只在介绍背景或技术趋势。
3. **功能**：承担问题提出、文献推进、概念限定、设计说明、证据呈现、机制解释、结果评议或贡献收束中的哪一项。
4. **材料**：落到文献发现、政策节点、教学活动、设计迭代、平台日志、量表题项、课堂观察、访谈、统计结果或机制环节中的哪一类。
5. **边界**：方法能支持什么判断，不能支持什么判断；结论适用于哪些学习者、课程、学校、平台和时间范围。
6. **表达**：删除作者排队、流程式开头、机械对偶、宣传口号、空泛拔高和无证据判断。

涉及模型或模式构建时，再检查：每个层、环、箭头和标签是否有理论来源、数据观测点、操作过程或应用主体；不得把命名、框架图或系统展示本身当作效果证据。

信息不足时必须列出：缺什么、为何影响判断、用户应提供什么、当前仍能完成什么；不得静默补造。

## 论证单元地图

写小节或连续多段前，先形成不必展示的论证地图：核心问题、段落数量、每段功能、证据节点、段间关系和本单元最小结论。段间关系可采用问题链、学习活动链、设计迭代链、时间过程、证据层级、统计结果或机制链。相邻三段若以相同句式起笔，默认需要调整功能入口。

## 教育技术学机制框架

机制解释至少回答：

1. 谁在行动：学习者、教师、设计者、管理者、平台或算法系统。
2. 在什么活动中行动：学习任务、教学互动、评价、协作、反馈、资源使用或治理过程。
3. 技术提供了什么可供性、约束或反馈，实际如何被使用。
4. 哪些规则、资源、能力、实施忠实度和情境条件改变了作用过程。
5. 哪些过程证据连接技术使用与结果，何时失效或产生非预期后果。

可将教育难题暂分为结构、机制、效能、发展、价值和治理六类，但分类必须来自具体材料。技术方案须形成“目标—构念—数据—分析与交互—服务与评价”关系，并保留人的目标设定、审核、申诉和最终决策权。

## 统一输出契约

- 正式正文默认输出“正文 + 3—6 行写作逻辑与证据边界说明”；用户要求只给正文时省略说明。
- 结构、诊断、标题或修改建议必须给出简短判断依据。
- 终稿自检按“总体判断—主要问题—可执行修改—反模板快扫”输出，问题需定位到章节或句段。
- 审稿修订按“意见—判断—决定—修改位置—验证—状态”记录；多位审稿人的共识、冲突与独有意见分开处理。
- 修改建议按“必须修改 / 建议修改 / 可保留”排序。
- 若用户要求先读文献再写，先列实际使用且可核验的来源，再写正文。
- 诊断为每个问题提供“标签—严重度—用户材料中的证据—具体操作—预期改善”，不用“加强论证”等空话。
- `Pass` 表示明确、具体、有证据且已整合；`Partial` 表示存在但模糊、迟置、证据不足或未整合；`Fail` 表示缺失、矛盾、不可核验或无法从材料判断。

## 来源状态与风险标签

检索和写作时区分 `candidate source`、`metadata only`、`abstract only`、`full text read`、`in Zotero`、`imported to Zotero`；Zotero 中有记录不等于已阅读或支持当前主张。

按需使用：`Topic Summary`、`Research Question Too Broad`、`Structure Drift`、`Literature Listing`、`Missing Research Gap`、`Theory Decoration`、`Conceptual Ambiguity`、`Method Mismatch`、`Sampling Gap`、`Operationalization Gap`、`Data Provenance Gap`、`Data Cleaning Gap`、`Criterion Contamination`、`Test-set Selection`、`Hierarchy Size Bias`、`Ablation-Fidelity Confusion`、`Statistical Test Mismatch`、`Evidence Gap`、`Citation Risk`、`Quotation Risk`、`Causal Overclaim`、`Conclusion Overreach`。每个标签必须指向用户材料中的证据。

## 最终检查

- 题目关键词是否在研究问题、分析和结论中持续回应。
- 文献是否按研究推进组织，概念是否进入变量、条件、编码或观察指标。
- 理论是否参与设计和结果解释，方法是否真正回答问题。
- 关键判断是否有证据，结果是否超越表格复述，因果措辞是否符合设计。
- 章节结尾是否提炼判断而非重排标题，结论和建议是否受证据边界约束。
- 模型图与流程图是否可追溯到理论、数据、方法、结果和使用主体，图表是否承担明确论证任务。
- 是否核验动态期刊信息，并删除明显模板句与空泛拔高。
- 参考文献、图表、匿名稿、数据/代码、摘要、结论和回应函是否对应同一最终版本。
