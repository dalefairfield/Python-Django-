from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class RegisterManager(models.Manager):
    def register(self, first_name, last_name, email, password, password_confirmation):
        message = []
        if  EMAIL_REGEX.match(email):
            print "blah"
        else:
            message.append("Email is not valid")
        if len(first_name)>2:
            print "blah"
        else:
            message.append("Please enter a valid first name")
        if len(last_name)>2:
            print "blah"
        else:
            message.append("Please enter a valid last name")
        if len(password)>=8 and password == password_confirmation:
            print "blah"
        else:
            message.append("Please enter a password containing at least 8 characters and/or make sure password matches the password confirmation.")
        if len(message)==0:
            pw_hash = bcrypt.hashpw(str(password), bcrypt.gensalt())
            registration = Users.registerManager.create(first_name=first_name, last_name=last_name,email=email, password=pw_hash)
            registration.save()
            return (True, registration)
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
                return (True, login[0])
            else:
                login_message.append("Password invalid.")
            return (False, login_message)
        else:
            login_message.append("Email and/or Password invalid.")
            return (False, login_message)


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    registerManager = RegisterManager()
    loginManager = LoginManager()

# class Authors(models.Model):
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
# class Books(models.Model):
#     title = models.CharField(max_length=255)
#     author_id = models.ForeignKey(Authors)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class ReviewManager(models.Manager):
    def login(self, rating, review):
        review_message = []
        if len(title)<1:
            review.append("Invalid Title.")
        elif len(review) < 1:
            review_message.append("Must include a review.")
        elif len(author) < 1:
            review_message.append("Must include an author.")
        if len(review_message)==0:
            review = Users.reviewManager.filter(rating=rating, review=review)
            return (True, review[0])
        else:
            review_message.append("Invalid.")
            return (False, review_message)

class Reviews(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    review = models.TextField()
    book_id = models.ForeignKey(Books)
    user_id = models.ForeignKey(Users)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviewManager = ReviewManager()
