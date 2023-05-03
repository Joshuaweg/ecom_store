from datetime import datetime
from orders.models import CartProductTable,Cart
from orders import models
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def home(request):

    if request.user.is_authenticated :
        cart = models.Cart.objects.get(associated_user=request.user.id)
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