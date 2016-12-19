from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def add(self, email):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        message = []
        if  EMAIL_REGEX.match(email):
            message = message.append("Email is valid")
            email = Users.userManager.create(email=email)
            email.save()
            return (True, email)
        else:
           message = message.append("Email is not valid")
           return (False, message)
class Users(models.Model):
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()
