from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DATA = ROOT / "data" / "raw" / "DataCoSupplyChainDataset.csv"
OUTPUT_DIR = ROOT / "outputs"
CLEAN_DATA = OUTPUT_DIR / "DataCoSupplyChain_Cleaned.csv"
