from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def home(request):
    return render(request,'home/index.html',{'today':datetime.today()})