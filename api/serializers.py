from dataclasses import fields
from email.policy import default
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"
   
"""
assignee = serializers.PrimaryKeyRelatedField(read_only = True, default = serializers.CurrentUserDefault())
creator = serializers.PrimaryKeyRelatedField(read_only = True, default = serializers.CurrentUserDefault())

class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'priority', 'state', 'creation_date', 'completion_date', 'assignee', 'creator', 'time_since_its_creation',]
"""
