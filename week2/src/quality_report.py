import pandas as pd
from config import OUTPUT_DIR
from load_data import load_raw_data

def create_quality_report(df):
    report = pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "missing_count": df.isna().sum(),
        "missing_percent": (df.isna().mean() * 100).round(4),
        "unique_count": df.nunique(dropna=False),
    })
    return report.sort_values(
        ["missing_percent", "unique_count"],
        ascending=[False, False]
    )

def main():
    df = load_raw_data()
    OUTPUT_DIR.mkdir(exist_ok=True)
    report = create_quality_report(df)
    report.to_csv(OUTPUT_DIR / "data_quality_report.csv")
    print(report.head(20).to_string())
    print(f"\nExact duplicate rows: {df.duplicated().sum():,}")

if __name__ == "__main__":
    main()
