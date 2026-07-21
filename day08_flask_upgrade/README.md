# 第8天：Flask项目强化

## 学生信息

- 学号：24012412
- 项目目录：`day08_flask_upgrade/`
- 测试文件：`tests/test_app.py`
- 已完成接口：`/health`、`/api/metrics`、`/api/categories`、`/api/ask`

## 项目说明

本项目在第7天电商数据看板功能基础上增加可测试的 JSON API。指标和品类结果均从 `data/` 下的统计结果读取，接口中没有写死业务数值。

页面路由：

- `/login`：登录页面，使用 `request.form` 读取账号和密码；
- `/dashboard`：数据看板，使用 `request.args` 读取 `category`；
- `/assistant`：项目数据问答页面。

API 路由：

- `/health`：服务健康检查，无需登录；
- `/api/metrics`：登录后返回指标卡数据；
- `/api/categories`：登录后返回全部品类，或通过 `category` 参数筛选；
- `/api/ask`：使用 `request.get_json()` 读取问题并返回问答结果。

`render_template()` 用于生成 HTML 页面，`jsonify()` 用于返回 JSON 数据。

## 安装与运行

在本目录执行：

```bash
python -m pip install -r requirements.txt
python validate_day08_environment.py
python validate_day08_submission.py
python -m pytest -q
python app.py
```

浏览器访问：`http://127.0.0.1:5500`

演示账号：

- 用户名：`student`
- 密码：`day07`

## 接口检查

登录后可访问：

```text
http://127.0.0.1:5500/dashboard?category=Fashion
http://127.0.0.1:5500/api/metrics
http://127.0.0.1:5500/api/categories
http://127.0.0.1:5500/api/categories?category=Fashion
```

健康检查：

```text
http://127.0.0.1:5500/health
```

错误请求会返回非 200 状态码，并采用 `ok` 与 `error` 字段。例如未登录访问业务 API 返回 401，不存在的品类返回 400。

## 提交

从课程仓库根目录执行：

```bash
git status
git add day08_flask_upgrade
git diff --cached
git commit -m "完成第8天Flask项目强化"
git push
```

提交前确认未包含 `.venv/`、`__pycache__/`、`.pytest_cache/`、`.env` 或真实密钥。
