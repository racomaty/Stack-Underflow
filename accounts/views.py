from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect
from .forms import *
from .models import Avatar
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            reqUser = form.cleaned_data.get('username')
            reqPassword = form.cleaned_data.get('password')
            user = authenticate(request, username = reqUser, password = reqPassword)
            if user is not None:
                auth_login(request, user)
                return redirect('main:inicio')
            else:
                return render(request, 'accounts/login.html', {'formErrors': form.errors})
        else:
            return render(request, 'accounts/login.html', {'formErrors': form.errors})
    elif request.user.is_authenticated != True:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'formErrors': form.errors})
    else:
        return redirect('main:inicio')

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            reqUser = form.cleaned_data['username']
            reqPassword = form.cleaned_data['password1']
            form.save()
            user = authenticate(request, username = reqUser, password = reqPassword)
            if user is not None:
                auth_login(request, user)
                return redirect('main:inicio')
            else:
                form.errors.customError = 'Error al registrar user'
                return render(request, 'accounts/signup.html', {'formErrors': form.errors.customError})
        else:
            return render(request, 'accounts/signup.html', {'formErrors': form.errors})
    if request.user.is_authenticated != True:
        form = UserRegistrationForm()
        return render(request, 'accounts/signup.html')
    else:
        return redirect('main:inicio')

@login_required
def profile(request, username):
    user = User.objects.get(username = username)
    user.avatar = getAvatar(user)
    return render(request, 'accounts/profile.html', {'user': user, "userAvatar": getAvatar(request.user)})

@login_required
def editProfile(request):
    user = User.objects.get(username = request.user.username)
    user.avatar = getAvatar(user)
    if request.method == "POST":
        userForm = UserEditForm(request.POST)
        avatarForm = AvatarForm(request.POST, request.FILES)
        if avatarForm.is_valid() & userForm.is_valid():
            user.first_name = userForm.cleaned_data["first_name"]
            user.last_name = userForm.cleaned_data["last_name"]
            user.email = userForm.cleaned_data["email"]
            user.password1 = userForm.cleaned_data["password1"]
            user.password2 = userForm.cleaned_data["password2"]
            user.biography = userForm.cleaned_data["biography"]
            user.save()
            if avatarForm.cleaned_data["image"]:
                avatarOld = Avatar.objects.all().filter(user = user)
                if len(avatarOld) > 0:
                    avatarOld[0].delete()
                avatar = Avatar(user = user, image = avatarForm.cleaned_data["image"])
                avatar.save()
            return redirect('accounts:profile', username = user.username)
        else:
            return render(request, 'accounts/editProfile.html', {'user': user, 'userForm': userForm, 'avatarForm': avatarForm})
    else:
        userForm = UserEditForm()
    return render(request, 'accounts/editProfile.html', {'form':userForm, 'user':user, 'userAvatar': getAvatar(user)})

##################### Funciones

def getAvatar(user):
    if user.id:
        avList = Avatar.objects.all().filter(user = user.id)
        if len(avList) > 0:
            return avList[0].image.url
        else:
            return os.path.join(settings.MEDIA_URL, 'avatars/default.png')