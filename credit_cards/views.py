from django.shortcuts import render

def credit_c(request):  # Rename is necessary
    cart=request.POST["cart_id"]
    Shipping={
        "name":request.POST["name"],
        "address1":request.POST["address1"],
        "address2":request.POST["address2"],
        "city":request.POST["city"],
        "state":request.POST["state"],
        "zipcode":request.POST["zipcode"],
        }

    return render(request, 'credit_cards/index.html',{'cart':cart,'shipping':Shipping})
