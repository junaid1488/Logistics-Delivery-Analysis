import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from config import OUTPUT_DIR, VIS_DIR, MODEL_DIR
from features import get_xy

def main():
    X, y = get_xy()
    _, X_test, _, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    model = joblib.load(MODEL_DIR / "late_delivery_model.joblib")
    pred = model.predict(X_test)

    cm = confusion_matrix(y_test, pred)

    VIS_DIR.mkdir(exist_ok=True)
    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["On-time", "Late"]
    )
    disp.plot()
    plt.title("Late Delivery Risk — Confusion Matrix")
    plt.tight_layout()
    plt.savefig(
        VIS_DIR / "confusion_matrix.png",
        dpi=180,
        bbox_inches="tight"
    )
    plt.close()

    print("Confusion matrix saved.")
    print(cm)

if __name__ == "__main__":
    main()
