from django.shortcuts import render
from orders.models import CartProductTable, Cart # If not here, then CartProductTable gives error


# Create your views here.
def order(request):  # Rename is necessary
    if request.user.is_authenticated :
        cart=CartProductTable.objects.get(pk=request.GET.get("id"))
        cartList=CartProductTable.objects.get(associated_cart=cart.id) 
        return render(request, 'orders/index.html', {"cart":cartList}) # Does this datetime?
    else:
         return render(request, 'orders/index.html')
def AddtoCart(request):  
        # This Funcsiton is For Joshua to work on
        cart=CartProductTable.objects.get(pk=request.GET.get("id"))
        cartList=CartProductTable.objects.get(associated_cart=cart.id) # Does this need to be here?
        # Does this need statement?

# ORIGINAL CODE:
# def order(request):  # Rename is necessary
#    cart=CartProductTable.objects.get(pk=request.GET.get("id"))
#    return render(request, 'orders/index.html')
# def AddtoCart(request):  # Rename is necessary
#    cart=CartProductTable.objects.get(pk=request.GET.get("id")) 

#    if request.user.is_authenticated :
#        cart = Cart.objects.get(associated_user=request.user.id)
#        cartList=CartProductTable.objects.get(associated_cart=cart.id)
#        return render(request,'home/index.html',{'today':datetime.today(),"cart":cartList}) #add 'cart':cart
#    else:
#        return render(request,'home/index.html',{'today':datetime.today()})    
    