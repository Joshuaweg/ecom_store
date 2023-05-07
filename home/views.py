from datetime import datetime
from os.path import lexists
from orders.models import CartProductTable,Cart
from orders import models
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def home(request):

    if request.user.is_authenticated :
        cartfil = models.Cart.objects.filter(associated_user_id=request.user)
        if(len(cartfil)==0):
            newCart= Cart(associated_user_id=request.user.id)
            newCart.save()
        cart=models.Cart.objects.filter(associated_user_id=request.user)[0]
        cartList=models.CartProductTable.objects.filter(associated_cart=cart.id)
        print(len(cartList))
        return render(request,'home/index.html',{'today':datetime.today(),"cartList":cartList,'cart':cart}) #add 'cart':cart
    else:
        return render(request,'home/index.html',{'today':datetime.today()})
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('../home')
    else:
        form = UserCreationForm()
    return render(request, '../templates/registration/signup.html', {'form': form})
def test_layout(request):
        return render(request,'test.html')