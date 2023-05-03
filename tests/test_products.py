import unittest
import os
#this will serve to test the home app
#right now this is mainly check that the required paths exist in the project
def test_p():
    assert os.path.exists('products\\templates\\products') == True
    assert os.path.exists('products\\templates\\products\\product_list.html') == True
    assert os.path.exists('products\\templates\\products\\product_page.html') == True
    assert os.path.exists('products\\urls.py') == True
    assert os.path.exists('products\\views.py') == True
