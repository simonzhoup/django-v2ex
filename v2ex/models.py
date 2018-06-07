from django.db import models
from django.contrib.auth.admin import User


class Category(models.Model):
    name = models.CharField(max_length=20)
    info = models.TextField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    category = models.ForeignKey(Category, blank=True,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    info = models.TextField()

    def __str__(self):
        return self.name

class Topic(models.Model):
    Tag = models.ForeignKey(Tag, blank=True,null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField()
    author = models.ForeignKey(User, blank=True,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
