from django.db import models
from users.models import User
from books.models import Book


class ShoppingBasket(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book, related_name='shoppingbasket_book')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False)

    def __str__(self):
        return f'{self.customer.username}'
