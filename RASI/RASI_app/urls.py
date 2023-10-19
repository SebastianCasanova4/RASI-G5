from django.urls import path,include
from .views import home, registro
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', registro, name='registro'),
    
]

