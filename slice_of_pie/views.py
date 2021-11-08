from django.shortcuts import redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket

    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust the quantity of an item in the basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {basket[item_id]}')
    else:
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def remove_item(request, item_id):
    """ Remove item entirely from basket """
    product = get_object_or_404(Product, pk=item_id)
    try:
        basket = request.session.get('basket', {})
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def add_to_wishlist(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    print(product)
    redirect_url = request.POST.get('redirect_url')
    print(redirect_url)
    wishlist = request.session.get('wishlist', {})
    print(f'wishlist:{wishlist}')

    if item_id in list(wishlist.keys()):
        messages.info(request, f'{product.name} has already been favourited.')
    else:
        wishlist[item_id] = 1
        messages.success(request, f'Added {product.name} to your favourites.')

    request.session['wishlist'] = wishlist
    return redirect(redirect_url)


def remove_from_wishlist(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    try:
        wishlist = request.session.get('wishlist', {})
        wishlist.pop(item_id)
        messages.success(request, f'Removed {product.name} from your favourites')

        request.session['wishlist'] = wishlist
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def into_basket(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    try:
        basket = request.session.get('basket', {})
        wishlist = request.session.get('wishlist', {})

        wishlist.pop(item_id)
        basket[item_id] = 1
        messages.success(request, f'{product.name} moved into your basket')

        request.session['basket'] = basket
        request.session['wishlist'] = wishlist
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error moving item: {e}')
        return HttpResponse(status=500)
