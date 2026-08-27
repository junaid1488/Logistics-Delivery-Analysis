import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from features import TARGET, FEATURES

def test_feature_definition():
    assert TARGET == "Late_delivery_risk"
    assert "Days for shipment (scheduled)" in FEATURES
    assert "Days for shipping (real)" not in FEATURES
    assert "Delivery Status" not in FEATURES
