# 在 Claude 中使用

## Claude Code：本地安装

Claude Code 不会自动扫描本仓库的 `SKILL.md`，但会自动加载 `CLAUDE.md`，且支持通过 `@路径` 导入其他 Markdown 指令。先克隆仓库：

无论使用本地目录还是项目指令，都保留通用核心指令中的“阻断 / 探索性可写 / 投稿就绪”发布状态：存在测试集选模、泄漏或不可复核结果时，不让模型生成定稿式摘要和结论。

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
git clone https://github.com/Starry-cz/edtech-cssci-research-skill.git "$HOME\.claude\skills\edtech-cssci-research-skill"
```

然后在**论文项目根目录**的 `CLAUDE.md` 中加入以下一行：

```markdown
@~/.claude/skills/edtech-cssci-research-skill/platforms/universal-research-assistant.md
```

这样只有该项目会加载教育技术研究规则。若确实希望所有 Claude Code 项目默认使用，可将同一行加入 `~/.claude/CLAUDE.md`；但这会增加所有项目的上下文，不推荐用于无关的编程任务。启动 Claude Code 后可用 `/memory` 检查已加载的指令。

## Claude Desktop / 网页版：Project

本地安装 Claude Desktop 并不意味着它会读取电脑上的 Skill 目录。推荐创建一个论文或研究 Project，在 Project Instructions 中粘贴 [通用核心指令](universal-research-assistant.md) 的“核心指令”；将研究草稿、编码本、数据字典、审稿意见或允许共享的文献笔记添加至 Project Knowledge。

为保持上下文准确，请按任务上传必要材料，而不是一次上传来源不明的大量文件：

- 写综述：检索日志、阅读笔记、已阅读全文或可核验的来源信息；
- 做实证分析：数据字典、样本流向、变量说明、分析代码/语法和匿名化数据摘要；
- 写回应函：审稿意见、当前版本及已修改位置；
- 核验投稿：目标期刊官网链接或最新作者指南。

每轮对话开始时可以使用 [通用核心指令](universal-research-assistant.md) 中的“推荐的首条请求”。Claude 未实际读取或未核验的材料，不得据此声称文献或期刊要求已经得到确认。
