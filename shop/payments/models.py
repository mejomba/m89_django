from django.db import models
from supermarket.models import Category
from users.models import Customers
from supermarket.models import ShoppingOrder, Products


class Payment(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


class TransactionReports(models.Model):
    report_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    order_id = models.ForeignKey(ShoppingOrder, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)