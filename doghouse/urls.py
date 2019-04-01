from django.urls import path
from .views import animal_list

urlpatterns = [
    path('animals/', animal_list, name='animal_list'),
]
