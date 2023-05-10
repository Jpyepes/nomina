from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from core import views as coreViews

# Create your views here.

def login(request):
    msgError = ''
    if request.method == 'POST':
        usuario = request.POST['usuario']
        clave = request.POST['clave']
        print(request.POST)
        user = authenticate(request,username=usuario,password=clave)
        print(user)
        if user is not None:
            auth_login(request,user)
            permisoUsuario = user.has_perm('produccion.produccion')
            return redirect(coreViews.landing)
        else:
            msgError = 'Usuario y/o contraseña incorrectos'
        
    return render(request, 'login.html',{'msgError': msgError})