from django.urls import path

from posted.views import (
    # CategoryListView,
    TagListView,
    TagPostView,
    idea_generator,
    post_list,
    like,
    # api_like,
    mypost,
    post_detail,
    comment_delete,
    mypost_update,
    mypost_delete,
    post_search_list,
    category_list,
    category_post,
    popular_tag_post,
    )

app_name = 'posted'

urlpatterns = [
    path('', post_list, name='post'),
    path('search/', post_search_list, name='post_search_list'),
    path('<int:pk>/like', like, name='like'),
    # path("api/<int:pk>/like", api_like, name="api_like"),
    path('new/', idea_generator,name='post_new'),
    path('<int:id>/', post_detail, name='post_detail'),
    path('comment_delete/<int:pk>/', comment_delete, name='comment_delete'),
    path('categories/', category_list, name='category_list'),   
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tag/<str:tag_slug>/', popular_tag_post, name='popular_tag_post'),
    path('category/<str:category_slug>/', category_post, name='category_post'),
    path('mypost/', mypost, name='mypost'),
    path('mypost/<int:id>/update/', mypost_update, name='mypost_update'),
    path('mypost/<int:id>/delete', mypost_delete, name='mypost_delete'),

    # path('list_create/<int:id>/',list_create, name='list_create' )
]


