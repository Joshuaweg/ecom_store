import unittest
import os
#this will serve to test the Order app
#right now this is mainly check that the required paths exist in the project
def test_o():
    assert os.path.exists('orders\\templates\\orders') == True
    assert os.path.exists('orders\\urls.py') == True
    assert os.path.exists('orders\\views.py') == True
    assert os.path.exists('orders\\models.py') == True
