---
name: excellent-resume-patterns
description: De-identified resume patterns distilled from a local collection of strong product, data, AI, business-analysis, operations and supply-chain resumes. Use when tailoring a resume, selecting role-specific evidence, choosing a resume structure, improving quantified bullets, translating a non-target background, or checking whether a resume reaches the quality level of strong peer examples. Never use this skill to copy another person's facts or wording.
---

# Excellent Resume Patterns

## 在“简历雷达”中的职责边界

**负责：** 基于 `pattern_index.json` 选择结构和证据模式，提供岗位能力基准、量化方式和质量参照。

**不负责：** 不替用户写经历，不计算 JD 匹配分，不生成面试题。

**交叉验证：** 为 `resume-refiner` 提供结构基准；对 JD 匹配结果提供模式层面的合理性检查；发现“结构很强但事实不足”时必须明确提示。


This skill is a de-identified pattern library, not a set of resumes to copy.

## Core rules

1. Use patterns only for structure, emphasis, metrics, and language strategy.
2. Never transfer a school, employer, project, metric, award, or achievement from a pattern to the user.
3. A bullet can only use facts explicitly supplied or verified by the user.
4. Preserve the difference between actual results, expected results, team results, and individual contribution.
5. Prefer the user's strongest verified evidence over a superficially similar example from this library.

## Read order

1. Read `references/case_patterns.md` to find the closest background-to-role path.
2. Read `references/role_playbooks.md` to determine the evidence required for the target role.
3. Read `references/writing_system.md` for bullet structure and quantification.
4. Read `references/rewrite_workflow.md` when performing a full resume rewrite.
5. Use `references/quality_standard.md` for the final audit.
6. Read `references/privacy_and_provenance.md` if the user asks where the patterns came from or how they were anonymized.

## Matching procedure

Choose at most three case patterns:

- Pattern 1: closest background transition.
- Pattern 2: target-role evidence structure.
- Pattern 3: strongest comparison for quantification or project depth.

Do not mix patterns until the user's own main narrative is stable.

## Output contract

When recommending changes, return:

- the selected patterns and why they fit;
- the user's verified evidence mapped to target competencies;
- missing evidence or unclear metrics;
- rewritten bullets;
- one change log explaining why each rewrite is stronger;
- a final no-fabrication check.
