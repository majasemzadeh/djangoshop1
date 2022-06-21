from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.
admin.site.register(Cart)


class CartItemAdmin(admin.ModelAdmin):

    list_display = ['id', 'cart', 'product', 'count']


admin.site.register(CartItem, CartItemAdmin)