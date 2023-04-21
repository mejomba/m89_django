from django.db.models import Count
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Question, Answer
from user.models import User


class Home(generic.ListView):
    model = Question
    template_name = 'qa/home.html'
    context_object_name = 'questions'


class CreateQuestion(generic.CreateView):
    model = Question
    fields = '__all__'
    template_name = 'qa/create_question.html'

    def get_success_url(self):
        return reverse_lazy('home')


class CreateAnswer(generic.CreateView):
    model = Answer
    fields = '__all__'
    template_name = 'qa/create_answer.html'

    def get_success_url(self):
        return reverse_lazy('home')


class QuestionDetail(generic.DetailView):

    model = Question
    template_name = 'qa/question_detail.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answers = Answer.objects.filter(question_id=self.kwargs.get('pk'))
        context['answers'] = answers
        return context


class AnswerList(generic.ListView):
    def get_queryset(self):
        pass


class UserQuestionsList(generic.ListView):

    template_name = 'user/users_questions_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        data = User.objects.filter(question__user__is_active=True)
        print(data)
        return data


class UserMostAnsweredList(generic.ListView):

    template_name = 'qa/user_most_answered_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        data = User.objects.annotate(answer_count=Count('answer')).filter(answer_count__gte=1).order_by('-answer_count')
        return data


class QuestionDetailPaginate(generic.ListView):

    template_name = 'qa/question.html'
    context_object_name = 'answers'
    paginate_by = 1

    def get_queryset(self, **kwargs):
        answers = Answer.objects.filter(question__id=self.kwargs['pk'])
        print(answers)
        return answers

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        question = Question.objects.get(pk=self.kwargs['pk'])
        context['question'] = question
        return context


class QuestionWithTwoAnswers(generic.ListView):

    template_name = 'qa/question_with_two_answers.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.question_with_two_answers()


class QuestionUpdate(generic.UpdateView):
    template_name = 'qa/question_update.html'
    model = Question
    fields = '__all__'

    success_url = reverse_lazy('home')


class QuestionDelete(generic.DeleteView):
    template_name = 'qa/question_delete.html'
    model = Question

    success_url = reverse_lazy('home')


class Search(generic.ListView):

    template_name = 'qa/search_result.html'
    context_object_name = 'questions'

    def get_queryset(self, **kwargs):
        questions = Question.objects.filter(Q(title__contains=self.request.GET['query']) | Q(content__contains=self.request.GET['query']))
        return questions

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        answers = Answer.objects.filter(content__contains=self.request.GET['query'])
        context['answers'] = answers
        return context
