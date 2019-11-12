from django.urls import path
from . import views

urlpatterns = [
    path('', views.qq_list, name='home'),
    path('search/', views.search, name="search"),
    path('qq/<int:pk>/', views.qqdetail, name="qqdetail"),
    path('about/', views.about, name='about')
]