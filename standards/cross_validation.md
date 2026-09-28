# 四个 Skill 交叉验证协议

## 职责分工

| Skill | 负责 | 不负责 |
|---|---|---|
| `job-application-assistant` | JD 解析、证据映射、100 分评分、差距分析 | 不重写简历、不生成面试题 |
| `resume-refiner` | 事实提取、逐句改写、结构、ATS/视觉 | 不评分 JD 匹配、不生成面试题 |
| `excellent-resume-patterns` | 模式选择、岗位基准、结构和量化参照 | 不代替事实、不直接改写 |
| `interview-prep` | 面试问题、STAR、声明可解释性验证 | 不重写简历、不重算匹配分 |

## 交叉验证流程

```text
JD → job-application-assistant 要求和证据矩阵
     ↓
resume-refiner 改写并回填证据 ID
     ↓
excellent-resume-patterns 检查结构和模式合理性
     ↓
interview-prep 检查声明能否被面试官验证
     ↓
resume-coach 汇总冲突、封顶和最终输出
```

## 冲突等级

- `GREEN`：四个 Skill 均通过。
- `YELLOW`：一个 Skill 提出非致命冲突，修复后输出。
- `RED`：两个以上 Skill 冲突，或出现 P0 诚信问题，停止最终投递版本。

## Claim ID 规则

每个关键声明分配：

```text
[CLAIM-001] 原始事实
[EVIDENCE-001] 证据来源/材料
[REWRITE-001] 改写版本
[RISK-001] 面试或诚信风险
```

最终报告必须能追溯：

```text
CLAIM → EVIDENCE → REWRITE → RISK
```
