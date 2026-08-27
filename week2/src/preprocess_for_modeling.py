import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from config import CLEAN_DATA, OUTPUT_DIR

TARGET = "Late_delivery_risk"

def build_preprocessor(X):
    numeric = X.select_dtypes(include="number").columns.tolist()
    categorical = X.select_dtypes(exclude="number").columns.tolist()

    return ColumnTransformer([
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

def main():
    df = pd.read_csv(CLEAN_DATA)

    # Pre-outcome features only: exclude realized delivery outcomes.
    excluded = [
        TARGET,
        "Days for shipping (real)",
        "Delivery Status",
        "Order Id",
        "Order Customer Id"
    ]
    excluded = [c for c in excluded if c in df.columns]

    X = df.drop(columns=excluded)
    y = df[TARGET].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    preprocessor = build_preprocessor(X_train)

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", LogisticRegression(
            max_iter=500,
            solver="liblinear",
            class_weight="balanced"
        ))
    ])

    # Fitting verifies that the cleaned data is model-ready.
    pipeline.fit(X_train, y_train)

    print("Preprocessing/model pipeline fitted successfully.")
    print("Training rows:", len(X_train))
    print("Testing rows:", len(X_test))
    print("Encoded feature count:",
          len(pipeline.named_steps["preprocessor"].get_feature_names_out()))

if __name__ == "__main__":
    main()
