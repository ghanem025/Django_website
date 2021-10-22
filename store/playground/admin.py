from django.contrib import admin
from .models import Product #this is called a relative import
from .models import Store
# Register your models here.

admin.site.register(Product)
admin.site.register(Store)
