# 个人提交检查清单

## 通用检查

- [x] 学号已填写为 24012412
- [x] Day03 至 Day06 四个 Notebook 均存在
- [x] 四个 Notebook 均已从头运行
- [x] Notebook 中没有错误输出
- [x] Notebook 中没有“请填写”、`TODO` 或学号占位内容
- [x] 没有提交教师演示或参考答案
- [x] 没有提交 `.venv`、`.idea`、`.git` 或缓存文件

## Day03

- [x] `category_summary.csv` 存在
- [x] `province_summary.csv` 存在

## Day04

- [x] 六个清洗输出文件齐全
- [x] 清洗后数据为 5630 行、22 列
- [x] CSV 不包含多余索引列

## Day05

- [x] `overall_metrics.csv` 存在
- [x] `segment_analysis.csv` 存在
- [x] `cross_analysis.csv` 存在
- [x] 加分项分析输出已保留

## Day06

- [x] 四张独立图均已生成
- [x] 2×2 综合图已生成
- [x] `chart_manifest.csv` 包含 5 行
- [x] 任期分组使用课程要求的五个有序阶段
- [x] 标题、标签、图例、颜色和百分比格式已优化
- [x] 四个业务问题和图表选择理由已填写
- [x] 观察、证据、边界和综合结论已填写
- [x] `python scripts/validate_submission.py` 检查通过

## Day08

- [x] `day08_flask_upgrade/` 目录已补充
- [x] 第7天登录、看板和问答页面可继续运行
- [x] `/health`、`/api/metrics`、`/api/categories` 可返回 JSON
- [x] `category=Fashion` 会进入实际筛选逻辑
- [x] 未登录业务 API 返回 401，错误请求返回 400 或 404
- [x] API 数据已转换为普通字典、列表、字符串和数字
- [x] `tests/test_app.py` 包含 7 条可重复运行的断言测试
- [x] README 已填写学号、接口和测试说明


## Day09

- [x] CustomerID和Churn均未进入特征矩阵
- [x] 固定随机种子42并使用 `stratify=y`
- [x] 预处理器只在训练集上拟合
- [x] 训练、测试矩阵均为36列有限数值
- [x] 已解释高准确率与零流失召回率的矛盾
- [x] 第9天4项CSV成果齐全，验证通过

## Day10

- [x] 三个模型使用同一划分和预处理流程
- [x] 四组混淆矩阵的TN、FP、FN、TP均合计1126
- [x] 模型选择同时比较准确率、召回率、FN和FP
- [x] 预测文件、高风险名单和特征重要性齐全
- [x] 流失概率仅作为风险筛查依据
- [x] 模型保存后可以重新加载，验证通过
