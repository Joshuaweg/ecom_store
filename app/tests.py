"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import re
import django
from django.test import TestCase

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/home')
        self.assertContains(response, 'Home Page', 1, 200)
    def test_productList(self):
        """Tests the products page."""
        response = self.client.get('/products')
        self.assertContains(response, 'These are the products', 1, 200)
    def test_productPage(self):
        """Tests the products page."""
        response = self.client.get('/products/item?id=3&User=1')
        print(response)
        self.assertContains(response, 'Blue Shirt Small', 0, 200)
class CompleteCheckoutTest(TestCase):
    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(CompleteCheckoutTest, cls).setUpClass()
            django.setup()
        def test_newCreditCard(self):
            payload={
                'cart_id':1,
                'name':'root',
                'address1':'root',
                'address2':'00',
                'city':'root',
                'state':'AL',
                'zipcode':'00000',
                'CreditCardNumber':'1111222233334444',
                'exprdate':'00/00',
                'CVV':'123'
                }
            response=self.client.post("/orders/checkout",payload)
            print(response.status_code)
def test_find():
    assert 1 ==1
