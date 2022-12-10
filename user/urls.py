from django.urls import path

from user import views


urlpatterns = [
    path('add', views.add_user, name='add_user'),
]