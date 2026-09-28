# 架构

## 组件

```text
resume-coach plugin
├── agents/resume-coach.md        主协调 Agent
├── skills/                       四个分工明确的 Skill
├── standards/                    评分、校准、交叉验证
├── templates/                    标准输出 Schema
├── profile/                      用户事实库
├── scripts/                      脱敏与可读输出
├── hooks.json                    输出安全机制
└── evals/                        自动化评测
```

## 数据流

```text
用户简历 + JD
  ↓
resume-refiner：事实与证据
  ↓
job-application-assistant：要求、评分与差距
  ↓
excellent-resume-patterns：结构与模式校验
  ↓
resume-refiner：改写
  ↓
interview-prep：声明可解释性验证
  ↓
resume-coach：冲突处理、封顶、最终输出
  ↓
Markdown + HTML + DOCX
```

## 控制点

1. 事实控制：所有关键声明必须有 CLAIM/EVIDENCE ID。
2. 评分控制：每个分数必须对应子标准和锚点。
3. 诚信控制：P0 问题触发封顶。
4. 隐私控制：输出前删除姓名和联系方式。
5. 质量输出：默认生成 HTML 和 DOCX。
