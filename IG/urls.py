from django.urls import path
from . import views
from django.conf import settings       
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('category_forms/get', views.hello_get_query, name='hello_get_query'),
    # path('', views.home, name='IG-home'),
    # path('category_forms/', views.category_forms, name='category_forms'),
    path('bulletin_board/', views.bulletin_board, name='bulletin_board'),
    path('category_create/', views.category_create, name='category_create'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('contact/', views.contact, name='contact'),
    path('listing/', views.listing, name='listing'),
    path('listing_details/', views.listing_details, name='listing_details'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
