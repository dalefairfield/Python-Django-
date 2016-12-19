from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Messages(models.Model):
    message = models.TextField(max_length=1000)
    # Notice the association made with ForeignKey for a one-to-many relationship
    user_id = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Comments(models.Model):
    comment = models.TextField(max_length=1000)
    # Notice the association made with ForeignKey for a one-to-many relationship
    user_id = models.ForeignKey(User)
    message_id = models.ForeignKey(Message)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
