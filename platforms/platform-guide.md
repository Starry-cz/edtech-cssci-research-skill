# 跨平台使用说明

本仓库有两层内容：

1. `SKILL.md` 与 `agents/openai.yaml` 是 Codex 原生入口，支持按任务路由和按需读取 references；
2. 本目录的通用核心指令可粘贴到任意支持自定义指令、项目、助手、Gem 或系统提示词的平台。

| 使用场景 | 推荐文件 | 最合适的载体 |
|---|---|---|
| 任意对话式 AI 平台 | [universal-research-assistant.md](universal-research-assistant.md) | 项目指令、系统提示词或对话首条消息 |
| ChatGPT | [chatgpt.md](chatgpt.md) | Project；或 Custom GPT 的 Instructions/Knowledge |
| Claude Desktop / 网页版 | [claude.md](claude.md) | Project Instructions 与 Project Knowledge |
| Claude Code（本地） | [claude.md](claude.md) | `CLAUDE.md` 导入通用核心指令 |
| Gemini | [gemini.md](gemini.md) | Gem Instructions 与 Knowledge |
| Trae（本地） | [trae.md](trae.md) | 项目根目录 `.agents/skills/` 或界面导入 |

跨平台版本提供的是相同的研究规则、证据边界和输出协议；但不同平台不会自动读取 GitHub 目录。需要深度使用某一专题时，请将对应的 `references/` 文档作为知识文件上传，或在对话中明确粘贴相关段落。

## 本地安装：Trae 与 Claude Code

| 本地应用 | 能否直接克隆完整仓库 | 推荐做法 |
|---|---|---|
| Trae | 可以 | 克隆至项目根目录 `.agents/skills/edtech-cssci-research-skill`，由 Trae 作为项目级 Skill 发现；若未自动发现，则在 Skills 设置中导入 `SKILL.md`。详见 [trae.md](trae.md)。 |
| Claude Code | 可以，但不是自动 Skill 安装 | 克隆至 `~/.claude/skills/`，再在论文项目的 `CLAUDE.md` 通过 `@` 导入 `platforms/universal-research-assistant.md`。详见 [claude.md](claude.md)。 |
| Claude Desktop | 不可以自动安装 | 使用 Project Instructions 与 Project Knowledge；本地文件夹不会被应用自动读取。详见 [claude.md](claude.md)。 |

不要使用 Codex 的 `~/.codex/skills/` 命令去安装 Trae 或 Claude Code：每个平台的发现机制不同。克隆只负责下载文件；是否自动生效取决于该平台的目录约定或指令导入机制。

## 推荐的知识文件组合

| 任务 | 建议添加的仓库文件 |
|---|---|
| 选题、研究问题与模型 | `references/operating-modes-and-diagnostics.md`、`references/problem-model-evidence-practice.md`、`references/external-evidence-and-research-positioning.md` |
| 文献检索与综述 | `references/literature-search-and-zotero.md`、`assets/literature-review-matrix-template.md` |
| 实证数据分析与建模 | `references/education-data-analysis.md`、`references/interpretable-machine-learning.md`、相关报告模板 |
| 研究框架图、流程图、结果图或 DOCX/PDF 工件 | `references/cross-skill-artifact-routing.md`、`references/framework-defense-and-figure-audit.md`；再按平台可用能力调用 Drawio、文档、PDF、表格或图像 Skill |
| 论文主线、清洁正文与结构性修订 | `references/academic-writing-and-revision.md`、`references/writing-workflow.md`、`references/publication-prose-and-style-control.md`、`assets/argumentation-and-revision-workbook-template.md`、`assets/manuscript-surface-audit-template.md` |
| 返修与投稿 | `references/self-review.md`、`references/revision-and-reviewer-response.md`、`references/journal-verification.md`、`assets/reviewer-response-and-revision-ledger-template.md` |

无论使用哪个平台，期刊目录、投稿规范、政策和最新文献都必须在任务当下从官方或原始来源核验；不要把模型生成内容视为已核实证据。

## 官方兼容性说明

- [Trae Agent Skills 最佳实践](https://www.trae.ai/blog/trae_tutorial_0115?v=1)：说明 `SKILL.md` 的导入方式与 Skills 设置入口。
- [Trae 更新记录](https://www.trae.ai/ja/changelog)：记录 `.agents/skills` 项目级加载支持及版本变化。
- [Claude Code Memory](https://docs.anthropic.com/zh-CN/docs/claude-code/memory)：说明 `CLAUDE.md` 自动加载与 `@路径` 导入规则。
