from django.contrib import admin

# Register your models here.
from customer.models import Customer, Address

admin.site.register(Address)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    list_display_links = ['id']
    search_fields = ['user']


admin.site.register(Customer, CustomerAdmin)