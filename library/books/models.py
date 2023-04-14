from django.db import models
from users.models import Author
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator


class Book(models.Model):
    name = models.CharField(max_length=100)
    pages = models.IntegerField()
    weight = models.FloatField()
    price = models.PositiveIntegerField(null=True, blank=True)
    discount = models.ForeignKey('Discount', on_delete=models.CASCADE, null=True, blank=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    category = models.ManyToManyField('Category', related_name='book_category')
    author = models.ManyToManyField(Author, related_name='book_author')

    @property
    def totaly(self):
        if self.discount:
            return self.price - ((self.discount.percent/100) * self.price)
        return self.price

    def __str__(self):
        return f'{self.name}'


class Discount(models.Model):
    name = models.CharField(max_length=20)
    percent = models.PositiveIntegerField(validators=[RegexValidator(r'^[1-9][0-9]?$|^100$', message='0 - 100')])

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=50)
    category_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Publisher(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(max_length=500)
    phone = PhoneNumberField(blank=True)
    website = models.URLField()

    def __str__(self):
        return f'{self.name}'
