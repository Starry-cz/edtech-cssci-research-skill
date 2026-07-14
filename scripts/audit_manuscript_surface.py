#!/usr/bin/env python3
"""扫描稿件表层的候选风险；结果用于人工复核，不能替代方法审计。"""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree


WORD_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def read_text(path: Path) -> str:
    """读取 txt/md，或提取 docx 正文中的可见文字；仅支持本工具声明的三种格式。"""
    if path.suffix.lower() in {".md", ".txt"}:
        return path.read_text(encoding="utf-8")
    if path.suffix.lower() != ".docx":
        raise ValueError("仅支持 .docx、.md 或 .txt 文件")
    with zipfile.ZipFile(path) as archive:
        xml = archive.read("word/document.xml")
    root = ElementTree.fromstring(xml)
    paragraphs: list[str] = []
    for paragraph in root.iter(f"{WORD_NS}p"):
        value = "".join(node.text or "" for node in paragraph.iter(f"{WORD_NS}t"))
        if value.strip():
            paragraphs.append(value.strip())
    return "\n".join(paragraphs)


def first_matches(text: str, pattern: str, limit: int = 4) -> list[str]:
    """返回少量命中片段，避免把稿件全文或敏感材料写入审计报告。"""
    matches: list[str] = []
    for match in re.finditer(pattern, text, flags=re.IGNORECASE):
        start = max(0, match.start() - 24)
        end = min(len(text), match.end() + 42)
        snippet = re.sub(r"\s+", " ", text[start:end])
        if snippet not in matches:
            matches.append(snippet)
        if len(matches) == limit:
            break
    return matches


def add_if_found(items: list[tuple[str, str, list[str]]], text: str, name: str, pattern: str, advice: str) -> None:
    found = first_matches(text, pattern)
    if found:
        items.append((name, advice, found))


def main() -> int:
    if len(sys.argv) != 2:
        print("用法：python scripts/audit_manuscript_surface.py <稿件.docx|md|txt>")
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"找不到文件：{path}")
        return 2
    try:
        text = read_text(path)
    except (OSError, ValueError, KeyError, zipfile.BadZipFile, ElementTree.ParseError) as error:
        print(f"无法读取稿件：{error}")
        return 2

    candidates: list[tuple[str, str, list[str]]] = []
    add_if_found(candidates, text, "结构式摘要标签", r"(?:目的|方法|结果|结论)\s*[：:]", "除非期刊官方明确要求，改为连续摘要；保留内部论证卡而非正文标签。")
    add_if_found(candidates, text, "RQ/占位符泄漏", r"\bRQ\s*\d+\b|\[\s*(?:待补|待核验|TODO|TODO:|placeholder)[^\]]*\]", "将工作标签移至修改说明，清洁稿只保留已核验内容。")
    add_if_found(candidates, text, "预测研究强标题或强结论", r"何以达成|塑造(?:了|出)?|作用机制|最优(?:模型|方案)?|稳定阈值|决定(?:了|性)?", "核对设计是否支持因果、机制或阈值；预测研究通常改用预测、关联或模型依赖表述。")
    add_if_found(candidates, text, "方法堆叠", r"(?:SHAP|ALE|Bootstrap|XGBoost|随机森林|梯度提升|交叉验证|消融).{0,30}(?:SHAP|ALE|Bootstrap|XGBoost|随机森林|梯度提升|交叉验证|消融).{0,50}", "摘要只保留理解设计所需的方法功能；完整算法与诊断转入方法或附录。")
    add_if_found(candidates, text, "测试集选模候选", r"(?:同一|相同).{0,20}(?:训练[—-]测试|测试集).{0,60}(?:比较|筛选|选择).{0,60}(?:最高|最优|表现最好)|(?:测试集).{0,80}(?:20个|多个|若干).{0,80}(?:模型).{0,80}(?:最高|最优)", "人工核对训练/验证/最终测试角色；若测试集参与选模，阻断最终样本外结论并重跑或降级。")
    add_if_found(candidates, text, "机制链候选", r"(?:SHAP|特征重要性|预测重要性).{0,100}(?:闭环|链条|路径|机制)|(?:闭环|链条|路径|机制).{0,100}(?:SHAP|特征重要性|预测重要性)", "并列特征不构成时序或机制；要求过程、交互、时序或干预证据。")
    add_if_found(candidates, text, "非因果边界提示", r"(?:不(?:能|宜)|并非|不等同于).{0,24}(?:因果|机制|效应)|(?:预测|关联).{0,24}(?:不(?:能|宜)|并非|不等同于)", "这是正向信号，仍需核对标题、摘要、结果和结论是否保持同一边界。")

    blockers = {"测试集选模候选", "预测研究强标题或强结论"}
    blocker_names = [name for name, _, _ in candidates if name in blockers]
    status = "阻断" if blocker_names else ("探索性可写" if candidates else "投稿就绪候选")
    print(f"稿件表层审计：{path.name}")
    print(f"建议发布状态：{status}")
    if blocker_names:
        print("阻断原因：" + "、".join(blocker_names))
    if not candidates:
        print("未发现预设表层信号。仍须人工核对数据切分、泄漏、准则污染、结果复现与期刊要求。")
    for name, advice, snippets in candidates:
        print(f"\n[{name}]\n建议：{advice}")
        for snippet in snippets:
            print(f"- {snippet}")
    print("\n说明：本工具只扫描文字候选风险；不能证明不存在泄漏、因果识别或复现问题。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
