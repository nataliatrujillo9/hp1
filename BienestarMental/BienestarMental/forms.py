from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from core.models import Usuarios

class SignUpForm(UserCreationForm):
    role = forms.CharField(required=True)

    class Meta:
        model_meta = User, Usuarios
        fields = (
            'rol'
            'username',
            'email',
            'first_name'
            'last_name'
            'password1'
            'password2'
        )