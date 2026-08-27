import pandas as pd
from load_data import load_data

def prepare_eda_data(df):
    df = df.copy()
    df["order_date"] = pd.to_datetime(
        df["order date (DateOrders)"], errors="coerce"
    )
    df["delay_days"] = (
        df["Days for shipping (real)"]
        - df["Days for shipment (scheduled)"]
    )
    df["is_late"] = df["Late_delivery_risk"].astype(int)
    return df
