from django.shortcuts import render
from .models import ShoppingBasket

import itertools


def list_of_user_bought_books(request, id):
    user_bought_books = ShoppingBasket.objects.filter(customer=id)
    bought_books = [item.book.all() for item in user_bought_books]

    bought_books = itertools.chain.from_iterable(bought_books)
    # bought_books = set(bought_books)

    context = {'user_bought_books': bought_books}

    return render(request, 'shopping_basket/user_bought_books.html', context)
