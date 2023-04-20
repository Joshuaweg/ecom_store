import unittest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#this will serve to test the home app
#right now this is mainly check that the required paths exist in the project
def test_h():
    assert os.path.exists('home\\templates\\home') == True
    assert os.path.exists('home\\urls.py') == True
    assert os.path.exists('home\\views.py') == True

