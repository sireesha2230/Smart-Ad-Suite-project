# optimizer.py

def optimize_budget(total_budget, metrics_df):
    """
    Distributes ad budget based on ROI = (CTR * ConversionRate) / CPC
    """
    metrics_df["ROI"] = (metrics_df["CTR"] * metrics_df["ConversionRate"]) / metrics_df["CPC"]
    total_roi = metrics_df["ROI"].sum()
    metrics_df["AllocatedBudget"] = (metrics_df["ROI"] / total_roi) * total_budget
    return metrics_df[["Platform", "AllocatedBudget"]]
