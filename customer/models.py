from django.db import models

# Create your models here.
from core.models import Myuser, BaseModel


class Customer(models.Model):
    user = models.OneToOneField(Myuser, on_delete=models.CASCADE, related_name='customer', related_query_name='customer')

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'

    @property
    def cartitem_count(self):
        count = 0
        cart = self.cart.get(is_paid=False)

        return cart.cartitem_count

    def __str__(self):
        return self.user.username


class Address(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    address = models.TextField()

    class Meta:
        verbose_name = 'ادرس'
        verbose_name_plural = 'ادرس ها'