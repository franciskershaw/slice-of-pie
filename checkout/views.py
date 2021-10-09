from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from slice_of_pie.contexts import basket_contents


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket yet")
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J9onGJgDRRMupsm5uG2rYlRfvC1JFA8wGaa7DolbBPFAc8PS9UU3ZtuPaC6rbWIwi5vRkj6ybJOrDfqrRjRXfZ100fcIV6unS',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
