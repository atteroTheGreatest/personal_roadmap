from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Goal, Initiative, Task, Board, Tag


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email',
                  'is_staff', 'reported_tasks',
                  'assigned_tasks', 'boards',)


class GoalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goal
        fields = ('url', 'title', 'description', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at',)


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ('url', 'title', 'description', 'users')


class InitiativeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Initiative
        fields = ('url', 'title', 'description', 'created_at', 'updated_at', 'tasks', 'goal',)
        read_only_fields = ('created_at', 'updated_at',)


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('url', 'title', 'description',
                  'initiative', 'board', 'assignee', 'reporter',
                  'state', 'tags',
                  'created_at', 'updated_at',)
        read_only_fields = ('created_at', 'updated_at',)


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'tasks',)