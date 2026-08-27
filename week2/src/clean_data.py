import pandas as pd
import numpy as np
from config import OUTPUT_DIR, CLEAN_DATA
from load_data import load_raw_data

def iqr_bounds(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr

def clean_dataset(df):
    df = df.copy()

    # Remove columns with no information / excessive missingness
    remove_cols = [
        c for c in ["Product Description", "Order Zipcode"]
        if c in df.columns
    ]
    df = df.drop(columns=remove_cols)

    # Small missing-value groups
    if "Customer Lname" in df.columns:
        df["Customer Lname"] = df["Customer Lname"].fillna("Unknown")

    if "Customer Zipcode" in df.columns:
        df["Customer Zipcode"] = df["Customer Zipcode"].fillna(
            df["Customer Zipcode"].median()
        )

    # Convert date columns
    date_cols = ["order date (DateOrders)", "shipping date (DateOrders)"]
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # Add a useful retrospective delay feature
    if {
        "Days for shipping (real)",
        "Days for shipment (scheduled)"
    }.issubset(df.columns):
        df["delivery_delay_days"] = (
            df["Days for shipping (real)"]
            - df["Days for shipment (scheduled)"]
        )

    # Remove exact duplicate rows if any exist
    df = df.drop_duplicates().reset_index(drop=True)

    return df

def create_outlier_report(df):
    numeric_cols = df.select_dtypes(include=np.number).columns
    rows = []
    for col in numeric_cols:
        s = df[col].dropna()
        if s.empty:
            continue
        lower, upper = iqr_bounds(s)
        count = int(((s < lower) | (s > upper)).sum())
        rows.append({
            "column": col,
            "lower_bound": lower,
            "upper_bound": upper,
            "iqr_outlier_count": count,
            "outlier_percent": count / len(s) * 100
        })
    return pd.DataFrame(rows).sort_values(
        "iqr_outlier_count", ascending=False
    )

def main():
    df = load_raw_data()
    before_shape = df.shape
    before_duplicates = int(df.duplicated().sum())

    cleaned = clean_dataset(df)

    OUTPUT_DIR.mkdir(exist_ok=True)
    cleaned.to_csv(CLEAN_DATA, index=False)

    outliers = create_outlier_report(df)
    outliers.to_csv(OUTPUT_DIR / "iqr_outlier_report.csv", index=False)

    missing_after = pd.DataFrame({
        "missing_count": cleaned.isna().sum(),
        "missing_percent": (cleaned.isna().mean() * 100).round(4)
    }).sort_values("missing_count", ascending=False)
    missing_after.to_csv(OUTPUT_DIR / "missing_values_after_cleaning.csv")

    print("Before:", before_shape)
    print("After:", cleaned.shape)
    print("Exact duplicates before:", before_duplicates)
    print("Exact duplicates after:", cleaned.duplicated().sum())
    print(f"Saved cleaned data to: {CLEAN_DATA}")

if __name__ == "__main__":
    main()
