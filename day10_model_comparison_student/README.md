# 第10天：三个分类模型的比较与应用

学生：24012412（信计二班）

## 运行方法

```bash
python -m pip install -r requirements.txt
python validate_day10_environment.py
jupyter notebook
```

打开 `notebooks/day10_model_comparison_student.ipynb`，从任务0运行至提交检查。完成后执行：

```bash
python validate_day10_submission.py
```

## 本次成果

- 使用同一分层划分和同一预处理流程训练逻辑回归、决策树、随机森林；
- 与最低参照线共同输出准确率、精确率、流失召回率及TN、FP、FN、TP；
- 选择随机森林作为最终模型，并生成1126名测试用户预测、高风险名单和特征重要性；
- 保存完整流水线，重新加载后预测结果保持一致；
- 概率仅作为风险筛查依据，不代表用户一定会流失。
