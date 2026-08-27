import pandas as pd
from data_loader import load_dataset
from config import OUTPUT_DIR

def build_profile(df):
    profile = pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "missing_count": df.isna().sum(),
        "missing_percent": (df.isna().mean() * 100).round(2),
        "unique_count": df.nunique(dropna=False),
    })
    return profile.sort_values(["missing_percent", "unique_count"], ascending=[False, False])

def main():
    df = load_dataset()
    OUTPUT_DIR.mkdir(exist_ok=True)
    profile = build_profile(df)
    profile.to_csv(OUTPUT_DIR / "data_profile.csv")
    print("Shape:", df.shape)
    print("\nTop missing-value fields:")
    print(profile.head(15).to_string())

    duplicates = int(df.duplicated().sum())
    print(f"\nExact duplicate rows: {duplicates:,}")

if __name__ == "__main__":
    main()
