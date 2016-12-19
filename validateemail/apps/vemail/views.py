from django.shortcuts import render, redirect, HttpResponse
from .models import Users
# Create your views here.
def index(request):

    return render(request, 'vemail/index.html')

def add(request):
    result = Users.userManager.add(request.POST['email'])
    if result[0]:
        request.session['email']=result[1].email
        return redirect('/success')
    else:
        request.session['message']=result[1]
        return redirect('/')

def success(request):
    emails = Users.userManager.all()
    context = {
    'emails':emails,
    'email': request.session.get('email')
    }
    return render(request, 'vemail/list.html', context)
