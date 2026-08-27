import numpy as np
import matplotlib.pyplot as plt
from config import VIS_DIR
from load_data import load_data
from prepare_eda import prepare_eda_data

def save(fig, filename):
    VIS_DIR.mkdir(exist_ok=True)
    fig.tight_layout()
    fig.savefig(VIS_DIR / filename, dpi=180, bbox_inches="tight")
    plt.close(fig)

def main():
    df = prepare_eda_data(load_data())

    # 1. Late delivery by shipping mode
    mode = df.groupby("Shipping Mode")["is_late"].mean().mul(100).sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8,5))
    mode.plot(kind="bar", ax=ax)
    ax.set_title("Late Delivery Rate by Shipping Mode")
    ax.set_xlabel("Shipping Mode")
    ax.set_ylabel("Late Delivery Rate (%)")
    ax.tick_params(axis="x", rotation=25)
    save(fig, "late_rate_shipping_mode.png")

    # 2. Actual shipping-day distribution
    fig, ax = plt.subplots(figsize=(8,5))
    ax.hist(df["Days for shipping (real)"].dropna(),
            bins=np.arange(-0.5, 7.5, 1), rwidth=.8)
    ax.set_title("Distribution of Actual Shipping Days")
    ax.set_xlabel("Actual Shipping Days")
    ax.set_ylabel("Number of Records")
    save(fig, "shipping_days_distribution.png")

    # 3. Market comparison
    market = df.groupby("Market")["is_late"].mean().mul(100).sort_values()
    fig, ax = plt.subplots(figsize=(8,5))
    market.plot(kind="barh", ax=ax)
    ax.set_title("Late Delivery Rate by Market")
    ax.set_xlabel("Late Delivery Rate (%)")
    ax.set_ylabel("Market")
    save(fig, "late_rate_market.png")

    # 4. Top categories by sales
    category = df.groupby("Category Name")["Sales"].sum().sort_values(ascending=False).head(10).sort_values()
    fig, ax = plt.subplots(figsize=(8,5))
    category.plot(kind="barh", ax=ax)
    ax.set_title("Top 10 Product Categories by Sales")
    ax.set_xlabel("Total Sales")
    ax.set_ylabel("Category")
    save(fig, "top_categories_sales.png")

    # 5. Correlation matrix
    corr_cols = [
        "Sales", "Order Item Total", "Order Item Quantity",
        "Days for shipping (real)", "Days for shipment (scheduled)",
        "Benefit per order", "Late_delivery_risk"
    ]
    corr = df[corr_cols].corr()
    fig, ax = plt.subplots(figsize=(9,7))
    im = ax.imshow(corr, aspect="auto")
    fig.colorbar(im, ax=ax, label="Correlation")
    ax.set_xticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=45, ha="right")
    ax.set_yticks(range(len(corr.index)))
    ax.set_yticklabels(corr.index)
    ax.set_title("Correlation Matrix of Selected Numeric Variables")
    save(fig, "correlation_matrix.png")

if __name__ == "__main__":
    main()
