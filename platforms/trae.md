# 在 Trae 中本地安装

Trae 支持标准 `SKILL.md`，因此可以直接使用本仓库的完整目录结构（包括 `references/`、`assets/` 与 `examples/`）。推荐将它作为**项目级 Skill**安装到论文或研究项目根目录：

```powershell
# 在你的论文/研究项目根目录运行
New-Item -ItemType Directory -Force "$PWD\.agents\skills" | Out-Null
git clone https://github.com/Starry-cz/edtech-cssci-research-skill.git "$PWD\.agents\skills\edtech-cssci-research-skill"
```

重启或刷新 Trae 后，在 Settings 的 Skills 区域确认该 Skill 已启用。需要稳定触发时，在对话中明确说：

```text
使用 edtech-cssci-research-skill，帮我诊断这篇教育技术学实证论文。
```

也可以通过 Trae 的 `Settings → Rule & Skills → Skills → Create` 导入仓库中的 `SKILL.md`。项目级安装适合与论文草稿、数据字典和分析文件放在同一工作区；不要把个人隐私数据或未授权全文提交到公开 Git 仓库。

Trae 对 Skill 的目录位置与界面可能随版本变化；若当前版本未自动发现 `.agents/skills`，使用界面导入 `SKILL.md` 即可。
