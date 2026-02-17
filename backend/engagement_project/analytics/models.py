from django.db import models


class UserEngagement(models.Model):
    """Persisted engagement features and derived analytics for each user."""

    session_time = models.FloatField(help_text="Time spent in minutes")
    pages_visited = models.IntegerField()
    clicks = models.IntegerField()
    last_login_gap = models.IntegerField(help_text="Days since last login")

    engagement_score = models.FloatField(null=True, blank=True)
    churn_probability = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.id} | Engagement: {self.engagement_score}"
