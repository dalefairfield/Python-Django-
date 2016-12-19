from django.shortcuts import render, redirect
import random
import string
# Create your views here.
def index(request):
    if 'random' not in request.session:
        request.session['random']=1
    request.session['random'] += 1
    size = 14
    chars = string.ascii_uppercase + string.digits
    context = {
        "random":''.join(random.choice(chars) for _ in range(size))
    }
    return render(request, 'random_word/index.html', context)

def generate(request):
    if request.method == "POST":
        request.session['random'] = request.POST['txt_random']
        size = 14
        chars = string.ascii_uppercase + string.digits
        context = {
            "random" : ''.join(random.choice(chars) for _ in range(size))
        }
        return render(request, 'random_word/index.html', context)
    else:
        return redirect('/')
