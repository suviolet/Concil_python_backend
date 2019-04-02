from django.urls import path
from .views import animal_list, animal_add, animal_remove

urlpatterns = [
    path('animals/', animal_list, name='animal_list'),
    path('animals/add/', animal_add, name='animal_add'),
    path('animals/remove/<int:id>/', animal_remove, name='animal_remove'),
]

