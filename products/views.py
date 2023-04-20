from django.shortcuts import render
from .models import Product

# Create your views here.
#this is th Product List View
def product_list(request):  # Rename is necessary

    
    all_products = Product.objects.all()
  
    return render(request, 'products/product_list.html', {'products': all_products}) #add 'cart':cart
#this is the product page View
def product_page(request):
    print(request.GET)
    product = Product.objects.get(pk=request.GET.get("id"))
    return render(request,'products/product_page.html',{'product':product})#add 'cart':cart