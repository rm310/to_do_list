from rest_framework import serializers
from .models import ToDoList

class ToDoLIstSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = (
            "id",
            "title",
            "description",
            "is_completed",
            "created_at",
        )