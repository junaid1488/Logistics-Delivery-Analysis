import pandas as pd
from config import RAW_DATA

def load_raw_data():
    if not RAW_DATA.exists():
        raise FileNotFoundError(f"Dataset not found: {RAW_DATA}")
    return pd.read_csv(RAW_DATA, encoding="latin1")

if __name__ == "__main__":
    df = load_raw_data()
    print(f"Loaded: {df.shape[0]:,} rows x {df.shape[1]} columns")
    print(df.head())
