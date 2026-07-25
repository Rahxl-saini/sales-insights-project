"""
eda_visualizations.py
----------------------
Exploratory Data Analysis on the cleaned sales dataset.
Generates key business charts saved to the /charts folder.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style("whitegrid")
os.makedirs("charts", exist_ok=True)

df = pd.read_csv("sales_data_clean.csv", parse_dates=["date"])


def revenue_by_category():
    data = df.groupby("category")["revenue"].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    sns.barplot(x=data.values, y=data.index, hue=data.index, palette="Blues_d", legend=False)
    plt.title("Total Revenue by Product Category (2025)")
    plt.xlabel("Revenue ($)")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.savefig("charts/revenue_by_category.png", dpi=120)
    plt.close()


def monthly_revenue_trend():
    monthly = df.groupby(df["date"].dt.to_period("M"))["revenue"].sum()
    plt.figure(figsize=(10, 5))
    monthly.plot(kind="line", marker="o", color="#1F3864")
    plt.title("Monthly Revenue Trend (2025)")
    plt.xlabel("Month")
    plt.ylabel("Revenue ($)")
    plt.tight_layout()
    plt.savefig("charts/monthly_revenue_trend.png", dpi=120)
    plt.close()


def revenue_by_region_channel():
    pivot = df.pivot_table(index="region", columns="channel", values="revenue", aggfunc="sum")
    pivot.plot(kind="bar", figsize=(8, 5), color=["#1F3864", "#8FAADC"])
    plt.title("Revenue by Region and Sales Channel")
    plt.xlabel("Region")
    plt.ylabel("Revenue ($)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("charts/revenue_by_region_channel.png", dpi=120)
    plt.close()


def weekend_vs_weekday():
    data = df.groupby("is_weekend")["revenue"].mean()
    data.index = ["Weekday", "Weekend"]
    plt.figure(figsize=(6, 5))
    sns.barplot(x=data.index, y=data.values, hue=data.index, palette="Blues_d", legend=False)
    plt.title("Average Order Revenue: Weekday vs Weekend")
    plt.ylabel("Average Revenue ($)")
    plt.tight_layout()
    plt.savefig("charts/weekend_vs_weekday.png", dpi=120)
    plt.close()


def generate_summary_stats():
    summary = {
        "total_revenue": round(df["revenue"].sum(), 2),
        "total_orders": len(df),
        "avg_order_value": round(df["revenue"].mean(), 2),
        "top_category": df.groupby("category")["revenue"].sum().idxmax(),
        "top_region": df.groupby("region")["revenue"].sum().idxmax(),
        "best_month": df.groupby(df["date"].dt.strftime("%b"))["revenue"].sum().idxmax(),
        "online_share_pct": round(
            df[df["channel"] == "Online"]["revenue"].sum() / df["revenue"].sum() * 100, 1
        ),
    }
    return summary


if __name__ == "__main__":
    revenue_by_category()
    monthly_revenue_trend()
    revenue_by_region_channel()
    weekend_vs_weekday()

    stats = generate_summary_stats()
    print("Charts saved to /charts")
    print("\nKey Summary Stats:")
    for k, v in stats.items():
        print(f"  {k}: {v}")

    pd.Series(stats).to_json("summary_stats.json")
    print("\nSaved summary_stats.json")
