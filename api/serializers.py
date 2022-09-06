from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User  # Built-in Django model that provides us with username, email, password, first_name, and last_name fields.

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        try:
            user = User.objects.get(username = validated_data['username'])
            return user

        except User.DoesNotExist:
            user = User.objects.create_user(**validated_data)
            user.save()
            return user
       
    class Meta:
        model = User
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'priority', 'state', 'creation_date', 'completion_date', 'assignee', 'creator', 'time_since_its_creation',]
