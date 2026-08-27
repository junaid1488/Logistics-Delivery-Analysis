import pandas as pd
from config import DATA_PATH

def load_dataset():
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at {DATA_PATH}. "
            "Place DataCoSupplyChainDataset.csv in data/raw/."
        )
    return pd.read_csv(DATA_PATH, encoding="latin1")

if __name__ == "__main__":
    df = load_dataset()
    print(f"Loaded dataset: {df.shape[0]:,} rows x {df.shape[1]} columns")
