from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    print(basket)
    if not basket:
        messages.error(request, "There's nothing in your basket yet")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J9onGJgDRRMupsm5uG2rYlRfvC1JFA8wGaa7DolbBPFAc8PS9UU3ZtuPaC6rbWIwi5vRkj6ybJOrDfqrRjRXfZ100fcIV6unS',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
