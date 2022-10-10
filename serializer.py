from rest_framework import serializers

from .models import Hope


class HopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hope
        fields = ('client_id', 'client_name', 'created_at', 'created_by')
        def __str__(self):
            return self.client_name


