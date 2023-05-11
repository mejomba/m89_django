from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
from .models import User
from shopping_basket.models import ShoppingBasket


def home(request):
    return render(request, 'users/home.html')


def profile(request):
    books = ShoppingBasket.objects.filter(customer=request.user)

    context = {'books': []}
    for shopping in books:
        # context['books'].extend(shopping.book.all())
        context['books'].append(shopping.book.all())
    return render(request, 'users/profile.html', context)


def list_customers(request):
    all_customers = User.objects.filter(is_customer=True)

    context = {'all_customers': all_customers}

    return render(request, 'users/all_customers.html', context)


def list_authors(request):
    all_authors = User.objects.filter(is_author=True)

    context = {'all_authors': all_authors}

    return render(request, 'users/all_authors.html', context)


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
