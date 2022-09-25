from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="E-Mail")
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Name')
    last_name = forms.CharField(label='Last name')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
        help_texts = { k:"" for k in fields }

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Modificar E-Mail', required=False)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput, required=False)
    first_name = forms.CharField(label='Modificar Nombre', required=False)
    last_name = forms.CharField(label='Modificar Apellido', required=False)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    image = forms.ImageField(label="image", required=False)

class BiographyForm(forms.Form):
    biography = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}), required=False)