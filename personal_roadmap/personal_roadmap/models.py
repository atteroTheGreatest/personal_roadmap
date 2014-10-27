from django.db import models
from django.contrib.auth.models import User


class Goal(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Goal: %s, %s" % (self.title, self.description)


class Initiative(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    goal = models.ForeignKey(Goal)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=80)


class Board(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    users = models.ManyToManyField(User, related_name='boards')


class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    initiative = models.ForeignKey(Initiative, related_name='tasks')
    board = models.ForeignKey(Board)

    assignee = models.ForeignKey(User, related_name='assigned_tasks')
    reporter = models.ForeignKey(User, related_name='reported_tasks')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    STARTED = 'ST'
    IN_DESIGN = 'ID'
    IN_PROGRESS = 'IP'
    BLOCKED = 'BL'
    FINISHED = 'FI'
    ABANDONED = 'AB'

    STATES = (
        (STARTED, 'started'),
        (IN_DESIGN, 'in design'),
        (IN_PROGRESS, 'in progress'),
        (BLOCKED, 'blocked'),
        (FINISHED, 'finished'),
        (ABANDONED, 'abandoned'),
    )

    state = models.CharField(max_length=2,
                             choices=STATES,
                             default=STARTED)

    tags = models.ManyToManyField(Tag, related_name="tasks")


