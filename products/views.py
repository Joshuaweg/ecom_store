from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):  # Rename is necessary

    # Store all products in our database
    all_products = Product.objects.all()

    return render(request, 'products/product_list.html', {'products': all_products})

    # return render(request, 'Name of html file goes here product.html', {'products': all_products})