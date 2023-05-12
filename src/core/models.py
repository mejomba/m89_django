from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel, AbstractUser):
    choice = (('a', 'admin'), ('u', 'user'))
    role = models.CharField(verbose_name='نقش کاربری', choices=choice, max_length=1, null=True, blank=True, default='u')
