from django.contrib import admin
from .models import Product, Category, Discount
# Register your models here.


admin.site.register(Discount)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pcategory']
    list_filter = ['pcategory']
    autocomplete_fields = ['pcategory',]
    search_fields = ['pcategory']


admin.site.register(Product, ProductAdmin)

admin.site.register(Category, CategoryAdmin)

# class ProductAdmin(admin.ModelAdmin):
