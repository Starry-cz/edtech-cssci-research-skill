#!/usr/bin/env python3
"""扫描稿件标题、摘要与全文的候选风险；结果用于人工复核，不能替代方法审计。"""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree


WORD_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

# 这些术语跨越方法、性能、解释和稳健性层，组合出现时才提示摘要可能在复述分析流程。
TECHNICAL_TERM_GROUPS = {
    "方法": ("模型比较", "交叉验证", "XGBoost", "GBRT", "梯度提升", "随机森林", "超参数"),
    "性能": ("R²", "R2", "MAE", "RMSE", "MSE", "准确率", "AUC"),
    "解释": ("SHAP", "ALE", "PDP", "置换重要性", "特征重要性"),
    "稳健性": ("Bootstrap", "重抽样", "删除节点", "消融", "稳定性"),
}


def read_paragraphs(path: Path) -> list[str]:
    """读取段落，保留文本边界，避免把正文小标题误判为摘要标签。"""
    if path.suffix.lower() in {".md", ".txt"}:
        return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
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
    return paragraphs


def find_abstract(paragraphs: list[str]) -> tuple[str, int | None]:
    """提取中文摘要；摘要缺失时返回空文本，避免用正文全文替代摘要审计。"""
    for index, paragraph in enumerate(paragraphs):
        match = re.match(r"^摘\s*要\s*[：:]?\s*(.*)$", paragraph, flags=re.IGNORECASE)
        if not match:
            continue
        abstract_parts = [match.group(1).strip()] if match.group(1).strip() else []
        for following in paragraphs[index + 1 :]:
            if re.match(r"^(?:关键词|关\s*键\s*词|Key\s*words?)\s*[：:]", following, flags=re.IGNORECASE):
                break
            if re.match(r"^[一二三四五六七八九十]+、|^\d+[.、]", following):
                break
            abstract_parts.append(following)
        return "\n".join(abstract_parts), index
    return "", None


def find_title(paragraphs: list[str], abstract_index: int | None) -> str:
    """只从摘要前的短标题区取题目，避免把文献引文中的强词误作论文标题。"""
    before_abstract = paragraphs[:abstract_index] if abstract_index is not None else paragraphs[:3]
    return " ".join(before_abstract[:3])


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


def add_technical_bandwidth_signal(items: list[tuple[str, str, list[str]]], abstract: str) -> None:
    """只在多个证据层同时拥挤时提示，避免把单个必要术语当成错误。"""
    matched_groups: dict[str, list[str]] = {}
    for group, terms in TECHNICAL_TERM_GROUPS.items():
        matched = [term for term in terms if term.lower() in abstract.lower()]
        if matched:
            matched_groups[group] = matched
    distinct_terms = {term for terms in matched_groups.values() for term in terms}
    if len(matched_groups) >= 3 and len(distinct_terms) >= 4:
        summary = "；".join(f"{group}：{'、'.join(terms)}" for group, terms in matched_groups.items())
        items.append((
            "摘要技术带宽过载候选",
            "这不是按术语数量自动判错。先删去不改变中心回答的算法目录、重复数字和次级诊断；仅保留能说明研究类型、验证角色或中心发现可信度的证据锚点。",
            [summary],
        ))


