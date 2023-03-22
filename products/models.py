
from django.db import models

# To be handled by Denshire 
# T-shirts


class Product(models.Model):

    # Size options for a shirt; by giving these choices to the size field, it will default to a select box instead of a
    #  text field, and will also validate that the input value is one of these options.
    # The first item in each tuple is what will be saved to the system; the second is the human-readable version.
    #  (These are currently identical, but can be replaced in case we decide to identify sizes by IDs or similar.)
    SIZE_CHOICES = (
        ("XXS", "XXS"),
        ("XS", "XS"),
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("XXL", "XXL")
    )

    title = models.CharField(max_length=200)           # Name of the product
    description = models.TextField(default='')         # Description of the item
    created = models.DateTimeField(auto_now_add=True)  # When the product is created (added to database)
    color = models.CharField(max_length=20, default='')
    size = models.CharField(max_length=4, choices=SIZE_CHOICES, default="M")
    price = models.FloatField(default=0)
    image_id = models.PositiveIntegerField(default=0)


class ProductImage(models.Model):
    title = models.CharField(max_length=200)           # title of image object
    created = models.DateTimeField(auto_now_add=True)  # time of image creation (upload)
    image = models.ImageField()                        # image file itself
