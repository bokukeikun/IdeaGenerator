from django.urls import path
from . import views
from django.conf import settings       
from django.conf.urls.static import static

urlpatterns = [
<<<<<<< HEAD
    path('category_forms', views.home, name='IG-home'),
    path('category_forms/', views.category_forms, name='category_forms'),
    path('bulletin_board/', views.bulletin_board, name='bulletin_board'),
    path('category_create/', views.category_create, name='category_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('', views.home, name='IG-home'),
    path('category_forms/', views.category_forms, name='category_forms'),
    path('bulletin_board/', views.bulletin_board, name='bulletin_board'),
    path('category_create/', views.category_create, name='category_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 6bc1e49fd85c0970e087d1136e37e88fde724c1a
