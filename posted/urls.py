from django.urls import path

from posted.views import (
    PostDetailView,
    CategoryListView,
    TagListView,
    CategoryPostView,
    TagPostView,
    idea_generator,
    post_list,
    like,
    # api_like,
    )

app_name = 'posted'

urlpatterns = [
    path('', post_list, name='post'),
    path('<int:pk>/like', like, name='like'),
    # path("api/<int:pk>/like", api_like, name="api_like"),
    path('new/', idea_generator,name='post_new'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('category/<str:category_slug>/',
         CategoryPostView.as_view(), name='category_post'),
    path('tag/<str:tag_slug>/', TagPostView.as_view(), name='tag_post'),
]


