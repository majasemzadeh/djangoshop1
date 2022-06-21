from django.forms import forms

from order.models import Cart, CartItem


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['count', 'product', 'cart']

