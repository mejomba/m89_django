from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    # phone = models.CharField(max_length=11)
    # created_at = models.DateTimeField(auto_now_add=True)
    # last_update = models.DateTimeField(auto_now=True)
    # image = models.ImageField(upload_to='images/user')
    # role = models.CharField([('u', 'user'), ('w', 'writer'), ('a', 'admin')])


class UserRequest(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    request_name = models.CharField(max_length=25)
    status = models.CharField(choices=[('pe', 'pending'), ('pu', 'published'), ('re', 'reject'), ('dr', 'draft')], max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user_id', 'request_name', 'status')


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
