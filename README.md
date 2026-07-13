<p align="center">
  <img src="assets/readme-hero.svg" alt="教育技术学 CSSCI 研究助手：问题、理论、模型、证据、实践与结论形成可追溯论证链" width="100%" />
</p>

# 教育技术学 CSSCI 研究助手

<p align="center"><strong>从真实教育问题出发，把“问题—理论—模型—证据—实践—结论”做成可追溯的研究论证链。</strong></p>

<p align="center">
  <a href="#一分钟开始"><strong>一分钟开始</strong></a> ·
  <a href="#从你的问题开始"><strong>按任务进入</strong></a> ·
  <a href="#能力全景"><strong>查看能力全景</strong></a> ·
  <a href="#文件功能速查"><strong>查找文件</strong></a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg" alt="CC BY 4.0 许可" /></a>
  <img src="https://img.shields.io/badge/语言-中文-d9480f.svg" alt="中文" />
  <img src="https://img.shields.io/badge/领域-教育技术学-6f42c1.svg" alt="教育技术学" />
  <img src="https://img.shields.io/badge/14-任务模式-0f766e.svg" alt="14 个任务模式" />
  <img src="https://img.shields.io/badge/18-研究参考模块-2563eb.svg" alt="18 个研究参考模块" />
  <img src="https://img.shields.io/badge/8-可复用模板-a16207.svg" alt="8 个可复用模板" />
</p>

> 一个面向中文教育技术学、教育数字化与智能教育研究的 Codex Skill，贯通选题诊断、文献检索、理论与模型建构、研究设计、实证数据分析与建模、论文写作及投稿前自检。

## 从你的问题开始

不用先理解全部文件。找到你此刻最需要完成的工作，复制对应提示词即可启动。

