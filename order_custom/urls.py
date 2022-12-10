from django.urls import path

from order_custom import views


urlpatterns = [
    path('add', views.add_purchase, name='add_purchase'),
    path('list', views.list_of_purchase, name='purchase_list'),
    path('payment-add', views.add_payment, name='add_payment'),
]