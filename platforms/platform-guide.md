# 跨平台使用说明

本仓库有两层内容：

1. `SKILL.md` 与 `agents/openai.yaml` 是 Codex 原生入口，支持按任务路由和按需读取 references；
2. 本目录的通用核心指令可粘贴到任意支持自定义指令、项目、助手、Gem 或系统提示词的平台。

| 使用场景 | 推荐文件 | 最合适的载体 |
|---|---|---|
| 任意对话式 AI 平台 | [universal-research-assistant.md](universal-research-assistant.md) | 项目指令、系统提示词或对话首条消息 |
| ChatGPT | [chatgpt.md](chatgpt.md) | Project；或 Custom GPT 的 Instructions/Knowledge |
| Claude | [claude.md](claude.md) | Project Instructions 与 Project Knowledge |
| Gemini | [gemini.md](gemini.md) | Gem Instructions 与 Knowledge |

跨平台版本提供的是相同的研究规则、证据边界和输出协议；但不同平台不会自动读取 GitHub 目录。需要深度使用某一专题时，请将对应的 `references/` 文档作为知识文件上传，或在对话中明确粘贴相关段落。

## 推荐的知识文件组合

| 任务 | 建议添加的仓库文件 |
|---|---|
| 选题、研究问题与模型 | `references/operating-modes-and-diagnostics.md`、`references/problem-model-evidence-practice.md` |
| 文献检索与综述 | `references/literature-search-and-zotero.md`、`assets/literature-review-matrix-template.md` |
| 实证数据分析与建模 | `references/education-data-analysis.md`、`references/interpretable-machine-learning.md`、相关报告模板 |
| 返修与投稿 | `references/self-review.md`、`references/revision-and-reviewer-response.md`、`references/journal-verification.md` |

无论使用哪个平台，期刊目录、投稿规范、政策和最新文献都必须在任务当下从官方或原始来源核验；不要把模型生成内容视为已核实证据。
