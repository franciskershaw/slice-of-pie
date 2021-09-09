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

    sort = None
    direction = None

    if request.GET:
        # Filtering
        if 'material' in request.GET:
            materials = request.GET.getlist('material')
            products_materials = list(products.filter(material__name__in=materials))
        if 'angle' in request.GET:
            angles = request.GET.getlist('angle')
            products_angles = list(products.filter(angle__name__in=angles))
        if 'levels' in request.GET:
            levels = request.GET.getlist('levels')
            products_levels = list(products.filter(level__name__in=levels))

        products_array = products_materials + products_angles + products_levels
        if products_array:
            products = list(dict.fromkeys(products_array))
            print(len(products))

        # Sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'levels':
                sortkey = 'level__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'current_sorting': current_sorting
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to return a product's detail page"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
