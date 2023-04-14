from django.urls import path
from . import views


urlpatterns = [
    path('list_customers', views.list_customers, name='list_customers'),
    path('list_authors', views.list_authors, name='list_authors'),
]
