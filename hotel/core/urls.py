from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('room_detail/<int:pk>/', views.RoomDetail.as_view(), name='room_detail'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('reserve/', views.reserve_room, name='reserve'),
    path('login/', views.Login.as_view(), name='login'),
    path('verify_login/', views.VerifyLogin.as_view(), name='verify_login'),
]
