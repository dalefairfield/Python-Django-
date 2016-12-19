from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def index(request):

    return render(request, 'surveyform/index.html')

def result(request):
    if request.method == "POST":
        request.session['count'] +=1
        name = request.POST['name']
        location = request.POST['location']
        language = request.POST['language']
        message = request.POST['message']
        context = {
        "name":name,
        "location":location,
        "language":language,
        "message":message
        }
        return render(request, 'surveyform/results.html', context)
    else:
        return redirect('/')
