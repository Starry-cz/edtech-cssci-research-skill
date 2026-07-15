# 在 Claude 中使用

## Claude Code：本地安装

Claude Code 不会自动扫描本仓库的 `SKILL.md`，但可通过项目的 `CLAUDE.md` 导入指令。先克隆仓库：

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
git clone https://github.com/Starry-cz/edtech-cssci-research-skill.git "$HOME\.claude\skills\edtech-cssci-research-skill"
```

然后在论文项目根目录的 `CLAUDE.md` 写入：

```markdown
@~/.claude/skills/edtech-cssci-research-skill/platforms/universal-research-assistant.md
```

通用指令默认走社会科学论文写作轨；只有明确要求方法审计或投稿前技术核验时，才单列分析设计、选模或复现问题。这样不会把技术审计语言自动搬进摘要、讨论和结论。

## Claude Desktop / 网页版：Project

创建论文 Project，在 Project Instructions 粘贴 [通用核心指令](universal-research-assistant.md)，并按当前任务将草稿、编码本、数据字典、审稿意见、期刊官网链接或允许共享的文献笔记添加到 Project Knowledge。

建议按任务上传材料：写综述时上传检索日志和阅读笔记；做实证分析时上传数据字典、样本说明和分析语法；写回应函时上传审稿意见和已修改位置；核验投稿时上传目标期刊官网或最新作者指南。Claude 未实际读取或未核验的材料，不得据此确认文献结论或期刊规则。
