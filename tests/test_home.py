import unittest
import os
from django.test import Client, TestCase
#this will serve to test the home app
#right now this is mainly check that the required paths exist in the project
def test_h():
    assert os.path.exists('home\\templates\\home') == True
    assert os.path.exists('home\\urls.py') == True
    assert os.path.exists('home\\views.py') == True

