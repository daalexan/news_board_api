from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128, null=False)
    link = models.CharField(max_length=200, null=False)
    pub_date = models.DateField(auto_now=True)
    author_name = models.CharField(max_length=64, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.IntegerField()


class Comment(models.Model):
    author_name = models.CharField(max_length=64, null=False)
    content = models.TextField()
    pub_date = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
