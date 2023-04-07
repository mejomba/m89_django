from django.db import models
from users.models import Customers


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_type = models.CharField(max_length=50)


class Products(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class ShoppingOrder(models.Model):
    order_id = models.AutoField(primary_key=True, editable=False)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Seller(models.Model):
    name = models.CharField(max_length=50)
    product_id = models.ManyToManyField(Products)
