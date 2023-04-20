from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from orders.models import CartProductTable,Cart
# Create your views here.
def home(request):
    if request.user.is_authenticated :
        cart = Cart.objects.get(associated_user=request.user.id)
        cartList=CartProductTable.objects.get(associated_cart=cart.id)
        return render(request,'home/index.html',{'today':datetime.today(),"cart":cartList}) #add 'cart':cart
    else:
        return render(request,'home/index.html',{'today':datetime.today()})