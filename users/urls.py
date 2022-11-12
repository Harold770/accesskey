from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.saludo, name='saludo'),
    path('index/', views.index, name='index')
]