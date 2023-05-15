from django.shortcuts import render
from .models import Product
from django.db.models import Q
from orders.models import CartProductTable,Cart # to add 'cart': cart 


# Create your views here.
#this is th Product List View
def product_list(request):  # Rename is necessary
    search = request.GET.get("search","")
    if(search == ''):
        all_products = Product.objects.exclude(pk=12)
    else:
        all_products = Product.objects.filter(Q(title__contains=search)|Q(description__contains=search))
        if(len(all_products)==0):
            all_products = Product.objects.exclude(pk=12)
    if request.user.is_authenticated:
        cart = Cart.objects.get(associated_user=request.user.id)
        cartList=CartProductTable.objects.filter(associated_cart=cart.id)
        
        return render(request, 'products/product_list.html', {'products': all_products, 'cartList': cartList,'cart':cart})
    else:
        return render(request, 'products/product_list.html', {'products': all_products}) #add 'cart':cart
    
#this is the product page View
def product_page(request):
    all_products = Product.objects.all()
    print(request.GET) 
    try:
        product = Product.objects.get(pk=request.GET.get("id"))
        print(product)
        if request.user.is_authenticated:
            cart = Cart.objects.get(associated_user=request.user.id)
            print(cart)
            print(cart.id)
            cartList=CartProductTable.objects.filter(associated_cart=cart.id)

            return render(request,'products/product_page.html',{'product':product,'cart': cart.id,'cartList':cartList})
        else:
            return render(request,'products/product_page.html',{'product':product})#add 'cart':cart
    except Exception as e:
        print(e)
        return render(request,'products/product_page.html',{'product':None})

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