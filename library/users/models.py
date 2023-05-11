from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    address = models.TextField(max_length=500)
    phone = PhoneNumberField(blank=True)
    website = models.URLField(null=True, blank=True)
    birth_day = models.DateField(null=True, blank=True)
    death_day = models.DateField(null=True, blank=True)
    is_author = models.BooleanField(default=False, verbose_name='نویسنده است')
    is_customer = models.BooleanField(default=False, verbose_name='مشتری است', editable=False)

    def __str__(self):
        return f'{self.username}'


# class Author(User):
#     website = models.URLField()
#     birth_day = models.DateField()
#     death_day = models.DateField(null=True, blank=True)
#
#     def __str__(self):
#         return f'{self.username}'


# class Customer(User):
#     phone = PhoneNumberField(blank=True)
#
#     def __str__(self):
#         return f'{self.username}'
