from django.urls import path
from . import views


urlpatterns = [
    path('list/bought/user/<int:id>/', views.list_of_user_bought_books, name='list_of_user_bought_books'),
]