'''
Last stage of the ordering process.
After the user has filled out their credit card information and the order
has been processed.  
The user will directed to a webpage that lets them know to check their email,
to see the order has been successful. 
'''
from django.shortcuts import render
from django.core.mail import send_mail

def email_confirmation(request):  
   
    print(request.user.email)
    # Message to be be placed inside the body of the email
    send_mail(
        "Order Confirmation",
        "Here is the confirmation for your order",
        "donotreply_confirmation@azecommerce.com",
        [request.user.email],fail_silently=False,)

    return render(request, 'email_confirmation/index.html') # html template goes here
