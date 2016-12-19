from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Comments(models.Model):
#     user_id = models.ForiegnKey(Users)
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
