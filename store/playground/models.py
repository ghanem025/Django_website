from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=1000)
    summary = models.TextField(default='this is a summary', null=True)
    featured = models.BooleanField(default=True)


class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    num_employees = models.DecimalField(decimal_places=0, max_digits=1000)
    summary = models.TextField(default='this is a summary', null=True)
