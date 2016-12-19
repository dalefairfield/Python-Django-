from django.shortcuts import render, redirect
from .models import Users
import datetime
# Create your views here.
def index(request):
    context = {
    'courses' : Users.objects.all()
    }
    print Users.objects.all()
    return render(request, 'project_course/index.html', context)

def add(request):
    now =  datetime.datetime.now()
    Users.objects.create(name=request.POST['name'], description=request.POST['description'])
    # name = Users.objects.create(name=request.POST['name'])
    # description = Users.objects.create(description=request.POST['description'])
    return redirect('/')

def delete(request, id):
    context = {
    'course' : Users.objects.filter(id=id)
    }
    return render(request, 'project_course/delete.html', context)

def DO_IT(request, id):
    Users.objects.filter(id=id).delete()
    return redirect('/')
