from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'shop'


router = routers.DefaultRouter()
router.register('shop', views.OrderViewSet)


urlpatterns = [
    path('products/',
         views.ProductListView.as_view(),
         name='product_list'),
    path('products/<pk>/',
         views.ProductDetailView.as_view(),
         name='product_detail'),
    path('', include(router.urls)),
]