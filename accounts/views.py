
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect
from .forms import *

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            reqUser = form.cleaned_data.get('username')
            reqPassword = form.cleaned_data.get('password')
            user = authenticate(request, username=reqUser, password=reqPassword)
            if user is not None:
                auth_login(request, user)
                return redirect('main:inicio')
            else:
                return render(request, 'accounts/login.html', {'message': 'Usuario o contraseña incorrectos', 'form': form})
        else:
            return render(request, 'accounts/login.html', {'message': 'Usuario o contraseña incorrectos', 'form': form})
    if request.user.is_authenticated!=True:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
    else:
        return redirect('main:inicio')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'main/inicio.html', {'message': f'Usuario {username} creado correctamente'})
        else:
            return render(request, 'accounts/register.html', {'form': form})
    if request.user.is_authenticated!=True:
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})
    else:
        return redirect('main:inicio')