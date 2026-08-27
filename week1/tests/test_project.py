import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from kpi_analysis import calculate_kpis

def test_kpi_calculation():
    df = pd.DataFrame({
        "Days for shipping (real)": [2, 4],
        "Days for shipment (scheduled)": [2, 3],
        "Late_delivery_risk": [0, 1],
    })
    kpis = calculate_kpis(df)
    assert kpis["late_delivery_rate_percent"] == 50
    assert kpis["average_actual_minus_scheduled_days"] == 0.5
