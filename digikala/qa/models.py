from django.db import models
from accounts.models import User
from shop.models import Product


class Question(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=2000)
    like = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)

    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


class Answer(models.Model):
    content = models.TextField(max_length=2000)
    like = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)