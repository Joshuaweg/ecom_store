from django.shortcuts import render
from .models import Product
from django.contrib.staticfiles import settings
import os

# Create your views here.
def product_list(request):  # Rename is necessary

    # Store all products in our database
    all_products = Product.objects.all()
    #cart = Cart.objects.get(userid=request.GET.get("User"))
    return render(request, 'products/product_list.html', {'products': all_products}) #add 'cart':cart

def product_page(request):
    print(request.GET)
    #cart = Cart.objects.get(userid=request.GET.get("User"))
    product = Product.objects.get(pk=request.GET.get("id"))
    return render(request,'products/product_page.html',{'product':product})#add 'cart':cart