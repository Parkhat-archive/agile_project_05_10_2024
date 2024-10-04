from anyio.abc import value
from rest_framework import serializers

from ..models import Project


class AllProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['di', 'name', 'created_at']


class CreateProjectSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Project
        fields = ['di', 'name', 'created_at']
        read_only_fields = ['created_at']

        def validate_description(self):
            if len(value) < 30:
                raise serializers.ValidationError('Description must be at least 30 characters')
            return value


