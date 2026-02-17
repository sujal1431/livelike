import pandas as pd
import joblib
import json

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


def train_churn_model(filepath):

    # ---------- LOAD DATA ----------
    df = pd.read_csv(filepath)

    # ---------- CLEAN DATA ----------
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df = df.dropna()

    # ---------- SELECT FEATURES ----------
    X = df[["tenure", "MonthlyCharges", "TotalCharges"]]

    # target column (Yes / No → 1 / 0)
    y = df["Churn"].map({"Yes": 1, "No": 0})

    # ---------- SPLIT DATA ----------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # ---------- TRAIN MODEL ----------
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # ---------- EVALUATE ----------
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)
    cm = confusion_matrix(y_test, y_pred)

    print("Model Accuracy:", accuracy)

    # ---------- SAVE MODEL ----------
    joblib.dump(model, "analytics/churn_model.pkl")

    # ---------- SAVE METRICS ----------
    with open("analytics/model_metrics.json", "w") as f:
        json.dump({
            "accuracy": accuracy,
            "classification_report": report
        }, f)

    # ---------- SAVE CONFUSION MATRIX ----------
    with open("analytics/confusion_matrix.json", "w") as f:
        json.dump(cm.tolist(), f)

    return {
        "accuracy": accuracy,
        "confusion_matrix": cm.tolist(),
        "classification_report": report
    }
