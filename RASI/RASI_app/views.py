from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'RASI_app/home.html')

from django.contrib import messages

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        else:
            data['form'] = formulario
    return render(request, 'registration/registro.html', data)

def healthCheck(request):
    
    return HttpResponse('ok')