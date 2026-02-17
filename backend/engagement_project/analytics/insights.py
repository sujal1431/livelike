from django.db.models import Avg

from .models import UserEngagement


def generate_insights():
    """Generate concise AI insights from persisted user analytics."""
    total_users = UserEngagement.objects.count()
    if total_users == 0:
        return ["No user data available"]

    high_risk = UserEngagement.objects.filter(churn_probability__gt=0.6).count()
    low_engagement = UserEngagement.objects.filter(engagement_score__lt=20).count()
    avg_engagement = UserEngagement.objects.aggregate(avg=Avg("engagement_score"))["avg"] or 0

    return [
        f"Total users tracked: {total_users}",
        f"High churn risk users: {high_risk}",
        f"Low engagement users: {low_engagement}",
        f"Average engagement score: {avg_engagement:.2f}",
    ]
