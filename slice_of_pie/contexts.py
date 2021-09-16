from django.conf import settings
from products.models import Product


def shopping_basket(request):
    """" Functionality for the shopping basket """
    print('Trying to stick something in the bag')
