#!/usr/bin/env python3
"""审计本 Skill 的本地元数据、资源路由与 README 声明；仅使用标准库。"""

from __future__ import annotations

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

    # 核心扩展必须同时提供入口、资源与代表性回归信号，避免 README 或路由单独漂移。
    required_files = (
        ROOT / "references" / "publication-prose-and-style-control.md",
        ROOT / "assets" / "manuscript-surface-audit-template.md",
        ROOT / "references" / "cross-skill-artifact-routing.md",
        ROOT / "references" / "eight-journal-writing-evidence.md",
        ROOT / "assets" / "abstract-argument-card-template.md",
        ROOT / "references" / "abstract-state-and-evidence-control.md",
        ROOT / "scripts" / "audit_manuscript_surface.py",
        ROOT / "references" / "claim-evidence-validation-contract.md",
        ROOT / "references" / "statistical-reporting-and-figure-evidence.md",
        ROOT / "references" / "source-grounded-paper-reading.md",
        ROOT / "references" / "pre-submission-peer-review.md",
        ROOT / "assets" / "claim-evidence-validation-matrix-template.md",
        ROOT / "assets" / "figure-evidence-contract-template.md",
    )
    for required in required_files:
        if not required.is_file():
            errors.append(f"缺少投稿表层资源：{required.relative_to(ROOT)}")
    validation_text = read(ROOT / "references" / "validation-scenarios.md")
    for signal in ("目的：", "Test-set Selection", "Sequence Invention", "drawio", "投稿就绪", "八刊", "主张—决定性证据", "图表证据契约", "共同事实底稿", "四个发现", "删减检验"):
        if signal not in validation_text:
            errors.append(f"验证场景缺少回归信号：{signal}")

    # SKILL 的反引号资源路径必须真实存在，防止按需路由在运行时失效。
    routes = sorted(set(re.findall(r"`((?:references|assets|examples)/[^`\s]+\.md)`", skill_text)))
    for route in routes:
        if not (ROOT / route).is_file():
            errors.append(f"失效资源路由：{route}")
    for required_route in (
        "references/publication-prose-and-style-control.md",
        "assets/manuscript-surface-audit-template.md",
        "references/cross-skill-artifact-routing.md",
        "references/eight-journal-writing-evidence.md",
        "assets/abstract-argument-card-template.md",
        "references/abstract-state-and-evidence-control.md",
        "references/claim-evidence-validation-contract.md",
        "references/statistical-reporting-and-figure-evidence.md",
        "references/source-grounded-paper-reading.md",
        "references/pre-submission-peer-review.md",
        "assets/claim-evidence-validation-matrix-template.md",
        "assets/figure-evidence-contract-template.md",
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

    reference_count = len(list((ROOT / "references").glob("*.md")))
    template_count = len(list((ROOT / "assets").glob("*.md")))
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
