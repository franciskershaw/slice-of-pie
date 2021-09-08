from django.shortcuts import render, get_object_or_404
from .models import Product, Material

# Create your views here.


def all_products(request):
    """A view to return the all products page"""

    products = Product.objects.all()
    products_array = []
    products_materials = []
    products_angles = []
    products_levels = []

    if request.GET:
        print(request.GET)
        print(request.GET.getlist('material'))
        if 'material' in request.GET:
            materials = request.GET.getlist('material')
            products_materials = list(products.filter(material__name__in=materials))
        if 'angle' in request.GET:
            angles = request.GET.getlist('angle')
            products_angles = list(products.filter(material__name__in=angles))
        if 'levels' in request.GET:
            levels = request.GET.getlist('levels')
            products_levels = list(products.filter(material__name__in=levels))
        products_array = products_materials + products_angles + products_levels
        print(products_array)

        if products_array:
            products = products_array

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to return a product's detail page"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
