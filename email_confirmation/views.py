from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def email_confirmation(request):  # Rename is necessary
   
    print(request.user.email)
    send_mail(
        "Order Confirmation",
        "Here is the confirmation for your order",
        "donotreply_confirmation@azecommerce.com",
        [request.user.email],fail_silently=False,)

    return render(request, 'email_confirmation/index.html') # html template goes here
