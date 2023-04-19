from django.shortcuts import render

# Create your views here.
def order(request):  # Rename is necessary
    cart=CartProductTable.objects.get(pk=request.GET.get("id"))
    

    return render(request, 'orders/index.html')