from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from core import views as coreViews
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    msgError = ''
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(request,user='usuario',password='contraseña')
        print(user)
        if user is not None:
            login(request, user)
            return redirect(coreViews.landing)
        else:
            msgError = 'Usuario y/o contraseña incorrectos'
        
    return render(request, 'login.html',{'msgError': msgError})