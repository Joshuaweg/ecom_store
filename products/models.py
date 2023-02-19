
from django.db import models

class Product(models.Model):
    # More model fields ? or Re-name them?
    title = models.CharField(max_length=200) # Name of the product
    text = models.TextField() # Description of the item
    created = models.DateTimeField(auto_now_add=True) # When the product is created 
