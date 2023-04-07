from django.db import models
from users.models import Customers


class Deliveries(models.Model):
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
