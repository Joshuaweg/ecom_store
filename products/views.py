from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):  # Rename is necessary

    # Store all products in our database
    all_products = Product.objects.all()

    return render(request, 'products/product_list.html', {'products': all_products})

def product_page(request):
    print(request.GET)
    product = Product.objects.get(pk=request.GET.get("id"))
    return render(request,'products/product_page.html',{'product':product})