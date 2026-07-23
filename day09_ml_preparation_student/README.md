# 第9天：机器学习数据准备

## 学生信息

- 姓名/标识：24012412
- 学号：24012412
- 班级：信计二班

## 运行方法

```bash
python -m pip install -r requirements.txt
python validate_day09_environment.py
jupyter lab
```

打开 `notebooks/day09_ml_preparation_student.ipynb`，按顺序运行全部单元格，最后执行：

```bash
python validate_day09_submission.py
```

## 关键理解

- **样本、特征与标签：** 一行是一名用户，也就是一个样本；Tenure、Complain等字段是模型判断的线索；Churn是需要预测的标签。
- **分类：** 本任务把用户分为“流失”和“不流失”两类，预测结果为0或1。
- **训练集与测试集：** 训练集用于学习预处理规则和分类规律，测试集模拟未见过的新用户，只用于最后评价。
- **建模口径：** CustomerID只负责识别用户，Churn是答案，因此二者都不能进入特征矩阵。
- **高准确率的陷阱：** 最低参照线全部预测为不流失，准确率仍约83%，但流失召回率为0，说明它没有找到任何真实流失用户。
