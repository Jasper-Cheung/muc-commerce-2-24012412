# 电商用户数据分析实训项目

学号：24012412

本仓库包含 Day03 至 Day07 的个人实训成果，目录结构与课程种子项目保持一致。

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
├── day07_web_student/
│   ├── app.py
│   ├── data/
│   ├── services/
│   ├── static/
│   ├── templates/
│   └── screenshots/
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
├── scripts/
│   ├── validate_seed.py
│   └── validate_submission.py
├── .gitattributes
├── .gitignore
├── README.md
├── requirements.txt
├── validate_day07_environment.py
├── validate_day07_submission.py
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
Day07 Flask Web 展示、交互与离线问答
```

## 第 7 天 Web 项目

进入 `day07_web_student` 后运行：

```bash
python -m pip install -r requirements.txt
python app.py
```

访问 `http://127.0.0.1:5000`，使用账号 `24012412`、密码 `day07` 登录。

