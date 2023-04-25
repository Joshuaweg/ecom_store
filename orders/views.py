from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import products.models
from .models import Cart, CartProductTable
# Create your views here.
def order(request):  # Rename is necessary
    cart=Cart.objects.get(pk=request.GET.get("id"))
    return render(request, 'orders/index.html')
def AddtoCart(request):  # Rename is necessary
    cart=Cart.objects.get(pk=request.POST.get("cart"))
    prod=products.objects.get(pk=request.POST.get("id"))
    count=request.POST.get("count")
    cartItem = CartProductTable(prod,count,cart)
    cartItem.save()
    return HttpResponseRedirect(request.path_info)