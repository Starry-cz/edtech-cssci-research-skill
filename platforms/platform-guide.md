# 跨平台使用说明

本仓库有两层内容：

1. `SKILL.md` 与 `agents/openai.yaml` 是 Codex 原生入口，支持按任务路由和按需读取 `references/`；
2. [通用核心指令](universal-research-assistant.md) 可粘贴到任意支持项目指令、系统提示词或自定义助手的平台。

所有版本默认将“论文写作”和“方法审计”分开：写作时先完成社会科学论证；只有用户明确检查研究设计、泄漏、选模、复现或投稿前技术问题时，才单列审计。真实性、来源核验与终稿无占位符的要求在所有平台保持一致。

| 使用场景 | 推荐文件 | 最合适的载体 |
|---|---|---|
| 任意对话式 AI 平台 | [universal-research-assistant.md](universal-research-assistant.md) | 项目指令、系统提示词或对话首条消息 |
| ChatGPT | [chatgpt.md](chatgpt.md) | Project；或 Custom GPT 的 Instructions/Knowledge |
| Claude Desktop / 网页版 | [claude.md](claude.md) | Project Instructions 与 Project Knowledge |
| Claude Code（本地） | [claude.md](claude.md) | `CLAUDE.md` 导入通用核心指令 |
| Gemini | [gemini.md](gemini.md) | Gem Instructions 与 Knowledge |
| Trae（本地） | [trae.md](trae.md) | 项目根目录 `.agents/skills/` 或界面导入 |

不同平台不会自动读取整个 GitHub 仓库。需要某一专题时，请上传所需的 `references/` 文件，或将相关规则粘贴到当前项目中。

## 本地安装：Trae 与 Claude Code

| 本地应用 | 能否直接克隆完整仓库 | 推荐做法 |
|---|---|---|
| Trae | 可以 | 克隆到项目根目录 `.agents/skills/edtech-cssci-research-skill`，由 Trae 作为项目级 Skill 发现；未自动发现时，在 Skills 设置导入 `SKILL.md`。详见 [trae.md](trae.md)。 |
| Claude Code | 可以，但不是自动 Skill 安装 | 克隆到 `~/.claude/skills/`，再在论文项目的 `CLAUDE.md` 通过 `@` 导入 `platforms/universal-research-assistant.md`。详见 [claude.md](claude.md)。 |
| Claude Desktop | 不可以自动安装 | 使用 Project Instructions 与 Project Knowledge；本地文件夹不会被应用自动读取。详见 [claude.md](claude.md)。 |

## 推荐的知识文件组合

| 任务 | 建议添加的仓库文件 |
|---|---|
| 选题、研究问题与模型 | `references/operating-modes-and-diagnostics.md`、`references/problem-model-evidence-practice.md`、`references/external-evidence-and-research-positioning.md` |
| 文献检索与综述 | `references/literature-search-and-zotero.md`、`assets/literature-review-matrix-template.md` |
| 实证数据分析与建模 | `references/education-data-analysis.md`、`references/interpretable-machine-learning.md`、相关报告模板 |
| 论文写作与修订 | `references/academic-writing-and-revision.md`、`references/writing-workflow.md`、`references/publication-prose-and-style-control.md`、章节提示模板 |
| 返修与投稿 | `references/self-review.md`、`references/revision-and-reviewer-response.md`、`references/journal-verification.md`、投稿包清单 |

期刊目录、投稿规范、政策和最新文献仍须在任务当下从官方或原始来源核验；不要把模型生成内容当作已核实证据。
