# 第 7 天学生项目：电商用户留存洞察平台

## 学生信息

- 姓名/项目标识：24012412
- 学号：24012412
- 专题方向：电商用户留存与生命周期分析
- 已完成功能：4 张指标卡、2 张真实图表、品类筛选、5 类离线问答、当前筛选结果导出、生命周期详情页
- 选择的拓展任务：A. 导出当前筛选 CSV；B. 生命周期详情页
- 拓展访问或运行方法：看板点击“导出 CSV”或“查看生命周期”
- 拓展证据文件：`screenshots/05_extension.png`
- 尚未解决的问题：无

## 运行方法

```bash
python -m pip install -r requirements.txt
python app.py
```

浏览器访问 `http://127.0.0.1:5000`。

- 用户名：`24012412`
- 密码：`day07`

## 数据来源

- `data/overall_metrics.csv`：第 5 天总体指标输出
- `data/segment_analysis.csv`：第 5 天生命周期分析输出
- `data/category_analysis.csv`：按用户偏好品类汇总的交互表格数据
- `static/images/`：第 6 天生成的品类对比图与生命周期折线图

## 已实现功能

1. Session 登录、退出与访问拦截；
2. 总用户数、流失人数、总体流失率、平均订单数指标卡；
3. 偏好品类筛选与两张分析图表；
4. 总用户数、流失率、偏好品类、生命周期风险、订单数据五类离线问答；
5. `/download` 导出当前品类筛选对应的 CSV；
6. `/segments` 展示生命周期阶段的用户数、占比、流失人数、流失率与平均订单数。

## 验证方法

在项目根目录运行：

```bash
python validate_day07_environment.py day07_web_student
python validate_day07_submission.py day07_web_student
```
