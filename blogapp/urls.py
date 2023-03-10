from django.urls import path
from . import views

urlpatterns = [
    path('olamide', views.index, name='index'),
]
