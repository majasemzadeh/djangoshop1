from django_filters import FilterSet

from product.models import Category, Product


class CategoryFilter(FilterSet):
    class Meta:
        model = Product
        fields = ['pcategory']

# class ProductFilter(FilterSet):
