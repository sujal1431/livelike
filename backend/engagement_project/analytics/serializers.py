from rest_framework import serializers
from .models import UserEngagement

class UserEngagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEngagement
        fields = '__all__'
