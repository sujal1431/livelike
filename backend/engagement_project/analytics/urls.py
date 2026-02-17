from django.urls import path
from . import views

urlpatterns = [
    path('process/', views.process_users),
    path('users/', views.get_users),
    path('summary/', views.analytics_summary),
    path('insights/', views.insights),
    path('load-data/', views.load_dataset),
    path('train-model/', views.train_model),
    path('model-metrics/', views.model_metrics),
    path('confusion-matrix/', views.confusion_matrix_data),

]
