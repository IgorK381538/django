from rest_framework import serializers
from ..models import Category, Product
from orders.models import Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
    products = ProductCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'products']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'product_name', 'price', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code',
                  'city', 'created', 'updated', 'paid', 'items']



# from shop.api.serializers import ProductSerializer, CategorySerializer, OrderItemSerializer, OrderSerializer, ProductCategorySerializer
# from shop.models import Product, Category
# from orders.models import Order, OrderItem
# from rest_framework.renderers import JSONRenderer
# subject = Order.objects.first()
# serializer = OrderSerializer(subject)
# serializer.data
