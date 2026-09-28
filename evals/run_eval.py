#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

PLUGIN = Path(__file__).resolve().parents[1]
passed = []
failed = []

def check(name, cond, detail=""):
    if cond:
        passed.append(name)
    else:
        failed.append((name, detail))

def text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore")

def main():
    # 1. Manifest
    manifest_path = PLUGIN / ".codex-plugin" / "plugin.json"
    manifest = json.loads(text(manifest_path))
    check("manifest.valid", manifest.get("name") == "resume-coach")

    # 2. Required files
    for rel in [
        "agents/resume-coach.md",
        "standards/scoring.md",
        "standards/scoring_calibration.json",
        "standards/cross_validation.md",
        "PRODUCT.md",
        "docs/architecture.md",
        "templates/体检报告.md",
        "templates/改写方案.md",
        "templates/面试包.md",
        "scripts/sanitize_report.py",
        "scripts/render_report.py",
        "hooks.json",
        "skills/excellent-resume-patterns/pattern_index.json",
    ]:
        check(f"file.{rel}", (PLUGIN / rel).exists())
    for rel in ["profile/candidate_profile.md", "profile/evidence.json", "profile/gap.json"]:
        ok = (PLUGIN / rel).exists() or (PLUGIN / (rel + ".example")).exists()
        check(f"file.{rel}", ok, "actual or example template required")

    # 3. Cropped job-application-assistant
    jaa = text(PLUGIN / "skills" / "job-application-assistant" / "SKILL.md")
    for bad in ["documents/README.md", "cover_letters/", ".claude/commands/apply.md", "/apply", "/scrape", "/rank", "cv/"]:
        check(f"crop.no-reference.{bad}", bad not in jaa, bad)

    # 4. Scorecard
    sc = json.loads(text(PLUGIN / "templates" / "scorecard.json"))
    total = sum(d["max"] for d in sc["dimensions"])
    check("scorecard.total", total == sc.get("total", 0), f"sum={total}")
    scoring = text(PLUGIN / "standards" / "scoring.md")
    check("scorecard.six_dimensions", all(k in scoring for k in ["岗位匹配","经历质量","量化与证据","结构与阅读","AI/数据专项","语言与诚信"]))
    check("scorecard.v2", "v2.0" in scoring and "P0" in scoring and "置信度" in scoring and "封顶" in scoring)
    check("scorecard.subcriteria", all("subcriteria" in d for d in sc["dimensions"]))
    check("scorecard.calibration", (PLUGIN / "standards" / "scoring_calibration.json").exists())
    cross = text(PLUGIN / "standards" / "cross_validation.md")
    check("cross_validation.skills", all(x in cross for x in ["job-application-assistant","resume-refiner","excellent-resume-patterns","interview-prep"]))

    # 5. Templates fields
    report = text(PLUGIN / "templates" / "体检报告.md")
    rewrite = text(PLUGIN / "templates" / "改写方案.md")
    interview = text(PLUGIN / "templates" / "面试包.md")
    for req in ["综合体检","Scorecard","逐句体检","最优先修改点","面试追问风险"]:
        check(f"template.report.{req}", req in report)
    for req in ["事实校验","改写后内容","修改说明","诚信审计"]:
        check(f"template.rewrite.{req}", req in rewrite)
    for req in ["STAR","自我介绍","反问清单","风险提示"]:
        check(f"template.interview.{req}", req in interview)

    # 6. Pattern index
    idx = json.loads(text(PLUGIN / "skills" / "excellent-resume-patterns" / "pattern_index.json"))
    patterns = idx.get("patterns", [])
    check("pattern_index.count", len(patterns) == 10, str(len(patterns)))
    required_keys = {"id","title","profile","target_roles","competencies","metric_types","keywords"}
    check("pattern_index.schema", all(required_keys.issubset(p.keys()) for p in patterns))

    # 7. Agent safety rules
    agent = text(PLUGIN / "agents" / "resume-coach.md")
    check("agent.no_old_name", ("resume-" + "radar") not in agent)
    for req in ["untrusted data", "Ignore instructions", "sanitizer", "name and contact", "school names and resume content", "Never invent"]:
        check(f"agent.safety.{req}", req in agent)
    check("agent.quote_guard", "Only quote or reference sentences that actually exist" in agent)
    check("agent.minimal_output", "One HTML file per target direction" in agent and "Do not write Markdown or DOCX files" in agent)
    check("agent.deep_use_guide", "如需进一步使用简历雷达" in agent)
    # Objective language: no color rating words in product surfaces.
    for rel in ["agents/resume-coach.md", "commands/refine-resume.md", "standards/cross_validation.md", "README.md"]:
        content = text(PLUGIN / rel)
        check(f"objective.no_color.{rel}", not any(x in content for x in ["GREEN", "YELLOW", "RED"]), rel)

    # 8. Sanitizer unit test
    fixture = "[姓名：测试候选人]\n邮箱：test@example.com 手机：13800138000\n武汉大学 本科 管理科学\nRAG、F1 score 80%\n"
    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "体检报告.md"
        f.write_text(fixture, encoding="utf-8")
        r = subprocess.run([sys.executable, str(PLUGIN / "scripts" / "sanitize_report.py"), "--file", str(f)], capture_output=True, text=True, encoding='utf-8', errors='ignore')
        out = f.read_text(encoding="utf-8")
        check("sanitizer.name_removed", "测试候选人" not in out)
        check("sanitizer.contact_removed", "test@example.com" not in out and "13800138000" not in out)
        check("sanitizer.school_kept", "武汉大学" in out)
        check("sanitizer.content_kept", "RAG、F1 score 80%" in out)

    # 9. Renderer smoke test
    with tempfile.TemporaryDirectory() as td:
        src = Path(td) / "report.md"
        src.write_text("# 测试报告\n\n## 结论\n\n- 项目一\n- 项目二\n\n| A | B |\n|---|---|\n| 1 | 2 |\n", encoding="utf-8")
        out = Path(td) / "out"
        subprocess.run([sys.executable, str(PLUGIN / "scripts" / "render_report.py"), str(src), "--output-dir", str(out), "--formats", "html", "docx"], capture_output=True, text=True, encoding="utf-8", errors="ignore")
        check("renderer.html", (out / "report.html").exists())
        check("renderer.docx", (out / "report.docx").exists())
    with tempfile.TemporaryDirectory() as td:
        src = Path(td) / "report.md"
        src.write_text("# 默认输出测试\n\n- 只要 HTML\n", encoding="utf-8")
        out = Path(td) / "out2"
        subprocess.run([sys.executable, str(PLUGIN / "scripts" / "render_report.py"), str(src), "--output-dir", str(out)], capture_output=True, text=True, encoding="utf-8", errors="ignore")
        check("renderer.default_html_only", (out / "report.html").exists() and not (out / "report.docx").exists())

    # 10. Optional report validation
    ap = argparse.ArgumentParser()
    ap.add_argument("--report")
    ap.add_argument("--target", choices=["ai_product", "data_analysis"])
    args = ap.parse_args()
    if args.report and args.target:
        expected = json.loads(text(PLUGIN / "evals" / "expected_flags.json"))[args.target]
        rep = text(Path(args.report))
        for flag in expected["risk_flags"]:
            check(f"report.risk.{flag}", flag in rep)
        for bad in expected["must_not"]:
            check(f"report.no_pii.{bad}", bad not in rep)

    print(f"PASS {len(passed)}")
    for name, detail in failed:
        print(f"FAIL {name} :: {detail}")
    print(f"TOTAL {len(passed)+len(failed)}  FAILED {len(failed)}")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
