from pathlib import Path

import pandas as pd


def _read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, encoding="utf-8-sig")


def _load_source_tables(base_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    data_dir = base_dir / "data"
    metrics_df = _read_csv(data_dir / "overall_metrics.csv")
    category_df = _read_csv(data_dir / "category_analysis.csv")
    segment_df = _read_csv(data_dir / "segment_analysis.csv")
    return metrics_df, category_df, segment_df


def get_available_categories(base_dir: Path) -> list[str]:
    _, category_df, _ = _load_source_tables(base_dir)
    return ["全部", *category_df["PreferedOrderCat"].astype(str).tolist()]


def _build_metrics(metrics_df: pd.DataFrame) -> list[dict]:
    metric_map = dict(zip(metrics_df["指标"], metrics_df["数值"]))
    return [
        {"label": "总用户数", "value": f"{int(metric_map['用户数']):,}", "note": "人"},
        {"label": "流失用户", "value": f"{int(metric_map['流失人数']):,}", "note": "人"},
        {"label": "总体流失率", "value": f"{float(metric_map['流失率']):.1%}", "note": "用户占比"},
        {"label": "平均订单数", "value": f"{float(metric_map['平均订单数']):.2f}", "note": "单/人"},
    ]


def _build_category_rows(category_df: pd.DataFrame, selected_category: str) -> list[dict]:
    table_df = category_df.copy()
    if selected_category != "全部":
        table_df = table_df.loc[table_df["PreferedOrderCat"] == selected_category]

    rows = []
    for record in table_df.to_dict("records"):
        rows.append(
            {
                "偏好品类": str(record["PreferedOrderCat"]),
                "用户数": int(record["用户数"]),
                "流失率": f"{float(record['流失率']):.1%}",
                "平均订单数": f"{float(record['平均订单数']):.2f}",
            }
        )
    return rows


def load_dashboard_data(base_dir: Path, selected_category: str = "全部") -> dict:
    metrics_df, category_df, segment_df = _load_source_tables(base_dir)
    highest_risk = segment_df.loc[segment_df["流失率"].idxmax()]
    insight = (
        f"{highest_risk['TenureGroup']}的流失率最高，为{float(highest_risk['流失率']):.1%}。"
        "该结果用于描述当前样本，不直接代表因果关系。"
    )
    return {
        "metrics": _build_metrics(metrics_df),
        "categories": ["全部", *category_df["PreferedOrderCat"].astype(str).tolist()],
        "category_rows": _build_category_rows(category_df, selected_category),
        "insight": insight,
    }


def load_metric_api_data(base_dir: Path) -> list[dict]:
    metrics_df, _, _ = _load_source_tables(base_dir)
    return _build_metrics(metrics_df)


def load_category_api_data(base_dir: Path, selected_category: str = "全部") -> list[dict]:
    _, category_df, _ = _load_source_tables(base_dir)
    return _build_category_rows(category_df, selected_category)
