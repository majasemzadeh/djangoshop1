from rest_framework import serializers

from order.models import CartItem, Cart
from product.models import Product


class CartItemSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        instance.product = validated_data.get('product', instance.product)
        instance.count = validated_data.get('count', instance.count)
        instance.cart = validated_data.get('cart', instance.cart)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

    def create(self, validated_data):
        return CartItem.objects.create(**validated_data)

    id = serializers.IntegerField(read_only=True)
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all(), required=False)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    count = serializers.IntegerField(required=True)
    price = serializers.IntegerField(required=False, allow_null=True)


class CartSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        instance.customer = validated_data.get('customer', instance.customer)
        instance.address = validated_data.get('address', instance.address)
        instance.is_paid = validated_data.get('is_paid', instance.is_paid)
        instance.deleted_timestamp = validated_data.get('deleted_timestamp', instance.deleted_timestamp)
        instance.deleted_at = validated_data.get('deleted_at', instance.deleted_at)
        return instance

    def create(self, validated_data):
        return Cart.objects.create(**validated_data)

    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    address = serializers.PrimaryKeyRelatedField(read_only=True, allow_null=True, required=False)
    is_paid = serializers.BooleanField(default=False)
    discount_code = serializers.CharField(max_length=10, allow_null=True, required=False)
    created = serializers.DateTimeField(read_only=True)
    last_update = serializers.DateTimeField(read_only=True)
    deleted_timestamp = serializers.DateTimeField(required=False, allow_null=True)
    deleted_at = serializers.DateTimeField(required=False, allow_null=True)
