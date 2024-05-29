from django.urls import path
from shop.views import orders
from shop.views import catalog
from shop.views import order_create


urlpatterns = [
    path('orders/',orders),
    path('catalog/',catalog),
    path('order_create/',order_create),
]

