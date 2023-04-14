from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=500)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name}'


class Author(User):
    website = models.URLField()
    birth_day = models.DateField()
    death_day = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Customer(User):
    phone = PhoneNumberField(blank=True)

    def __str__(self):
        return f'{self.name}'
