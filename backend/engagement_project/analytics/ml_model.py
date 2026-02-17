from pathlib import Path

import joblib
import pandas as pd

MODEL_PATH = Path("analytics/churn_model.pkl")
_MODEL_CACHE = None


def load_trained_model():
    """Load trained churn model and cache it for repeated predictions."""
    global _MODEL_CACHE
    if _MODEL_CACHE is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                "Trained model not found. Run /api/train-model/ before processing users."
            )
        _MODEL_CACHE = joblib.load(MODEL_PATH)
    return _MODEL_CACHE


def predict_churn(user):
    """Predict churn probability for a single user object."""
    model = load_trained_model()
    features = pd.DataFrame(
        [
            {
                "tenure": user.session_time,
                "MonthlyCharges": user.pages_visited,
                "TotalCharges": user.clicks,
            }
        ]
    )
    probability = model.predict_proba(features)[0][1]
    return float(probability)
