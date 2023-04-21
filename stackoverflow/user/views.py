from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import User


class CreateUser(generic.CreateView):
    model = User
    fields = ['username', 'email', 'password', 'first_name', 'last_name']
    # fields = '__all__'
    template_name = 'user/create_user.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.id})


class UserProfile(generic.DetailView):
    model = User
    template_name = 'user/profile.html'


# class UserQuestionsList(generic.ListView):
#
#     model = User
#     template_name = 'user/users_questions_list.html'
#     context_object_name = 'users'
#
#     def get_queryset(self):
#         from django.db.models import F
#         users = User.objects.filter()
#         data = User.objects.filter().annotate(
#             question__user=F('question__user')
#         )
#         data = User.objects.all().select_related('Question')
#         print(data)
#         return data
