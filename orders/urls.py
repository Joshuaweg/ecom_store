from django.urls import path

from . import views 

urlpatterns = [
    path('orders', views.order),
    path('orders/AddtoCart', views.AddtoCart),
    path('orders/checkout', views.CompleteCheckout),
]