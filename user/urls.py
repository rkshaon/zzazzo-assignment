from django.urls import path

from user import views


urlpatterns = [
    path('add', views.add_user, name='add_user'),
    path('list', views.list_of_user, name='user_list'),
    path('reports', views.reports, name='reports'),
    path('reports-api', views.reports_api),
]