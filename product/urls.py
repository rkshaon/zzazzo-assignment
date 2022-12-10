from django.urls import path
from django.conf.urls import url

from product import views

urlpatterns = [
    # path('', views.all_products, name='all_products'),
    url('', views.all_products, name='all_products'), 
]