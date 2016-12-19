from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from datetime import date, time
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class RegisterManager(models.Manager):
    def register(self, name, username, email, password, password_confirmation):
        message = []
        if  EMAIL_REGEX.match(email):
            print "email"
        else:
            message.append("Email is not valid")
        if len(name)>3:
            print "name"
        else:
            message.append("Please enter a valid first name")
        if len(username)>3:
            print "username"
        else:
            message.append("Please enter a valid last name")
        if len(password)>=8 and password == password_confirmation:
            print "password"
        else:
            message.append("Please enter a password containing at least 8 characters and/or make sure password matches the password confirmation.")
        if len(message)==0:
            pw_hash = bcrypt.hashpw(str(password), bcrypt.gensalt())
            registration = Users.registerManager.create(name=name, username=username,email=email, password=pw_hash)
            registration.save()
            print registration.id
            return (True, registration, registration.id)
        else:
            return (False, message)

class LoginManager(models.Manager):
    def login(self, email, password):
        login_message = []
        if len(email)==0:
            login_message.append("Email invalid.")
        elif not EMAIL_REGEX.match(email):
            login_message.append("Email invalid.")
        elif len(password) < 8:
            login_message.append("Password invalid.")
        if len(login_message)==0:
            login = Users.loginManager.filter(email=email)
            if len(login)<1:
                login_message.append("Email and/or Password invalid.")
            elif (bcrypt.checkpw(str(password), str(login[0].password))):
                return (True, login, login[0].id)
            else:
                login_message.append("Password invalid.")
            return (False, login_message)
        else:
            login_message.append("Email and/or Password invalid.")
            return (False, login_message)

class TripManager(models.Manager):
    def addtrip2(self, destination, description, start, end, user_id):
        trip_message = []
        if len(destination)<2:
            trip_message.append("Invalid destination!")
        elif len(description)<2:
            trip_message.append("Invalid description!")
        if len(start)==0:
            trip_message.append("Invalid start date")
        if len(end)==0:
            trip_message.append("Invalid end date")
        now=unicode(date.today())
        if start<now or end<now:
            trip_message.append("Start and/or end date cannot before today")
        if end<start:
            trip_message.append("Cannot end your trip before you leave")
        if len(trip_message)==0:
            return (True, '')
        else:
            trip_message.append("Destination and/or Description invalid.")
            return (False, trip_message)


class Users(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    registerManager = RegisterManager()
    loginManager = LoginManager()


class Trips(models.Model):
    destination = models.CharField(max_length=255)
    description = models.TextField()
    start = models.CharField(max_length=255)
    end = models.CharField(max_length=255)
    user = models.ForeignKey(Users)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tripManager = TripManager()

class Join(models.Model):
    user = models.ForeignKey(Users)
    trip = models.ForeignKey(Trips)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
