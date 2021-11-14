from django.shortcuts import render
from products.models import Product

# Create your views here.


def index(request):
    """A view to return the homepage"""

    most_popular = Product.objects.get(pk=2)
    most_expensive = Product.objects.get(pk=36)

    context = {
        'most_popular': most_popular,
        'most_expensive': most_expensive
    }

    return render(request, 'home/index.html', context)
