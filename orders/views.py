from django.shortcuts import render

# Create your views here.
def order(request):  # Rename is necessary

    # Store all products in our database

    return render(request, 'orders/index.html')