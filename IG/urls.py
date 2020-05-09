from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='IG-home'),
    path('category_forms/', views.category_forms, name='category_forms'),
]