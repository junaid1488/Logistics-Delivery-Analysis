from load_data import load_data

TARGET = "Late_delivery_risk"

FEATURES = [
    "Days for shipment (scheduled)",
    "Shipping Mode",
    "Customer Segment",
    "Market",
    "Order Region",
    "Order Item Quantity",
    "Product Price",
    "Sales",
    "Order Item Discount",
    "Order Item Discount Rate",
    "Order Item Profit Ratio",
    "Department Name",
    "Category Id",
    "Department Id",
    "Type",
    "Benefit per order",
    "Customer Country",
    "Customer State",
]

def get_xy():
    df = load_data()
    cols = [c for c in FEATURES if c in df.columns]
    X = df[cols].copy()
    y = df[TARGET].astype(int)
    return X, y
