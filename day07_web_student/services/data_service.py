from pathlib import Path

import pandas as pd


def _read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, encoding="utf-8-sig")


def _metric(metric_map: dict, *labels: str) -> float:
    """兼容 Day05 输出中的中文指标命名。"""
    for label in labels:
        if label in metric_map:
            return float(metric_map[label])
    raise KeyError(f"未找到指标：{' / '.join(labels)}")


def load_dashboard_data(base_dir: Path, selected_category: str = "全部") -> dict:
    data_dir = base_dir / "data"
    metrics_df = _read_csv(data_dir / "overall_metrics.csv")
    category_df = _read_csv(data_dir / "category_analysis.csv")
    segment_df = _read_csv(data_dir / "segment_analysis.csv")

    metric_map = dict(zip(metrics_df["指标"], metrics_df["数值"]))

    # 4张指标卡：总用户数、流失用户、总体流失率、平均订单数
    metrics = [
        {"label": "总用户数", "value": f"{int(_metric(metric_map, '总用户数', '用户数')):,}", "note": "有效用户样本"},
        {"label": "流失用户", "value": f"{int(_metric(metric_map, '流失人数')):,}", "note": "已流失用户"},
        {"label": "总体流失率", "value": f"{_metric(metric_map, '总体流失率', '流失率'):.1%}", "note": "流失人数 / 总用户数"},
        {"label": "平均订单数", "value": f"{_metric(metric_map, '平均订单数'):.2f}", "note": "每位用户平均订单"},
    ]

    categories = ["全部", *category_df["PreferedOrderCat"].tolist()]
    table_df = category_df.copy()

    # 品类筛选
    if selected_category != "全部":
        table_df = table_df[table_df["PreferedOrderCat"] == selected_category]

    table_df = table_df.rename(
        columns={
            "PreferedOrderCat": "偏好品类",
            "用户数": "用户数",
            "流失率": "流失率",
            "平均订单数": "平均订单数",
        }
    )[["偏好品类", "用户数", "流失率", "平均订单数"]]
    table_df["流失率"] = table_df["流失率"].map(lambda value: f"{value:.1%}")
    table_df["平均订单数"] = table_df["平均订单数"].map(lambda value: f"{value:.2f}")

    # 数据观察：找出流失率最高的生命周期阶段
    max_churn_idx = segment_df['流失率'].idxmax()
    max_churn_stage = segment_df.loc[max_churn_idx, 'TenureGroup']
    max_churn_rate = segment_df.loc[max_churn_idx, '流失率']

    min_churn_idx = segment_df['流失率'].idxmin()
    min_churn_stage = segment_df.loc[min_churn_idx, 'TenureGroup']
    min_churn_rate = segment_df.loc[min_churn_idx, '流失率']
    insight = f"生命周期阶段中，“{max_churn_stage}”流失率最高（{max_churn_rate:.1%}），“{min_churn_stage}”最低（{min_churn_rate:.1%}）。建议优先为“{max_churn_stage}”用户设计首购后的留存触达。"

    return {
        "metrics": metrics,
        "categories": categories,
        "category_rows": table_df.to_dict("records"),
        "insight": insight,
    }


def load_segment_data(base_dir: Path) -> dict:
    """准备生命周期详情页所需的表格和摘要。"""
    segment_df = _read_csv(base_dir / "data" / "segment_analysis.csv").copy()
    segment_df["用户占比"] = segment_df["用户占比"].map(lambda value: f"{value:.1%}")
    segment_df["流失率"] = segment_df["流失率"].map(lambda value: f"{value:.1%}")
    segment_df["平均订单数"] = segment_df["平均订单数"].map(lambda value: f"{value:.2f}")

    raw_df = _read_csv(base_dir / "data" / "segment_analysis.csv")
    highest = raw_df.loc[raw_df["流失率"].idxmax()]
    lowest = raw_df.loc[raw_df["流失率"].idxmin()]
    summary = (
        f"“{highest['TenureGroup']}”流失率最高，为 {highest['流失率']:.1%}；"
        f"“{lowest['TenureGroup']}”最低，为 {lowest['流失率']:.1%}。"
        "阶段差异明显，留存资源应向高风险的新近用户倾斜。"
    )
    return {"segment_rows": segment_df.to_dict("records"), "segment_summary": summary}
