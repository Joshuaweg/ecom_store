from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'user/login.html')

def sign_up(request):
    return render(request,'user/register.html')