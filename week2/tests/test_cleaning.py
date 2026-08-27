import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from clean_data import clean_dataset

def test_cleaning_rules():
    df = pd.DataFrame({
        "Product Description": [None, None],
        "Order Zipcode": [None, None],
        "Customer Lname": ["A", None],
        "Customer Zipcode": [1000, None],
        "Days for shipping (real)": [2, 4],
        "Days for shipment (scheduled)": [2, 3],
    })
    out = clean_dataset(df)
    assert "Product Description" not in out.columns
    assert "Order Zipcode" not in out.columns
    assert out["Customer Lname"].isna().sum() == 0
    assert out["Customer Zipcode"].isna().sum() == 0
    assert "delivery_delay_days" in out.columns
