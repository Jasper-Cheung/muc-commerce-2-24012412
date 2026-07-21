# 电商用户数据分析实训项目

学号：24012412

本仓库包含 Day03 至 Day06 的数据分析成果，以及在原有看板基础上完成的 Day08 Flask 项目强化。

## 项目结构

```text
.
├── data/
│   ├── E Commerce Dataset.xlsx
│   ├── README.md
│   └── 淘宝全品类全国数据.csv
├── docs/
│   ├── day03_task.md
│   ├── day04_task.md
│   └── day05_student_manual.md
├── notebooks/
│   ├── day03_pandas_product_analysis.ipynb
│   ├── day04_pm_user_cleaning_project.ipynb
│   ├── day05_pm_student_project.ipynb
│   └── day06_pm_student_visualization.ipynb
├── output/
│   ├── day03_analysis/
│   ├── day04_project/
│   ├── day05_analysis/
│   └── day06_visualization/
├── day08_flask_upgrade/
│   ├── app.py
│   ├── services/
│   ├── templates/
│   ├── static/
│   ├── tests/
│   ├── validate_day08_environment.py
│   └── validate_day08_submission.py
├── scripts/
│   ├── validate_seed.py
│   └── validate_submission.py
├── .gitattributes
├── .gitignore
├── README.md
├── requirements.txt
└── SUBMISSION_CHECKLIST.md
```

## 学习路径

```text
Day03 Pandas 商品数据探索
        ↓
Day04 电商用户数据清洗与预处理
        ↓
Day05 电商用户多维分析
        ↓
Day06 数据可视化与综合表达
        ↓
Day08 Flask 请求流程、JSON API 与自动测试
```



## Day08 Flask 项目强化

`day08_flask_upgrade/` 保留了登录、数据看板和离线问答页面，并新增 `/health`、`/api/metrics` 和 `/api/categories`。业务 API 使用登录鉴权，错误请求返回明确的非 200 状态码。

运行与检查：

```bash
cd day08_flask_upgrade
python -m pip install -r requirements.txt
python validate_day08_environment.py
python validate_day08_submission.py
python -m pytest -q
python app.py
```
