#!/usr/bin/env python3
"""根据期刊画像检查可机器识别的投稿工件信号；结论必须由人工复核。"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
WORD_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def read_text(path: Path) -> str:
    """读取常见稿件格式；DOCX 仅提取段落文本，版式需另行人工查看。"""
    suffix = path.suffix.lower()
    if suffix in {".md", ".txt"}:
        return path.read_text(encoding="utf-8-sig")
    if suffix == ".docx":
        with zipfile.ZipFile(path) as archive:
            root = ET.fromstring(archive.read("word/document.xml"))
        paragraphs = []
        for paragraph in root.iter(f"{WORD_NS}p"):
            paragraphs.append("".join(node.text or "" for node in paragraph.iter(f"{WORD_NS}t")))
        return "\n".join(paragraphs)
    raise ValueError("仅支持 .md、.txt 与 .docx 稿件。")


def resolve_profile(value: str) -> Path:
    candidate = Path(value)
    if candidate.is_file():
        return candidate
    by_id = ROOT / "references" / "journals" / f"{value}.md"
    if by_id.is_file():
        return by_id
    raise FileNotFoundError("未找到期刊画像；请传入画像文件路径或其文件名（不含 .md）。")


def load_profile(path: Path) -> dict:
    content = path.read_text(encoding="utf-8-sig")
    match = re.search(r"```journal-profile\s*\n(.*?)\n```", content, re.S)
    if not match:
        raise ValueError("画像文件缺少 journal-profile JSON 数据块。")
    profile = json.loads(match.group(1))
    for key in ("id", "journal", "official_urls", "last_verified", "valid_days", "checks"):
        if key not in profile:
            raise ValueError(f"画像缺少字段：{key}")
    return profile


def find_line(text: str, labels: tuple[str, ...]) -> str:
    for line in text.splitlines():
        normalized = line.strip().lstrip("#*- ")
        if any(normalized.startswith(label) for label in labels):
            return normalized
    return ""


def find_abstract(text: str) -> str:
    """兼容“摘要：正文”和“摘要”单独成行两种常见写法。"""
    match = re.search(
        r"(?ims)^\s*(?:#+\s*)?(?:摘\s*要|Abstract)\s*[:：]?\s*(.*?)"
        r"(?=^\s*(?:#+\s*)?(?:关\s*键\s*词|Keywords|引言|一[、.]|1[、.\s]))",
        text,
    )
    return match.group(1).strip() if match else ""


def count_units(text: str) -> int:
    """中文按字符、英文按词粗略计数，不能代替期刊系统的正式统计。"""
    chinese = re.findall(r"[\u4e00-\u9fff]", text)
    latin = re.findall(r"[A-Za-z0-9]+", text)
    return len(chinese) + len(latin)


def check(
    name: str,
    passed: bool | None,
    detail: str,
    results: list[tuple[str, str, str]],
    *,
    hard: bool = False,
) -> None:
    status = "Pass" if passed else ("Fail" if hard else "Partial") if passed is False else "待官方核验"
    results.append((name, status, detail))


def main() -> int:
    parser = argparse.ArgumentParser(description="根据期刊画像执行候选工件检查。")
    parser.add_argument("manuscript", type=Path, help=".md、.txt 或 .docx 稿件")
    parser.add_argument("profile", help="期刊画像路径，或 references/journals 下的文件名")
    parser.add_argument("--as-of", default=dt.date.today().isoformat(), help="核验日期，格式 YYYY-MM-DD")
    args = parser.parse_args()

    try:
        text = read_text(args.manuscript)
        profile_path = resolve_profile(args.profile)
        profile = load_profile(profile_path)
        as_of = dt.date.fromisoformat(args.as_of)
        verified = dt.date.fromisoformat(profile["last_verified"])
    except (OSError, ValueError, KeyError, json.JSONDecodeError, zipfile.BadZipFile) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 2

    checks = profile["checks"]
    stale = (as_of - verified).days > int(profile["valid_days"])
    results: list[tuple[str, str, str]] = []
    abstract = find_abstract(text)
    keyword_line = find_line(text, ("关键词", "Keywords"))
    body_units = count_units(text)

    if "abstract_max" in checks:
        check("摘要长度", bool(abstract) and count_units(abstract) <= checks["abstract_max"],
              f"近似 {count_units(abstract)} 单位；画像上限 {checks['abstract_max']}。", results)
    if "keywords_min" in checks:
        keywords = re.split(r"[；;、,，]", re.sub(r"^(关键词|Keywords)\s*[:：]?\s*", "", keyword_line, flags=re.I))
        keyword_count = len([item for item in keywords if item.strip()])
        minimum, maximum = checks["keywords_min"], checks.get("keywords_max")
        okay = keyword_count >= minimum and (maximum is None or keyword_count <= maximum)
        check("关键词", okay, f"识别到 {keyword_count} 个；画像范围 {minimum}–{maximum or '未注明'}。", results)
    if "english_required" in checks:
        has_english = bool(re.search(r"(?im)^\s*(abstract|keywords)\s*[:：]", text))
        detail = "检测到英文 Abstract/Keywords 标记；需人工确认完整性。" if has_english else "未检测到英文 Abstract/Keywords 标记。"
        check("英文信息", has_english, detail, results)
    if "figure_table_max" in checks:
        ids = set(re.findall(r"(图|表)\s*(\d+)", text))
        count = len(ids)
        check("图表数量", count <= checks["figure_table_max"],
              f"识别到约 {count} 个编号；画像上限 {checks['figure_table_max']}。", results)
    if "word_count" in checks:
        target = int(checks["word_count"]["target"])
        # 期刊“字数”统计口径常含参考文献或英文信息，故只作近似提示。
        check("篇幅信号", None, f"全文近似 {body_units} 单位；画像参考值 {target}，请以官方系统口径复核。", results)
    if checks.get("anonymous_required"):
        identity = bool(re.search(r"(?im)^\s*(作者|作者简介|基金项目|项目编号)\s*[:：]", text))
        check("匿名信息", not identity, "发现署名/基金栏候选。" if identity else "未发现常见署名/基金栏标记。", results, hard=True)

    if stale or not checks:
        overall = "待官方核验"
    elif any(status == "Fail" for _, status, _ in results):
        overall = "Fail"
    elif any(status == "Partial" for _, status, _ in results):
        overall = "Partial"
    else:
        overall = "Pass"

    print(f"期刊：{profile['journal']}")
    print(f"画像：{profile_path.relative_to(ROOT)}")
    print(f"核验：{profile['last_verified']}；有效期 {profile['valid_days']} 天；本次日期 {args.as_of}")
    print(f"总体：{overall}（机器候选检查，不等于期刊最终合格判断）")
    for name, status, detail in results:
        print(f"- [{status}] {name}：{detail}")
    if stale:
        print("- [待官方核验] 画像已超过 90 天有效窗口，请打开官方页面或下载当期模板复核。")
    if not checks:
        print("- [待官方核验] 当前画像未录入可机器执行的细则；不得据此声称格式合格。")
    print("官方来源：")
    for source in profile["official_urls"]:
        print(f"- {source}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
