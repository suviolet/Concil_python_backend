import json

from django.http import JsonResponse
from django.shortcuts import render

from .models import Animal

def animal_list(request):
    animals = [
        a for a in Animal.objects.all().values(
            'name', 'specie', 'gender',
            'age', 'size','hair', 'color',
            'description', 'address'
        )
    ]
    import pdb; pdb.set_trace()

    return JsonResponse(
        animals, safe=False
    )
