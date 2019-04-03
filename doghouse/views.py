from rest_framework import generics

from .models import Animal
from .serializers import AnimalSerializer


class AnimalList(generics.ListCreateAPIView):
    '''
    Class that inherits from:
    ListCreateAPIView: GET / POST
    in a collection of data (list)
    '''

    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    name = 'animal-list'


class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Class that inherits from:
    RetrieveUpdateDestroyAPIView: GET / PUT / DELETE
    on a single object (detail)
    '''
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    name = 'animal-details'
