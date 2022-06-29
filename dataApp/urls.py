
from .views import index, restaurant_data_list
from django.urls import path, include

urlpatterns = [
    path('', index),
    path('restaurant-data/', restaurant_data_list, name='restaurant'),
]
