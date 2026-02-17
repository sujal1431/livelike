from .ml_model import predict_churn
from .models import UserEngagement

BATCH_SIZE = 500


def calculate_engagement_score(user):
    """Calculate engagement score from usage and recency features."""
    score = (
        user.session_time * 0.5
        + user.pages_visited * 2
        + user.clicks * 0.1
        - user.last_login_gap * 1.5
    )
    return max(score, 0.0)


def process_all_users():
    """Compute analytics fields for all users and persist in batches."""
    users = list(UserEngagement.objects.all())
    for user in users:
        user.engagement_score = calculate_engagement_score(user)
        user.churn_probability = predict_churn(user)

    for start in range(0, len(users), BATCH_SIZE):
        batch = users[start : start + BATCH_SIZE]
        UserEngagement.objects.bulk_update(batch, ["engagement_score", "churn_probability"])

    return len(users)
