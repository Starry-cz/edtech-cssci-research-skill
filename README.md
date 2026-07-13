# 教育技术学 CSSCI 研究助手

一个面向中文教育技术学、教育数字化与智能教育研究的 Codex Skill，覆盖选题诊断、研究问题、文献检索、研究设计、论文写作、章节收束和投稿前自检。

本项目强调“研究问题—研究设计—证据—结论”的闭合关系。它不会只把句子改得更像论文，也不会用“技术赋能、融合创新、模式重塑”等抽象词代替机制解释。

## 主要能力

- 选题打磨、研究问题提炼与论文结构设计
- 中英文文献检索规划、结构化阅读、Zotero 整理与综述矩阵
- 题目、摘要、引言、文献综述、理论框架与机制写作
- 数据采集与分析诊断、结果解释、讨论、结论与政策/实践建议
- 博士论文和学位论文章节、小节及文献述评结尾
- CSSCI/中文核心投稿前终稿自检与反 AI 模板表达检查
- 目标期刊匹配、投稿规范和 CSSCI 收录状态核验
- 文献、DOI、政策、数据和引用真实性检查

## 九种任务模式

Skill 会先识别任务类型，再按需读取对应规则：

1. `topic_diagnosis`：判断选题价值、范围、证据可得性与伦理风险。
2. `research_question_refinement`：把宽泛主题改造成可回答的问题。
3. `outline_building`：为章节分配论证任务并检查结构漂移。
4. `literature_review_planning`：规划概念簇、检索式、综述结构与研究缺口。
5. `literature_search_to_review`：完成检索记录、来源筛选、结构化笔记、Zotero 与综述矩阵工作流。
6. `draft_review`：按具体文本证据诊断整稿。
7. `section_revision`：在不新增虚构材料的前提下修订章节。
8. `citation_and_evidence_check`：核对来源状态、主张强度和因果边界。
9. `pre_submission_check`：识别投稿阻断项、重要修改项和润色项。

## 支持的研究范式

- 设计型研究（DBR）
- 学习分析与教育数据挖掘
- 问卷、量表、回归与结构方程模型
- 实验与准实验
- 案例研究、访谈和质性研究
- QCA、指标体系与综合评价
- 政策、内容与计算文本分析
- 系统综述与元分析
- 定量、质性和混合方法研究

## 工作特点

### 论证功能优先

生成或改写前，先判断当前内容是在提出问题、推进文献、限定概念、说明设计、呈现证据、解释机制还是收束贡献，再决定段落结构和材料密度。

### 教育技术机制可解释

机制分析围绕以下关系展开：

```text
主体 → 学习/教学活动 → 技术功能与实际使用 → 情境条件
     → 过程证据 → 学习、教学或组织结果 → 适用边界
```

区分“技术存在”“技术被使用”“学习过程发生变化”和“学习结果发生变化”，避免从技术可用性直接推导教育效果。

### 证据边界明确

- 不编造文献、DOI、政策、访谈、数据、显著性或期刊要求。
- 相关研究不写成因果研究，预测性能不等同于教学效果。
- 未核实内容使用 `[待核验]`、`[待补材料]` 或明确的检索步骤。
- CSSCI 目录、期刊栏目和格式要求以当前官方信息为准。

### 诊断而非机械打分

- 每项审查使用 `Pass / Partial / Fail`，并引用草稿中的具体证据。
- 风险项必须同时给出位置、问题依据、修改动作和预期改善。
- 材料不足时使用 `[needs user verification]`、`[待核验]` 或 `[待补材料]`，不把“用户未提供”误判为“论文没有”。
- 不套用固定样本量、统一数据清理比例或单一统计阈值；判断服从研究问题、数据结构与识别条件。

### 来源状态可追踪

文献从检索到使用依次标记为 `candidate source`、`metadata only`、`abstract only`、`full text read`、`in Zotero` 或 `imported to Zotero`。Zotero 中存在条目不等于已阅读全文，也不等于元数据准确。

## 安装

将仓库克隆到 Codex 的 skills 目录：

```bash
git clone https://github.com/Starry-cz/edtech-cssci-research-skill.git ~/.codex/skills/edtech-cssci-research-skill
```

Windows PowerShell 示例：

```powershell
git clone https://github.com/Starry-cz/edtech-cssci-research-skill.git "$HOME\.codex\skills\edtech-cssci-research-skill"
```

也可以下载 ZIP，解压后将整个 `edtech-cssci-research-skill` 文件夹放入 Codex skills 目录。重新启动或刷新 Codex 后使用。

## 使用示例

显式调用 skill：

```text
使用 $edtech-cssci-research-skill，把“生成式人工智能促进大学生深度学习”改造成一个可研究的 CSSCI 选题，并说明研究对象、机制和可行证据。
```

