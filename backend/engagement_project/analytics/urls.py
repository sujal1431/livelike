from django.urls import path
from . import views

urlpatterns = [
    path("load-data/", views.load_dataset, name="load-data"),
    path("process/", views.process_users, name="process-users"),
    path("train-model/", views.train_model, name="train-model"),
    path("model-metrics/", views.model_metrics, name="model-metrics"),
    path("confusion-matrix/", views.confusion_matrix_data, name="confusion-matrix"),
    path("users/", views.get_users, name="users"),
    path("summary/", views.analytics_summary, name="summary"),
    path("insights/", views.insights, name="insights"),
]
