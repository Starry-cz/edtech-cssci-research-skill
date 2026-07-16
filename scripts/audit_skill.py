#!/usr/bin/env python3
"""审计本 Skill 的本地元数据、资源路由与 README 声明；仅使用标准库。"""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
README = ROOT / "README.md"
YAML = ROOT / "agents" / "openai.yaml"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def local_target(target: str) -> str | None:
    """提取 Markdown 链接中的本地文件目标；外链和页内锚点不在本地审计范围内。"""
    target = target.strip().strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    return target.split("#", 1)[0]


def audit_links(errors: list[str]) -> int:
    checked = 0
    pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for markdown in ROOT.rglob("*.md"):
        for target in pattern.findall(read(markdown)):
            relative = local_target(target)
            if relative is None:
                continue
            checked += 1
            if not (markdown.parent / relative).resolve().is_file():
                errors.append(f"失效链接：{markdown.relative_to(ROOT)} -> {target}")
    return checked


def badge_count(text: str, label: str) -> int | None:
    match = re.search(rf"badge/(\d+)-{re.escape(label)}-", text)
    return int(match.group(1)) if match else None


def main() -> int:
    errors: list[str] = []
    for required in (SKILL, README, YAML):
        if not required.is_file():
            errors.append(f"缺少必需文件：{required.relative_to(ROOT)}")
    if errors:
        print("\n".join(errors))
        return 1

    skill_text = read(SKILL)
    readme_text = read(README)
    yaml_text = read(YAML)

    # 前置元数据与界面元数据采用最小、明确的字段检查，避免引入 YAML 第三方依赖。
    frontmatter = re.match(r"^---\n(.*?)\n---", skill_text, re.DOTALL)
    if not frontmatter or not re.search(r"^name:\s*edtech-cssci-research-skill\s*$", frontmatter.group(1), re.MULTILINE):
        errors.append("SKILL.md 缺少正确的 name 前置元数据")
    if not frontmatter or not re.search(r"^description:\s*\".+\"\s*$", frontmatter.group(1), re.MULTILINE):
        errors.append("SKILL.md 缺少带引号的 description 前置元数据")
    for key in ("display_name", "short_description", "default_prompt"):
        if not re.search(rf"^\s*{key}:\s*\".+\"\s*$", yaml_text, re.MULTILINE):
            errors.append(f"agents/openai.yaml 缺少带引号的 {key}")
    if not re.search(r'^\s*display_name:\s*"edtech-cssci-research"\s*$', yaml_text, re.MULTILINE):
        errors.append("agents/openai.yaml 的展示名称应为 edtech-cssci-research")
    if "$edtech-cssci-research-skill" not in yaml_text:
        errors.append("默认提示词未显式调用 $edtech-cssci-research-skill")

    # 五层架构是主入口、模式协议和 README 的共同导航，不允许三处各自演化。
    operating = ROOT / "references" / "operating-modes-and-diagnostics.md"
    operating_text = read(operating) if operating.is_file() else ""
    if not operating.is_file():
        errors.append("缺少任务模式与诊断协议")
    skill_layers = (
        "| 1. 研究定位与主线 |",
        "| 2. 理论、模型与研究设计 |",
        "| 3. 文献、数据与实证分析 |",
        "| 4. 写作、诊断与修订 |",
        "| 5. 投稿、工件与专项协作 |",
    )
    operating_layers = (
        "## 一、研究定位与主线",
        "## 二、理论、模型与研究设计",
        "## 三、文献、数据与实证验证",
        "## 四、写作、诊断与修订",
        "## 五、投稿、工件与专项协作",
    )
    for layer in skill_layers:
        if layer not in skill_text:
            errors.append(f"SKILL.md 缺少五层架构：{layer}")
    for layer in operating_layers:
        if layer not in operating_text:
            errors.append(f"任务模式协议缺少五层架构：{layer}")
    if "## 五层能力结构" not in readme_text:
        errors.append("README 缺少五层能力结构导航")
    if "reference-integrity-and-manuscript-artifacts.md" not in operating_text:
        errors.append("任务模式协议未路由稿件工件质检资源")

    # 核心写作、方法审计、期刊适配与终稿检查均须保留，但不要求一次任务加载全部资源。
    required_files = (
        ROOT / "references" / "publication-prose-and-style-control.md",
        ROOT / "references" / "revision-governance-and-style-diagnosis.md",
        ROOT / "assets" / "manuscript-surface-audit-template.md",
        ROOT / "references" / "cross-skill-artifact-routing.md",
        ROOT / "references" / "eight-journal-writing-evidence.md",
        ROOT / "assets" / "abstract-argument-card-template.md",
        ROOT / "references" / "abstract-state-and-evidence-control.md",
        ROOT / "references" / "education-technology-empirical-writing-closure.md",
        ROOT / "scripts" / "audit_manuscript_surface.py",
        ROOT / "references" / "claim-evidence-validation-contract.md",
        ROOT / "references" / "statistical-reporting-and-figure-evidence.md",
        ROOT / "references" / "source-grounded-paper-reading.md",
        ROOT / "references" / "pre-submission-peer-review.md",
        ROOT / "assets" / "claim-evidence-validation-matrix-template.md",
        ROOT / "assets" / "figure-evidence-contract-template.md",
        ROOT / "assets" / "empirical-writing-closure-canvas.md",
        ROOT / "references" / "journals" / "index.md",
        ROOT / "references" / "functional-phrasing-bank.md",
        ROOT / "scripts" / "check_journal_profile.py",
        ROOT / "scripts" / "check_section_function.py",
        ROOT / "scripts" / "test_checkers.py",
    )
    for required in required_files:
        if not required.is_file():
            errors.append(f"缺少投稿表层资源：{required.relative_to(ROOT)}")
    journal_cards = list((ROOT / "references" / "journals").glob("*.md"))
    if len(journal_cards) != 9:
        errors.append(f"期刊画像目录应包含索引和 8 张画像卡，当前为 {len(journal_cards)} 个 Markdown 文件")
    for card in journal_cards:
        if card.name == "index.md":
            continue
        match = re.search(r"```journal-profile\s*\n(.*?)\n```", read(card), re.DOTALL)
        if not match:
            errors.append(f"期刊画像缺少机器可读数据块：{card.relative_to(ROOT)}")
            continue
        try:
            profile = json.loads(match.group(1))
            for key in ("id", "journal", "last_verified", "valid_days", "official_urls", "checks"):
                if key not in profile:
                    errors.append(f"期刊画像缺少 {key}：{card.relative_to(ROOT)}")
            dt.date.fromisoformat(profile["last_verified"])
            if profile["valid_days"] != 90:
                errors.append(f"期刊画像有效期不是 90 天：{card.relative_to(ROOT)}")
            if not profile["official_urls"] or not all(url.startswith("https://") for url in profile["official_urls"]):
                errors.append(f"期刊画像缺少 HTTPS 官方入口：{card.relative_to(ROOT)}")
        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
            errors.append(f"期刊画像数据无效：{card.relative_to(ROOT)}（{exc}）")
    section_templates = list((ROOT / "assets" / "section-prompts").glob("*.md"))
    if len(section_templates) != 7:
        errors.append(f"章节提示模板应为 7 个，当前为 {len(section_templates)} 个")
    writing_examples = list((ROOT / "examples" / "writing").glob("*.md"))
    if len(writing_examples) < 4:
        errors.append(f"合成写作样例至少应为 4 个，当前为 {len(writing_examples)} 个")
    if "## 文类预路由" not in operating_text:
        errors.append("任务模式协议缺少文类预路由")
    for genre in ("理论/概念", "综述/系统综述", "实验/准实验", "设计型研究与实践模型", "质性/案例/政策", "混合方法", "学习分析/可解释机器学习"):
        if genre not in operating_text:
            errors.append(f"文类预路由缺少：{genre}")
    for entry in ("我要选题", "我要写摘要", "我要按某刊改稿", "我要投稿前自检"):
        if entry not in readme_text:
            errors.append(f"README 缺少直接入口：{entry}")
    validation_text = read(ROOT / "references" / "validation-scenarios.md")
    for signal in ("论文写作轨", "方法审计轨", "社会科学论文", "P0/P1/P2", "同一留出集用于选模", "SHAP", "八刊", "drawio", "待官方核验", "混合方法研究", "理论/概念预路由", "可直接提交的最终版论文", "理论—构念—指标—表图—讨论—启示"):
        if signal not in validation_text:
            errors.append(f"验证场景缺少回归信号：{signal}")

    # 摘要规则须避免退化为方法说明书，并明确将方法审计另行交付。
    abstract_rules = read(ROOT / "references" / "abstract-state-and-evidence-control.md")
    for signal in ("从方法报告到学术判断", "原始变量 → 教育构念", "方法审计"):
        if signal not in abstract_rules:
            errors.append(f"摘要规则缺少关键分层：{signal}")

    prose_control = read(ROOT / "references" / "publication-prose-and-style-control.md")
    for signal in ("正文的优先级", "何时才进入方法审计", "最终提交契约"):
        if signal not in prose_control:
            errors.append(f"投稿正文控制缺少关键分层：{signal}")

    # SKILL 的反引号资源路径必须真实存在，防止按需路由在运行时失效。
    routes = sorted(set(re.findall(r"`((?:references|assets|examples|scripts)/[^`\s]+(?:\.md|\.py))`", skill_text)))
    for route in routes:
        if not (ROOT / route).is_file():
            errors.append(f"失效资源路由：{route}")
    for required_route in (
        "references/publication-prose-and-style-control.md",
        "assets/abstract-argument-card-template.md",
        "references/abstract-state-and-evidence-control.md",
        "references/journals/index.md",
        "references/revision-governance-and-style-diagnosis.md",
        "references/education-technology-empirical-writing-closure.md",
        "assets/empirical-writing-closure-canvas.md",
        "assets/section-prompts/abstract.md",
        "scripts/audit_manuscript_surface.py",
    ):
        if required_route not in routes:
            errors.append(f"SKILL.md 未路由投稿表层资源：{required_route}")

    modes = re.findall(r"^\| `([a-z_]+)` \|", skill_text, re.MULTILINE)
    if len(modes) != 18 or len(set(modes)) != 18:
        errors.append(f"SKILL.md 任务模式应为 18 个，当前为 {len(modes)} 个")

    declared_modes = badge_count(readme_text, "任务模式")
    heading = re.search(r"^##\s+(\d+)\s+类任务模式\s*$", readme_text, re.MULTILINE)
    if declared_modes != len(modes):
        errors.append(f"README 徽章声明 {declared_modes} 个任务模式，实际为 {len(modes)} 个")
    if not heading or int(heading.group(1)) != len(modes):
        errors.append("README 的任务模式标题与实际数量不一致")
    readme_modes = set(re.findall(r"\| `([a-z_]+)` \|", readme_text))
    missing_readme_modes = sorted(set(modes) - readme_modes)
    if missing_readme_modes:
        errors.append("README 未列出任务模式：" + "、".join(missing_readme_modes))

    # 新增期刊画像和章节模板均为分层目录，数量统计必须递归进行。
    reference_count = len(list((ROOT / "references").rglob("*.md")))
    template_count = len(list((ROOT / "assets").rglob("*.md")))
    if badge_count(readme_text, "研究参考模块") != reference_count:
        errors.append("README 的研究参考模块数量与 references/ 实际数量不一致")
    if badge_count(readme_text, "可复用模板") != template_count:
        errors.append("README 的可复用模板数量与 assets/ 实际数量不一致")

    link_count = audit_links(errors)
    if errors:
        print("审计未通过：")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print(
        "审计通过："
        f"{len(modes)} 个模式，{reference_count} 个参考模块，{template_count} 个模板，"
        f"{len(routes)} 条资源路由，{link_count} 条本地 Markdown 链接。"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
