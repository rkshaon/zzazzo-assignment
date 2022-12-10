from django.contrib import admin

from order_custom.models import Purchase
from order_custom.models import Payment


admin.site.register(Purchase)
admin.site.register(Payment)