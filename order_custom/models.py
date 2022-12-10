from django.db import models

from user.models import User
from oscar.apps.catalogue.models import Product

# Purchase
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

# Payment