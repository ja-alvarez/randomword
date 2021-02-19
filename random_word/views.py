from django.shortcuts import render, redirect, HttpResponse
import random
import string

def index (request):
    request.session['counter'] = 0
    return render (request, 'index.html')

def random_word (request):
    request.session['counter'] += 1
    allowed_chars = ''.join((string.ascii_letters, string.digits))
    r_w = ''.join(random.choice(allowed_chars) for i in range(14))
    print(r_w)
    context = {
        "word" : r_w.capitalize(),
    }
    return render(request,'index.html', context)

def reset (request):
    request.session['counter'] = 0
    return render (request, 'index.html')