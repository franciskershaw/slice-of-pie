from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_required_attributes(self):
        form = OrderForm({
            'full_name': '',
            'email': '',
            'phone_number': '',
            'postcode': '',
            'town_or_city': '',
            'street_address1': '',
            'street_address2': '',
            'county': '',
            })
        self.assertFalse(form.is_valid())

        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0], 'This field is required.')

        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0], 'This field is required.')

        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0], 'This field is required.')

        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(form.errors['street_address1'][0], 'This field is required.')

    def test_fields_are_explicit_in_metaclass(self):
        form = OrderForm
        self.assertEqual(form.Meta.fields, ('full_name', 'email',
                                            'phone_number',
                                            'street_address1',
                                            'street_address2',
                                            'town_or_city', 'postcode',
                                            'country', 'county'))
