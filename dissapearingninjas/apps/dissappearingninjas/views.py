from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'greeting' : 'no ninjas here'}
    return render(request, 'dissappearingninjas/index.html', context)

def ninjas(request):
    context ={'ninja':'ninja'}
    return render(request, 'dissappearingninjas/index.html', context)


def ninjacolors(request, color):
    context ={'color':color}
    return render(request, 'dissappearingninjas/index.html', context)
