# 教育技术学八刊期刊画像卡

本目录提供投稿前的**官方规范工作缓存**，不是永久有效的期刊数据库，也不替代目标期刊当日的官方要求。指定目标期刊时先读取对应卡片；距 `last_verified` 超过 90 天、卡片标为“待核验”，或用户提供更新的官网材料时，优先重新核验。

| 期刊 | 画像卡 | 当前可自动检查范围 |
| --- | --- | --- |
| 开放教育研究 | [open-education-research.md](open-education-research.md) | 投稿入口、栏目画像；格式细则待官网材料核验 |
| 远程教育杂志 | [distance-education-journal.md](distance-education-journal.md) | 官方入口与格式细则待核验 |
| 中国电化教育 | [china-educational-technology.md](china-educational-technology.md) | 官网下载文件存在性、栏目画像；具体格式待下载文件核验 |
| 现代远程教育研究 | [modern-distance-education-research.md](modern-distance-education-research.md) | 官方入口与格式细则待核验 |
| 电化教育研究 | [electric-education-research.md](electric-education-research.md) | 字数、摘要、关键词、英文信息、图表、匿名稿 |
| 现代教育技术 | [modern-educational-technology.md](modern-educational-technology.md) | 官方入口与格式细则待核验 |
| 现代远距离教育 | [modern-distance-education.md](modern-distance-education.md) | 官方入口与格式细则待核验 |
| 中国远程教育 | [china-distance-education.md](china-distance-education.md) | 官方入口与格式细则待核验 |

`scripts/check_journal_profile.py` 只执行卡片中明确、可机器检查的规则。未缓存或已失效的要求统一输出“待官方核验”，不以“通过”替代人工核验。
