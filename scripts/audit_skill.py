#!/usr/bin/env python3
"""??? Skill ???????????? README ??????????"""

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
    """?? Markdown ????????????????????????????"""
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
                errors.append(f"?????{markdown.relative_to(ROOT)} -> {target}")
    return checked


def badge_count(text: str, label: str) -> int | None:
    match = re.search(rf"badge/(\d+)-{re.escape(label)}-", text)
    return int(match.group(1)) if match else None


def main() -> int:
    errors: list[str] = []
    for required in (SKILL, README, YAML):
        if not required.is_file():
            errors.append(f"???????{required.relative_to(ROOT)}")
    if errors:
        print("\n".join(errors))
        return 1

    skill_text = read(SKILL)
    readme_text = read(README)
    yaml_text = read(YAML)

    # ???????????????????????????? YAML ??????
    frontmatter = re.match(r"^---\n(.*?)\n---", skill_text, re.DOTALL)
    if not frontmatter or not re.search(r"^name:\s*edtech-cssci-research-skill\s*$", frontmatter.group(1), re.MULTILINE):
        errors.append("SKILL.md ????? name ?????")
    if not frontmatter or not re.search(r"^description:\s*\".+\"\s*$", frontmatter.group(1), re.MULTILINE):
        errors.append("SKILL.md ?????? description ?????")
    for key in ("display_name", "short_description", "default_prompt"):
        if not re.search(rf"^\s*{key}:\s*\".+\"\s*$", yaml_text, re.MULTILINE):
            errors.append(f"agents/openai.yaml ?????? {key}")
    if not re.search(r'^\s*display_name:\s*"edtech-cssci-research"\s*$', yaml_text, re.MULTILINE):
        errors.append("agents/openai.yaml ??????? edtech-cssci-research")
    if "$edtech-cssci-research-skill" not in yaml_text:
        errors.append("?????????? $edtech-cssci-research-skill")

    # ?????????????????????????? README ????????
    required_files = (
        ROOT / "references" / "publication-prose-and-style-control.md",
        ROOT / "assets" / "manuscript-surface-audit-template.md",
        ROOT / "references" / "cross-skill-artifact-routing.md",
        ROOT / "references" / "eight-journal-writing-evidence.md",
        ROOT / "assets" / "abstract-argument-card-template.md",
        ROOT / "scripts" / "audit_manuscript_surface.py",
    )
    for required in required_files:
        if not required.is_file():
            errors.append(f"?????????{required.relative_to(ROOT)}")
    validation_text = read(ROOT / "references" / "validation-scenarios.md")
    for signal in ("???", "Test-set Selection", "Sequence Invention", "drawio", "????", "??"):
        if signal not in validation_text:
            errors.append(f"???????????{signal}")

    # SKILL ????????????????????????????
    routes = sorted(set(re.findall(r"`((?:references|assets|examples)/[^`\s]+\.md)`", skill_text)))
    for route in routes:
        if not (ROOT / route).is_file():
            errors.append(f"???????{route}")
    for required_route in (
        "references/publication-prose-and-style-control.md",
        "assets/manuscript-surface-audit-template.md",
        "references/cross-skill-artifact-routing.md",
        "references/eight-journal-writing-evidence.md",
        "assets/abstract-argument-card-template.md",
    ):
        if required_route not in routes:
            errors.append(f"SKILL.md ??????????{required_route}")

    modes = re.findall(r"^\| `([a-z_]+)` \|", skill_text, re.MULTILINE)
    if len(modes) != 18 or len(set(modes)) != 18:
        errors.append(f"SKILL.md ?????? 18 ????? {len(modes)} ?")

    declared_modes = badge_count(readme_text, "????")
    heading = re.search(r"^##\s+(\d+)\s+?????\s*$", readme_text, re.MULTILINE)
    if declared_modes != len(modes):
        errors.append(f"README ???? {declared_modes} ????????? {len(modes)} ?")
    if not heading or int(heading.group(1)) != len(modes):
        errors.append("README ???????????????")
    readme_modes = set(re.findall(r"\| `([a-z_]+)` \|", readme_text))
    missing_readme_modes = sorted(set(modes) - readme_modes)
    if missing_readme_modes:
        errors.append("README ????????" + "?".join(missing_readme_modes))

    reference_count = len(list((ROOT / "references").glob("*.md")))
    template_count = len(list((ROOT / "assets").glob("*.md")))
    if badge_count(readme_text, "??????") != reference_count:
        errors.append("README ?????????? references/ ???????")
    if badge_count(readme_text, "?????") != template_count:
        errors.append("README ????????? assets/ ???????")

    link_count = audit_links(errors)
    if errors:
        print("??????")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print(
        "?????"
        f"{len(modes)} ????{reference_count} ??????{template_count} ????"
        f"{len(routes)} ??????{link_count} ??? Markdown ???"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
