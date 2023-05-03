from importlib.metadata import requires
from wsgiref.util import request_uri
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from products.models import Product
from .models import Cart, CartProductTable, Order
from credit_cards.models import CreditCard, UserCreditCard
# Create your views here.
def order(request):  # Rename is necessary
    cart=Cart.objects.get(pk=request.GET.get("cart"))
    items = CartProductTable.objects.filter(associated_cart=cart)
    total = 0.0
    for item in items:
        total+=item.product.price
    return render(request, 'orders/index.html',{'items':items,'cart':cart,'total':total})
def AddtoCart(request):  # Rename is necessary
    print(request.POST)
    cart=request.POST['cart']
    prod=Product.objects.get(pk=request.POST['id'])
    count=request.POST['count']
    print(cart,prod,count)
    cartItem = CartProductTable(product=prod,productQuantity=count,associated_cart_id=cart)
    cartItem.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
def CompleteCheckout(request):  # Rename is necessary
    print(request.POST)
    cart=request.POST['cart_id']
    cart=Cart.objects.get(pk=cart)
    cartItems=CartProductTable.objects.filter(associated_cart=cart)
    ship_name=request.POST['name']
    ship_address=request.POST['address1']
    ship_address2=request.POST['address2']
    ship_city=request.POST['city']
    ship_state=request.POST['state']
    ship_zipcode=request.POST['zipcode']
    

    creditcard = CreditCard.objects.get(credit_card_number=request.POST["CreditCardNumber"])
    if(creditcard):
        UserCred = UserCreditCard.objects.filter(user_id=request.user.id).filter(credit_card=creditcard)
        if(UserCred):
            pass
        else:
            UseCC=UserCreditCard(user_id=request.user,credit_card=creditcard)
            UseCC.save()
        for item in cartItems:
            ordered_item =Order(associated_user=request.user,product=item.product,shipping_name=ship_name,shipping_address=ship_address,shipping_address_2=ship_address2,city=ship_city,state=ship_state,zip_code=ship_zipcode,credit_card=creditcard)
            ordered_item.save()
            item.delete()
    else:
        credit=CreditCard(credit_card_number=request.POST["CreditCardNumber"],experation_date=request.POST['exprdate'],cvv=request.POST['CVV'])
        credit.save()
        UseCC=UserCreditCard(user_id=request.user,credit_card=credit)
        UseCC.save()
        for item in cartItems:
            ordered_item =Order(associated_user=request.user,product=item.product,shipping_name=ship_name,shipping_address=ship_address,shipping_address_2=ship_address2,city=ship_city,state=ship_state,zip_code=ship_zipcode,credit_card=creditcard)
            ordered_item.save()
            item.delete()
    return HttpResponseRedirect("../email_confirmation")
def RemovefromCart(request):  # Rename is necessary
    print(request.POST)
    cart=request.POST['cart']
    prod=Product.objects.get(pk=request.POST['id'])
    count=request.POST['count']
    print(cart,prod,count)
    cartItem = CartProductTable.objects.filter(associated_cart=request.POST['cart'],product=request.POST['id'])
    if(len(cartItem)>0):
        cartItem.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])