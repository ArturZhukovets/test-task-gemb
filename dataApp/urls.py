
from .views import index, kfc_data, restaurant_data_list
from django.urls import path, include

urlpatterns = [
    path('', index),
    path('kfc-data/', kfc_data, name='kfc'),
    path('restaurant-data/', restaurant_data_list, name='restaurant'),
]
