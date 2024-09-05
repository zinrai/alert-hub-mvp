from rest_framework import serializers
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    urgency_display = serializers.CharField(source='get_urgency_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Alert
        fields = ['id', 'subject', 'body', 'identifier', 'urgency', 'urgency_display', 'status', 'status_display', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
