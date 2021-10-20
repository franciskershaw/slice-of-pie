from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Product, Material
from .forms import ProductForm

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


def add_product(request):
    """Admin add product to store"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """Admin edit existing product"""
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Succesffully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing a product ({product.name})')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """Delete a product from store"""
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('products'))
