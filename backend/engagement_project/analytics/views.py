from rest_framework.decorators import api_view
from rest_framework.response import Response
from .load_dataset import load_kaggle_data
from .models import UserEngagement
from .serializers import UserEngagementSerializer
from .processor import process_all_users
from .insights import generate_insights
import json

# Process users (AI calculation)
@api_view(['GET'])
def process_users(request):
    count = process_all_users()
    return Response({"message": f"Processed {count} users"})


# Get all users
@api_view(['GET'])
def get_users(request):
    users = UserEngagement.objects.all()
    serializer = UserEngagementSerializer(users, many=True)
    return Response(serializer.data)


# Dashboard summary
@api_view(['GET'])
def analytics_summary(request):
    total_users = UserEngagement.objects.count()
    high_risk = UserEngagement.objects.filter(churn_probability__gt=0.6).count()
    low_engagement = UserEngagement.objects.filter(engagement_score__lt=20).count()

    return Response({
        "total_users": total_users,
        "high_churn_risk": high_risk,
        "low_engagement_users": low_engagement
    })


# AI insights
@api_view(['GET'])
def insights(request):
    return Response(generate_insights())

@api_view(['GET'])
def load_dataset(request):
    count = load_kaggle_data("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    return Response({"loaded_records": count})

from .train_model import train_churn_model

@api_view(['GET'])
def train_model(request):
    result = train_churn_model("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    return Response({
        "message": "Model trained successfully",
        "accuracy": result["accuracy"]
    })

@api_view(['GET'])
def model_metrics(request):
    try:
        with open("analytics/model_metrics.json") as f:
            data = json.load(f)
    except:
        data = None

    return Response(data)


@api_view(['GET'])
def confusion_matrix_data(request):
    try:
        with open("analytics/confusion_matrix.json") as f:
            matrix = json.load(f)
    except:
        matrix = None

    return Response({"matrix": matrix})
from .train_model import train_churn_model
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def train_model(request):
    result = train_churn_model("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

    return Response({
        "message": "Model retrained successfully",
        "accuracy": result["accuracy"]
    })
