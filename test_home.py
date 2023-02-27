import unittest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
def test_h():
    assert os.path.exists('home\\templates\\home') == True
    assert os.path.exists('home\\urls.py') == True
    assert os.path.exists('home\\views.py') == True

