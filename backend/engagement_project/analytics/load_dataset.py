from pathlib import Path

import pandas as pd

from .models import UserEngagement


def _build_records(df):
    """Convert cleaned dataframe rows into UserEngagement instances."""
    records = []
    for _, row in df.iterrows():
        records.append(
            UserEngagement(
                session_time=float(row["tenure"]),
                pages_visited=int(float(row["MonthlyCharges"])),
                clicks=int(float(row["TotalCharges"])),
                last_login_gap=0,
            )
        )
    return records


def load_kaggle_data(filepath):
    """Load and clean Kaggle churn CSV, then replace UserEngagement data."""
    dataset_path = Path(filepath)
    df = pd.read_csv(dataset_path)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df = df.dropna(subset=["tenure", "MonthlyCharges", "TotalCharges"])

    UserEngagement.objects.all().delete()
    records = _build_records(df)
    UserEngagement.objects.bulk_create(records, batch_size=1000)
    return len(records)
