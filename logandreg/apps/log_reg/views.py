from django.shortcuts import render, redirect
from .models import Users

# Create your views here.
def index(request):
    return render(request, 'log_reg/index.html')

def register(request):
    result = Users.registerManager.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['password_confirmation'])
    if result[0]:
        request.session['first_name']=result[1].first_name
        return redirect('/success')
    else:
        request.session['message']=result[1]
        return redirect('/')

def login(request):
    result = Users.loginManager.login(request.POST['email_login'], request.POST['password_login'])
    display = Users.loginManager.filter(email=request.POST['email_login'])
    context = { 'login_display' : display}
    if result[0]:
        return render(request, 'log_reg/success.html', context)
    else:
        request.session['login_message']=result[1]
        return redirect('/')

def success(request):
    emails = Users.registerManager.all()
    context = {
    'emails':emails,
    'first_name': request.session.get('first_name')
    }
    return render(request, 'log_reg/success.html', context)
