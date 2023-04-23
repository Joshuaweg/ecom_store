from django.shortcuts import render
from .models import Product

from orders.models import CartProductTable,Cart # to add 'cart': cart 


# Create your views here.
#this is th Product List View
def product_list(request):  # Rename is necessary
    all_products = Product.objects.all()
    
    if request.user.is_authenticated:
        cart = Cart.objects.get(associated_user=request.user.id)
        cartList=CartProductTable.objects.get(associated_cart=cart.id)
        
        return render(request, 'products/product_list.html', {'products': all_products, 'cart': cart})
    else:
        return render(request, 'products/product_list.html', {'products': all_products}) #add 'cart':cart
    
#this is the product page View
def product_page(request):
    all_products = Product.objects.all()
    print(request.GET)  # previous commit
    product = Product.objects.get(pk=request.GET.get("id"))

    if request.user.is_authenticated:
        cart = Cart.objects.get(associated_user=request.user.id)
        cartList=CartProductTable.objects.get(associated_cart=cart.id)

        return render(request,'products/product_page.html',{'product':product ,'cart': cart})
    else:
        return render(request,'products/product_page.html',{'product':product})#add 'cart':cart

# ORIGINAL CODE BEFORE THE IF/ELSE BLOCK
#def product_list(request):  # Rename is necessary
#    all_products = Product.objects.all()
#    return render(request, 'products/product_list.html', {'products': all_products}) #add 'cart':cart
##this is the product page View
#def product_page(request):
#    print(request.GET)
#    product = Product.objects.get(pk=request.GET.get("id"))
#    return render(request,'products/product_page.html',{'product':product})#add 'cart':cart



#    if request.user.is_authenticated :
#        cart = Cart.objects.get(associated_user=request.user.id)
#        cartList=CartProductTable.objects.get(associated_cart=cart.id)
#        return render(request,'home/index.html',{'today':datetime.today(),"cart":cartList}) #add 'cart':cart
#    else:
#        return render(request,'home/index.html',{'today':datetime.today()})