| 你正卡在什么地方？ | 立即进入 | 你会得到什么 |
|---|---|---|
| 热点很大，不知道怎样形成可研究的题目 | [选题与研究问题](references/operating-modes-and-diagnostics.md) | 有对象、情境、机制、证据需求与边界的候选选题 |
| 文献很多，但综述只是作者罗列 | [文献与理论](references/literature-search-and-zotero.md) | 可复现的检索路径、综述矩阵与研究缺口 |
| 有模型或框架，却经不起“为什么这样分”的追问 | [理论、模型与框架](references/problem-model-evidence-practice.md) | 理论—构念—证据映射与框架防御方案 |
| 有问卷、前后测、课堂或平台数据，或想做预测与 SHAP | [实证数据分析与建模](#实证数据分析与建模) | 从数据审计、统计推断到防泄漏预测、解释与稳健性检验的分层方案 |
| 收到审稿意见，或准备投 CSSCI/中文核心 | [返修与投稿](references/revision-and-reviewer-response.md) | 意见台账、回应函、终稿自检与投稿包清单 |

## 为什么这个 Skill 值得安装

它不是通用“论文润色器”。它将教育技术研究中的技术、学习者、教师、教学活动、情境条件与证据链放在同一张论证图中，帮助你把研究做实、写清、审严。

| 核心优势 | 对你的直接价值 | 它拒绝什么 |
|---|---|---|
| **机制先于口号** | 追问技术通过何种活动与条件影响谁、影响什么，而非只描述“采用了技术” | 用“技术赋能、融合创新、模式重塑”替代解释 |
| **证据贯穿全程** | 把问题、理论、研究设计、数据、结果与结论逐一对应 | 只有漂亮概念或显著性结果、没有可追溯证据 |
| **实证数据分析与建模一体化** | 从数据审计、测量、推断、多层/纵向分析，到防泄漏预测、样本外验证、SHAP/ALE 与稳定性检验 | 只报 *p* 值，或把相关、预测、特征重要性和模型表现误作因果效应 |
| **面向中文期刊的最终交付** | 兼顾匿名、引文、图表、DOCX/PDF 渲染与实时投稿规范核验 | 编造期刊要求、参考文献、数据或审稿结果 |

## 一分钟开始

### 1. 安装到 Codex

```bash
git clone https://github.com/Starry-cz/edtech-cssci-research-skill.git ~/.codex/skills/edtech-cssci-research-skill
```

Windows PowerShell：

```powershell
git clone https://github.com/Starry-cz/edtech-cssci-research-skill.git "$HOME\.codex\skills\edtech-cssci-research-skill"
```

也可以下载 ZIP，将整个文件夹解压到 Codex skills 目录，再重新启动或刷新 Codex。

### 2. 用一个真实问题启动

```text
使用 $edtech-cssci-research-skill，诊断我的教育技术学论文。
研究主题：[填写]
当前阶段：[选题 / 综述 / 设计 / 分析 / 写作 / 返修 / 投稿]
已有材料：[填写]
目标期刊：[可选]

请先判断最适合的任务模式，再指出当前最关键的问题、需要的证据和下一步动作。
```

### 3. 获得一份可执行的研究下一步

Skill 会先补足问题与证据链，再给出符合你当前阶段的输出；若材料不足，会明确标记缺口与影响，不会以虚构文献、数据或期刊规则填补。

## 跨平台使用

Codex 版本支持任务路由与按需读取参考文件；研究规则本身并不局限于 Codex。仓库现提供可直接粘贴到项目指令、助手指令或对话首条消息的跨平台版本。

| 平台或场景 | 推荐入口 | 使用方式 |
|---|---|---|
| 任意支持自定义提示词的 AI 平台 | [通用核心指令](platforms/universal-research-assistant.md) | 粘贴到系统提示词、项目指令或对话首条消息 |
| ChatGPT | [ChatGPT 适配说明](platforms/chatgpt.md) | 优先使用 Project；也可配置 Custom GPT |
| Claude | [Claude 适配说明](platforms/claude.md) | 使用 Project Instructions 与 Project Knowledge |
| Gemini | [Gemini 适配说明](platforms/gemini.md) | 创建 Gem，并添加必要的 Knowledge 文件 |

完整说明与按任务上传的知识文件组合见 [跨平台使用说明](platforms/platform-guide.md)。不同平台不会自动读取整个 GitHub 仓库；涉及某一专题时，请上传相关 `references/` 文件，或在对话中粘贴必要材料。

## 能力全景

```mermaid
flowchart LR
    A[真实教育问题] --> B[理论解释]
    B --> C[模型或研究设计]
    C --> D[可核验证据]
    D --> E[教育实践与应用]
    E --> F[有边界的结论]
    F -.反思与迭代.-> A
```

| 研究阶段 | 主要工作 | 可交付结果 |
|---|---|---|
| **发现问题** | 选题诊断、对象与情境界定、研究问题精炼 | 选题画布、问题链、证据需求清单 |
| **建立论证** | 文献检索、综述、理论、机制、概念模型与框架审查 | 检索日志、综述矩阵、理论—构念—证据表 |
| **设计研究** | DBR、实验/准实验、问卷、质性、混合方法、学习分析 | 可执行的研究设计、数据字典、分析计划 |
| **分析数据** | 描述、测量、推断、多层/纵向、教育机器学习与可视化 | 结果表图、稳健性说明、教育解释与结论边界 |
| **写作与交付** | 全文诊断、章节改写、审稿回应、匿名与投稿包自检 | 修订报告、回应函、投稿前清单 |

## 任务导航

不用先理解全部文件。找到你当前的问题，复制最后一列的问法即可。

| 你现在需要什么 | 推荐模式 | 主要入口 | 可以这样问 |
|---|---|---|---|
| 把宽泛热点变成可研究选题 | `topic_diagnosis` | [任务模式](references/operating-modes-and-diagnostics.md) | “把‘AI赋能教育’改成三个可研究的CSSCI选题” |
| 凝练研究问题、对象与范围 | `research_question_refinement` | [任务模式](references/operating-modes-and-diagnostics.md) | “检查这些研究问题是否可回答，并说明需要什么证据” |
| 搭建或修复论文大纲 | `outline_building` | [写作工作流](references/writing-workflow.md) | “按问题—证据—结论关系重构这份大纲” |
| 检索中英文文献、整理 Zotero | `literature_search_to_review` | [检索与 Zotero](references/literature-search-and-zotero.md) | “生成检索式、筛选日志、Zotero标签和综述矩阵” |
| 写文献综述、理论框架或机制 | `section_revision` | [写作工作流](references/writing-workflow.md) | “把作者罗列式综述改成围绕争论推进的综述” |
| 构建概念模型、实践模式或智能系统 | `conceptual_model_building` / `practice_model_design` | [问题—模型—证据—实践](references/problem-model-evidence-practice.md) | “检查模型每个节点是否有理论、数据、活动和验证证据” |
| 审查二维框架、类型学或机制图 | `framework_defense` | [框架防御与图示审计](references/framework-defense-and-figure-audit.md) | “检查维度依据、边界案例、缺失象限和图中箭头” |
| 设计问卷、实验、DBR、质性或混合研究 | 按研究范式选择 | [研究范式](references/research-paradigms.md) | “为这个问题比较实验、DBR和混合方法的适配性” |
| 开展教育数据分析 | `education_data_analysis` | [教育数据分析](references/education-data-analysis.md) | “为问卷、前后测和班级嵌套数据设计完整分析流程” |
| 审查抽样、测量、清洗和统计分析 | `draft_review` | [数据采集与分析](references/data-collection-and-analysis.md) | “检查分析单位、缺失处理、统计检验和因果措辞” |
| 开展教育可解释机器学习 | `interpretable_ml_analysis` | [可解释机器学习](references/interpretable-machine-learning.md) | “设计防泄漏建模、样本外验证、SHAP/ALE和图表流程” |
| 处理层次 SHAP、PCA-ALE 与稳定性 | `interpretable_ml_analysis` | [层次机器学习解释](references/hierarchical-ml-interpretation.md) | “审查维度汇总、分组排名、Bootstrap和节点消融” |
| 严格诊断或修改整篇论文 | `draft_review` / `section_revision` | [终稿自检](references/self-review.md) | “按Pass/Partial/Fail定位问题，并给出可执行修法” |
| 降低模板腔、宣传腔和机械表达 | `pre_submission_check` | [原创性与反模板快扫](references/self-review.md) | “按章节定位模板句和空泛句，保留数据、引用与结论边界” |
| 回应导师、同行或匿名审稿意见 | `reviewer_response_and_revision` | [审稿回应与修订治理](references/revision-and-reviewer-response.md) | “整理意见冲突，生成回应函和修订台账” |
| 写本章小结或文献述评结尾 | `section_revision` | [章节收束](references/chapter-synthesis.md) | “提炼本章判断并自然引向下一章，不复述小标题” |
| 核查引用、因果与证据真实性 | `citation_and_evidence_check` | [证据与引用](references/evidence-and-citation.md) | “建立主张—证据—来源状态表，标出越界结论” |
| 核验期刊、CSSCI目录和投稿规则 | `pre_submission_check` | [期刊核验](references/journal-verification.md) | “只使用当前官方来源核验目标期刊投稿要求” |
| 检查匿名稿、图表、DOCX/PDF 和投稿包 | `reference_and_artifact_audit` | [稿件工件质检](references/reference-integrity-and-manuscript-artifacts.md) | “核对引文、匿名信息、图表和最终渲染” |

## 细化能力与研究边界

| 核心优势 | 它具体做什么 | 避免什么问题 |
|---|---|---|
| **真实问题驱动** | 从学习、教学、评价、教师发展或教育治理中的矛盾进入 | 把技术热点或政策口号直接当作研究问题 |
| **机制解释优先** | 连接主体、活动、技术功能、实际使用、情境、过程证据和结果 | 从“有技术”直接跳到“有效果” |
| **论证链可追溯** | 检查问题—理论—模型—证据—实践—结论是否逐环闭合 | 模型命名漂亮但没有理论、数据或验证 |
| **研究范式完整** | 覆盖 DBR、学习分析、问卷、实验、质性、QCA、系统综述和混合方法 | 用教材式方法介绍代替针对研究问题的设计 |
| **实证数据分析与建模一体化** | 从数据审计、测量、统计推断、多层/纵向模型，到防泄漏预测、样本外验证、SHAP/ALE 与稳定性检验 | 只报 p 值，或把相关、预测、特征重要性和模型表现误作因果效应 |
| **证据状态透明** | 区分候选来源、元数据、摘要、全文阅读和 Zotero 状态 | 把“搜到”“导入”误写成“读过并支持结论” |
| **修订过程可治理** | 管理多审稿人意见、冲突、回应函、修改位置、验证和版本 | 只写“已认真修改”却无法定位实际变化 |
| **投稿交付完整** | 审查引文、匿名稿、图表、DOCX/PDF 渲染和投稿包 | 内容已定稿但因格式、匿名或版本错位返工 |
| **原创性而非检测规避** | 修复模板句、机械对偶、宣传腔和无证据判断 | 预测AI率、插入错误或提供检测规避技巧 |

## 完整研究工作流

| 阶段 | 主要任务 | 典型交付物 | 对应文件 |
|---|---|---|---|
| 1. 选题与问题意识 | 识别真实教育矛盾、对象、场景、范围、证据与伦理风险 | 选题诊断、候选研究问题、证据需求 | [任务模式](references/operating-modes-and-diagnostics.md) |
| 2. 文献检索与综述 | 中英文概念簇、完整检索式、筛选、结构化阅读、Zotero、研究缺口 | 检索日志、阅读笔记、综述矩阵、gap statement | [检索与 Zotero](references/literature-search-and-zotero.md) · [综述矩阵模板](assets/literature-review-matrix-template.md) |
| 3. 理论、机制与模型 | 让理论进入概念、变量、设计、编码、解释和边界 | 理论—部件—证据表、机制链、概念模型 | [问题—模型—证据—实践](references/problem-model-evidence-practice.md) · [研究画布](assets/problem-model-evidence-canvas.md) |
| 4. 研究设计与数据 | 选择范式，界定样本、测量、数据生成、分析单位、清洗、统计/预测模型与识别条件 | 研究设计、数据字典、分析计划、伦理与权限清单 | [研究范式](references/research-paradigms.md) · [教育数据分析](references/education-data-analysis.md) · [可解释机器学习](references/interpretable-machine-learning.md) · [分析报告模板](assets/education-data-analysis-report-template.md) |
| 5. 结果、讨论与写作 | 组织题目、摘要、引言、综述、方法、结果、讨论和结论 | 正文章节、证据边界说明、章节结尾 | [写作工作流](references/writing-workflow.md) · [章节收束](references/chapter-synthesis.md) |
| 6. 诊断、返修与回应 | 全文诊断、框架防御、多审稿人意见处理和版本传播检查 | 修订报告、回应函、修改台账 | [终稿自检](references/self-review.md) · [修订治理](references/revision-and-reviewer-response.md) · [修订台账模板](assets/reviewer-response-and-revision-ledger-template.md) |
| 7. 投稿与交付 | 动态期刊核验、引文一致性、匿名化、图表和最终文件检查 | 投稿判断、匿名稿、投稿包清单 | [期刊核验](references/journal-verification.md) · [稿件工件质检](references/reference-integrity-and-manuscript-artifacts.md) · [投稿包清单](assets/submission-package-checklist.md) |

## 专项研究方法

### 教育技术学研究范式

| 研究类型 | Skill 重点检查 | 可以这样问 |
|---|---|---|
| 设计型研究（DBR） | 真实问题、理论驱动设计、迭代证据、修改理由和设计原则 | “检查两轮设计修改是否由课堂证据支持，并提炼设计原则” |
| 学习分析与教育数据挖掘 | 日志生成、分析单位、时间窗口、特征、验证切分、隐私与公平 | “审查日志时间窗口、特征构造和验证切分是否存在泄漏” |
| 问卷、回归与结构方程 | 量表来源、情境适配、样本结构、测量质量与结构逻辑 | “检查量表质量、样本结构与机制路径是否匹配” |
| 实验与准实验 | 分配方式、对照条件、实施忠实度、效应量、污染与剩余偏差 | “判断该研究的分配、对照与效应量报告是否支持结论” |
| 案例、访谈与质性研究 | 案例选择、研究者位置、编码、过程证据、反例与替代解释 | “审查案例选择、编码链、反例与替代解释是否充分” |
| QCA 与综合评价 | 条件选择、校准、必要/充分性、一致性、覆盖度和反事实 | “检查条件校准与必要/充分性分析是否可以复核” |
| 政策与计算文本分析 | 语料来源、时间边界、筛选、编码规则和可复核性 | “界定语料来源、时间边界和编码规则，并检查可复核性” |
| 系统综述与元分析 | 协议、数据库、检索式、纳排、质量评价与综合方法 | “设计可复现的检索、纳排、质量评价与综合方案” |
| 混合方法 | 设计类型、整合节点、冲突处理和整合后的新增认识 | “确定量化与质性材料的整合节点及冲突处理方式” |

完整规则见 [research-paradigms.md](references/research-paradigms.md)。

### 实证数据分析与建模

教育数据分析与可解释机器学习属于同一类实证工作：先根据研究问题、数据结构和结论目标选择分析路径，再使用相应方法建立证据。

| 你的目标 | 优先路径 | 结论边界 |
|---|---|---|
| 描述差异、检验关系、估计干预或解释机制 | 教育数据分析：测量、统计推断、回归、SEM、多层或纵向模型 | 结论强度取决于设计、测量、识别条件与稳健性 |
| 预测学习结果、识别风险模式、比较模型并解释特征贡献 | 可解释机器学习：防泄漏切分、样本外验证、SHAP/ALE 与稳定性检验 | 预测表现和特征贡献不等于因果效应 |

两条路径可以衔接，但不能互相替代：统计推断回答“在何种条件下存在何种关系或差异”，预测建模回答“基于何种已有信息能够多好地预测目标”。

#### 教育数据分析

面向问卷、测验、课堂观察、前后测、平台日志、教师/学校调查和追踪数据，形成从数据质量到教育解释的完整链条：

```text
研究问题与估计对象
  → 数据字典与样本流向
  → 清理、缺失与变量构造
  → 描述统计与可视化
  → 测量与构念质量
  → 推断模型与诊断
  → 稳健性与不确定性
  → 教育解释、复现与结论边界
```

支持：

- 描述统计、分布与组别/时间可视化
- 量表计分、信度、结构效度、跨组或跨时可比性
- 组间/配对比较、回归、广义模型、中介与调节
- CFA、SEM、潜变量关系与替代模型
- 班级/学校嵌套、多层数据、重复测量与纵向轨迹
- 干预、准实验和观察性数据的识别条件与因果边界
- 效应量、置信区间、模型诊断、多重比较与敏感性分析
- 结果表图、论文写作、分析记录、代码/语法与数据可用性说明

入口：[education-data-analysis.md](references/education-data-analysis.md) · [数据采集与分析审查](references/data-collection-and-analysis.md) · [分析报告模板](assets/education-data-analysis-report-template.md)

#### 可解释机器学习

这不是“跑一个随机森林再画 SHAP 图”，而是一条从数据生成到结论边界的完整分析链：

```text
预测目标与时点
  → 分组/时间切分
  → 训练折内预处理
  → 透明基线与候选模型
  → 样本外性能与不确定性
  → SHAP / ALE / 置换重要性
  → 层次、分组与稳定性分析
  → 教育含义、风险与因果边界
```

支持：

- 学习者、班级、学校或时间层面的防泄漏切分
- 透明基线、随机森林、Boosting 等多模型比较
- 训练/验证/最终测试集隔离与样本外报告
- SHAP、ALE、置换重要性与相关特征解释
- 理论维度汇总、层次 SHAP、PCA-ALE 与分组比较
- Bootstrap 稳定性、节点消融、敏感性和可视化
- CSSCI 论文中的方法、结果、图表与安全措辞

入口：[interpretable-machine-learning.md](references/interpretable-machine-learning.md) · [hierarchical-ml-interpretation.md](references/hierarchical-ml-interpretation.md) · [报告模板](assets/interpretable-ml-report-template.md)

### 概念模型、实践模式与框架防御

模型研究按“目标—构念—数据—分析与交互—服务与评价”审查。每个层、环、箭头和标签都要能够回溯到理论来源、观测证据、操作过程或应用主体。

矩阵、连续谱、类型学和机制图还会检查：

- 为什么选择这些维度，竞争性维度为何不采用
- 不同维度是否处在可比较的分析层级
- 理论组合与实际类型不一致时如何解释
- 边界案例能否按操作化标准被复核
- 是否为了图形整齐而过度简化经验材料
- 图中箭头、颜色和位置是否暗示了正文没有证明的关系

入口：[problem-model-evidence-practice.md](references/problem-model-evidence-practice.md) · [framework-defense-and-figure-audit.md](references/framework-defense-and-figure-audit.md)

## 十四类任务模式

Skill 会根据用户请求选择一种主模式，并按需加载对应资料，而不是一次读取全部文件。

| 模式 | 适用任务 | 核心产出 |
|---|---|---|
| `topic_diagnosis` | 选题价值、范围、相关性、证据与伦理风险 | 选题判断与聚焦方向 |
| `research_question_refinement` | 把主题改成可回答的问题 | 候选问题、分析单位、证据与方法 |
| `outline_building` | 新建或修复论文结构 | 章节—功能—证据—问题对应表 |
| `conceptual_model_building` | 理论、机制、概念框架和模型 | 理论—模型—证据映射 |
| `practice_model_design` | 系统、画像、测评、推荐和实践模式 | 目标—构念—数据—交互—评价设计 |
| `literature_review_planning` | 综述范围、概念簇、纳排与研究缺口 | 检索和综述方案 |
| `literature_search_to_review` | 从检索到 Zotero、矩阵和综述草稿 | 可追溯文献工作流 |
| `draft_review` | 全文或章节诊断 | `Pass / Partial / Fail` 证据化报告 |
| `section_revision` | 题目、摘要、引言、综述、方法、讨论等改写 | 修订正文、变更说明与剩余风险 |
| `reviewer_response_and_revision` | 导师、同行或匿名审稿返修 | 回应函、意见矩阵、修订台账 |
| `framework_defense` | 二维框架、连续谱、类型学和机制图 | 框架风险与图示重构方案 |
| `education_data_analysis` | 教育数据审计、清理、描述、测量、推断、回归、SEM、多层与纵向分析 | 分析计划、结果报告与复现边界 |
| `citation_and_evidence_check` | 引文、来源、证据和因果边界 | 主张—证据—来源状态表 |
| `reference_and_artifact_audit` | 参考文献、匿名稿、图表、DOCX/PDF | 投稿工件检查与阻断项 |
| `interpretable_ml_analysis` | 教育预测与可解释机器学习 | 防泄漏建模、解释、稳定性与图表方案 |
| `pre_submission_check` | CSSCI/中文核心投稿前终审 | `submit / revise / restructure` 判断 |

## 可直接复制的提示词

<details>
<summary><strong>选题诊断与研究问题</strong></summary>

```text
使用 $edtech-cssci-research-skill，把“生成式人工智能促进大学生深度学习”改造成三个可研究的CSSCI选题。

每个选题说明：真实教育问题、研究对象、活动场景、技术作用机制、所需证据、适配方法和结论边界。不要虚构文献。
```

</details>

<details>
<summary><strong>文献检索、Zotero 与综述</strong></summary>

```text
使用 $edtech-cssci-research-skill，为“生成式人工智能反馈与大学生论证写作修订”设计中英文检索式、数据库组合、纳排标准、筛选日志、Zotero标签和综述矩阵。

请区分 candidate source、metadata only、abstract only、full text read 和 Zotero 状态。没有阅读全文的来源不要写成已核实结论。
```

</details>

<details>
<summary><strong>理论、模型与图表审查</strong></summary>

```text
使用 $edtech-cssci-research-skill，诊断这个教师—智能体协同教学模型。

先识别主难题，再检查每个节点、层级和箭头是否有理论、数据、教学活动、使用主体和验证证据；区分模型提出、技术实现、可用性、初步效果、机制成立和可推广性，并给出图表重构方案。
```

</details>

<details>
<summary><strong>研究设计与数据分析</strong></summary>

```text
使用 $edtech-cssci-research-skill，审查这项平台日志研究。

重点检查数据生成、分析单位、预测时点、缺失处理、特征构造、训练/验证隔离、统计方法、隐私与因果措辞。逐项给出 Pass、Partial 或 Fail，并引用材料中的具体证据。
```

</details>

<details>
<summary><strong>教育数据分析</strong></summary>

```text
使用 $edtech-cssci-research-skill，为一项大学生问卷、课程前后测和班级归属数据研究设计教育数据分析方案。

请先建立数据字典、样本流向、缺失和变量构造规则，再规划描述统计与可视化、量表/指标质量、与班级嵌套和重复测量相称的主模型、效应量与区间、敏感性分析、结果表图和教育解释边界。不要把横断面关联直接写成干预效果。
```

</details>

<details>
<summary><strong>可解释机器学习</strong></summary>

```text
使用 $edtech-cssci-research-skill，为学生学习结果预测设计可解释机器学习流程。

按学校分组切分数据，比较透明基线、随机森林和XGBoost，报告样本外性能与不确定性，再用SHAP和ALE解释；同时规划层次维度汇总、稳定性检验、CSSCI论文图表和不能使用的因果措辞。
```

</details>

<details>
<summary><strong>整稿自检与反模板表达</strong></summary>

```text
使用 $edtech-cssci-research-skill，对这篇论文做教育技术学CSSCI投稿前自检和原创性快扫。

按摘要、引言、综述、理论、方法、结果、讨论和结论分区，输出“位置—问题—依据—修改动作—预期改善”。重点处理模板句、机械对偶、作者罗列、宣传腔和无证据拔高；保留真实数据、引用、专业术语和结论边界，不预测AI检测率。
```

</details>

<details>
<summary><strong>审稿意见回应</strong></summary>

```text
使用 $edtech-cssci-research-skill，整理两位审稿人的意见。

拆分复合意见，区分共识、互补、冲突和独有问题；为每条意见给出 accept、partial、decline 或 needs verification，写明修改位置、验证方式，并生成回应函和修订台账。
```

</details>

<details>
<summary><strong>投稿包与最终文件</strong></summary>

```text
使用 $edtech-cssci-research-skill，检查这篇终稿的正文引文与文后条目、匿名信息、图表、附录、声明和DOCX/PDF渲染。

目标期刊的动态要求只采用当前官方来源。输出投稿阻断项、主要修改项、润色项和最终提交判断。
```

</details>

## 文件功能速查

### 主入口

| 文件 | 功能 | 什么时候看 |
|---|---|---|
| [`SKILL.md`](SKILL.md) | Skill 总入口：触发范围、任务路由、强制工作流、输出契约 | 想了解 Skill 如何判断和执行任务 |
| [`agents/openai.yaml`](agents/openai.yaml) | Codex 界面名称、简介与默认提示词 | 检查安装后的展示信息 |
| [`README.md`](README.md) | 面向使用者的功能导航与使用说明 | 不知道从哪里开始时 |

### 研究流程与专项规则

| 文件 | 主要用途 | 典型触发 |
|---|---|---|
| [`references/operating-modes-and-diagnostics.md`](references/operating-modes-and-diagnostics.md) | 选题、问题、大纲、诊断、修订和投稿模式 | “帮我诊断”“怎么选题”“如何重构” |
| [`references/writing-workflow.md`](references/writing-workflow.md) | 题目、摘要、引言、综述、理论、方法、结果、讨论与结论 | “帮我写/改这一部分” |
| [`references/literature-search-and-zotero.md`](references/literature-search-and-zotero.md) | 检索式、筛选、阅读状态、Zotero 与综述矩阵 | “检索文献”“整理Zotero”“写综述” |
| [`references/problem-model-evidence-practice.md`](references/problem-model-evidence-practice.md) | 概念模型、智能系统、画像、测评、实践模式与证据闭环 | “构建模型”“设计系统”“研究实践模式” |
| [`references/framework-defense-and-figure-audit.md`](references/framework-defense-and-figure-audit.md) | 矩阵、连续谱、类型学、机制图和图文一致性 | “框架为什么成立”“图怎么改” |
| [`references/research-paradigms.md`](references/research-paradigms.md) | DBR、实验、问卷、质性、QCA、综述和混合方法 | “这种问题适合什么方法” |
| [`references/data-collection-and-analysis.md`](references/data-collection-and-analysis.md) | 抽样、测量、数据清理、统计方法与诊断 | “检查数据处理和分析” |
| [`references/education-data-analysis.md`](references/education-data-analysis.md) | 数据字典、描述与可视化、测量、推断、回归、SEM、多层、纵向、稳健性与复现 | “做教育数据分析”“问卷/前后测/班级数据怎么分析” |
| [`references/interpretable-machine-learning.md`](references/interpretable-machine-learning.md) | 防泄漏建模、多模型比较、SHAP/ALE、可视化与报告 | “做可解释机器学习” |
| [`references/hierarchical-ml-interpretation.md`](references/hierarchical-ml-interpretation.md) | 层次 SHAP、PCA-ALE、分组比较、稳定性与节点消融 | “特征有理论层级”“做分组与稳定性” |
| [`references/evidence-and-citation.md`](references/evidence-and-citation.md) | 来源状态、引文真实性、直接引语和因果边界 | “核对引用和证据” |
| [`references/chapter-synthesis.md`](references/chapter-synthesis.md) | 章节、小节与文献述评的结尾 | “写本章小结”“收束这一节” |

### 修订、投稿与项目治理

| 文件 | 主要用途 | 典型触发 |
|---|---|---|
| [`references/self-review.md`](references/self-review.md) | 教育技术学 C 刊终稿自检、原创性与反模板快扫 | “投稿前审查”“检查模板腔” |
| [`references/revision-and-reviewer-response.md`](references/revision-and-reviewer-response.md) | 审稿意见、回应函、意见冲突与修订台账 | “审稿意见怎么回”“返修” |
| [`references/project-memory-and-decision-log.md`](references/project-memory-and-decision-log.md) | 长周期项目记忆、术语决定和版本传播 | “多轮修订”“记录项目决定” |
| [`references/journal-verification.md`](references/journal-verification.md) | CSSCI资格、目标期刊、栏目和投稿规范实时核验 | “这个期刊是否CSSCI”“投稿格式” |
| [`references/reference-integrity-and-manuscript-artifacts.md`](references/reference-integrity-and-manuscript-artifacts.md) | 参考文献、匿名稿、图表、DOCX/PDF 与投稿包 | “终稿文件检查”“匿名化” |
| [`references/validation-scenarios.md`](references/validation-scenarios.md) | Skill 更新后的代表性行为测试 | 开发或修改 Skill 后验证 |

### 可复用模板与示例

| 文件 | 可直接用于 | 建议使用时机 |
|---|---|---|
| [`assets/literature-review-matrix-template.md`](assets/literature-review-matrix-template.md) | 文献综述矩阵 | 完成初步检索、准备组织文献争论时 |
| [`assets/revision-report-template.md`](assets/revision-report-template.md) | 全文诊断与修订报告 | 已有完整草稿，需要确定修改优先级时 |
| [`assets/problem-model-evidence-canvas.md`](assets/problem-model-evidence-canvas.md) | 问题—模型—证据—实践画布 | 构建或审查概念模型、实践模式时 |
| [`assets/education-data-analysis-report-template.md`](assets/education-data-analysis-report-template.md) | 教育数据分析计划与结果报告 | 规划问卷、前后测、课堂或平台数据分析时 |
| [`assets/interpretable-ml-report-template.md`](assets/interpretable-ml-report-template.md) | 可解释机器学习分析报告 | 设计预测、SHAP/ALE 与稳健性检验时 |
| [`assets/reviewer-response-and-revision-ledger-template.md`](assets/reviewer-response-and-revision-ledger-template.md) | 审稿回应函与修订台账 | 收到导师、同行或匿名审稿意见时 |
| [`assets/project-context-template.md`](assets/project-context-template.md) | 长周期论文项目上下文 | 进入多轮写作、协作或返修时 |
| [`assets/submission-package-checklist.md`](assets/submission-package-checklist.md) | 投稿包最终核对 | 定稿后准备匿名稿、附件与投稿文件时 |
| [`examples/good-outline.md`](examples/good-outline.md) | 学习可用的大纲结构 | 不确定章节如何共同回答研究问题时 |
| [`examples/weak-outline.md`](examples/weak-outline.md) | 识别结构漂移和背景堆积 | 检查大纲是否“背景多、论证少”时 |
| [`examples/sample-review.md`](examples/sample-review.md) | 查看证据化诊断的输出方式 | 希望预览 `Pass / Partial / Fail` 诊断格式时 |

## 输出形式

| 任务 | 默认输出 | 最终用途 |
|---|---|---|
| 正文写作 | 正文 + 简短的写作逻辑与证据边界 | 形成可继续修改的章节草稿 |
| 结构设计 | 章节/方案 + 功能、证据和研究问题对应关系 | 对齐论文大纲、研究问题与材料 |
| 文献任务 | 检索策略 + 来源状态 + 筛选日志 + 阅读笔记/矩阵 + 引文风险 | 保证综述来源可追溯 |
| 全文诊断 | 总体判断 + `Pass / Partial / Fail` + 定位证据 + 修改路径 | 确定阻断项和修订顺序 |
| 框架审查 | 主张—依据—竞争解释—操作化—边界—图示对应 | 支撑模型图与正文的一致性 |
| 审稿返修 | 意见矩阵 + 处理决定 + 修改位置 + 回应函 + 修订台账 | 管理多轮返修与版本变化 |
| 教育数据分析 | 数据审计 + 分析计划 + 描述/测量/模型结果 + 诊断、稳健性与复现边界 | 形成可复现、可解释的分析报告 |
| 可解释机器学习 | 数据流程 + 模型比较 + 解释图表 + 稳定性 + 复现与边界 | 避免把预测结果误写为因果结论 |
| 投稿前检查 | 阻断项 + 主要修改 + 润色项 + 提交判断 | 完成目标期刊的最终交付质检 |
| 资料不足 | 缺失信息 + 影响 + 用户需提供内容 + 当前仍能完成的部分 | 明确补充材料与暂缓结论的边界 |

## 规范、边界与许可

### 证据与研究边界

- 不编造文献、DOI、政策、访谈、数据、显著性、期刊要求或审稿结果。
- 相关研究不写成因果研究，预测性能不等同于教学效果。
- 未核实内容使用 `[待核验]`、`[待补材料]` 或明确的检索步骤。
- CSSCI目录、期刊栏目、模板、摘要字数、引文格式和伦理要求以当前官方信息为准。
- 不使用固定样本量、文献比例、清理比例或单一统计阈值替代方法判断。
- 原创性检查用于提高论证质量，不预测AI检测率，也不提供检测规避方法。

### 参考规范与专业资源

本项目要求在实际任务中核验以下规范的当前版本：

- [AERA：经验社会科学研究报告标准](https://www.aera.net/Research-Policy-Advocacy/AERA-Shaping-Research-Policy/Standards-for-Research-Conduct/Standards-for-Empirical-Social-Science-Research)
- [APA：Journal Article Reporting Standards](https://www.apa.org/journals/authors/all-instructions.html)
- [PRISMA 2020](https://www.prisma-statement.org/prisma-2020)
- [Society for Learning Analytics Research](https://www.solaresearch.org/publications/hla-17/hla17-chapter4/)
- [scikit-learn：数据泄漏与 Pipeline](https://scikit-learn.org/stable/common_pitfalls.html)
- [SHAP TreeExplainer 官方文档](https://shap.readthedocs.io/en/latest/generated/shap.TreeExplainer.html)
- [Apley 与 Zhu：Accumulated Local Effects](https://doi.org/10.1111/rssb.12377)
- [钱佳、崔晓楠：是什么塑造了中小学生的创新能力](https://doi.org/10.16382/j.cnki.1000-5560.2026.07.005)
- [南京大学中国社会科学研究评价中心](https://cssrac.nju.edu.cn/)
- [《中国电化教育》官方网站](https://zdjy.cbpt.cnki.net/portal)
- [《电化教育研究》官方网站](https://aver.nwnu.edu.cn/)

### 项目来源说明

本项目在功能设计层面参考了以下公开项目：

- [`c-journal-paper-self-review-zh`](https://github.com/Smoothsailing0/Data-/tree/main/skills/c-journal-paper-self-review-zh)
- [`public-management-c-journal-writing-zh`](https://github.com/Smoothsailing0/Data-/tree/main/skills/public-management-c-journal-writing-zh)
- [`public-management-chapter-ending-synthesis-zh`](https://github.com/Smoothsailing0/Data-/tree/main/skills/public-management-chapter-ending-synthesis-zh)
- [`social-science-paper-writing-skill`](https://github.com/fakerqwq/social-science-paper-writing-skill)
- [`cn-academic-paper-pro`](https://github.com/MasutaFu/cn-academic-paper-pro)

上述项目仅用于功能分析和结构参考。教育技术学规则、研究范式、证据边界、示例和正文均为独立整理与重写；未复制或再发布来源仓库文本。固定禁词、固定文献比例、统一篇幅阈值、未经官网核实的期刊规则、AI检测规避方法和特定项目作者信息均未迁移。

仓库不包含论文PDF、全文摘录、Zotero数据库或私人文件路径。本 Skill 不能替代作者的真实研究、学术判断、伦理审查和目标期刊编辑部要求；使用者对数据、引用、署名、原创性和研究伦理承担最终责任。

### License

本项目采用 [CC BY 4.0](LICENSE) 许可。允许分享和改编，但须保留适当署名。
