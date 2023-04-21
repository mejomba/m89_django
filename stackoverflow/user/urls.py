from django.urls import path
from . import views


urlpatterns = [
    path('create_user', views.CreateUser.as_view(), name='create_user'),
    path('profile-<int:pk>', views.UserProfile.as_view(), name='profile'),
    # path('users_questions_list', views.UserQuestionsList.as_view(), name='user_questions_list')
]