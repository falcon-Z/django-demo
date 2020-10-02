from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'password/index.html')

def about(request):
    return render(request, 'password/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length',12))

    password = ''
    for x in range(length):
        password += random.choice(characters)

    return render(request, 'password/password.html', {'password':password})
