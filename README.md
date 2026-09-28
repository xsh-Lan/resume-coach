# 简历雷达

一个本地 Codex 插件：把简历体检、JD 匹配评分、简历定制和面试准备组织成一个可追溯、可交叉验证的 Agent 工作流。

- 产品名：**简历雷达**
- Agent：`resume-coach`
- 仓库：`resume-coach`
- 核心原则：只使用用户提供的事实，不编造经历、数字或结果
- 输出：Markdown 源文件 + HTML 阅读版 + DOCX 编辑版

## 四个 Skill 的分工

| Skill | 负责 | 不负责 |
|---|---|---|
| `job-application-assistant` | JD 解析、证据映射、100 分匹配评分、差距分析 | 不重写简历、不生成面试题 |
| `resume-refiner` | 事实提取、逐句改写、结构与 ATS | 不评分 JD 匹配、不生成面试题 |
| `excellent-resume-patterns` | 模式选择、岗位基准、结构与量化参照 | 不代替事实、不直接改写 |
| `interview-prep` | 面试问题、STAR、自我介绍、声明可验证性 | 不重写简历、不重算匹配分 |

## 交叉验证

```text
JD → job-application-assistant → 要求与证据矩阵
证据 → resume-refiner → 带 CLAIM/EVIDENCE ID 的改写
模式 → excellent-resume-patterns → 结构与质量基准
面试 → interview-prep → 可解释性与追问风险
        ↓
      resume-coach 汇总、封顶、输出
```

一致性结论使用客观语言：

- 四个 Skill 结论一致。
- 存在一处分歧，需要补充证据后确认。
- 证据不足或结论冲突，暂不给出最终结论。

不使用颜色评级。

详见 `standards/cross_validation.md`。

## 评分体系

使用 `standards/scoring.md` v2.0：

- 六维 100 分制
- 每个维度包含可解释子标准
- 0-4 级评分锚点
- 置信度 A/B/C/D
- P0 诚信封顶
- 交叉验证冲突修正
- 评分校准样例

## 快速使用

```text
/refine-resume
```

或直接说：

> 调用简历雷达，根据这个 JD 体检并修改我的简历。

## 可读输出

默认只交付一个 HTML 逐句体检报告，文字要点直接在对话中说明。需要时再额外输出 DOCX。

```bash
python scripts/render_report.py report.md --output-dir out --formats html
```

## 隐私

输出前通过 `scripts/sanitize_report.py` 和 `hooks.json` 删除姓名、邮箱、手机、微信等联系方式，保留院校、公司和项目内容。姓名和联系方式不写入事实库。

详细结构见 `docs/architecture.md`。
