# 简历雷达自动化评测

## 运行

```bash
python evals/run_eval.py
```

不带参数时执行结构和机制自检；可以传入已生成的报告文件检查是否命中预期高风险点：

```bash
python evals/run_eval.py --report path/to/体检报告.md --target ai_product
```

## 检查内容

- 插件结构完整
- 技能裁剪后无缺失引用
- 评分标准一致
- 模板字段完整
- 模式库索引合法
- 脱敏脚本能删除姓名和联系方式、保留院校信息
- Agent 安全规则完整
- 报告命中样例风险点
