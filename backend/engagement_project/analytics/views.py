import json
from pathlib import Path

from django.db.models import Avg
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .insights import generate_insights
from .load_dataset import load_kaggle_data
from .models import UserEngagement
from .processor import process_all_users
from .train_model import train_churn_model

DATASET_PATH = Path("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
METRICS_PATH = Path("analytics/model_metrics.json")
CONFUSION_MATRIX_PATH = Path("analytics/confusion_matrix.json")


def _read_json(path: Path):
    """Safely read JSON file content and return None when missing/invalid."""
    try:
        with path.open("r", encoding="utf-8") as file_obj:
            return json.load(file_obj)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return None


@api_view(["GET"])
def load_dataset(request):
    """Load Kaggle churn dataset into the UserEngagement table."""
    loaded_count = load_kaggle_data(str(DATASET_PATH))
    return Response({"loaded_records": loaded_count})


@api_view(["GET"])
def process_users(request):
    """Compute engagement score and churn probability for all users."""
    processed_count = process_all_users()
    return Response({"message": f"Processed {processed_count} users"})


@api_view(["GET", "POST"])
def train_model(request):
    """Train or retrain churn model and persist metrics artifacts."""
    result = train_churn_model(str(DATASET_PATH))
    return Response(
        {
            "message": "Model trained successfully",
            "accuracy": result["accuracy"],
        }
    )


@api_view(["GET"])
def model_metrics(request):
    """Return persisted model metrics JSON."""
    return Response(_read_json(METRICS_PATH))


@api_view(["GET"])
def confusion_matrix_data(request):
    """Return persisted confusion matrix JSON."""
    matrix = _read_json(CONFUSION_MATRIX_PATH)
    return Response({"matrix": matrix})


@api_view(["GET"])
def get_users(request):
    """Return all users for frontend table rendering."""
    users = UserEngagement.objects.values(
        "id",
        "session_time",
        "pages_visited",
        "clicks",
        "last_login_gap",
        "engagement_score",
        "churn_probability",
        "created_at",
    )
    return Response(list(users))


@api_view(["GET"])
def analytics_summary(request):
    """Return aggregate dashboard metrics."""
    total_users = UserEngagement.objects.count()
    high_risk = UserEngagement.objects.filter(churn_probability__gt=0.6).count()
    low_engagement = UserEngagement.objects.filter(engagement_score__lt=20).count()
    avg_engagement = UserEngagement.objects.aggregate(avg=Avg("engagement_score"))["avg"] or 0

    return Response(
        {
            "total_users": total_users,
            "high_churn_risk": high_risk,
            "low_engagement_users": low_engagement,
            "avg_engagement_score": round(avg_engagement, 2),
        }
    )


@api_view(["GET"])
def insights(request):
    """Return generated insight messages based on user analytics."""
    return Response(generate_insights())
