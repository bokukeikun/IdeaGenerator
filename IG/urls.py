from django.urls import path
from . import views

urlpatterns = [
    path('category_forms/', views.home, name='IG-home'),
    path('category_forms/get', views.hello_get_query, name='hello_get_query'),
]