from typing import Generic

from django.shortcuts import render

# Create your views here.
from django.views import View
# from django.views.generic.list import ListView
from django.views.generic import DetailView, ListView

from .filters import CategoryFilter
from .models import Product, Discount, Category
from order.models import Cart, CartItem


class ProductDetail(DetailView):
    model = Product
    template_name = 'product1.html'


class ProductList(ListView):
    model = Product
    template_name = 'products.html'


class ProductCategory(View):
    def get(self, request, category_slug):
        category = Category.objects.get(category_slug=category_slug)
        products = Product.objects.all()
        list_products = []
        for product in products:
            if product.pcategory == category:
                list_products.append(product)
        return render(request, 'category.html', {'products': list_products})



def category(request):
    if request.method == "GET":
        categorys = Category.objects.all()
        products = Product.objects.all()
        categorylist = []
        for category in categorys:
            category.name = []
            for product in products:
                if product.pcategory == category:
                    category.name.append(product)

            categorylist.append(category.name)

        contex = {'categorys': categorylist}
        render(request, 'categury.html', context=contex)
