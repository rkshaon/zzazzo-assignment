from django.urls import path

from order_custom import views


urlpatterns = [
    path('add', views.add_purchase, name='add_purchase'),
]