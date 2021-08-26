from rest_framework import serializers

class TodoSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    uuid = serializers.CharField()
    subject = serializers.CharField()
    projects = serializers.ListField()
    due = serializers.CharField()
    completed = serializers.BooleanField()
    completedDate = serializers.CharField()
    archived = serializers.BooleanField()
    isPriority = serializers.BooleanField()
    notes = serializers.ListField()
    