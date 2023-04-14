from django.db import models
from users.models import Customer
from books.models import Book


class ShoppingBasket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book, related_name='shoppingbasket_book')

    def __str__(self):
        return f'{self.customer.name}'
