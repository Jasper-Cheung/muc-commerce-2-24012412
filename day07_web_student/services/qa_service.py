from pathlib import Path

import pandas as pd


def _metric(metrics: dict, *labels: str) -> float:
    for label in labels:
        if label in metrics:
            return float(metrics[label])
    raise KeyError(f"未找到指标：{' / '.join(labels)}")


def answer_question(base_dir: Path, question: str) -> str:
    data_dir = base_dir / "data"
    metrics_df = pd.read_csv(data_dir / "overall_metrics.csv", encoding="utf-8-sig")
    category_df = pd.read_csv(data_dir / "category_analysis.csv", encoding="utf-8-sig")
    segment_df = pd.read_csv(data_dir / "segment_analysis.csv", encoding="utf-8-sig")

    metrics = dict(zip(metrics_df["指标"], metrics_df["数值"]))
    normalized = question.replace(" ", "").lower()

    # 问题1: 总用户数
    if any(word in normalized for word in ["多少用户", "用户数", "总用户"]):
        total_users = int(_metric(metrics, "总用户数", "用户数"))
        return f"当前分析样本共包含 {total_users:,} 名用户。"

    # 问题2: 流失率
    if any(word in normalized for word in ["流失率", "流失比例", "留存率"]):
        churn_rate = _metric(metrics, "总体流失率", "流失率")
        churn_count = int(_metric(metrics, "流失人数"))
        total_users = int(_metric(metrics, "总用户数", "用户数"))
        return f"总体流失率是 {churn_rate:.1%}：{total_users:,} 名用户中有 {churn_count:,} 名流失。"

    # 问题3: 偏好品类
    if any(word in normalized for word in ["偏好品类", "哪个品类", "最多用户", "热门品类"]):
        sorted_categories = category_df.sort_values('用户数', ascending=False)
        top_category = sorted_categories.iloc[0]['PreferedOrderCat']
        top_count = int(sorted_categories.iloc[0]['用户数'])
        top_rate = sorted_categories.iloc[0]['流失率']

        bottom_category = sorted_categories.iloc[-1]['PreferedOrderCat']
        bottom_count = int(sorted_categories.iloc[-1]['用户数'])

        return f"“{top_category}”用户最多，共 {top_count:,} 人，流失率为 {top_rate:.1%}；“{bottom_category}”用户最少，共 {bottom_count:,} 人。"

    # 问题4: 生命周期风险
    if any(word in normalized for word in ["生命周期", "哪个阶段", "风险", "最危险", "最高"]):
        max_churn_idx = segment_df['流失率'].idxmax()
        max_stage = segment_df.loc[max_churn_idx, 'TenureGroup']
        max_rate = segment_df.loc[max_churn_idx, '流失率']
        max_users = int(segment_df.loc[max_churn_idx, '用户数'])
        max_churned = int(segment_df.loc[max_churn_idx, '流失人数'])

        min_idx = segment_df['流失率'].idxmin()
        min_stage = segment_df.loc[min_idx, 'TenureGroup']
        min_rate = segment_df.loc[min_idx, '流失率']
        return f"风险最高的是“{max_stage}”：{max_users:,} 名用户中流失 {max_churned:,} 人，流失率 {max_rate:.1%}。风险最低的是“{min_stage}”，流失率 {min_rate:.1%}。"

    # 问题5: 订单相关
    if any(word in normalized for word in ["订单", "平均订单", "订单数", "购买频次", "下单"]):
        avg_orders = _metric(metrics, "平均订单数")
        median_orders = _metric(metrics, "订单数中位数")
        total_orders = round(_metric(metrics, "总用户数", "用户数") * avg_orders)
        return f"每位用户平均下单 {avg_orders:.2f} 笔，中位数为 {median_orders:.1f} 笔；按均值估算，样本订单总量约 {total_orders:,} 笔。"

    # 默认回复
    return (
        "暂时没有匹配到这个问题。你可以询问：总用户数、总体流失率、热门偏好品类、"
        "生命周期风险，或平均订单数。"
    )
