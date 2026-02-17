from .models import UserEngagement

def generate_insights():
    total_users = UserEngagement.objects.count()

    if total_users == 0:
        return ["No user data available"]

    high_risk = UserEngagement.objects.filter(churn_probability__gt=0.6).count()
    low_engagement = UserEngagement.objects.filter(engagement_score__lt=20).count()

    avg_engagement = (
        sum([u.engagement_score for u in UserEngagement.objects.all() if u.engagement_score])
        / total_users
    )

    insights = [
        f"Total users tracked: {total_users}",
        f"High churn risk users: {high_risk}",
        f"Low engagement users: {low_engagement}",
        f"Average engagement score: {round(avg_engagement,2)}"
    ]

    return insights
