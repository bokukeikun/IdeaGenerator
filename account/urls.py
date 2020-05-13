from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings       
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)