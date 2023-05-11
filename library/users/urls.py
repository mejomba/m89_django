from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('profile/', views.profile, name='profile'),
    path('list_customers', views.list_customers, name='list_customers'),
    path('list_authors', views.list_authors, name='list_authors'),
]
