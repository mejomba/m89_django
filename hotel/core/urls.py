from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('room_detail/<int:pk>/', views.RoomDetail.as_view(), name='room_detail'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('reserve/', views.reserve_room, name='reserve'),
    path('login/', views.Login.as_view(), name='login'),
    path('verify_login/', views.VerifyLogin.as_view(), name='verify_login'),
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
    path('<str:uidb64>/<str:token>', views.activate, name='activate')
]
