from django.db import models
from django.conf import settings


class User(models.Model):
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    short_description = models.CharField(max_length=100)
    description = models.TextField()


class Post(models.Model):
    text = models.TextField(max_length=100)
    comments = models.CharField(max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
