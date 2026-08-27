import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from prepare_eda import prepare_eda_data

def test_derived_eda_fields():
    df = pd.DataFrame({
        "order date (DateOrders)": ["2018-01-01"],
        "Days for shipping (real)": [4],
        "Days for shipment (scheduled)": [3],
        "Late_delivery_risk": [1],
    })
    out = prepare_eda_data(df)
    assert out.loc[0, "delay_days"] == 1
    assert out.loc[0, "is_late"] == 1
    assert pd.notna(out.loc[0, "order_date"])
