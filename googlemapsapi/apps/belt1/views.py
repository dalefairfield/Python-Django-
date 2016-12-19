from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Users, Trips, Join
from django.contrib import messages


# Create your views here.
def index(request):
    # Users= Users.registerManager.all().delete()
    # Users2= Users.loginManager.all().delete()
    # Trip= Trips.tripManager.all().delete()
    # Join= Join.objects.all().delete()
    return render(request, 'belt1/index.html')

def register(request):
    result = Users.registerManager.register(request.POST['name'], request.POST['username'], request.POST['email'], request.POST['password'], request.POST['password_confirmation'])
    if result[0]:
        request.session['user_id']=result[2]
        request.session['name']=result[1].name
        print result[1].name
        return redirect('/dashboard')
    else:
        for x in xrange(len(result[1])):
            messages.error(request, result[1][x])
        return redirect('/')

def login(request):
    print request.POST
    # name = Users.loginManager.filter(name=request.POST['name'])
    result = Users.loginManager.login(request.POST['email_login'], request.POST['password_login'])
    name = Users.loginManager.filter(email=request.POST['email_login'])
    if len(name) >0:
        name = name[0].name
        request.session['name']=name
    #     print name
    if result[0]:
        request.session['user_id']=result[2]
        return redirect('/dashboard')
    else:
        for x in xrange(len(result[1])):
            messages.error(request, result[1][x])
        return redirect('/')

def logout(request, id):
    request.session.pop('user_id')
    request.session.pop('email_login')
    request.session.clear()
    return redirect('/')

def dashboard(request):
    trip = Trips.tripManager.filter(user_id=request.session.get('user_id'))
    other_trips = Trips.tripManager.exclude(user_id=request.session.get('user_id'))
    join = Join.objects.filter(user_id=request.session['user_id'])
    for x in join:
        other_trips = other_trips.exclude(id=x.trip.id)
    context = {
    'trip' : trip,
    'other_trips' : other_trips,
    'join' : join
    }
    return render(request, 'belt1/dashboard.html', context)

def addtrip2(request):
    if request.method == 'GET':
        return render(request, 'belt1/addtrip.html')
    elif request.method == 'POST':
        trip = Trips.tripManager.addtrip2(destination=request.POST['destination'], description=request.POST['description'], start=request.POST['start'], end=request.POST['end'], user_id= request.session.get('user_id'))
        if trip[0]:
            trip = Trips.tripManager.create(destination=request.POST['destination'], description=request.POST['description'], start=request.POST['start'], end=request.POST['end'], user_id= request.session.get('user_id'))
            join= Join.objects.create(trip_id=trip.id, user_id=request.session['user_id'])
            trip.save()
            return redirect('/dashboard')
        else:
            request.session['trip_message']=trip[1]
            return redirect('/addtrip2')

def destination(request, trip_id):
    join = Join.objects.filter(trip_id=trip_id)
    other_trips = Trips.tripManager.exclude(user_id=request.session.get('user_id'))
    context = {
    'trip' : Trips.tripManager.filter(id=trip_id),
    'other_trips' : other_trips,
    'join' : join
    }
    return render(request, 'belt1/destination.html', context)

def join(request, trip_id):
    measure = Join.objects.filter(trip_id=trip_id).filter(user_id=request.session['user_id'])
    if len(measure)==0:
        join = Join.objects.create(user_id=request.session['user_id'], trip_id=trip_id)
    return redirect('/dashboard')

def profile(request, user_id):
    trip = Trips.tripManager.filter(user_id=request.session.get('user_id'))
    join = Join.objects.filter(user_id=request.session['user_id'])
    context = {
    'trip' : trip,
    'join' : join
    }
    return render(request, 'belt1/profile.html', context)

# def delete(request, trip_id):
#     context = {
#     'removed' : Trips.tripManager.filter(id=id).delete()
#     }
#     return render(request, 'belt1/dashboard.html', context)
