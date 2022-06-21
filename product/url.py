from django.urls import path
from .views import *

app_name = "products"
urlpatterns = [
    path('products/', ProductList.as_view(), name='list_product'),
    path('<slug>/', ProductDetail.as_view(), name='product'),

    # path('category/<categuryslug>/')


]