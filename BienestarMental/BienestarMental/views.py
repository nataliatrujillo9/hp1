from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from .forms import SignUpForm
from core.models import Usuarios, User, Missions
from django.contrib.auth.forms import UserCreationForm 
from .forms import SignUpForm


def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request='POST')
        if form.is_valid():
            user = form.save()
            user.Usuarios.role = form.cleaned_data['role']
            user.Usuarios.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('InicioSesion.html')

    else:
        form = SignUpForm()
    return render(request, 'Register.html', {'form': form})

def SignIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('InicioAprendiz.html')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'InicioSesion.html',{
        
    })

def inicio(request):
    return render(request, 'index.html', {

    })

def chat(request):
    return render(request, 'chat.html', {

    })

def inicioapr(request):
    return render(request, 'InicioAprendiz.html', {

    })
    

def iniciopsico(request):
    return render(request, 'InicioPsicologo.html', {

    })

def misionesapr(request):
    return render(request, 'MisionesApr.html', {

    })

def misionespsi(request):
    name = Missions.objects
    return render(request, 'MisionesPsi.html', {'name':name})