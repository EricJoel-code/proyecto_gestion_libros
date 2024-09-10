from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.db import IntegrityError

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def registro(request):
    if request.method == 'GET':
        return render(request,'registro.html',{
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #Registro de usuario
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('libreria')
            except IntegrityError:
                return render(request,'registro.html',{
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request,'registro.html',{
            'form': UserCreationForm,
            'error': 'La contraseña no coincide'
        })

def libreria(request):
    return render(request,'libreria.html')

def salir(request):
    logout(request)
    return redirect('inicio')