from rest_framework import serializers
from rest_framework.fields import UUIDField

class TodoSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    uuid = serializers.CharField()
    subject = serializers.CharField()
    projects = serializers.CharField()
    due = serializers.CharField()
    completed = serializers.BooleanField()
    completedDate = serializers.CharField()
    archived = serializers.BooleanField()
    isPriority = serializers.BooleanField()
    notes = serializers.CharField()
    