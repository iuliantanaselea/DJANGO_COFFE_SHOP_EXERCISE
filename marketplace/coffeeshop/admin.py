from django.contrib import admin
from .models import User, Product, Order, Home
# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Home)
