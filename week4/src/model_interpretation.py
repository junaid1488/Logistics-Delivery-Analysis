import pandas as pd
import joblib
from config import MODEL_DIR, OUTPUT_DIR

def main():
    model = joblib.load(MODEL_DIR / "late_delivery_model.joblib")
    pre = model.named_steps["preprocessor"]
    clf = model.named_steps["classifier"]

    names = pre.get_feature_names_out()
    coef = pd.Series(clf.coef_[0], index=names)

    top_positive = coef.sort_values(ascending=False).head(15)
    top_negative = coef.sort_values().head(15)

    positive = pd.DataFrame({
        "feature": top_positive.index,
        "coefficient": top_positive.values,
        "direction": "positive"
    })
    negative = pd.DataFrame({
        "feature": top_negative.index,
        "coefficient": top_negative.values,
        "direction": "negative"
    })

    interpretation = pd.concat([positive, negative], ignore_index=True)
    interpretation.to_csv(
        OUTPUT_DIR / "model_coefficients.csv", index=False
    )
    print(interpretation.to_string(index=False))

if __name__ == "__main__":
    main()
