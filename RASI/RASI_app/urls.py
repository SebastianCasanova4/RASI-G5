
from django.urls import path,include
from .views import home, registro, healthCheck
from django.conf import settings
from django.conf.urls import url, include
from django.views.static import serve
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', registro, name='registro'),
    path('health-check/', healthCheck),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    url(r'^cedulas/$', cedulas),
    url(r'^cedulas/(?P<pk>\w+)/$', cedulasDetail)
]

