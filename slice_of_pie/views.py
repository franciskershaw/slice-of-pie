from django.shortcuts import redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    print('Add to bag function has been called')
