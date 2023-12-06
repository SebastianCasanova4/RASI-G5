from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from pymongo import MongoClient
import datetime
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from django.conf import settings
from bson.objectid import ObjectId

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
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_>
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        else:
            data['form'] = formulario
    return render(request, 'registration/registro.html', data)

def healthCheck(request):
    
    return HttpResponse('ok')

    @api_view(["GET", "POST"])
def cedulas(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.rasi_db
    cedulas = db['cedulas']
    if request.method == "GET":
        result = []
        data = cedulas.find({})
        for dto in data:
            jsonData = {
                'id': str(dto['_id']),
                "cedula": dto['cedula'],
                'sedes': dto['sedes']
            }
            result.append(jsonData)
        client.close()
        return JsonResponse(result, safe=False)
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        result = cedulas.insert(data)
        respo ={
            "MongoObjectID": str(result),
            "Message": "nuevo objeto en la base de datos"
        }
        client.close()
        return JsonResponse(respo, safe=False)


@api_view(["GET", "POST"])
def cedulasDetail(request, pk):
    client = MongoClient(settings.MONGO_CLI)
    db = client.rasi_db
    cedulas  = db['cedulas']
    if request.method == "GET":
        data = cedulas.find({'cedula': pk})
        result = []
        for dto in data:
            jsonData ={
                'id': str(dto['_id']),
                "cedula": dto['cedula'],
                'sedes': dto['sedes']
            }
            result.append(jsonData)
        client.close()
        return JsonResponse(result[0], safe=False)
    if request.method == "POST":
        data = JSONParser().parse(request)
        result = variables.update(
            {'cedula': pk},
            {'$push': {'sedes': data}}
        )
        respo ={
            "MongoObjectID": str(result),
            "Message": "nuevo objeto en la base de datos"
        }
        return JsonResponse(respo, safe=False)
