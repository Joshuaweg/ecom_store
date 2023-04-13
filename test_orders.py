import unittest
import os
def test_o():
    assert os.path.exists('orders\\templates\\orders') == True
    assert os.path.exists('orders\\urls.py') == True
    assert os.path.exists('orders\\views.py') == True
    assert os.path.exists('orders\\models.py') == True
