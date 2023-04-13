from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def home(request):
    #cart = Cart.objects.get(userid=request.GET.get("User"))
    return render(request,'home/index.html',{'today':datetime.today()}) #add 'cart':cart