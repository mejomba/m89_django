from django.db import models
from core.models import BaseModel, User


class Post(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=4000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField('Category', related_name='sub_category_post', null=True, blank=True)


class Category(BaseModel):
    name = models.CharField(max_length=255)
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='category', null=True, blank=True)