from django.test import TestCase
from .models import Discount, Product
from .models import Cart, CartItem
# Create your tests here.


class CartTest(TestCase):
    def setUp(self) -> None:
        self.product1 = Product.objects.create(name='kif', price=3000)
        self.discount1 = Discount.objects.create(discount_cod='1234', dproduct=self.product1, percentage=0.2)
        self.product2 = Product.objects.create(name='kafsh', price=4000)
        self.product3 = Product.objects.create(name='shalvar', price=200)
        self.product4 = Product.objects.create(name='saat', price=500)
        self.discount2 = Discount.objects.create(discount_cod='code1', percentage=0.6)
        self.discount3 = Discount.objects.create(discount_cod='23', dproduct=self.product2, integer=400)
        self.discount4 = Discount.objects.create(discount_cod='code2', integer=5000)
        self.cart1 = Cart.objects.create()
        self.cart2 = Cart.objects.create()
        self.cart3 = Cart.objects.create(discount_code='code1')
        self.cart4 = Cart.objects.create(discount_code='code2')
        self.cart5 = Cart.objects.create()
        self.cartitem1 = CartItem.objects.create(cart=self.cart5, product=self.product1, count=4)
        self.cartitem2 = CartItem.objects.create(cart=self.cart5, product=self.product2, count=3)
        self.cartitem3 = CartItem.objects.create(cart=self.cart5, product=self.product3, count=2)
        self.cartitem4 = CartItem.objects.create(cart=self.cart4, product=self.product1, count=4)
        self.cartitem5 = CartItem.objects.create(cart=self.cart4, product=self.product2, count=3)
        self.cartitem6 = CartItem.objects.create(cart=self.cart4, product=self.product3, count=2)
        self.cartitem7 = CartItem.objects.create(cart=self.cart3, product=self.product1, count=4)
        self.cartitem8 = CartItem.objects.create(cart=self.cart3, product=self.product2, count=3)
        self.cartitem8= CartItem.objects.create(cart=self.cart3, product=self.product3, count=2)
        self.cartitem10 = CartItem.objects.create(cart=self.cart2, product=self.product3, count=2)
        self.cartitem11 = CartItem.objects.create(cart=self.cart2, product=self.product4, count=2)
        self.cartitem12 = CartItem.objects.create(cart=self.cart1, product=self.product4, count=3)

    def test_total_price(self):
        self.assertEqual(self.cart1.total_price, 1500)
        self.assertEqual(self.cart2.total_price, 1400)
        self.assertEqual(self.cart3.total_price, 14640)
        self.assertEqual(self.cart4.total_price, 19400)
        self.assertEqual(self.cart5.total_price, 24400)