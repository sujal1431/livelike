import numpy as np
import joblib

# load trained model once
model = joblib.load("analytics/churn_model.pkl")


def predict_churn(user):
    data = np.array([[
        user.session_time,
        user.pages_visited,
        user.clicks
    ]])

    prob = model.predict_proba(data)[0][1]
    return float(prob)
