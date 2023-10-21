from django.urls import path,include
from .views import home, registro
from django.conf import settings
from RASI.RASI_app import views
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', registro, name='registro'),
    path('health-check/', views.healthCheck)
]

