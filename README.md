# 简历雷达

一个本地 Codex 插件，将简历诊断、JD 匹配评分、简历定制和面试准备封装为 `resume-radar` 子 Agent。

## 组成

- `resume-radar`：主协调 Agent
- `resume-refiner`：事实提取、逐句改写、结构与 ATS
- `job-application-assistant`：JD 解析、匹配评分、简历定制、面试准备（已裁剪为自包含版本）
- `interview-prep`：岗位面试准备
- `excellent-resume-patterns`：去标识化优秀简历模式库

## 关键机制

- `standards/scoring.md`：统一 100 分评分标准
- `templates/`：体检报告、改写方案、面试包模板
- `profile/`：用户事实库、证据库、缺口库和版本
- `scripts/sanitize_report.py` + `hooks.json`：输出前删除姓名和联系方式，保留院校与简历内容
- `evals/`：自动化结构和机制评测

## 使用

```text
/refine-resume
```

或直接说：

> 调用简历雷达，根据这个 JD 体检并修改我的简历。

## 隐私

姓名和联系方式不会写入输出文件。事实库同样不保存姓名和联系方式。

## 可读格式

Markdown 作为源文件保留，同时使用 `scripts/render_report.py` 自动导出：

- HTML：浏览器直接阅读，也可打印为 PDF
- DOCX：Word/WPS 编辑，并可另存为 PDF

```bash
python scripts/render_report.py report.md --output-dir out --formats html docx
```
