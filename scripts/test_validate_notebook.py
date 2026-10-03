from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("validate_notebook.py")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_valid_notebook(root: Path) -> None:
    write(root / "00 口径与生成规范.md", "# 规范\n\n[完成态口径]\n")
    write(
        root / "01 项目总览与 60 秒介绍.md",
        "# 总览\n\n"
        "[[10 并发/01 完成态设计]]\n\n"
        "[并发设计](10%20并发/01%20完成态设计.md)\n\n"
        "[统一指标](80%20容量估算与统一指标.md)\n\n"
        "[站外资料](https://example.com) · [邮件](mailto:test@example.com) · [本页](#总览)\n",
    )
    write(root / "04 术语、不变量与状态机.md", "# 术语\n\n状态：OPEN → CLOSED\n")
    write(root / "80 容量估算与统一指标.md", "# 指标\n\n[容量估算] 峰值 800 QPS；假设：读占 80%。\n")
    write(root / "90 攻击性追问与答辩.md", "# 攻击性追问与答辩\n")
    write(root / "99 面试前速记卡.md", "# 面试前速记卡\n")
    write(
        root / "10 并发/01 完成态设计.md",
        "# 完成态设计\n\n"
        "![[assets/architecture/main.svg]]\n\n"
        "![主架构](../assets/architecture/main.svg)\n",
    )
    write(root / "10 并发/02 三级问答树.md", "# 三级问答树\n")
    write(root / "10 并发/03 故障与质疑.md", "# 故障与质疑\n")
    write(root / "assets/architecture/main.svg", '<svg xmlns="http://www.w3.org/2000/svg"><rect width="10" height="10" fill="#fff"/></svg>')
    write(root / "assets/architecture/source/main.drawio", '<mxfile><diagram><mxGraphModel><root/></mxGraphModel></diagram></mxfile>')


class ValidatorTests(unittest.TestCase):
    def run_validator(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(root)],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_valid_notebook_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build_valid_notebook(root)
            result = self.run_validator(root)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("PASS", result.stdout)

    def test_broken_wiki_link_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build_valid_notebook(root)
            write(root / "01 项目总览与 60 秒介绍.md", "# 总览\n\n[[不存在页面]]\n")
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("broken link", result.stdout)

    def test_broken_relative_markdown_link_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build_valid_notebook(root)
            write(
                root / "01 项目总览与 60 秒介绍.md",
                "# 总览\n\n[不存在页面](10%20并发/不存在页面.md)\n",
            )
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("broken link", result.stdout)

    def test_missing_mainline_document_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build_valid_notebook(root)
            (root / "10 并发/03 故障与质疑.md").unlink()
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("missing mainline document", result.stdout)

    def test_future_tense_and_unlabelled_estimate_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build_valid_notebook(root)
            write(root / "10 并发/01 完成态设计.md", "# 完成态设计\n\n后续计划支持 5000 QPS。\n")
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("future-tense implementation language", result.stdout)
            self.assertIn("unclassified quantitative claim", result.stdout)

    def test_malformed_xml_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build_valid_notebook(root)
            write(root / "assets/architecture/main.svg", "<svg>")
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("invalid XML", result.stdout)


if __name__ == "__main__":
    unittest.main()
