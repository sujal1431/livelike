import pandas as pd
from .models import UserEngagement


def load_kaggle_data(filepath):
    df = pd.read_csv(filepath)

    # ---------- CLEAN DATA ----------
    # convert to numeric safely
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # remove rows with missing values
    df = df.dropna()

    # clear old data
    UserEngagement.objects.all().delete()

    count = 0

    for _, row in df.iterrows():

        session_time = float(row["tenure"])
        pages_visited = float(row["MonthlyCharges"])
        clicks = float(row["TotalCharges"])
        last_login_gap = 0

        UserEngagement.objects.create(
            session_time=session_time,
            pages_visited=int(pages_visited),
            clicks=int(clicks),
            last_login_gap=last_login_gap
        )

        count += 1

    return count
