from django.conf import settings
from decimal import Decimal
from products.models import Product
from django.shortcuts import get_object_or_404


def basket_contents(request):
    """" Functionality for the shopping basket """

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,

    }

    return context


def wishlist_contents(request):
    wishlist_items = []
    product_count_wishlist = 0
    wishlist = request.session.get('wishlist', {})

    for item_id, quantity in wishlist.items():
        product = get_object_or_404(Product, pk=item_id)
        product_count_wishlist += quantity
        wishlist_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'wishlist_items': wishlist_items,
        'product_count_wishlist': product_count_wishlist,
    }

    return context
