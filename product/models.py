from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Category(BaseModel):
    name = models.CharField(max_length=64)
    ccategory = models.ManyToManyField('self', null=True, blank=True)
    category_slug = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی'

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=64)
    image = models.FileField(null=True)
    price = models.PositiveIntegerField()
    pcategory = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    brand = models.CharField(max_length=64, null=True, blank=True)
    amount = models.PositiveIntegerField()
    slug = models.CharField(max_length=64, unique=True)
    description = models.TextField(null=True, blank=True)
    # discount = models.PositiveIntegerField(null=True, blank=True)
    product_property = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name


class Discount(models.Model):
    amount = models.IntegerField(null=True, blank=True)
    discount_cod = models.CharField(max_length=10, null=True)
    dcategory = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    dproduct = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='discount' ,related_query_name='discount')
    percentage = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'تخفیف'
        verbose_name_plural = 'تخفیفات'

    def aplly_discount(self):

        if self.dproduct and self.percentage:
            discountprice= self.dproduct.price * (self.percentage)
            return float(discountprice)


    # def __str__(self):
    #     return self.aplly_discount


class Comments(BaseModel):
    name = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField()
    comment = models.TextField(null=True, blank=True)