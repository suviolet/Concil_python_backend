from django.urls import path

from .views import AnimalDetail, AnimalList

urlpatterns = [
    path('animals/', AnimalList.as_view(), name=AnimalList.name),
    path('animals/<int:pk>/', AnimalDetail.as_view(), name=AnimalDetail.name),
]
