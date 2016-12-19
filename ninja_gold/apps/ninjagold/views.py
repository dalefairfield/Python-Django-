from django.shortcuts import render
import datetime
import random
# Create your views here.
def index(request):
    request.session['result'] = 0
    request.session['activity']=[]
    return render(request, 'ninjagold/index.html')

def show(request):
    now =  datetime.datetime.now()
    if request.POST['building'] == 'farm':
        g = random.randrange(10, 21)
        request.session['result'] += g
        result = request.session['result']
        request.session['activity'].append(['Earned', result, 'gold at the farm'])
        context = {'time_date':now, 'result' : result}
        return render(request, 'ninjagold/index.html', context)

    elif request.POST['building'] == 'cave':
        g=random.randrange(5, 11)
        request.session['result'] += g
        result = request.session['result']
        request.session['activity'].append(['Earned', result, 'gold at the cave'])
        context = {'time_date':now,  'result' : result}
        return render(request, 'ninjagold/index.html', context)

    elif request.POST['building'] == 'house':
        g=random.randrange(2, 6)
        request.session['result'] += g
        result = request.session['result']
        request.session['activity'].append(['Earned', result, 'gold at the house'])
        context = {'time_date':now, 'result' : result}
        return render(request, 'ninjagold/index.html', context)

    elif request.POST['building'] == 'casino':
        g=random.randrange(-50, 51)
        request.session['result'] += g
        result = request.session['result']
        request.session['activity'].append(['Earned', result, 'gold at the casino'])
        context = {'time_date':now,  'result' : result}
        return render(request, 'ninjagold/index.html', context)
