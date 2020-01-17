from rest_framework import generics
from ..models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from orders.models import Order
from rest_framework import viewsets
from .serializers import OrderSerializer
from rest_framework.decorators import action


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(methods=['get'],
            serializer_class=OrderSerializer,
            detail=True)
    def products(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
