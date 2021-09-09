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
        print('-----------------------------')
        print(f'Full get request: {request.GET}')
        print('-----------------------------')
        if 'material' in request.GET:
            print(f'Material GET request: {request.GET.getlist("material")}')
            materials = request.GET.getlist('material')
            print(f'Materials: {materials}')
            print('-----------------------------')
            products_materials = list(products.filter(material__name__in=materials))
            print('-----------------------------')
            print(f'products_materials: {products_materials}')
            print('-----------------------------')
        if 'angle' in request.GET:
            print(f'Angle GET request: {request.GET.getlist("angle")}')
            angles = request.GET.getlist('angle')
            print(f'Angles: {angles}')
            print('-----------------------------')
            products_angles = list(products.filter(angle__name__in=angles))
            print(list(products.filter(angle__name__in=angles)))
            print('-----------------------------')
            print(f'products_angles: {products_angles}')
            print('-----------------------------')
        if 'levels' in request.GET:
            print(f'Levels GET request: {request.GET.getlist("levels")}')
            levels = request.GET.getlist('levels')
            print(f'Levels: {levels}')
            print('-----------------------------')
            products_levels = list(products.filter(level__name__in=levels))
            print('-----------------------------')
            print(f'products_levels: {products_levels}')
            print('-----------------------------')

        products_array = products_materials + products_angles + products_levels
        print('-----------------------------')
        print(f'products_array: {products_array}')

        if products_array:
            products = list(dict.fromkeys(products_array))
            print(len(products))

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
