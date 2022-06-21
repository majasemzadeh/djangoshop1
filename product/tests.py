from django.test import TestCase
from .models import Discount, Product
# Create your tests here.


class DiscountTest(TestCase):
    def setUp(self) -> None:
        self.product1 = Product.objects.create(name='kif', price=3000)
        self.discount1 = Discount.objects.create(discount_cod='1234', dproduct=self.product1, percentage=0.1)

    def test1_apply_discount(self):
        self.assertEqual(self.discount1.apply_discount(), 300)