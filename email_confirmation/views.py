from django.shortcuts import render
from django.core.mail import send_mail
from orders.models import Cart, CartProductTable

# Create your views here.

def email_confirmation(request):  # Rename is necessary
    if request.user.is_authenticated:
        cart = Cart.objects.get(associated_user=request.user.id)
        cartList=CartProductTable.objects.filter(associated_cart=cart.id)
    print(request.user.email)
    send_mail(
        "Order Confirmation",
        "Here is the confirmation for your order",
        "donotreply_confirmation@azecommerce.com",
        [request.user.email],fail_silently=False,)

    return render(request, 'email_confirmation/index.html',{'cart':cart,'cartList':cartList}) # html template goes here
