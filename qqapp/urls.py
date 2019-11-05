from django.urls import path
from . import views

urlpatterns = [
    path('', views.qq_list, name='qq_list'),
    path('search/', views.search, name="search"),
    path('qq/<int:id>/', views.qqdetail, name="qqdetail"),
]