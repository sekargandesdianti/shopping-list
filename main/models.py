from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField(max_length=1000)