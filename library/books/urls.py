from django.urls import path
from . import views


urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    path('list_categories/', views.list_category, name='list_category'),
    path('list_publishers/', views.list_publisher, name='list_publisher'),
    path('list/books/author/<int:id>/', views.list_of_author_books, name='list_of_author_books'),
    path('list/books/publisher/<int:id>/', views.list_of_publisher_books, name='list_of_publisher_books'),
    path('list/books/category/<int:id>/', views.list_of_category_books, name='list_of_category_books'),
    path('list/books/popular/', views.list_of_popular_books, name='list_of_popular_books'),
]