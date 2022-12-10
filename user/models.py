from django.db import models

# from oscar.apps.customer.abstract_models import AbstractUser


# class User(AbstractUser):
#     first_name = models.CharField(max_length=255, blank=False, null=False)
#     last_name = models.CharField(max_length=255, blank=False, null=False)
#     img = models.ImageField(upload_to='user', blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
class User(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    img = models.ImageField(upload_to='user', blank=True, null=True)
    address = models.TextField(blank=True, null=True)