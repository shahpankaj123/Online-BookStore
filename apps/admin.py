from django.contrib import admin
from .models import Product, Order,Contact,OrderItem,Cart,CartItem


# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Contact)
admin.site.register(CartItem)
admin.site.register(Cart)

