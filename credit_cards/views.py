from django.shortcuts import render

def credit_c(request):  # Rename is necessary

    # Store all products in our database

    return render(request, 'credit_cards/index.html')
