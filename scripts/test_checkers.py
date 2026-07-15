#!/usr/bin/env python3
"""为期刊、章节与终稿表层检查器生成最小样本并执行回归测试。"""

from __future__ import annotations

import html
import os
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def make_docx(path: Path, paragraphs: list[str]) -> None:
    """用最小 OOXML 生成仅供文本提取回归测试使用的 DOCX。"""
    body = "".join(
        f'<w:p><w:r><w:t xml:space="preserve">{html.escape(item)}</w:t></w:r></w:p>'
        for item in paragraphs
    )
    document = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        f"<w:body>{body}<w:sectPr/></w:body></w:document>"
    )
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        "</Types>"
    )
    relationships = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
        'Target="word/document.xml"/></Relationships>'
    )
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types)
        archive.writestr("_rels/.rels", relationships)
        archive.writestr("word/document.xml", document)


def run(*args: str) -> str:
    result = subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        check=True,
        text=True,
        encoding="utf-8",
        capture_output=True,
        env={**os.environ, "PYTHONUTF8": "1"},
    )
    return result.stdout


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="edtech-skill-check-") as temp:
        folder = Path(temp)
        complete = folder / "complete.md"
        complete.write_text(
            """# 合成研究标题
摘要：本研究基于合成课堂观察材料，考察反馈组织与学习参与的关系。研究设计、结果与含义均采用虚构示例，仅用于检查器回归。
关键词：课堂观察；反馈；学习参与；研究设计；教育技术
Abstract: This synthetic study is used only for checker regression.
Keywords: classroom observation; feedback; engagement; design; educational technology
# 引言
现有研究仍存在问题，因此提出本研究。
# 研究方法
样本、数据、工具、研究过程与分析方案如下。
# 研究结果
结果见表1，主要发现表现为变量关系差异。
# 讨论
该发现与既有研究一致，其解释、意义和适用范围仍需讨论。
# 结论
本研究结论、贡献、启示与局限如下。
""",
            encoding="utf-8",
        )
        incomplete = folder / "incomplete.txt"
        incomplete.write_text("作者：合成作者\n摘要：简短测试。\n关键词：教育技术；课堂\n", encoding="utf-8")
        mixed = folder / "mixed.md"
        mixed.write_text("本研究采用混合方法，并在定量阶段使用 SHAP。\n" + complete.read_text(encoding="utf-8"), encoding="utf-8")
        final_placeholder = folder / "final-placeholder.md"
        final_placeholder.write_text(
            """# 合成研究标题
摘要：本研究基于合成课堂观察材料形成初步分析。关键词：课堂观察；教育技术
# 研究方法
编码质量、数据授权和伦理信息应如实说明，投稿时补充完整材料。
""",
            encoding="utf-8",
        )
        docx = folder / "complete.docx"
        make_docx(docx, complete.read_text(encoding="utf-8").splitlines())

        journal_pass = run("scripts/check_journal_profile.py", str(complete), "electric-education-research", "--as-of", "2026-07-15")
        journal_fail = run("scripts/check_journal_profile.py", str(incomplete), "electric-education-research", "--as-of", "2026-07-15")
        journal_stale = run("scripts/check_journal_profile.py", str(complete), "electric-education-research", "--as-of", "2027-01-15")
        section_md = run("scripts/check_section_function.py", str(complete), "experiment")
        section_docx = run("scripts/check_section_function.py", str(docx), "auto")
        section_mixed = run("scripts/check_section_function.py", str(mixed), "auto")
        final_surface = run("scripts/audit_manuscript_surface.py", str(final_placeholder), "--final")

        assertions = (
            ("总体：Pass", journal_pass, "期刊规则通过样本"),
            ("总体：Fail", journal_fail, "期刊规则失败样本"),
            ("总体：待官方核验", journal_stale, "画像过期样本"),
            ("总体：Pass", section_md, "章节功能 Markdown 样本"),
            ("总体：Pass", section_docx, "章节功能 DOCX 样本"),
            ("自动暂定", section_docx, "自动文类路由"),
            ("文类：mixed", section_mixed, "混合方法优先路由"),
            ("最终提交不通过", final_surface, "终稿占位式兜底阻断"),
            ("最终稿合规兜底候选", final_surface, "终稿合规兜底识别"),
        )
        failed = [label for expected, output, label in assertions if expected not in output]
        if failed:
            print("回归失败：" + "、".join(failed))
            return 1
    print("检查器回归通过：MD/TXT/DOCX、Pass/Fail、画像过期与自动文类路由均符合预期。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
