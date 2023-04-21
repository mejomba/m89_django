from django.db import models
from django.db.models import Count

from user.models import User


class QuestionManager(models.Manager):
    def question_with_two_answers(self):
        # data = Answer.objects.annotate(answer_count=Count('question')).filter(answer_count__gte=2).order_by('-answer_count')
        data = self.annotate(answer_count=Count('answer')).filter(answer_count__gte=2)
        print(data)
        return data


class Question(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    content = models.TextField(max_length=2000, verbose_name='متن سوال')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title}'

    objects = QuestionManager()


class Answer(models.Model):
    content = models.TextField(max_length=2000, verbose_name='متن پاسخ')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.question.title}'
