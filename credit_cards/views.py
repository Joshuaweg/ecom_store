from django.shortcuts import render

def credit_c(request):  # Rename is necessary
    #order_id = request.GET.get("id")
    #orders = Orders.objects.get(pk=order_id)
    # Store all products in our database

    return render(request, 'credit_cards/index.html')
