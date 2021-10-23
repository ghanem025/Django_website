from django.contrib import admin
from .models import Product #this is called a relative import
from .models import Store
from .models import Customer
# Register your models here.

admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Customer)
