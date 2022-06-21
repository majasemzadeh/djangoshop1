from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from core.models import Myuser
from customer.models import Customer, Address
from order.models import CartItem, Cart
from order.serializer import CartSerializer, CartItemSerializer
from product.models import Product


# @api_view(['POST', 'GET'])
# def OrderRegistration(request):
#     data = request.POST
#     print(data)
#     cartitem_serializer = CartItemSerializer(data=data)
#     if cartitem_serializer.is_valid():
#         if request.user.is_authenticated:
#             user = request.user
#         customer = Customer.objects.get(user=user)
#         cart = Cart.objects.get_or_create(customer=customer, is_paid=False)
#         new_serializer = CartItemSerializer(data=data)
#         if new_serializer.is_valid():
#             no = new_serializer.save()
#             print(type(cart))
#             sdf = CartItemSerializer(instance=no,
#                                      data={'cart': 4, 'product': data['product'], 'count': data['count']})
#             if sdf.is_valid():
#                 sdf.save()
#                 return JsonResponse({'new cart': no.product})
#         else:
#             return JsonResponse({'new cart': 'error'}, status=400)
#     else:
#         return JsonResponse({'error': cartitem_serializer.errors})


from django.db.backends.postgresql.features import DatabaseFeatures

DatabaseFeatures.can_defer_constraint_checks = False


class CartItemAPI(APIView):
    def post(self, request):
        data = request.data
        print(data)
        if 'cart' in data.keys():
            cart = Cart.objects.get(id=data['cart'])
            cart_item = CartItem.objects.get(id=data['product'])
            data = {'product': cart_item.product.id, 'count':data['count'], 'cart': data['cart']}
            cartitem_serializer = CartItemSerializer(instance=cart_item, data=data)
            if cartitem_serializer.is_valid():
                cartitem_serializer.save()
                return HttpResponse('success')
            else:
                print({'error': cartitem_serializer.errors})
                return JsonResponse({'error': cartitem_serializer.errors})
        else:
            print(123)
            if request.user.is_authenticated:
                user = request.user
                print(user.username)
            customer = Customer.objects.get(user=user)
            print(1)
            cart = Cart.objects.get_or_create(customer=customer, is_paid=False)[0]
            print(cart)

            new_serializer = CartItemSerializer(data=data)
            if new_serializer.is_valid():
                no = new_serializer.save()
                cartid = cart.id

                sdf = CartItemSerializer(instance=no,
                                         data={'cart': cart.id, 'product': data['product'], 'count': data['count'],
                                               'price': data['price']})

                if sdf.is_valid():
                    sdf.save()
                    print({'new cart': no.product})
                    return JsonResponse({'new cart': no.product})
                else:
                    print({'new cart': sdf.errors})
                    return JsonResponse({'new cart': sdf.errors})
            else:
                print({'new cart': 'error'})
                return JsonResponse({'new cart': 'error'}, status=400)


class ShowCart(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            # print(user.customer.cart)
            customer = Customer.objects.get(user=user)
            try:
                cart = Cart.objects.get(customer=customer, is_paid=False)
                cartitems = CartItem.objects.filter(cart=cart)
                addresses = Address.objects.filter(customer=customer)
                print(addresses)
                context = {'cart': cart, 'cartitems': cartitems, "addresses":addresses}
                return render(request, 'cartpage.html', context=context)
            except ObjectDoesNotExist:
                return render(request, 'cartpage.html')

    def post(self, request):
        user = request.user
        customer = Customer.objects.get(user=user)
        cart = Cart.objects.get(customer=customer, is_paid=False)
        cart.is_paid = True
        cart.save(update_fields=['is_paid'])
        return HttpResponse('buy success')


@api_view(['POST'])
def remove_cartitem(request):
    data = request.data
    cart_item = CartItem.objects.get(id=data['id'])
    cart_item.delete()
    return HttpResponse('remove success')


@api_view(['POST'])
def empty_car(request):
    data = request.data
    cart = Cart.objects.get(id=data['cart'])
    cart_itmes = CartItem.objects.filter(cart=cart)
    for cart_item in cart_itmes:
        cart_item.delete()
    return HttpResponse('remove success')


class Checkout(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            # print(user.customer.cart)
            customer = Customer.objects.get(user=user)
            cart = Cart.objects.get(customer=customer, is_paid=False)
            cartitems = CartItem.objects.filter(cart=cart)
            addresses = Address.objects.filter(customer=customer)
            print(addresses)
            context = {'cart': cart, 'cartitems': cartitems, "addresses": addresses}
            return render(request, 'checkout.html', context=context)