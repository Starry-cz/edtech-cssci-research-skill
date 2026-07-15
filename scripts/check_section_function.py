#!/usr/bin/env python3
"""识别论文各节的功能候选缺口；不以词语出现与否替代论文质量判断。"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


WORD_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
GENRES = ("auto", "theory", "review", "experiment", "dbr", "qualitative", "mixed", "analytics")
SECTION_ALIASES = {
    "引言": ("引言", "问题提出", "研究背景"),
    "综述": ("文献综述", "研究述评", "相关研究", "理论基础"),
    "方法": ("研究方法", "研究设计", "研究对象与方法", "研究过程"),
    "结果": ("研究结果", "结果与分析", "研究发现", "结果"),
    "讨论": ("讨论", "结果讨论", "讨论与结论"),
    "结论": ("结论", "结语", "研究结论"),
}
REQUIRED = {
    "generic": ("引言", "方法", "结果", "讨论", "结论"),
    "theory": ("引言", "综述", "讨论", "结论"),
    "review": ("引言", "综述", "方法", "讨论", "结论"),
    "experiment": ("引言", "方法", "结果", "讨论", "结论"),
    "dbr": ("引言", "方法", "结果", "讨论", "结论"),
    "qualitative": ("引言", "方法", "结果", "讨论", "结论"),
    "mixed": ("引言", "方法", "结果", "讨论", "结论"),
    "analytics": ("引言", "方法", "结果", "讨论", "结论"),
}
CUES = {
    "引言": ("问题", "不足", "缺口", "然而", "因此"),
    "方法": ("样本", "对象", "数据", "工具", "过程", "编码", "分析"),
    "结果": ("结果", "发现", "表", "图", "差异", "关系"),
    "讨论": ("解释", "一致", "不同", "意义", "局限", "适用"),
    "结论": ("结论", "贡献", "启示", "建议", "局限"),
}


def read_text(path: Path) -> str:
    if path.suffix.lower() in {".md", ".txt"}:
        return path.read_text(encoding="utf-8-sig")
    if path.suffix.lower() == ".docx":
        with zipfile.ZipFile(path) as archive:
            root = ET.fromstring(archive.read("word/document.xml"))
        return "\n".join("".join(t.text or "" for t in paragraph.iter(f"{WORD_NS}t")) for paragraph in root.iter(f"{WORD_NS}p"))
    raise ValueError("仅支持 .md、.txt 与 .docx 稿件。")


def identify_sections(text: str) -> dict[str, str]:
    """按显式标题切分；未识别标题时保留空结果而不臆测段落功能。"""
    lines = text.splitlines()
    markers: list[tuple[int, str]] = []
    for index, line in enumerate(lines):
        clean = re.sub(r"^\s*(?:#+|\d+(?:\.\d+)*[.、]?|[一二三四五六七八九十]+、)\s*", "", line).strip()
        for name, aliases in SECTION_ALIASES.items():
            if clean in aliases or any(clean.startswith(alias + " ") for alias in aliases):
                markers.append((index, name))
                break
    sections: dict[str, str] = {}
    for position, (start, name) in enumerate(markers):
        end = markers[position + 1][0] if position + 1 < len(markers) else len(lines)
        sections.setdefault(name, "\n".join(lines[start + 1:end]))
    return sections


def infer_genre(text: str) -> str:
    """只在用户未指定时作暂定路由；输出中保留该判断供人工确认。"""
    rules = (
        ("mixed", r"混合方法|定量.{0,12}定性|定性.{0,12}定量"),
        ("analytics", r"SHAP|ALE|机器学习|预测模型|学习分析|教育数据挖掘"),
        ("review", r"系统综述|范围综述|PRISMA|纳入标准|检索式"),
        ("dbr", r"设计型研究|DBR|迭代设计|设计原则"),
        ("experiment", r"准实验|随机分配|对照组|前测.{0,8}后测"),
        ("qualitative", r"质性|扎根理论|案例研究|访谈编码|主题分析"),
        ("theory", r"概念模型|理论模型|理论建构|概念辨析"),
    )
    for genre, pattern in rules:
        if re.search(pattern, text, re.I | re.S):
            return genre
    return "generic"


def main() -> int:
    parser = argparse.ArgumentParser(description="检查论文各节的功能候选缺口。")
    parser.add_argument("manuscript", type=Path, help=".md、.txt 或 .docx 稿件")
    parser.add_argument("genre", nargs="?", choices=GENRES, default="auto", help="文类；默认 auto")
    args = parser.parse_args()
    try:
        text = read_text(args.manuscript)
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 2

    sections = identify_sections(text)
    genre = infer_genre(text) if args.genre == "auto" else args.genre
    required = REQUIRED[genre]
    candidates: list[str] = []
    for name in required:
        if name not in sections:
            candidates.append(f"未识别“{name}”标题；请确认该功能是否由合并章节承担。")
    for name, cues in CUES.items():
        content = sections.get(name, "")
        if content and not any(cue in content for cue in cues):
            candidates.append(f"“{name}”未检出常见功能线索；请人工判断其是否承担应有论证。")
    results = sections.get("结果", "")
    if results and re.search(r"(因此证明|普遍适用|本质上说明|必然导致)", results):
        candidates.append("结果节出现强解释/外推候选语句；请确认解释是否应移入讨论并补充证据。")
    discussion = sections.get("讨论", "")
    if discussion and not re.search(r"(文献|研究|一致|不同|解释|局限|适用)", discussion):
        candidates.append("讨论节缺少文献对话、解释或适用范围线索；请人工检查。")

    overall = "Pass" if not candidates and sections else "Partial"
    route_note = "自动暂定，需人工确认" if args.genre == "auto" else "用户指定"
    print(f"文类：{genre}（{route_note}）")
    print(f"总体：{overall}（候选风险，不替代章节阅读与学术判断）")
    print("识别章节：" + ("、".join(sections) if sections else "未识别到标准标题"))
    if candidates:
        print("候选缺口：")
        for item in candidates:
            print(f"- {item}")
    else:
        print("未发现预设功能缺口；仍需核对问题、证据与结论是否相称。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
