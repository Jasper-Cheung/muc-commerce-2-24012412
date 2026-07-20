from functools import wraps
from pathlib import Path

from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for, Response
import pandas as pd

from services.data_service import load_dashboard_data, load_segment_data
from services.qa_service import answer_question

BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__)
app.config["SECRET_KEY"] = "day07-24012412-demo-key"


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if "username" not in session:
            flash("请先登录后再访问数据看板。", "warning")
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapped_view


@app.route("/")
def index():
    return redirect(url_for("dashboard") if "username" in session else url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        if username == "24012412" and password == "day07":
            session["username"] = username
            flash("登录成功，欢迎进入电商用户分析系统。", "success")
            return redirect(url_for("dashboard"))
        flash("账号或密码错误。演示账号：24012412 / day07", "danger")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("你已安全退出。", "success")
    return redirect(url_for("login"))


@app.route("/dashboard")
@login_required
def dashboard():
    category = request.args.get("category", "全部")
    dashboard_data = load_dashboard_data(BASE_DIR, category)
    return render_template(
        "dashboard.html",
        username=session["username"],
        selected_category=category,
        **dashboard_data,
    )


@app.route("/assistant")
@login_required
def assistant():
    return render_template("assistant.html", username=session["username"])


@app.route("/segments")
@login_required
def segments():
    return render_template(
        "segments.html",
        username=session["username"],
        **load_segment_data(BASE_DIR),
    )


@app.route("/api/ask", methods=["POST"])
@login_required
def ask():
    payload = request.get_json(silent=True) or {}
    question = str(payload.get("question", "")).strip()
    if not question:
        return jsonify({"ok": False, "answer": "请输入一个与项目数据有关的问题。"}), 400
    return jsonify({"ok": True, "answer": answer_question(BASE_DIR, question)})


@app.route("/download")
@login_required
def download_csv():
    """导出当前筛选结果的CSV"""
    category = request.args.get("category", "全部")

    data_dir = BASE_DIR / "data"
    category_df = pd.read_csv(data_dir / "category_analysis.csv", encoding="utf-8-sig")

    if category != "全部":
        category_df = category_df[category_df["PreferedOrderCat"] == category]

    export_df = category_df.rename(columns={
        "PreferedOrderCat": "偏好品类",
        "用户数": "用户数",
        "流失率": "流失率",
        "平均订单数": "平均订单数",
        "平均优惠券数": "平均优惠券数",
        "平均返现": "平均返现",
        "用户占比": "用户占比"
    })

    export_df["流失率"] = export_df["流失率"].map(lambda x: f"{x:.1%}")
    export_df["用户占比"] = export_df["用户占比"].map(lambda x: f"{x:.1%}")

    from io import StringIO
    output = StringIO()
    export_df.to_csv(output, index=False, encoding="utf-8-sig")
    output.seek(0)

    from datetime import datetime

    if category == "全部":
        category_en = "all"
    else:
        category_en = category.replace(" ", "_")

    filename = f"category_analysis_{category_en}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )


@app.errorhandler(404)
def page_not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=False, port=5000)
