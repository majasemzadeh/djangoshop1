from django.db import models
from core.models import BaseModel
from customer.models import Customer, Address
from product.models import Product, Discount
# Create your models here.


class Cart(BaseModel):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, related_name='cart', related_query_name='cart')
    address = models.OneToOneField(to=Address, on_delete=models.SET_NULL, null=True)
    is_paid = models.BooleanField(default=False)
    discount_code = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد خرید'

    @property
    def cartitem_count(self):
        count = 0
        for cartitem in self.cartitems:
            count += 1

        return count

    @property
    def total_price(self):
        total = 0
        for cart_item in self.cartitems.all():
            final_price = cart_item.price
            for discount in Discount.objects.all():
                if discount.dproduct == cart_item.product:
                    final_price = final_price - discount.amount
            total += (final_price * cart_item.count)

        for discount in Discount.objects.all():
            if discount.discount_cod == self.discount_code:
                discount = Discount.objects.get(discount_cod=self.discount_code)
                if discount.percentage:
                    total = total * discount.percentage
                if discount.amount:
                    total = total - discount.amount

        return int(total)

    # def __str__(self):
    #         if self.total_price != None:
    #             return self.total_price
    #         else:
    #             return self.customer


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField(null=True)

    @property
    def total_price(self):

        total = self.price * self.count
        return int(total)

    def __str__(self):
        return f'{self.product.name}, {self.count}'