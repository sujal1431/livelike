import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

MODEL_PATH = Path("analytics/churn_model.pkl")
METRICS_PATH = Path("analytics/model_metrics.json")
CONFUSION_MATRIX_PATH = Path("analytics/confusion_matrix.json")


def _prepare_training_data(filepath):
    """Load and clean data for churn model training."""
    df = pd.read_csv(filepath)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df = df.dropna(subset=["tenure", "MonthlyCharges", "TotalCharges", "Churn"])
    features = df[["tenure", "MonthlyCharges", "TotalCharges"]]
    target = df["Churn"].map({"Yes": 1, "No": 0})
    return features, target


def train_churn_model(filepath):
    """Train churn model and persist model, metrics, and confusion matrix."""
    features, target = _prepare_training_data(filepath)
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions, output_dict=True)
    matrix = confusion_matrix(y_test, predictions).tolist()

    joblib.dump(model, MODEL_PATH)
    METRICS_PATH.write_text(
        json.dumps({"accuracy": accuracy, "classification_report": report}),
        encoding="utf-8",
    )
    CONFUSION_MATRIX_PATH.write_text(json.dumps(matrix), encoding="utf-8")

    return {"accuracy": accuracy, "classification_report": report, "confusion_matrix": matrix}
