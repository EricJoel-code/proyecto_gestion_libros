from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.http import HttpResponse # type: ignore
from django.contrib.auth import login, logout, authenticate # type: ignore
from django.db import IntegrityError # type: ignore
from .forms import BookForm
from .models import Libros
from django.contrib.auth.decorators import login_required

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

@login_required
def libreria(request):
    libros = Libros.objects.filter(user=request.user)
    return render(request,'libreria.html',{'libros':libros})

@login_required
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

@login_required
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

@login_required
def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libros, pk=libro_id, user=request.user)
    
    if request.method == 'GET':
        form = BookForm(instance=libro)
        return render(request, 'detalles_libros.html', {'libro': libro, 'form': form})
    
    else:
        try:
            # Maneja POST y también archivos (imágenes)
            form = BookForm(request.POST, request.FILES, instance=libro)
            
            if form.is_valid():
                form.save()  # Guarda los cambios solo si el formulario es válido
                return redirect('libreria')  # Redirige a la lista de libros
            
            else:
                # Si el formulario no es válido, vuelve a mostrarlo con errores
                return render(request, 'detalles_libros.html', {
                    'libro': libro,
                    'form': form,
                    'error': 'Por favor, revisa los datos introducidos.'
                })
        
        except ValueError:
            # Si ocurre un error inesperado, muestra un mensaje de error
            return render(request, 'detalles_libros.html', {
                'libro': libro,
                'form': form,
                'error': "Error al actualizar. Revise los datos e intente de nuevo."
            })

@login_required
def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libros, pk=libro_id, user=request.user)
    if request.method == 'POST':
        libro.delete()
        return redirect('libreria')