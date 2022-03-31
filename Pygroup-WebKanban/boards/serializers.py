from rest_framework import serializers
from .models import Board, Column, Task, User


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'name')


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'user', 'column', 'description', 'priority', 'registration_date')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'avatar')