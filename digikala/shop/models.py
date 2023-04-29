from django.db import models
from accounts.models import User
import jsonfield


class ShoppingBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ManyToManyField('Product')

    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=250)
    count = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    image = models.FileField(null=True)
    # json_data = jsonfield.JSONField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey('self', on_delete=models.PROTECT, related_name='shop_category')

    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=2000)
    like = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='shop_comment')

    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