```text
使用 $edtech-cssci-research-skill，重写这篇论文的引言。不要堆政策背景，要从课堂中的具体矛盾进入，并保留已有引用。
```

```text
使用 $edtech-cssci-research-skill，检查这个学习分析研究的方法与结果，重点判断预测指标是否被错误解释成学习成效。
```

```text
使用 $edtech-cssci-research-skill，为本章写一个结尾段。不要复述小标题，要提炼作者判断并轻指下一章。
```

```text
使用 $edtech-cssci-research-skill，按教育技术学 CSSCI 审稿视角做投稿前自检，并按“必须修改、建议修改、可保留”分类。
```

```text
使用 $edtech-cssci-research-skill，为“生成式人工智能反馈与大学生论证写作修订”设计中英文检索式、筛选日志、Zotero 标签和综述矩阵。没有读到全文的来源不要写成已核实结论。
```

```text
使用 $edtech-cssci-research-skill，诊断这份平台日志研究的数据生成、分析单位、缺失处理、训练/验证隔离和因果措辞；逐项给出 Pass、Partial 或 Fail。
```

若只需要正文，可在请求中明确说明“只给正文，不要写作说明”。

## 输出形式

- 正文写作：正文 + 简短的写作逻辑与证据边界说明
- 结构或诊断：方案/问题 + 判断依据
- 文献任务：检索策略 + 来源状态 + 筛选日志 + 阅读笔记/矩阵 + 引文风险
- 终稿自检：总体判断 + 5—8 个主要问题 + 修改建议 + 反模板快扫
- 章节收束：默认一段式正文 + 收束逻辑说明
- 资料不足：待补信息、可选研究设计或检索核验步骤

## 项目结构

```text
edtech-cssci-research-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── writing-workflow.md
│   ├── operating-modes-and-diagnostics.md
│   ├── literature-search-and-zotero.md
│   ├── data-collection-and-analysis.md
│   ├── self-review.md
│   ├── chapter-synthesis.md
│   ├── research-paradigms.md
│   ├── evidence-and-citation.md
│   ├── journal-verification.md
│   └── validation-scenarios.md
├── assets/
│   ├── literature-review-matrix-template.md
│   └── revision-report-template.md
├── examples/
│   ├── good-outline.md
│   ├── weak-outline.md
│   └── sample-review.md
├── LICENSE
└── README.md
```

`SKILL.md` 负责核心规则和任务路由；`references/` 按任务读取；`assets/` 提供可复用交付模板；`examples/` 展示诊断和改写的质量边界。

## 研究与投稿规范

本项目参考以下公开规范和专业资源，并要求在实际任务中核验最新版本：

- [AERA：经验社会科学研究报告标准](https://www.aera.net/Research-Policy-Advocacy/AERA-Shaping-Research-Policy/Standards-for-Research-Conduct/Standards-for-Empirical-Social-Science-Research)
- [APA：Journal Article Reporting Standards](https://www.apa.org/journals/authors/all-instructions.html)
- [PRISMA 2020](https://www.prisma-statement.org/prisma-2020)
- [Society for Learning Analytics Research](https://www.solaresearch.org/publications/hla-17/hla17-chapter4/)
- [南京大学中国社会科学研究评价中心](https://cssrac.nju.edu.cn/)
- [《中国电化教育》官方网站](https://zdjy.cbpt.cnki.net/portal)
- [《电化教育研究》官方网站](https://aver.nwnu.edu.cn/)

## 项目来源说明

本项目的通用中文 C 刊写作、自检和章节收束能力受到以下开源仓库内容的启发：

- [`c-journal-paper-self-review-zh`](https://github.com/Smoothsailing0/Data-/tree/main/skills/c-journal-paper-self-review-zh)
- [`public-management-c-journal-writing-zh`](https://github.com/Smoothsailing0/Data-/tree/main/skills/public-management-c-journal-writing-zh)
- [`public-management-chapter-ending-synthesis-zh`](https://github.com/Smoothsailing0/Data-/tree/main/skills/public-management-chapter-ending-synthesis-zh)
- [`social-science-paper-writing-skill`](https://github.com/fakerqwq/social-science-paper-writing-skill)：启发了任务模式、诊断标签、来源状态、检索到综述和修订报告等功能设计。

上述项目用于功能分析和结构参考。教育技术学规则、研究范式、证据边界、示例和全部正文均为独立整理与重写；未复制或再发布来源仓库文本。

## 使用边界

本 skill 是研究设计、写作和审查辅助工具，不能替代作者的学术判断、真实研究过程、伦理审查或目标期刊编辑部要求。使用者应对论文中的数据、引用、署名、原创性和研究伦理承担最终责任。

## License

本项目采用 [CC BY 4.0](LICENSE) 许可。允许分享和改编，但须保留适当署名。
