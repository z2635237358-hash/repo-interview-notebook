from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit


FUTURE_PATTERNS = ("后续计划", "计划支持", "未来将", "待实现", "TODO", "TBD")
EVIDENCE_LABELS = ("[已验证]", "[完成态口径]", "[容量估算]", "[边界条件]")
ESTIMATE_HINTS = ("估算", "预计", "目标", "预算", "计划支持", "后续计划")
REQUIRED_ROOT_PAGES = (
    "01 项目总览与 60 秒介绍.md",
    "04 术语、不变量与状态机.md",
    "80 容量估算与统一指标.md",
    "90 攻击性追问与答辩.md",
    "99 面试前速记卡.md",
)
REQUIRED_MAINLINE_PAGES = ("01 完成态设计.md", "02 三级问答树.md", "03 故障与质疑.md")


@dataclass(frozen=True)
class Issue:
    path: Path
    message: str


def strip_code(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`]*`", "", text)


def markdown_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        return target[1:target.index(">")]
    return target.split(maxsplit=1)[0]


def validate(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    files = [path for path in root.rglob("*") if path.is_file()]
    markdown = [path for path in files if path.suffix == ".md"]
    relative = {str(path.relative_to(root)): path for path in files}
    by_stem: dict[str, list[Path]] = {}
    for path in markdown:
        by_stem.setdefault(path.stem, []).append(path)

    for name in REQUIRED_ROOT_PAGES:
        if name not in relative:
            issues.append(Issue(root, f"missing root page: {name}"))

    for directory in root.iterdir():
        if directory.is_dir() and re.match(r"^[1-6]0\s", directory.name):
            for name in REQUIRED_MAINLINE_PAGES:
                if not (directory / name).is_file():
                    issues.append(Issue(directory, f"missing mainline document: {name}"))

    for path in markdown:
        text = strip_code(path.read_text(encoding="utf-8"))
        for raw in re.findall(r"\[\[([^\]]+)\]\]", text):
            target = raw.split("|", 1)[0].split("#", 1)[0]
            if not target:
                continue
            if "/" in target or Path(target).suffix:
                candidates = [target] if Path(target).suffix else [target, target + ".md"]
                found = any(candidate in relative for candidate in candidates)
            else:
                found = len(by_stem.get(target, [])) == 1
            if not found:
                issues.append(Issue(path, f"broken link: {raw}"))

        for raw in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
            target = markdown_target(raw)
            parsed = urlsplit(target)
            if parsed.scheme.lower() in {"http", "https", "mailto"} or target.startswith("#"):
                continue
            decoded_path = unquote(parsed.path)
            if not decoded_path:
                continue
            candidate = (path.parent / decoded_path).resolve()
            try:
                candidate.relative_to(root)
            except ValueError:
                found = False
            else:
                found = candidate.exists()
            if not found:
                issues.append(Issue(path, f"broken link: {raw}"))

        for phrase in FUTURE_PATTERNS:
            if phrase in text:
                issues.append(Issue(path, f"future-tense implementation language: {phrase}"))

        for line_number, line in enumerate(text.splitlines(), 1):
            visible_line = re.sub(r"(!?\[[^\]]*\])\([^)]+\)", r"\1", line)
            quantitative = re.search(r"\b\d+(?:\.\d+)?\s*(?:QPS|TPS|ms|毫秒|秒|万|%|并发)\b", visible_line, re.I)
            needs_classification = path.name == "80 容量估算与统一指标.md" or any(hint in visible_line for hint in ESTIMATE_HINTS)
            if quantitative and needs_classification:
                context = "\n".join(text.splitlines()[max(0, line_number - 3):line_number + 1])
                if not any(label in context for label in EVIDENCE_LABELS):
                    issues.append(Issue(path, f"unclassified quantitative claim at line {line_number}"))

    for path in files:
        if path.suffix in {".svg", ".drawio"}:
            try:
                ET.parse(path)
            except ET.ParseError as exc:
                issues.append(Issue(path, f"invalid XML: {exc}"))

    return issues


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_notebook.py NOTEBOOK_ROOT")
        return 2
    root = Path(argv[1]).expanduser().resolve()
    if not root.is_dir():
        print(f"not a directory: {root}")
        return 2
    issues = validate(root)
    if issues:
        for issue in issues:
            print(f"FAIL {issue.path}: {issue.message}")
        return 1
    print(f"PASS {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
