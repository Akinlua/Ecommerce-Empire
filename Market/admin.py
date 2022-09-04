from django.contrib import admin
from .models import Store, Cart, Category, Items, Order
# Register your models here.

admin.site.register(Store)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Items)
admin.site.register(Order)
