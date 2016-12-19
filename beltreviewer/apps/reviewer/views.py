from django.shortcuts import render, redirect
from .models import Users

# Create your views here.
def index(request):
    return render(request, 'reviewer/index.html')

def register(request):
    result = Users.registerManager.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['password_confirmation'])
    if result[0]:
        request.session['first_name']=result[1].first_name
        return redirect('/books')
    else:
        request.session['message']=result[1]
        return redirect('/')

def login(request):
    result = Users.loginManager.login(request.POST['email_login'], request.POST['password_login'])
    if result[0]:
        return redirect('/books')
    else:
        request.session['login_message']=result[1]
        return redirect('/')

def logout(request):
    result = Users.loginManager.login(request.POST['email_login'], request.POST['password_login'])
    request.session['password_login']=""
    request.session['email_login']=""
    return redirect('/')

def books(request):
    result = Reviews.reviewManager.books(request.POST['rating'], request.POST['review'], request.POST['author'], request.POST['title'])
    if result[0]:
        request.session['rating']=result[1].rating
        request.session['review']=result[1].review
        request.session['author']=result[1].author
        request.session['title']=result[1].title
        return redirect('/review')
    else:
        request.session['message']=result[1]
        return redirect('/')

def add_review(request):
    result = Reviews.reviewManager.add_review(request.POST['rating'], request.POST['review'], request.POST['user_id'], request.POST['book_id'])
    if result[0]:
        return redirect('/review')
    else:
        request.session['review_message']=result[1]
        return redirect('/')

def review(request):
    result = Reviews.reviewManager.review(request.POST['rating'], request.POST['review'])
    if result[0]:
        return redirect('/user_review')
    else:
        request.session['review_message']=result[1]
        return redirect('/')

def user_review(request):
    result = Users.registerManager.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'])
    request.session['first_name']=result[1].first_name
    request.session['last_name']=result[1].last_name
    request.session['email']=result[1].email
    return redirect('/user_review')
