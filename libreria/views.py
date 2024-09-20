from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import BookForm

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

def inicio_sesion(request):
    if request.method == 'GET':
        return render (request, 'iniciar_sesion.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render (request, 'iniciar_sesion.html',{
                'form': AuthenticationForm,
                'error':'El usuario o la contraseña es incorrecto'
            })
        else:
            login(request, user)
            return redirect('libreria')

def agregar_libro(request):
    if request.method == 'GET':
        return render(request, 'agregar_libro.html', {
            'form': BookForm
        })
    else:
        try:
            form = BookForm(request.POST, request.FILES)  # Incluye request.FILES para manejar la imagen
            if form.is_valid():  # Valida el formulario
                new_book = form.save(commit=False)
                new_book.user = request.user
                new_book.save()
                return redirect('libreria')  # Redirige si el formulario es válido y el libro se guarda
            else:
                return render(request, 'agregar_libro.html', {
                    'form': form,
                    'error': 'Introduce datos válidos'
                })
        except Exception as e:
            return render(request, 'agregar_libro.html', {
                'form': BookForm,
                'error': f'Ocurrió un error: {str(e)}'
            })
