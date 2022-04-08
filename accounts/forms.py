from os import link

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

import email

class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repetir Password", widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class UserEditForm(forms.Form):

    email = forms.EmailField(label='Modificar E-mail')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repetir el password', widget=forms.PasswordInput())
    last_name = forms.CharField(label="Apellido", max_length = 20)
    first_name = forms.CharField(label="Nombre", max_length = 20)
    avatar = forms.ImageField(required=False)
    link = forms.URLField(required = False)
    additional_description = forms.CharField(max_length = 100, required = False)