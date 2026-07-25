"""
data_cleaning.py
-----------------
Cleans the raw sales dataset: handles missing values, removes duplicates,
fixes invalid entries, and engineers useful columns for analysis.
"""

import pandas as pd
import numpy as np


def load_and_clean(path="sales_data_raw.csv"):
    df = pd.read_csv(path, parse_dates=["date"])

    before = len(df)

    # 1. Remove exact duplicate rows
    df = df.drop_duplicates()

    # 2. Fix invalid (negative) units_sold -> treat as data entry error, take absolute value
    df["units_sold"] = df["units_sold"].abs()

    # 3. Handle missing unit_price -> impute using category median price
    df["unit_price"] = df.groupby("category")["unit_price"].transform(
        lambda x: x.fillna(x.median())
    )

    # 4. Recompute revenue after cleaning (source of truth)
    df["revenue"] = (df["unit_price"] * df["units_sold"]).round(2)

    # 5. Feature engineering
    df["month"] = df["date"].dt.month
    df["month_name"] = df["date"].dt.strftime("%b")
    df["quarter"] = df["date"].dt.quarter
    df["weekday"] = df["date"].dt.day_name()
    df["is_weekend"] = df["date"].dt.weekday >= 5

    after = len(df)
    print(f"Cleaned dataset: {before} -> {after} rows "
          f"({before - after} duplicate rows removed)")
    print(f"Missing unit_price values imputed via category median")
    print(f"Negative units_sold corrected: taken as data-entry errors")

    return df


if __name__ == "__main__":
    df = load_and_clean()
    df.to_csv("sales_data_clean.csv", index=False)
    print("\nSaved cleaned dataset -> sales_data_clean.csv")
    print(df.describe(include="all").T)
