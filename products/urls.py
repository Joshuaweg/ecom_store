from django.urls import path

from . import views 

urlspatterns = [
    path('products', views.product_list)
]