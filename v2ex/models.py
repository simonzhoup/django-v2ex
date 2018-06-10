from django.db import models
from django.contrib.auth.admin import User

from datetime import datetime
import hashlib


class Category(models.Model):
    name = models.CharField(max_length=20)
    info = models.TextField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    category = models.ForeignKey(Category, blank=True,null=True, on_delete=models.CASCADE,db_constraint=True)
    name = models.CharField(max_length=20)
    info = models.TextField()

    def __str__(self):
        return self.name

class Topic(models.Model):
    tag = models.ForeignKey(Tag, blank=True,null=True, on_delete=models.CASCADE,db_constraint=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User, blank=True,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar_hash = models.CharField(max_length=100)

    def avatar(self, size=100, default='identicon', rating='g'):
        url = 'http://www.gravatar.com/avatar'
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(
            url=url, hash=hash, size=size, default=default, rating=rating)

    def __str__(self):
        return self.user.username
