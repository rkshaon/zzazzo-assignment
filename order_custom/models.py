from django.db import models

from user.models import User
from oscar.apps.catalogue.models import Product

# Purchase
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name) + ' : ' + str(self.product.title)


class Payment(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    amount = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)