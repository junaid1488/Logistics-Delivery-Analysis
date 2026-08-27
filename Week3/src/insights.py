from config import OUTPUT_DIR
from load_data import load_data
from prepare_eda import prepare_eda_data

def main():
    df = prepare_eda_data(load_data())
    late = df["is_late"].mean() * 100
    actual = df["Days for shipping (real)"].mean()
    scheduled = df["Days for shipment (scheduled)"].mean()
    delay = df["delay_days"].mean()

    mode = df.groupby("Shipping Mode")["is_late"].mean().mul(100).sort_values(ascending=False)
    market = df.groupby("Market")["is_late"].mean().mul(100).sort_values(ascending=False)

    lines = [
        "# Week 3 EDA Insights",
        "",
        f"- Overall late-delivery risk rate: {late:.2f}%.",
        f"- Average actual shipping duration: {actual:.2f} days.",
        f"- Average scheduled shipping duration: {scheduled:.2f} days.",
        f"- Average actual-minus-scheduled difference: {delay:.2f} days.",
        f"- Highest late-rate shipping mode: {mode.index[0]} ({mode.iloc[0]:.2f}%).",
        f"- Highest late-rate market: {market.index[0]} ({market.iloc[0]:.2f}%).",
        "",
        "These are descriptive associations. They do not establish causation."
    ]
    (OUTPUT_DIR / "eda_insights.md").write_text("\n".join(lines))
    print("\n".join(lines))

if __name__ == "__main__":
    main()
