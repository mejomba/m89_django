from django.shortcuts import render
from .models import Customer, Author


def list_customers(request):
    all_customers = Customer.objects.all()

    context = {'all_customers': all_customers}

    return render(request, 'users/all_customers.html', context)


def list_authors(request):
    all_authors = Author.objects.all()

    context = {'all_authors': all_authors}

    return render(request, 'users/all_authors.html', context)

