from django.db.models import Count
from django.shortcuts import render
from .models import Book, Category, Publisher
from shopping_basket.models import ShoppingBasket


def list_books(request):
    all_books = Book.objects.all()
    context = {'all_books': all_books}

    return render(request, 'books/all_books.html', context)


def list_category(request):
    all_category = Category.objects.all()
    context = {'all_category': all_category}

    return render(request, 'books/all_category.html', context)


def list_publisher(request):
    all_publisher = Publisher.objects.all()
    context = {'all_publisher': all_publisher}

    return render(request, 'books/all_publisher.html', context)


def list_of_author_books(request, id):
    author_books = Book.objects.filter(author=id)
    context = {'author_books': author_books}

    return render(request, 'books/author_books.html', context)


def list_of_publisher_books(request, id):
    publisher_books = Book.objects.filter(publisher=id)
    context = {'publisher_books': publisher_books}

    return render(request, 'books/publisher_books.html', context)


def list_of_category_books(request, id):
    category_books = Book.objects.filter(category=id)
    context = {'category_books': category_books}

    return render(request, 'books/category_books.html', context)


def list_of_popular_books(request):
    import itertools
    from collections import Counter

    popular_books = ShoppingBasket.objects.all()
    # popular_books = ShoppingBasket.objects.filter(book_in=Book.objects.all()).annotate(num_books=Count('id'))
    # final = popular_books
    items = [item.book.all() for item in popular_books]
    items = itertools.chain.from_iterable(items)
    final = dict(Counter(items))

    print(final)

    context = {'popular_books': final}
    return render(request, 'books/popular_books.html', context)