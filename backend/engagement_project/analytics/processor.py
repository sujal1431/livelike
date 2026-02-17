from .models import UserEngagement
from .engagement import calculate_engagement
from .ml_model import predict_churn


BATCH_SIZE = 500   # safe for SQLite


def process_all_users():

    users = list(UserEngagement.objects.all())

    for user in users:
        user.engagement_score = calculate_engagement(user)
        user.churn_probability = predict_churn(user)

    # ---------- BATCH UPDATE ----------
    total = len(users)

    for i in range(0, total, BATCH_SIZE):
        batch = users[i:i + BATCH_SIZE]

        UserEngagement.objects.bulk_update(
            batch,
            ["engagement_score", "churn_probability"]
        )

    return total
