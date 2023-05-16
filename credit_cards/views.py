'''
The purpose of this view is to all the user to input their shipping information for their credit card.
The dictionary Shipping handles all the fields thats that user needs to fill out
Each field is a post request because we need the database to be updated.
After the Shipping data is filled out, then the user would be returned to next part of the shipping process,
the order confirmation.
'''
from django.shortcuts import render

def credit_c(request):  # Function to handle Credit Card info
    cart=request.POST["cart_id"]
    # Shipping dictionary to handle user input
    Shipping={
        "name":request.POST["name"],
        "address1":request.POST["address1"],
        "address2":request.POST["address2"],
        "city":request.POST["city"],
        "state":request.POST["state"],
        "zipcode":request.POST["zipcode"],
        }
    return render(request, 'credit_cards/index.html',{'cart':cart,'shipping':Shipping})
