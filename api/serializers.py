from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User  # Built-in Django model that provides us with username, email, password, first_name, and last_name fields.

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    assignee = UserSerializer()
    creator = UserSerializer()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'priority', 'state', 'creation_date', 'completion_date', 'assignee', 'creator', 'time_since_its_creation',]
