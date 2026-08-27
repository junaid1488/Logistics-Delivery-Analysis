import pandas as pd
import joblib
from config import MODEL_DIR, OUTPUT_DIR
from features import get_xy

def main():
    X, _ = get_xy()
    model = joblib.load(MODEL_DIR / "late_delivery_model.joblib")

    risk = model.predict_proba(X)[:, 1]

    queue = X.copy()
    queue["predicted_late_probability"] = risk
    queue = queue.sort_values(
        "predicted_late_probability",
        ascending=False
    )

    # Example operational intervention tiers
    queue["priority"] = pd.cut(
        queue["predicted_late_probability"],
        bins=[-0.01, 0.50, 0.75, 1.00],
        labels=["Standard", "High", "Critical"]
    )

    OUTPUT_DIR.mkdir(exist_ok=True)
    queue.head(1000).to_csv(
        OUTPUT_DIR / "high_risk_intervention_queue.csv",
        index=False
    )

    summary = queue["priority"].value_counts().rename_axis("priority").reset_index(name="orders")
    summary.to_csv(
        OUTPUT_DIR / "intervention_priority_summary.csv",
        index=False
    )

    print(summary.to_string(index=False))
    print("\nTop 10 high-risk records:")
    print(queue.head(10).to_string(index=False))

if __name__ == "__main__":
    main()
