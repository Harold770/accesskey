from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='User-Index'),
    path('addUser', views.add, name='Add-User')
]