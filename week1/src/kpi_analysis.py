import pandas as pd
from data_loader import load_dataset
from config import OUTPUT_DIR

REQUIRED = [
    "Days for shipping (real)",
    "Days for shipment (scheduled)",
    "Late_delivery_risk",
]

def calculate_kpis(df):
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Required KPI columns are missing: {missing}")

    result = {
        "records": len(df),
        "late_delivery_rate_percent": df["Late_delivery_risk"].mean() * 100,
        "average_actual_shipping_days": df["Days for shipping (real)"].mean(),
        "average_scheduled_shipping_days": df["Days for shipment (scheduled)"].mean(),
        "average_actual_minus_scheduled_days": (
            df["Days for shipping (real)"] -
            df["Days for shipment (scheduled)"]
        ).mean(),
    }
    return pd.Series(result)

def main():
    df = load_dataset()
    kpis = calculate_kpis(df).round(4)
    OUTPUT_DIR.mkdir(exist_ok=True)
    kpis.to_csv(OUTPUT_DIR / "week1_kpis.csv", header=["value"])
    print(kpis.to_string())

if __name__ == "__main__":
    main()
