from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('post/', views.post_list, name='post-list'),
    path('post/create/', views.post_create, name='post-create'),
    # path('post/detail/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/update/<int:pk>/', views.post_update, name='post-update'),
    path('post/delete/<int:pk>/', views.post_delete, name='post-delete'),
]