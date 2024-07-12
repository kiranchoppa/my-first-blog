from django.shortcuts import render


# Create your views here.
def available_items(request):
    return render(request, "shopping/items.html", {})
