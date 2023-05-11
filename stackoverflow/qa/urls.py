from django.urls import path
from . import views


urlpatterns = [
    path('create_question', views.CreateQuestion.as_view(), name='create_question'),
    path('create_answer', views.CreateAnswer.as_view(), name='create_answer'),
    path('question_detail-<int:id>', views.QuestionDetail.as_view(), name='question_detail'),
    path('users_questions_list', views.UserQuestionsList.as_view(), name='user_questions_list'),
    path('users_most_answered_list', views.UserMostAnsweredList.as_view(), name='users_most_answered_list'),
    path('question-<int:pk>/', views.QuestionDetailPaginate.as_view(), name='question_detail_paginate'),
    path('question_with_two_answers', views.QuestionWithTwoAnswers.as_view(), name='question_with_two_answers'),
    path('question_update-<int:pk>', views.QuestionUpdate.as_view(), name='question_update'),
    path('question_delete-<int:pk>', views.QuestionDelete.as_view(), name='question_delete'),
    path('search', views.Search.as_view(), name='search'),
]