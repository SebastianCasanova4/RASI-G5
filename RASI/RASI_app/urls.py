
from django.urls import path,include
from .views import home, registro, healthCheck
from django.conf import settings
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', registro, name='registro'),
    path('health-check/', healthCheck)
]

