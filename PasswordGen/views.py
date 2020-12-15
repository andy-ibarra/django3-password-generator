from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, "PasswordGen/home.html")

def about(request):
    return  render(request, "PasswordGen/about.html")

def password(request):

    thepassword = ''
    characters = list("qwertyuiopasdfghjklzxcvbnm")
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTASDFGZXCVBNMHJKLYUIOP'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()=+'))
    if request.GET.get('numbers'):
        characters.extend(list('7946132850'))

    length = int(request.GET.get('length'))

    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, "PasswordGen/password.html", {'password':thepassword})