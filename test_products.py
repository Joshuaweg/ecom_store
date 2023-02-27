import unittest
import os
def test_p():
    assert os.path.exists('products\\templates\\products') == True
    assert os.path.exists('products\\urls.py') == True
    assert os.path.exists('products\\views.py') == True
