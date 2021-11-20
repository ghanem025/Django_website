from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import datetime

import uuid
# Create your models here.
# models are for the back-end, they let you change the fields of the objects you are
#storing in the django admin database

class Customer(models.Model):
    # eyw_transactionref=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null= True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(blank=True,null=True)
    date_added = models.DateField(default = datetime.date.today)

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=1000)
    summary = models.TextField(default='this is a summary', null=True)
    stock = models.DecimalField(default=0, decimal_places=0, max_digits=1000000)
    featured = models.BooleanField(default=True)
    email = models.EmailField(blank=True, null=True)
    def get_dynamic_urls(self):#instances method
        return reverse("website:product-detail",kwargs={"my_id":self.id})

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    num_employees = models.DecimalField(decimal_places=0, max_digits=1000)
    summary = models.TextField(default='this is a summary', null=True)
