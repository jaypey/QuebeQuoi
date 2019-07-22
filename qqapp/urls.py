from django.urls import path
from . import views

urlpatterns = [
    path('', views.qq_list, name='qq_list'),
]