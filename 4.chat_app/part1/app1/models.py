
from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Team, 
        on_delete=models.CASCADE,
    )
    starter = models.ForeignKey(User, 
        on_delete=models.CASCADE,
    )

class Comment(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, 
        on_delete=models.CASCADE,
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, 
        on_delete=models.CASCADE,
        related_name='testing')
    updated_by = models.ForeignKey(User, null=True, 
        on_delete=models.CASCADE,
        related_name='+')