from config import OUTPUT_DIR
from load_data import load_data
from prepare_eda import prepare_eda_data

NUMERIC = [
    "Sales", "Order Item Total", "Order Item Quantity",
    "Days for shipping (real)", "Days for shipment (scheduled)",
    "Benefit per order"
]

def main():
    df = prepare_eda_data(load_data())
    OUTPUT_DIR.mkdir(exist_ok=True)

    cols = [c for c in NUMERIC + ["delay_days"] if c in df.columns]
    stats = df[cols].describe().T.round(4)
    stats.to_csv(OUTPUT_DIR / "descriptive_statistics.csv")

    corr_cols = [c for c in cols + ["Late_delivery_risk"] if c in df.columns]
    corr = df[corr_cols].corr().round(4)
    corr.to_csv(OUTPUT_DIR / "correlation_matrix.csv")

    print(stats)
    print("\nCorrelation matrix:")
    print(corr)

if __name__ == "__main__":
    main()
