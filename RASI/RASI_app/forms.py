from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuarios

class CustomUserCreationForm(UserCreationForm):
    pass