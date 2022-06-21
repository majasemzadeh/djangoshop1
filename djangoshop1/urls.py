"""djangoshop1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import Home
from customer.views import LoginView, logout_view
from customer.views import SingUp
from order.views import CartItemAPI, ShowCart, remove_cartitem, empty_car, Checkout
from product.views import ProductCategory


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('singup/', SingUp.as_view(), name='sing_up'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('category/<category_slug>', ProductCategory.as_view(), name='categoryproducts'),
    path('add-cartitem/', CartItemAPI.as_view(), name='add_cartitem'),
    path('cart/', ShowCart.as_view(), name='cart'),
    path('remove_cartitem/', remove_cartitem, name='remove_cartitem'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('empty/', empty_car, name='empty_cart'),
    path('products/', include("product.url")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)
