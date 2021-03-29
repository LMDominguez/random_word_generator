from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string


def index(request):
    request.session['counter'] = 0
    request.session['output'] = ''
    return render(request, 'index.html')

def generate(request):
    request.session['counter'] += 1
    request.session['output'] = get_random_string(length=14)
    return redirect('/random_word')

def random_word(request):
    return render(request, 'index.html')