from django.db import models


class Customers(models.Model):
    name = models.CharField(max_length=50)
    contact_add = models.DateTimeField(auto_now_add=True)
    address = models.TextField(max_length=300)
