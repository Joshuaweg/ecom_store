import unittest
import os
from django.test import Client, TestCase
#this will serve to test the home app
#right now this is mainly check that the required paths exist in the project
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    '.ecom_store.settings')
class TestViews(TestCase):
    def test_product_list(self):
        client=Client()
        response=client.get("/home")
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"home/index.html")