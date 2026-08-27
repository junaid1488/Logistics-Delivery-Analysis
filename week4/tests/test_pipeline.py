import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from train_model import build_pipeline

def test_pipeline_fits_small_data():
    X = pd.DataFrame({
        "Days for shipment (scheduled)": [2,3,2,4,3,2],
        "Sales": [100,200,150,300,250,175],
        "Shipping Mode": ["A","B","A","C","B","A"]
    })
    y = [0,1,0,1,1,0]
    pipe = build_pipeline(X)
    pipe.fit(X, y)
    assert len(pipe.predict(X)) == len(y)
