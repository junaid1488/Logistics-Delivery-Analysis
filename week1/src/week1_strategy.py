from pathlib import Path
from data_loader import load_dataset
from profile_dataset import build_profile
from kpi_analysis import calculate_kpis
from config import OUTPUT_DIR

def main():
    df = load_dataset()
    OUTPUT_DIR.mkdir(exist_ok=True)

    profile = build_profile(df)
    profile.to_csv(OUTPUT_DIR / "data_profile.csv")

    kpis = calculate_kpis(df).round(4)
    kpis.to_csv(OUTPUT_DIR / "week1_kpis.csv", header=["value"])

    summary = [
        "# Week 1 Strategic Analysis Output",
        "",
        f"- Dataset rows: {len(df):,}",
        f"- Dataset columns: {df.shape[1]:,}",
        f"- Exact duplicate rows: {df.duplicated().sum():,}",
        f"- Late delivery rate: {kpis['late_delivery_rate_percent']:.2f}%",
        f"- Average actual shipping days: {kpis['average_actual_shipping_days']:.2f}",
        f"- Average scheduled shipping days: {kpis['average_scheduled_shipping_days']:.2f}",
        f"- Average actual-minus-scheduled days: {kpis['average_actual_minus_scheduled_days']:.2f}",
        "",
        "## Strategic roadmap",
        "1. Validate the source data.",
        "2. Clean missing, duplicate, inconsistent, and unusual values.",
        "3. Perform exploratory analysis and KPI segmentation.",
        "4. Engineer prediction-time features without future information leakage.",
        "5. Evaluate classification models for late-delivery risk.",
        "6. Translate model findings into logistics optimization actions.",
    ]
    (OUTPUT_DIR / "week1_strategy_output.md").write_text("\n".join(summary))
    print("\n".join(summary))

if __name__ == "__main__":
    main()
