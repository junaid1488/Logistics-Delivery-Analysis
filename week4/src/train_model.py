import json
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, confusion_matrix
)

from config import OUTPUT_DIR, MODEL_DIR
from features import get_xy

def build_pipeline(X):
    numeric = X.select_dtypes(include="number").columns.tolist()
    categorical = X.select_dtypes(exclude="number").columns.tolist()

    preprocessor = ColumnTransformer([
        ("num", Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]), numeric),
        ("cat", Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(
                handle_unknown="ignore",
                min_frequency=20
            ))
        ]), categorical)
    ])

    return Pipeline([
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(
            max_iter=500,
            solver="liblinear",
            class_weight="balanced"
        ))
    ])

def main():
    X, y = get_xy()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    pipeline = build_pipeline(X_train)
    pipeline.fit(X_train, y_train)

    pred = pipeline.predict(X_test)
    prob = pipeline.predict_proba(X_test)[:, 1]

    metrics = {
        "accuracy": accuracy_score(y_test, pred),
        "precision": precision_score(y_test, pred),
        "recall": recall_score(y_test, pred),
        "f1": f1_score(y_test, pred),
        "roc_auc": roc_auc_score(y_test, prob),
        "train_rows": len(X_train),
        "test_rows": len(X_test),
    }

    OUTPUT_DIR.mkdir(exist_ok=True)
    MODEL_DIR.mkdir(exist_ok=True)

    pd.DataFrame([metrics]).to_csv(
        OUTPUT_DIR / "model_metrics.csv", index=False
    )

    cm = confusion_matrix(y_test, pred)
    pd.DataFrame(
        cm,
        index=["actual_on_time", "actual_late"],
        columns=["predicted_on_time", "predicted_late"]
    ).to_csv(OUTPUT_DIR / "confusion_matrix.csv")

    joblib.dump(pipeline, MODEL_DIR / "late_delivery_model.joblib")

    with open(OUTPUT_DIR / "model_metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print("Model trained successfully.")
    for k, v in metrics.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