def main() -> int:
    if len(sys.argv) != 2:
        print("用法：python scripts/audit_manuscript_surface.py <稿件.docx|md|txt>")
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"找不到文件：{path}")
        return 2
    try:
        paragraphs = read_paragraphs(path)
    except (OSError, ValueError, KeyError, zipfile.BadZipFile, ElementTree.ParseError) as error:
        print(f"无法读取稿件：{error}")
        return 2

    text = "\n".join(paragraphs)
    abstract, abstract_index = find_abstract(paragraphs)
    title = find_title(paragraphs, abstract_index)
    candidates: list[tuple[str, str, list[str]]] = []
    if abstract:
        add_if_found(candidates, abstract, "结构式摘要标签", r"(?:目的|方法|结果|结论)\s*[：:]", "除非期刊官方明确要求，改为连续摘要；保留内部论证卡而非正文标签。")
        add_if_found(candidates, abstract, "摘要内部标签候选", r"\bRQ\s*\d+\b|\[\s*(?:待补|待核验|TODO|TODO:|placeholder)[^\]]*\]", "将工作标签移至修改说明，清洁摘要只保留已核验内容。")
        add_if_found(candidates, abstract, "摘要强结论候选", r"塑造(?:了|出)?|作用机制|最优(?:模型|方案)?|稳定阈值|决定(?:了|性)?", "回查设计与验证角色；预测研究通常改用预测、关联或模型依赖表述。")
        add_if_found(candidates, abstract, "摘要方法堆叠", r"(?:SHAP|ALE|Bootstrap|XGBoost|随机森林|梯度提升|交叉验证|消融).{0,30}(?:SHAP|ALE|Bootstrap|XGBoost|随机森林|梯度提升|交叉验证|消融).{0,50}", "摘要只保留理解设计所需的方法功能；完整算法与诊断转入方法或附录。")
        add_technical_bandwidth_signal(candidates, abstract)
        add_if_found(candidates, abstract, "摘要机制跃迁候选", r"(?:SHAP|特征重要性|预测重要性).{0,100}(?:闭环|链条|路径|机制)|(?:闭环|链条|路径|机制).{0,100}(?:SHAP|特征重要性|预测重要性)", "并列特征不构成时序或机制；要求过程、交互、时序或干预证据。")
        add_if_found(candidates, abstract, "摘要非因果边界提示", r"(?:不(?:能|宜)|并非|不等同于|不表示).{0,36}(?:因果|机制|效应|导致|提高)|(?:预测|关联).{0,24}(?:不(?:能|宜)|并非|不等同于|不表示)", "这是正向信号，仍需核对标题、摘要、结果和结论是否保持同一边界。")
    else:
        candidates.append(("未识别中文摘要", "未找到以“摘要”开头且以关键词或章节边界结束的摘要区；请人工指定摘要后再审计。", []))

    add_if_found(candidates, title, "预测研究强标题候选", r"何以达成|塑造(?:了|出)?|作用机制|最优(?:模型|方案)?|稳定阈值|决定(?:了|性)?", "核对题目动词是否超过设计；预测研究通常改用预测、关联或模型依赖表述。")
    add_if_found(candidates, text, "测试集选模候选", r"(?:同一|相同).{0,45}(?:训练[—-]测试|测试集).{0,180}(?:比较|筛选|选择).{0,120}(?:20个|多个|若干|候选).{0,220}(?:模型|GBRT|梯度提升)|(?:测试集).{0,120}(?:20个|多个|若干).{0,160}(?:模型).{0,160}(?:最高|最优|表现最好)", "人工核对训练/验证/最终测试角色；若测试集参与选模，阻断最终样本外结论并重跑或降级。")
    add_if_found(candidates, text, "全文占位符候选", r"\[\s*(?:待补|待核验|TODO|TODO:|placeholder)[^\]]*\]", "将工作标签移至修改说明，清洁稿只保留已核验内容。")

    blockers = {"测试集选模候选", "预测研究强标题候选", "摘要强结论候选"}
    blocker_names = [name for name, _, _ in candidates if name in blockers]
    status = "阻断" if blocker_names else ("探索性可写" if candidates else "投稿就绪候选")
    print(f"稿件表层审计：{path.name}")
    print(f"识别范围：标题 {'已识别' if title else '未识别'}；中文摘要 {'已识别' if abstract else '未识别'}。")
    print(f"建议发布状态：{status}")
    if blocker_names:
        print("阻断原因：" + "、".join(blocker_names))
    if not candidates:
        print("未发现预设表层信号。仍须人工核对数据切分、泄漏、准则污染、结果复现与期刊要求。")
    for name, advice, snippets in candidates:
        print(f"\n[{name}]\n建议：{advice}")
        for snippet in snippets:
            print(f"- {snippet}")
    print("\n说明：结构式标签、方法堆叠和机制跃迁只在已识别摘要中扫描；测试集选模和占位符在全文扫描。本工具只提示候选风险，不能证明不存在泄漏、因果识别或复现问题。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
